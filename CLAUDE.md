# PikaPet — macOS port of a Windows .exe

## What this repo actually is

Not a normal source repo. `PikaPet.exe` was a PyInstaller onefile bundle; this is
what came out of it plus the work to run it on macOS.

**There is no `pet.py`.** The game is 19,070 lines of Python 3.14 bytecode in
`run/pet.pyc`, and it is the only copy. Everything under `src/` is recovered
after the fact and is *not* the build input — never treat it as editable source
and never regenerate `pet.pyc` from it.

The port works by loading that bytecode unmodified and patching four things at
runtime. Keep it that way: patch from the launcher, don't rewrite the game.

## Commands

```bash
run/pikapet.sh                                        # launch
python -m unittest discover -s run -v                 # 34 tests, all should pass
PIKAPET_VENV=/path/to/venv run/pikapet.sh             # use a different venv
```

Tests and the app need the venv's interpreter, not the system one:
`/tmp/pikaenv/bin/python -m unittest discover -s run`.

### Environment

```bash
brew install python@3.14 python-tk@3.14
python3.14 -m venv /tmp/pikaenv
/tmp/pikaenv/bin/pip install -r requirements.txt
```

`python-tk@3.14` is not optional — Homebrew's python@3.14 ships without
`_tkinter` and the app is pure tkinter.

**The venv lives in `/tmp` and will not survive a reboot.** If `run/pikapet.sh`
suddenly fails, recreate it with the commands above. Moving it somewhere durable
is a reasonable change to make.

## Layout

| Path | What it is |
|---|---|
| `run/pikapet_mac.py` | The launcher. All four runtime patches live here. |
| `run/maclayer.py` | macOS implementation of the app's `winlayer` API. |
| `run/test_maclayer.py` | Contract tests for `maclayer`. |
| `run/pet.pyc` | **The game.** Windows-built bytecode, run as-is. |
| `disasm/` | CPython `dis` output. Authoritative. |
| `src/decompiled/` | Per-function decompilation. Partially wrong — see below. |
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

## The four patches, and why each exists

All in `run/pikapet_mac.py`. Do not "simplify" these without reading the reason.

1. **`sys.modules["winlayer"] = maclayer`** — the app's Win32 shim, swapped for
   the Quartz/AppKit one. Safe because `pet.pyc` never touches
   `winlayer.IS_WINDOWS`; it only calls the ten public functions.

2. **`-transparentcolor` → `-transparent`** — patched on `tk.Wm`, not wrapped in
   try/except at the call sites. It has to be a *translation*: in
   `Companion.__init__` the sprite label is created inside the same try block as
   the attribute call, so letting it raise leaves companion windows empty.

3. **`MAGIC` → `systemTransparent`** — the magenta chroma key. Only applied
   after probing that this Tk really supports it.

4. **`PetApp.setup_tray` → `MacTray`** — pystray's macOS backend calls
   `NSApplication.run()`, which is main-thread-only; the app starts it on a
   daemon thread. That is a native `SIGTRAP` that kills the process and which
   the app's own try/except cannot catch. The tray menu is not reimplemented
   because `PetApp.build_menu` (right-click on the pet) already has everything
   the tray had and more.

## Gotchas found the hard way

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
