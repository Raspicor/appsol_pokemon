#!/bin/bash
# Launch PikaPet on macOS. Needs: brew install python@3.14 python-tk@3.14
# and a venv with the app's dependencies (see ../README.md).
set -e
cd "$(dirname "$0")"
VENV="${PIKAPET_VENV:-/tmp/pikaenv}"
exec "$VENV/bin/python" -u pikapet_mac.py "$@"
