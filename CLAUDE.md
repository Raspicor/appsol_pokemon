# PikaPet — macOS port of a Windows .exe

## What this repo actually is

Not a normal source repo. `PikaPet.exe` was a PyInstaller onefile bundle; this is
what came out of it plus the work to run it on macOS.

**There is no `pet.py`.** The game is 19,070 lines of Python 3.14 bytecode in
`run/pet.pyc`, and it is the only copy. Everything under `src/` is recovered
after the fact and is *not* the build input — never treat it as editable source
and never regenerate `pet.pyc` from it.

The port works by loading that bytecode unmodified and patching five things at
runtime. Keep it that way: patch from the launcher, don't rewrite the game.

## Commands

```bash
./install.sh                                          # set the machine up (idempotent)
run/pikapet.sh                                        # launch
tools/make_dmg.sh                                     # build dist/PikaPet-<ver>.dmg (default 0.0.1)
.venv/bin/python -m unittest discover -s run -v       # 131 tests, all should pass
.venv/bin/python tools/doctor.py                      # diagnose a broken environment
PIKAPET_VENV=/path/to/venv run/pikapet.sh             # use a different venv
```

Tests and the app need the venv's interpreter, not the system one.

### Environment

`./install.sh` does all of this and is safe to re-run; the manual equivalent is:

```bash
brew install python@3.14 python-tk@3.14
python3.14 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

`python-tk@3.14` is not optional — Homebrew's python@3.14 ships without
`_tkinter` and the app is pure tkinter. Python 3.14 itself is not optional
either: `pet.pyc` is 3.14 bytecode and fails to import on anything else.

The venv now lives in `.venv` inside the repo (gitignored) so it survives a
reboot. `run/pikapet.sh` prefers it, still honours `PIKAPET_VENV`, and falls
back to the old `/tmp/pikaenv` if that is the only one present.

### Windows

The port is macOS-only, but the repo runs on Windows too — natively, since
`pet.pyc` is a Windows build. `install.ps1` sets it up and `run/pikapet.bat`
launches `pet.pyc` directly; none of the macOS patches are involved and
`winlayer.pyc` is used as-is (it needs nothing beyond `ctypes`).

The one thing that breaks there: `run/assets`, `run/assets_v3`, `run/assets_v4`
and `run/badges_trainer` are committed as symlinks, and git on Windows writes
them out as text files unless `core.symlinks` is on. `pet.pyc` resolves assets
from its own directory, so the pet renders empty. `install.ps1` replaces them
with junctions, which need no admin rights.

## Layout

| Path | What it is |
|---|---|
| `run/pikapet_mac.py` | The macOS launcher. All five runtime patches live here. |
| `run/overlay.py` | Native AppKit sprite windows — the only way to get real transparency. |
| `run/pikapet.bat` | The Windows launcher: runs `pet.pyc` directly. |
| `run/maclayer.py` | macOS implementation of the app's `winlayer` API. |
| `run/mactray.py` | Menu bar item carrying the three tray-only actions. |
| `run/test_maclayer.py` | Contract tests for `maclayer`. |
| `run/test_overlay.py` | Tests for the overlay's tracking logic. |
| `run/test_macui.py` | Tests for the glyph fix and the coloured-button swap. |
| `run/macupdate.py` | Checks GitHub Releases for a newer version. |
| `run/test_macupdate.py` | Tests for the update check. |
| `run/pet.pyc` | **The game.** Windows-built bytecode, run as-is. |
| `disasm/` | CPython `dis` output. Authoritative. |
| `src/decompiled/` | Per-function decompilation. Partially wrong — see below. |
| `install.sh` / `install.ps1` | Setup for macOS / Windows. |
| `tools/doctor.py` | Environment check both installers end with. |
| `tools/make_dmg.sh` | Builds PikaPet.app and wraps it in a .dmg. |
| `tools/make_icon.py` | Builds the app icon from `tools/icon.png`. |
| `tools/pikapet.spec` | The PyInstaller spec that script drives. |
| `tools/` | Unpackers, and a pycdc patched for Python 3.14. |
| `README.md` | Full analysis: how the app works, what was found, why. |

## Reading the game's code

Two sources, and they are not equally trustworthy.

- `disasm/pet.dis.txt` — produced by CPython's own `dis`. **100% accurate.**
- `src/decompiled/*.py` — readable, but **any function containing try/except
  (~35% of them) has garbled code after the `try`**. Symptoms: `for None in (...)`,
  `'' = None`, stray `continue`. pycdc mismodels the 3.11+ exception table, which
  puts handlers at the end of the function; it treats the handler address as the
  end of the try block and swallows everything in between.

**Rule: when the decompiled source looks strange, it is wrong. Check the
disassembly before acting on it.** `src/decompiled/_INDEX.txt` maps every
function to its source line.

## The five patches, and why each exists

All in `run/pikapet_mac.py`. Do not "simplify" these without reading the reason.

1. **`sys.modules["winlayer"] = maclayer`** — the app's Win32 shim, swapped for
   the Quartz/AppKit one. Safe because `pet.pyc` never touches
   `winlayer.IS_WINDOWS`; it only calls the ten public functions.

2. **`-transparentcolor` → `-transparent`** — patched on `tk.Wm`, not wrapped in
   try/except at the call sites. It has to be a *translation*: in
   `Companion.__init__` the sprite label is created inside the same try block as
   the attribute call, so letting it raise leaves companion windows empty.

3. **`MAGIC` → `systemTransparent`** — the magenta chroma key. Only applied
   after probing that this Tk really supports it, and only on the fallback
   path — the overlay reads `#ff00ff` as its marker and leaves it alone.

4. **`PetApp.setup_tray` → `MacTray` + `mactray.py`** — pystray's macOS backend
   calls `NSApplication.run()`, which is main-thread-only; the app starts it on a
   daemon thread. That is a native `SIGTRAP` that kills the process and which
   the app's own try/except cannot catch.

   `PetApp.build_menu` (right-click the pet) covers nearly all of the tray, but
   **three actions live only in the tray**: `exit_ball`,
   `_open_pending_encounter` and `_restore_battle_window`. `exit_ball` is the
   dangerous one — once the pet is in the Poké Ball its window is unmapped, so
   there is nothing left to right-click and the pet can never come out. The
   wild-Pokémon notification even tells the user to click the tray icon. So
   `mactray.py` puts those three (plus a recall and quit) in a real NSStatusItem,
   created on Tk's main thread, which needs no run loop of its own. Its menu
   actions are AppKit callbacks, so they only enqueue -- see the Tcl rule below.

5. **The magenta plate → `overlay.py`** — every sprite frame is pasted onto a
   literal `Image.new('RGB', size, (255, 0, 255))` (pet.py:4264 and 7252), so
   patch 3 cannot reach it. Tk cannot make that plate disappear either: on aqua
   it renders each toplevel into a backing store with **no alpha channel**
   (`kCGImageAlphaNoneSkipLast`, even though the content view reports
   `isOpaque = NO` and the NSWindow is already non-opaque with a clear
   background), so anything Tk draws composites solid. Measured on Tk 9.0.4;
   Tk 8.6.18 instead punches the whole window out, contents and all. So the
   plate becomes a real transparent RGBA one and the sprite is drawn by a
   borderless NSWindow parked over the Tk window, which keeps geometry,
   dragging and the context menu at alpha 0.004 — low enough to be invisible,
   high enough that AppKit still hit-tests it. A window is only made invisible
   once its overlay is actually drawing, so a misjudged window falls back to the
   old look rather than vanishing. `PIKAPET_OVERLAY=0` forces the old path.

## Packaging a .dmg

`tools/make_dmg.sh` builds a self-contained `PikaPet.app` (Python 3.14, Tcl/Tk,
pillow, pyobjc and the 123 MB of assets all inside) and wraps it in a
compressed disk image. ~173 MB app, ~114 MB dmg, about five minutes.

It builds its own venv under `build/` so the runtime `.venv` is untouched, and
`build/` and `dist/` are gitignored.

Two things make this work, and neither is obvious:

- **PyInstaller is the app's native format.** `PikaPet.exe` was a PyInstaller
  onefile bundle, and that branch is still live in the bytecode: when
  `sys.frozen` is set, pet.pyc reads assets from `sys._MEIPASS` and saves to
  `$APPDATA/PikaPet` (pet.py:33-50). `_here()` in the launcher returns
  `sys._MEIPASS` for the same reason. A side benefit: the duplicate
  `run/pet_state.json` that a source run writes does not happen in the bundle.
- **pet.pyc is a data file, so PyInstaller cannot see its imports.** The spec
  lists them by hand, extracted from `IMPORT_NAME` in `disasm/pet.dis.txt`
  (plus `xml.etree.ElementTree` for spriteanim.pyc). If the game ever gains an
  import, add it to `hiddenimports` or the bundle will fail at runtime, not at
  build time. The script's bundle check catches missing *data*, not missing
  modules.

Without an Apple Developer certificate the app is only ad-hoc signed, so
Gatekeeper blocks it on another Mac until the user right-click-opens it once.
`PIKAPET_SIGN_ID=...` signs with a real identity instead.

## Releasing

The repo is public (`Raspicor/appsol_pokemon`), so GitHub Releases is the
distribution channel: 2 GB per asset against a 115 MB dmg, anonymous downloads,
and an anonymous `releases/latest` API the app itself can read.

**The tag is the only place a version is written.** It used to be hardcoded in
`make_dmg.sh`, and it drifted -- tag 0.0.2 shipped as an app that called itself
0.0.1. `make_dmg.sh` now reads `git describe --tags --abbrev=0`, strips a
leading `v`, and passes it to the spec as `PIKAPET_VERSION`, which lands in
`CFBundleShortVersionString`. `macupdate.app_version()` reads it back out of the
bundle. Tag -> dmg name -> Info.plist -> update comparison, one source.

If HEAD is not exactly on a tag the build is not a release, and the dmg is named
`PikaPet-<ver>+<sha>.dmg` so that is visible without opening anything. The
Info.plist keeps the plain `x.y.z` -- `CFBundleShortVersionString` has to stay
numeric.

Tag on `main` only. `0.0.1` is on a develop merge and `0.0.2` is on main, which
is why `git describe` gives a different answer depending on the branch you build
from. After tagging main, merge it back into develop or the next feature branch
forks from a stale base -- develop is currently behind main for exactly this
reason.

    develop -> main, git tag 0.0.3, git push --tags
    tools/make_dmg.sh                      # reads the tag
    upload dist/PikaPet-0.0.3.dmg to the release
    git checkout develop && git merge main

Gatekeeper is the real friction, not the download. An ad-hoc signed app needs
the recipient to go to System Settings > Privacy & Security > "Open Anyway" --
since macOS 15 right-click-open no longer covers it. A Developer ID plus
notarization removes that step and nothing else does.

## Gotchas found the hard way

- **Tk aqua does not restore a window's decorations.** Turning
  `overrideredirect` back off flips Tk's own flag but leaves the NSWindow's
  styleMask alone (78 -> 14, titled bit never returns), and a
  withdraw/deiconify remap does not help either. The window then has no title
  bar *and* none of the drag bindings the game puts on its own compact
  windows, so it cannot be moved at all -- which is what the Rocket raid's
  "화면 키우기" produces. `install_titlebar_restore()` sets the styleMask
  directly after the fact.
- **U+2694 (⚔) is unusable in Tk text on macOS.** The system font has no real
  text glyph for it and Tk does not draw a tofu box -- it falls back to a
  hairline glyph, so at the 9px the game uses, `⚔ Fight` reads as `× Fight`.
  Appending VS16 (U+FE0F) switches it to emoji presentation and Apple Color
  Emoji picks it up. Only ⚔ needs this: all 134 symbols in the game's strings
  were rendered at 9px bold and their ink counted, and it is the only one that
  breaks. Don't "fix" ▶ ↩ ⚙ ⬇ -- they render fine in monochrome, and
  emoji-fying them changes the game's look rather than repairing it. The hook
  goes on `tkinter.Misc._options`, the single choke point every widget option
  passes through (`Widget.__init__`, `Misc.configure`, `Menu.add`,
  `Canvas._create`).
- **aqua's `tk.Button` throws `-background` away.** No combination of `bd=0`,
  `relief=flat` or `highlightthickness=0` brings it back;
  `highlightbackground` only rings the button. Just 8 of the game's 181
  buttons set a colour, 7 of them the same `#ffd54a` action yellow, so only
  those are swapped for `MacColorButton` (a `tk.Label` that does paint its
  background) and the other 173 stay native. This is safe because the game
  never uses `isinstance` or `winfo_class` on widgets. Keep the replacement's
  padding at `padx=17, pady=5`: that is measured to make its requested size
  match a native button exactly, and without it the coloured buttons come out
  14x2 px smaller than the native ones beside them.
- **macOS system colours follow dark mode; the game assumes Windows' light
  defaults.** Two things break, both fixed by `install_contrast_fix()`:
  aqua paints the area around a widget's native bezel with
  `-highlightbackground`, whose default is `systemWindowBackgroundColor` --
  near black in dark mode -- so every button on the game's cream
  (`#fff6e0`) battle window gets a black rectangle around it (measured: a 4px
  `#1c1c1c` band at the widget bounds, white bezel inside). And `Label`'s
  default `-foreground` is `systemTextColor`, white in dark mode, so a label
  that sets `bg` but not `fg` is invisible on a light background (measured:
  "야생 ？？？ Lv.2" at (255,252,245) on (255,244,221)). The launcher fills in
  `highlightbackground` from the *parent's* background and `fg` from the
  widget's *own* background, and only where the game left them unset.
  Do not extend the `fg` rule to Button: aqua pins a Button's default
  foreground to `Black` and its bezel is always light, so deriving white text
  there would make it unreadable. Menu has no `-highlightbackground` at all --
  passing it makes widget creation fail.
- **The pet stands still whenever a battle window is open, by design.**
  `_update_walk` (pet.py:9279) returns immediately on `self.battle_open`,
  while `Companion._step_free_roam` has no such check -- so companions keep
  roaming and the pet looks frozen. `open_battle` sets the flag and registers
  `WM_DELETE_WINDOW` -> `_close_battle`, which clears it, so the native close
  button that `install_titlebar_restore()` adds does unfreeze the pet.
- **`wm iconphoto` sets the *application* icon on aqua, `-default` or not.**
  The game calls `win.iconphoto(True, <pet sprite>)` at startup
  (`_setup_taskbar_icon`, pet.py:17476) -- on Windows that is the window's
  taskbar icon, here it replaces the Dock icon, so PikaPet shows up as
  Charmander instead of the Poké Ball. Dropping the `default` argument does
  not help: measured, `iconphoto(False, <32px>)` still takes the app icon down
  to 32x32. macOS windows have no title-bar icon to set in the first place, so
  the launcher lets the call through and re-asserts the app icon right after.
- **The sprite overlay must sit below the menu bar.** The menu bar composites at
  window layer 24, so an overlay at `NSStatusWindowLevel` (25) draws *over* it:
  the pet covers the menu bar as it walks up, and because the overlay is
  repositioned every 16 ms the window server recomposites that strip constantly
  and it visibly tears. `NSMainMenuWindowLevel - 1` (23) keeps the pet behind
  the menu bar -- which is what the plain Tk window used to do -- while staying
  above the pet's own Tk window (layer 19) so the overlay still gets the clicks.
- **Notifications need a real signature to belong to the app.** macOS gives an
  ad-hoc signed bundle no notification permission at all -- no prompt, no entry
  in Notification settings, just `UNErrorDomain Code=1 "Notifications are not
  allowed for this application"`, from `dist/` and from `~/Applications` alike.
  So the shipped build always falls back to osascript, whose banners belong to
  Script Editor. `run/macnotify.py` already implements the modern
  `UNUserNotificationCenter` path and a click delegate; signing with
  `PIKAPET_SIGN_ID=...` is all it takes to switch over.
- **`NSUserNotificationCenter` is a black hole on macOS 26.** It accepts a
  notification, adds it to `deliveredNotifications()` and shows no banner --
  without raising. Anything that treats "no exception" as success will silently
  drop every notification, which is exactly what happened here. `osascript -e
  'display notification'` does show a banner; the cost is that the banner is
  owned by Script Editor, so clicking it opens Script Editor rather than the
  pet. The ◓ menu bar item is what makes the notification's own advice
  ("click the tray icon") followable.
- **Never call Tcl from an AppKit callback.** Tk's mainloop pumps the macOS run
  loop, so an NSView mouse handler or an NSTimer target runs *inside*
  `Tcl_DoOneEvent`. Calling `event_generate` (or anything else Tcl) from there
  detaches the Python thread state, and the next `after` timer aborts the
  process with `PyEval_RestoreThread: the current Python thread state is NULL`.
  It is not a rare race: reproduced 2/2 in isolation and 2/2 in the real app,
  within seconds. overlay.py's mouse handlers therefore only append to a deque,
  and `_Manager.tick` -- already a Tcl callback -- drains it.
- The Dock can be on a **non-primary** screen. `get_taskbar_rect` scans every
  screen; a `screens()[0]`-only version returns `None` on this machine.
- `maclayer` signatures are pinned against the real `winlayer.pyc` by test.
  That test caught `interval_ms` (not `timeout`) and a default mutex name.
  Don't loosen it.
- Everything in `maclayer` swallows exceptions on purpose — these run inside Tk
  timer callbacks, and the original behaves the same way.
- Desktop-icon positions need an AppleScript prompt that blocks, so they are off
  unless `PIKAPET_DESKTOP_ICONS=1`.

## Git

`origin` is `github.com/Raspicor/appsol_pokemon`. The 123 MB of sprite assets
are committed. `run/`, `src/`, `disasm/`, `tools/` and the docs were untracked
as of the port; `assets/pokedex_data_v2.json` shows as modified.
