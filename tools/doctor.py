#!/usr/bin/env python3
"""Check that this interpreter can actually run PikaPet.

Both installers call this at the end, and it is worth running on its own when
the app misbehaves:

    .venv/bin/python tools/doctor.py          # macOS
    .venv\\Scripts\\python.exe tools\\doctor.py  # Windows

Every check prints ok/FAIL with the reason, and the exit code is the number of
failures, so a caller can just test for zero.
"""

import importlib.util
import os
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(ROOT, "run")

# run/ holds symlinks (macOS) or junctions (Windows) pointing at these.
ASSET_LINKS = ("assets", "assets_v3", "assets_v4", "badges_trainer")

failures = []


def check(label, ok, detail=""):
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}{'  -- ' + detail if detail else ''}")
    if not ok:
        failures.append(label)
    return ok


def pyc_magic(path):
    """The bytecode version tag a .pyc was written with."""
    with open(path, "rb") as fh:
        return struct.unpack("<H", fh.read(2))[0]


def main():
    print(f"PikaPet environment check\n  python: {sys.version.split()[0]} ({sys.executable})\n")

    # 1. interpreter. pet.pyc is bytecode, so the version is not negotiable:
    #    a mismatched magic number fails at import with a bare ValueError.
    is314 = sys.version_info[:2] == (3, 14)
    check("Python is 3.14", is314,
          "" if is314 else
          f"found {sys.version_info.major}.{sys.version_info.minor}; pet.pyc is 3.14 bytecode")

    pet = os.path.join(RUN, "pet.pyc")
    if check("run/pet.pyc present", os.path.isfile(pet)):
        want = struct.unpack("<H", importlib.util.MAGIC_NUMBER[:2])[0]
        got = pyc_magic(pet)
        check("pet.pyc bytecode matches this interpreter", got == want,
              f"pet.pyc={got}, interpreter={want}")

    # 2. tkinter. Homebrew's python@3.14 ships without it unless python-tk@3.14
    #    is installed, and the whole app is tkinter.
    try:
        import tkinter
        check("tkinter importable", True, f"Tk {tkinter.TkVersion}")
        if sys.platform == "darwin" and tkinter.TkVersion >= 9.0:
            print("         note: Tk 9 draws the pet on an opaque backdrop "
                  "(see the launcher docstring)")
    except Exception as exc:
        check("tkinter importable", False, f"{type(exc).__name__}: {exc}")

    # 3. the three packages the game actually imports
    for mod, pkg in (("PIL", "pillow"), ("pystray", "pystray"), ("websockets", "websockets")):
        try:
            __import__(mod)
            check(f"{pkg} installed", True)
        except Exception as exc:
            check(f"{pkg} installed", False, f"{type(exc).__name__}: {exc}")

    # 4. platform layer
    if sys.platform == "darwin":
        for mod in ("Quartz", "AppKit"):
            try:
                __import__(mod)
                check(f"pyobjc {mod} importable", True)
            except Exception as exc:
                check(f"pyobjc {mod} importable", False, f"{type(exc).__name__}: {exc}")
        check("run/maclayer.py present", os.path.isfile(os.path.join(RUN, "maclayer.py")))
        check("run/pikapet_mac.py present", os.path.isfile(os.path.join(RUN, "pikapet_mac.py")))
    elif os.name == "nt":
        check("run/winlayer.pyc present", os.path.isfile(os.path.join(RUN, "winlayer.pyc")),
              "the game imports this directly on Windows")

    # 5. assets. pet.pyc resolves them from its own directory, so run/assets must
    #    resolve to a real directory. On Windows a plain `git clone` writes the
    #    symlinks out as text files, which is the usual cause of a blank pet.
    for name in ASSET_LINKS:
        link = os.path.join(RUN, name)
        real = os.path.join(ROOT, name)
        if not os.path.exists(link):
            check(f"run/{name} resolves", False, "missing; re-run the installer")
        elif not os.path.isdir(link):
            size = os.path.getsize(link)
            check(f"run/{name} resolves", False,
                  f"is a {size}-byte file, not a directory -- git checked the symlink "
                  f"out as text; re-run the installer")
        else:
            check(f"run/{name} resolves", True,
                  "" if os.path.isdir(real) else "warning: source directory missing")

    print()
    if failures:
        print(f"{len(failures)} problem(s): " + ", ".join(failures))
    else:
        print("All good.")
    return len(failures)


if __name__ == "__main__":
    sys.exit(main())
