#!/bin/bash
# Set up PikaPet on macOS.
#
#   ./install.sh                 install into ./.venv
#   ./install.sh --force         rebuild the venv from scratch
#   ./install.sh --venv PATH     put the venv somewhere else
#
# Installs the Homebrew dependencies if they are missing, builds the venv,
# installs requirements.txt and then runs tools/doctor.py. Safe to re-run.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$ROOT/.venv"
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    --venv)  VENV="$2"; shift 2 ;;
    -h|--help) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1 (try --help)" >&2; exit 2 ;;
  esac
done

say()  { printf '\n==> %s\n' "$*"; }
warn() { printf '    !! %s\n' "$*" >&2; }
die()  { printf '\nERROR: %s\n' "$*" >&2; exit 1; }

[ "$(uname -s)" = "Darwin" ] || die "install.sh is for macOS. On Windows use install.ps1."

# --------------------------------------------------------------------------
# 1. Python 3.14 with tkinter
# --------------------------------------------------------------------------
# pet.pyc is 3.14 bytecode, so 3.14 is not a preference. Homebrew's python@3.14
# ships without _tkinter unless python-tk@3.14 is installed, and the whole app
# is tkinter -- so both formulae are required.
say "Looking for Python 3.14"
PY314=""
for c in python3.14 /opt/homebrew/bin/python3.14 /usr/local/bin/python3.14; do
  if command -v "$c" >/dev/null 2>&1; then PY314="$(command -v "$c")"; break; fi
done

if [ -z "$PY314" ]; then
  command -v brew >/dev/null 2>&1 || die \
"Python 3.14 not found and Homebrew is not installed.
  Install Homebrew from https://brew.sh then re-run, or install Python 3.14
  yourself and make sure 'python3.14' is on PATH."
  say "Installing python@3.14 via Homebrew"
  brew install python@3.14
  PY314="$(command -v python3.14 || echo /opt/homebrew/bin/python3.14)"
fi
[ -x "$PY314" ] || die "could not locate a usable python3.14"
echo "    $PY314 ($("$PY314" -V 2>&1))"

if ! "$PY314" -c 'import tkinter' >/dev/null 2>&1; then
  say "Python 3.14 has no tkinter; installing python-tk@3.14"
  command -v brew >/dev/null 2>&1 || die \
"tkinter is missing and Homebrew is not installed.
  Install python-tk for your Python 3.14 and re-run."
  brew install python-tk@3.14
  "$PY314" -c 'import tkinter' >/dev/null 2>&1 || die \
"tkinter is still missing after installing python-tk@3.14.
  If you are using a non-Homebrew Python 3.14, install its Tk bindings."
fi
echo "    tkinter ok ($("$PY314" -c 'import tkinter; print("Tk", tkinter.TkVersion)'))"

# --------------------------------------------------------------------------
# 2. the virtualenv
# --------------------------------------------------------------------------
if [ "$FORCE" = "1" ] && [ -d "$VENV" ]; then
  say "Removing existing venv at $VENV"
  rm -rf "$VENV"
fi
if [ -d "$VENV" ]; then
  say "Reusing venv at $VENV"
else
  say "Creating venv at $VENV"
  "$PY314" -m venv "$VENV"
fi

say "Installing requirements"
"$VENV/bin/python" -m pip install --quiet --upgrade pip
"$VENV/bin/python" -m pip install --quiet -r "$ROOT/requirements.txt"

# --------------------------------------------------------------------------
# 3. asset links
# --------------------------------------------------------------------------
# pet.pyc resolves assets from its own directory, so run/assets and friends have
# to exist. They are committed as symlinks and survive a clone on macOS, but a
# stale checkout can lose them.
say "Checking asset links"
for name in assets assets_v3 assets_v4 badges_trainer; do
  link="$ROOT/run/$name"
  if [ -d "$link" ]; then
    echo "    run/$name ok"
  elif [ -d "$ROOT/$name" ]; then
    rm -f "$link"
    ln -s "../$name" "$link"
    echo "    run/$name relinked"
  else
    warn "run/$name missing and $ROOT/$name does not exist -- assets are incomplete"
  fi
done

# --------------------------------------------------------------------------
# 4. verify
# --------------------------------------------------------------------------
say "Verifying"
"$VENV/bin/python" "$ROOT/tools/doctor.py" || die "environment check failed (see above)"

cat <<EOF

Done. Run it with:

    ./run/pikapet.sh

The launcher uses ./.venv by default; set PIKAPET_VENV to point somewhere else.
Right-click the pet for the menu.

Tests:  $VENV/bin/python -m unittest discover -s run
Doctor: $VENV/bin/python tools/doctor.py
EOF
