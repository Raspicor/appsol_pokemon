#!/usr/bin/env python3
"""Run PikaPet on macOS.

pet.pyc is Windows-built bytecode, but it is not Windows-specific: it makes no
Win32 calls of its own and routes everything platform-dependent through the
`winlayer` module. So rather than rewrite the game, this launcher loads the
original bytecode and patches the five places where Windows assumptions leak
through:

  1. `winlayer`        -> maclayer, the Quartz/AppKit implementation next door.
  2. `-transparentcolor` -> macOS has no colour-key transparency; translated to
                          the real `-transparent` window attribute.
  3. `MAGIC`           -> the magenta chroma key becomes `systemTransparent`,
                          which is what the translated attribute expects.
  4. `PetApp.setup_tray` -> pystray's macOS backend runs `NSApplication.run()`,
                          which only works on the main thread; PikaPet starts it
                          on a daemon thread, which traps the process. Replaced
                          with a stand-in that keeps notifications working.
  5. the magenta plate every sprite frame is pasted onto -> a transparent one.
                          The colour is a literal in the render path, so patch 3
                          cannot reach it.

Known limitation: Tk 9.0 on aqua accepts `-transparent` and the
`systemTransparent` colour but still paints the window's backdrop opaque, so the
pet sits on a solid rectangle rather than directly on the desktop. Patches 2, 3
and 5 make that rectangle black instead of magenta and keep the sprite's own
alpha intact, which is what a Tk build with working transparency would need.
Verified on Tk 9.0.4 / macOS 26: Label and Canvas, with and without
overrideredirect, `-alpha` below 1, and the `MacWindowStyle` plain/noActivates
route all render the backdrop opaque.

Nothing is written back to pet.pyc, so the patches cannot drift from the game
and none of this depends on the decompiled source being perfect.

    ./pikapet_mac.py
"""

import importlib.util
import os
import subprocess
import sys
import tkinter as tk

HERE = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# 1. environment: PikaPet looks for the Windows profile variables
# --------------------------------------------------------------------------

def install_save_paths():
    """Point %APPDATA%/%LOCALAPPDATA% at the usual macOS location.

    pet.pyc builds its save directory from these, and its fallback when they
    are unset puts pet_state.json next to the executable -- inside the app
    folder, where it would be easy to lose.
    """
    default = os.path.expanduser("~/Library/Application Support")
    os.environ.setdefault("APPDATA", default)
    os.environ.setdefault("LOCALAPPDATA", default)


# --------------------------------------------------------------------------
# 2. transparency
# --------------------------------------------------------------------------

def install_transparency_shim():
    """Translate Windows colour-key transparency into the macOS equivalent.

    On Windows the pet asks Tk to punch out every magenta pixel:

        win.attributes('-transparentcolor', '#ff00ff')
        win.config(bg='#ff00ff')

    macOS Tk has no such attribute and raises TclError. PikaPet catches that,
    but in `Companion.__init__` the label is created inside the same try block,
    so a raise there leaves a companion window with no sprite in it. Translating
    the call instead of letting it fail keeps every one of those paths intact.
    """
    original = tk.Wm.wm_attributes

    def wm_attributes(self, *args, **kwargs):
        if args and args[0] == "-transparentcolor":
            try:
                return original(self, "-transparent", True)
            except tk.TclError:
                return None
        return original(self, *args, **kwargs)

    tk.Wm.wm_attributes = wm_attributes
    tk.Wm.attributes = wm_attributes


def transparency_is_available(master):
    """True if this Tk really supports transparent windows.

    Probed on a throwaway window rather than assumed, because swapping MAGIC
    for `systemTransparent` on a Tk that rejects it would make every pet window
    fail to configure.
    """
    probe = None
    try:
        probe = tk.Toplevel(master)
        probe.withdraw()
        probe.wm_attributes("-transparent", True)
        probe.config(bg="systemTransparent")
        return True
    except Exception:
        return False
    finally:
        if probe is not None:
            try:
                probe.destroy()
            except Exception:
                pass


def install_sprite_alpha_patch():
    """Stop the sprite render path from flattening frames onto magenta.

    `Companion.step` and `PetApp.redraw` both build their frame the Windows way
    (pet.py:4264 and pet.py:7252):

        resized.putalpha(alpha)                       # thresholded to 0 or 255
        bg = Image.new('RGB', (w, h), (255, 0, 255))
        bg.paste(resized, (0, 0), resized)
        ImageTk.PhotoImage(bg)

    On Windows the window's `-transparentcolor` key erases those magenta pixels
    when the window is composited, so the plate is never seen. macOS has no
    colour key -- `-transparent` only clears widget backgrounds -- so the plate
    survives and the pet sits in a magenta box.

    Patch 3 cannot fix this: the colour here is a literal `(255, 0, 255)` tuple
    in the bytecode, not the `MAGIC` global. Handing back a transparent RGBA
    plate instead leaves `paste` (which uses the sprite as its own mask)
    working unchanged, and ImageTk then receives a real alpha channel.

    The two call sites are the only `(255, 0, 255)` constants in pet.pyc, so
    matching on mode and colour cannot catch anything else.
    """
    from PIL import Image

    original = Image.new

    def new(mode, size, color=0, *args, **kwargs):
        if mode == "RGB" and color == (255, 0, 255):
            return original("RGBA", size, (0, 0, 0, 0), *args, **kwargs)
        return original(mode, size, color, *args, **kwargs)

    Image.new = new


# --------------------------------------------------------------------------
# 3. the tray icon
# --------------------------------------------------------------------------

class MacTray:
    """Stands in for the pystray icon PetApp expects.

    PikaPet only ever touches four members of it -- `notify`, `update_menu`,
    `icon` and `stop` -- and guards each call with `if self.tray_icon:`. Leaving
    the attribute None would therefore silently drop every notification, so this
    keeps it truthy and forwards notifications to Notification Center.

    The menu is not reimplemented here: PikaPet already builds a full
    right-click menu in `PetApp.build_menu` -- skills, training, pokedex, daily
    quests, settings, quit -- and binds it to the pet itself, so the tray copy
    was redundant on macOS.
    """

    def __init__(self, app):
        self._app = app
        self.icon = None            # PetApp assigns a PIL image here; unused
        self.visible = False

    def notify(self, message, title="PikaPet"):
        """Post to Notification Center, without blocking the Tk event loop."""
        try:
            if _deliver_notification(message, title):
                return
        except Exception:
            pass
        try:
            script = 'display notification {} with title {}'.format(
                _applescript_string(message), _applescript_string(title))
            subprocess.Popen(["osascript", "-e", script],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    def update_menu(self):
        """No-op: the right-click menu is rebuilt from scratch on every click."""

    def stop(self):
        """No-op: there is no background tray thread to shut down."""


def _deliver_notification(message, title):
    """Post a banner that belongs to this process. True if it went out.

    `osascript -e 'display notification'` is the obvious way to do this, but the
    banner it posts is owned by Script Editor, so clicking one -- a wild-Pokemon
    alert, say -- brings up Script Editor instead of the pet. Going through the
    framework directly keeps the banner attributed to the running interpreter,
    so a click activates us and nothing else.

    NSUserNotificationCenter has been deprecated since macOS 11 but still
    delivers; the osascript path in `MacTray.notify` stays as the fallback for
    the release where it finally stops.
    """
    from Foundation import NSUserNotification, NSUserNotificationCenter

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    if center is None:
        return False
    note = NSUserNotification.alloc().init()
    note.setTitle_(str(title))
    note.setInformativeText_(str(message))
    center.deliverNotification_(note)
    return True


def _applescript_string(text):
    """Quote a Python string for embedding in AppleScript source."""
    escaped = str(text).replace("\\", "\\\\").replace('"', '\\"')
    escaped = escaped.replace("\r", " ").replace("\n", " ")
    return '"' + escaped + '"'


def install_window_patch(pet):
    """Decide about transparency once PikaPet has built its real root window.

    main() calls setup_pet_window(root) just before constructing PetApp, which
    is the first moment a Tk root exists and still the last moment before any
    widget is created with bg=MAGIC.
    """
    original = pet.setup_pet_window

    def setup_pet_window(root):
        transparent = transparency_is_available(root)
        if transparent:
            pet.MAGIC = "systemTransparent"
            install_sprite_alpha_patch()
        print("  transparency: "
              + ("attribute accepted (Tk 9 still draws an opaque backdrop)"
                 if transparent else "unavailable (opaque pet window)"),
              flush=True)
        return original(root)

    pet.setup_pet_window = setup_pet_window


def install_tray_replacement(pet):
    def setup_tray(self):
        self._pystray = None
        self.tray_icon = MacTray(self)

    setup_tray.__doc__ = MacTray.__doc__
    pet.PetApp.setup_tray = setup_tray


# --------------------------------------------------------------------------
# 4. right-click
# --------------------------------------------------------------------------

def install_right_click_fallback():
    """Make <Button-3> bindings also fire on Tk builds where right is button 2.

    Tk 9 normalised mouse buttons across platforms -- `tk.tcl` maps
    <<ContextMenu>> to <Button-3> for every windowing system -- so PikaPet's
    existing binding already works there. Tk 8.6 on aqua reported right-click
    as button 2, so on those builds the menu would never open.
    """
    if tk.TkVersion >= 9.0:
        return False

    original = tk.Misc.bind

    def bind(self, sequence=None, func=None, add=None):
        result = original(self, sequence, func, add)
        if isinstance(sequence, str) and "Button-3" in sequence:
            original(self, sequence.replace("Button-3", "Button-2"), func, "+")
        return result

    tk.Misc.bind = bind
    return True


# --------------------------------------------------------------------------
# loading pet.pyc
# --------------------------------------------------------------------------

def load_pet():
    """Import pet.pyc as a module without running its __main__ block."""
    path = os.path.join(HERE, "pet.pyc")
    if not os.path.exists(path):
        sys.exit(f"pet.pyc not found next to {__file__}")
    spec = importlib.util.spec_from_file_location("pet", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["pet"] = module
    spec.loader.exec_module(module)
    return module


def main():
    if sys.platform != "darwin":
        sys.exit("pikapet_mac.py is for macOS; run pet.pyc directly elsewhere.")

    sys.path.insert(0, HERE)        # so pet.pyc finds spriteanim.pyc
    install_save_paths()

    import maclayer
    sys.modules["winlayer"] = maclayer   # before pet.pyc runs `import winlayer`

    install_transparency_shim()
    remapped_buttons = install_right_click_fallback()

    pet = load_pet()
    install_window_patch(pet)
    install_tray_replacement(pet)

    print(f"PikaPet on macOS | Tk {tk.TkVersion} | menu: right-click the pet"
          + (" | Button-3 also bound to Button-2" if remapped_buttons else ""),
          flush=True)

    pet.main()


if __name__ == "__main__":
    main()
