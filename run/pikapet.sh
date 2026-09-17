#!/bin/bash
# Launch PikaPet on macOS. Set the machine up with ../install.sh first.
#
# The venv defaults to the repo's own .venv so it survives a reboot; PIKAPET_VENV
# overrides it, and the old /tmp/pikaenv is still honoured if that is all there is.
set -e
cd "$(dirname "$0")"

if [ -n "${PIKAPET_VENV:-}" ]; then
  VENV="$PIKAPET_VENV"
elif [ -x "../.venv/bin/python" ]; then
  VENV="../.venv"
elif [ -x "/tmp/pikaenv/bin/python" ]; then
  VENV="/tmp/pikaenv"
else
  echo "No virtualenv found. Run ./install.sh from the repo root," >&2
  echo "or set PIKAPET_VENV to an existing one." >&2
  exit 1
fi

exec "$VENV/bin/python" -u pikapet_mac.py "$@"
