#!/bin/bash
# macOS에서 PikaPet 실행. 먼저 ../install.sh로 환경을 준비하세요.
#
# venv는 재부팅 후에도 남도록 저장소 안의 .venv를 기본으로 쓴다. PIKAPET_VENV로
# 덮어쓸 수 있고, 예전 /tmp/pikaenv만 있는 경우에도 그것을 인정한다.
set -e
cd "$(dirname "$0")"

if [ -n "${PIKAPET_VENV:-}" ]; then
  VENV="$PIKAPET_VENV"
elif [ -x "../.venv/bin/python" ]; then
  VENV="../.venv"
elif [ -x "/tmp/pikaenv/bin/python" ]; then
  VENV="/tmp/pikaenv"
else
  echo "virtualenv를 찾을 수 없습니다. 저장소 루트에서 ./install.sh를 실행하거나," >&2
  echo "PIKAPET_VENV를 기존 venv 경로로 지정하세요." >&2
  exit 1
fi

exec "$VENV/bin/python" -u pikapet_mac.py "$@"
