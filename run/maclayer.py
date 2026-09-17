"""macOS implementation of PikaPet's `winlayer` API.

winlayer.py wraps the Win32 calls PikaPet needs in order to sit on top of other
windows, walk along the taskbar and flash for attention. Every function there
begins with `if not IS_WINDOWS: return <safe default>`, so the game already runs
on macOS without any of it -- it just loses those behaviours. This module gives
them back using Quartz and AppKit.

The launcher installs it as `sys.modules["winlayer"]` before pet.pyc is loaded,
so the app's own `import winlayer` picks this up instead. pet.pyc never touches
`winlayer.IS_WINDOWS`; it only calls the ten public functions, which is why a
straight swap is safe.

Coordinates match what Tk reports on macOS: points (not pixels), origin at the
top-left of the display holding the menu bar, y growing downwards. AppKit's own
origin is bottom-left, so anything read from NSScreen is flipped on the way out.

Like winlayer, nothing here raises: these run inside Tk timer callbacks, and a
missing permission or an unplugged monitor must never take the pet down.
"""

import fcntl
import os
import subprocess
import sys
import threading

IS_MACOS = sys.platform == "darwin"

try:
    import Quartz
    from AppKit import NSApplication, NSCriticalRequest, NSScreen
    _HAVE_PYOBJC = True
except Exception:                                           # pragma: no cover
    Quartz = None
    _HAVE_PYOBJC = False

# Windows sizes its taskbar in whole pixels and pet.pyc pastes these numbers
# straight into Tk geometry strings, so every rect leaves here as ints.
_MIN_LEDGE_WIDTH = 80
_MIN_LEDGE_HEIGHT = 40


# --------------------------------------------------------------------------
# displays
# --------------------------------------------------------------------------

def _display_bounds():
    """Every active display as (left, top, width, height), top-left origin.

    CGDisplayBounds already works in the global display space that Tk uses, so
    no flipping is needed here.
    """
    if not _HAVE_PYOBJC:
        return []
    try:
        err, ids, _count = Quartz.CGGetActiveDisplayList(16, None, None)
        if err:
            return []
        out = []
        for did in ids:
            r = Quartz.CGDisplayBounds(did)
            out.append((did, int(r.origin.x), int(r.origin.y),
                        int(r.size.width), int(r.size.height)))
        return out
    except Exception:
        return []


def get_virtual_screen_rect():
    """Bounding box of all displays as (left, top, width, height)."""
    try:
        rects = _display_bounds()
        if not rects:
            return None
        left = min(x for _, x, _, _, _ in rects)
        top = min(y for _, _, y, _, _ in rects)
        right = max(x + w for _, x, _, w, _ in rects)
        bottom = max(y + h for _, _, y, _, h in rects)
        if right <= left or bottom <= top:
            return None
        return (left, top, right - left, bottom - top)
    except Exception:
        return None


def get_secondary_monitor_rect():
    """The first non-primary display as (left, top, width, height)."""
    try:
        if not _HAVE_PYOBJC:
            return None
        main = Quartz.CGMainDisplayID()
        for did, x, y, w, h in _display_bounds():
            if did != main and w > 0 and h > 0:
                return (x, y, w, h)
        return None
    except Exception:
        return None


def _dock_rect_from_frames(frames, ref_height):
    """Find the Dock from each screen's (frame, visibleFrame) pair.

    `frames` holds AppKit geometry -- bottom-left origin, y growing upwards --
    as ((fx, fy, fw, fh), (vx, vy, vw, vh)) per screen. `ref_height` is the
    height of screens()[0], the origin of that coordinate space, and is what
    the result is flipped against to reach Tk's top-left coordinates.

    Kept pure so the multi-monitor cases can be tested without unplugging
    anything. Returns (left, top, right, bottom) or None when the Dock is
    hidden. A lone inset at the top is the menu bar, not the Dock.
    """
    for (fx, fy, fw, fh), (vx, vy, vw, vh) in frames:
        left_inset = vx - fx
        right_inset = (fx + fw) - (vx + vw)
        bottom_inset = vy - fy
        top_inset = (fy + fh) - (vy + vh)

        def flip(y):
            """AppKit y (from the bottom) -> Tk y (from the top)."""
            return int(round(ref_height - y))

        if bottom_inset > 1:
            return (int(fx), flip(fy + bottom_inset), int(fx + fw), flip(fy))
        if left_inset > 1:
            return (int(fx), flip(fy + fh - top_inset),
                    int(fx + left_inset), flip(fy))
        if right_inset > 1:
            return (int(fx + fw - right_inset), flip(fy + fh - top_inset),
                    int(fx + fw), flip(fy))
    return None


def get_taskbar_rect():
    """The Dock's rectangle as (left, top, right, bottom).

    The Dock is the closest thing macOS has to the Windows taskbar: a reserved
    strip the pet can stand on. Returns None when the Dock is set to auto-hide,
    matching what winlayer does when it cannot find Shell_TrayWnd.
    """
    try:
        if not _HAVE_PYOBJC:
            return None
        screens = NSScreen.screens()
        if not screens:
            return None
        # screens()[0] defines the origin of AppKit's coordinate space; the Dock
        # itself may be on any screen, so every one of them is checked.
        ref_height = screens[0].frame().size.height
        frames = []
        for s in screens:
            f, v = s.frame(), s.visibleFrame()
            frames.append(((f.origin.x, f.origin.y, f.size.width, f.size.height),
                           (v.origin.x, v.origin.y, v.size.width, v.size.height)))
        return _dock_rect_from_frames(frames, ref_height)
    except Exception:
        return None


# --------------------------------------------------------------------------
# other apps' windows -- the ledges the pet walks along
# --------------------------------------------------------------------------

def _list_windows():
    """On-screen windows as dicts of pid/layer/title/left/top/right/bottom.

    `kCGWindowName` needs Screen Recording permission; without it macOS simply
    omits the key, so the owning application's name is used instead. That is
    enough for the exclude list and for the tooltip the pet shows.
    """
    if not _HAVE_PYOBJC:
        return []
    try:
        options = (Quartz.kCGWindowListOptionOnScreenOnly
                   | Quartz.kCGWindowListExcludeDesktopElements)
        infos = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID) or []
    except Exception:
        return []

    out = []
    for info in infos:
        try:
            bounds = info.get("kCGWindowBounds") or {}
            x, y = float(bounds.get("X", 0)), float(bounds.get("Y", 0))
            w, h = float(bounds.get("Width", 0)), float(bounds.get("Height", 0))
            title = info.get("kCGWindowName") or info.get("kCGWindowOwnerName") or ""
            out.append({
                "pid": int(info.get("kCGWindowOwnerPID", -1)),
                "layer": int(info.get("kCGWindowLayer", 0)),
                "title": str(title),
                "left": int(x), "top": int(y),
                "right": int(x + w), "bottom": int(y + h),
            })
        except Exception:
            continue
    return out


def _ledges_from_records(records, exclude_titles, max_windows, own_pid):
    """Turn raw window records into winlayer's ledge dicts.

    Kept separate from the Quartz call so the filtering rules can be tested
    without a screen or a permission prompt.
    """
    if max_windows is not None and max_windows <= 0:
        return []
    excludes = [t for t in (exclude_titles or []) if t]

    kept = []
    for r in records:
        if r["pid"] == own_pid:
            continue                                  # never stand on ourselves
        if r["layer"] != 0:
            continue                                  # Dock, menu bar, our own topmost pet
        if r["right"] - r["left"] < _MIN_LEDGE_WIDTH:
            continue                                  # Tk scatters 1px helper windows
        if r["bottom"] - r["top"] < _MIN_LEDGE_HEIGHT:
            continue
        title = r["title"]
        if any(x in title for x in excludes):
            continue
        kept.append({"left": r["left"], "top": r["top"],
                     "right": r["right"], "title": title})

    # Highest ledge first, so the pet's choice does not depend on the order
    # Quartz happened to return windows in.
    kept.sort(key=lambda l: (l["top"], l["left"]))
    return kept[:max_windows] if max_windows is not None else kept


def get_window_ledges(exclude_titles=None, max_windows=40):
    """Top edges of other apps' windows, as [{left, top, right, title}, ...]."""
    try:
        return _ledges_from_records(_list_windows(), exclude_titles,
                                    max_windows, os.getpid())
    except Exception:
        return []


# --------------------------------------------------------------------------
# desktop icons
# --------------------------------------------------------------------------

_ICON_SCRIPT = 'tell application "Finder" to get desktop position of every item of desktop window'
_icon_cache = None


def get_desktop_icon_positions(max_icons=60):
    """Screen positions of the Finder desktop icons, as [(x, y), ...].

    Off by default. Unlike Windows, macOS has no way to read these without
    driving Finder over AppleScript, which raises an Automation consent prompt
    the first time and blocks until the user answers -- not something to do
    from a timer callback. Set PIKAPET_DESKTOP_ICONS=1 to opt in; the result is
    cached for the rest of the run so the prompt can only appear once.
    """
    global _icon_cache
    try:
        if max_icons is not None and max_icons <= 0:
            return []
        if not os.environ.get("PIKAPET_DESKTOP_ICONS"):
            return []
        if _icon_cache is None:
            _icon_cache = _read_desktop_icons()
        return _icon_cache[:max_icons] if max_icons is not None else list(_icon_cache)
    except Exception:
        return []


def _read_desktop_icons():
    try:
        out = subprocess.run(["osascript", "-e", _ICON_SCRIPT],
                             capture_output=True, text=True, timeout=5)
        if out.returncode != 0:
            return []
        # osascript prints a flat list: "12, 34, 12, 120, ..."
        nums = [int(float(p)) for p in out.stdout.replace("\n", "").split(",") if p.strip()]
        return list(zip(nums[0::2], nums[1::2]))
    except Exception:
        return []


# --------------------------------------------------------------------------
# single instance
# --------------------------------------------------------------------------

# The same default winlayer ships, so both layers agree on the lock identity.
_DEFAULT_MUTEX = "PikaPetSingleInstanceMutex_do_bro2"

_locks = {}
_lock_guard = threading.Lock()


def _lock_dir():
    base = os.environ.get("APPDATA") or os.path.expanduser("~/Library/Application Support")
    path = os.path.join(base, "PikaPet")
    os.makedirs(path, exist_ok=True)
    return path


def acquire_single_instance_lock(name=_DEFAULT_MUTEX):
    """True if this process may run, False if another instance already holds it.

    Uses flock, which the kernel drops when the process exits -- so a crashed
    run cannot lock the user out, which a stale lock file would. Errors return
    True: refusing to start because the lock itself broke would be worse than
    briefly allowing two pets, and that is how winlayer behaves too.
    """
    try:
        with _lock_guard:
            if name in _locks:
                return True                       # we already hold it
            safe = "".join(c if c.isalnum() or c in "-._" else "_" for c in str(name))
            fd = os.open(os.path.join(_lock_dir(), safe + ".lock"),
                         os.O_CREAT | os.O_RDWR, 0o644)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os.close(fd)
                return False
            _locks[name] = fd                     # keep the fd alive for the run
            return True
    except Exception:
        return True


# --------------------------------------------------------------------------
# attention and Dock
# --------------------------------------------------------------------------

_attention_request = None


def set_dpi_aware():
    """No-op. Tk on macOS already works in points and handles Retina itself."""
    return None


def flash_taskbar(hwnd, count=8, interval_ms=500):
    """Bounce the Dock icon to get the user's attention.

    macOS decides how long to bounce, so `count` and `interval_ms` are accepted
    for signature parity and ignored. AppKit must be touched from the main thread;
    pet.pyc calls this from Tk callbacks, but the guard keeps a stray background
    call from trapping the process the way pystray does.
    """
    global _attention_request
    try:
        if not _HAVE_PYOBJC or threading.current_thread() is not threading.main_thread():
            return None
        _attention_request = NSApplication.sharedApplication().requestUserAttention_(
            NSCriticalRequest)
    except Exception:
        pass
    return None


def stop_taskbar_flash(hwnd):
    """Stop the Dock bounce started by flash_taskbar."""
    global _attention_request
    try:
        if _HAVE_PYOBJC and _attention_request is not None \
                and threading.current_thread() is threading.main_thread():
            NSApplication.sharedApplication().cancelUserAttentionRequest_(_attention_request)
    except Exception:
        pass
    _attention_request = None
    return None


def hide_window_from_taskbar(hwnd):
    """No-op. macOS gives the whole process one Dock tile, not one per window,
    so there is no per-window equivalent of the WS_EX_TOOLWINDOW trick winlayer
    uses to keep the pet's helper windows out of the taskbar.
    """
    return None
