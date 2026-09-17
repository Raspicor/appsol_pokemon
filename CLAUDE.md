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
.venv/bin/python -m unittest discover -s run -v       # 51 tests, all should pass
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
| `run/pet.pyc` | **The game.** Windows-built bytecode, run as-is. |
| `disasm/` | CPython `dis` output. Authoritative. |
| `src/decompiled/` | Per-function decompilation. Partially wrong — see below. |
| `install.sh` / `install.ps1` | Setup for macOS / Windows. |
| `tools/doctor.py` | Environment check both installers end with. |
| `tools/make_dmg.sh` | Builds PikaPet.app and wraps it in a .dmg. |
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

## Gotchas found the hard way

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
