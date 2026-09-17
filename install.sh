#!/bin/bash
# macOS에서 PikaPet 환경을 준비한다.
#
#   ./install.sh                 ./.venv 에 설치
#   ./install.sh --force         venv를 처음부터 다시 만든다
#   ./install.sh --venv PATH     venv를 다른 곳에 만든다
#
# 빠진 Homebrew 의존성을 설치하고, venv를 만들고, requirements.txt를 설치한 뒤
# tools/doctor.py를 돌린다. 여러 번 실행해도 안전하다.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$ROOT/.venv"
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    --venv)  VENV="$2"; shift 2 ;;
    -h|--help) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "모르는 옵션: $1 (--help 참고)" >&2; exit 2 ;;
  esac
done

say()  { printf '\n==> %s\n' "$*"; }
warn() { printf '    !! %s\n' "$*" >&2; }
die()  { printf '\n오류: %s\n' "$*" >&2; exit 1; }

[ "$(uname -s)" = "Darwin" ] || die "install.sh는 macOS용입니다. Windows에서는 install.ps1을 쓰세요."

# --------------------------------------------------------------------------
# 1. tkinter가 있는 Python 3.14
# --------------------------------------------------------------------------
# pet.pyc가 3.14 바이트코드라서 3.14는 취향 문제가 아니다. Homebrew의
# python@3.14는 python-tk@3.14를 따로 깔지 않으면 _tkinter 없이 오고, 이 앱은
# 전부 tkinter다. 그래서 두 formula 모두 필요하다.
say "Python 3.14 찾는 중"
PY314=""
for c in python3.14 /opt/homebrew/bin/python3.14 /usr/local/bin/python3.14; do
  if command -v "$c" >/dev/null 2>&1; then PY314="$(command -v "$c")"; break; fi
done

if [ -z "$PY314" ]; then
  command -v brew >/dev/null 2>&1 || die \
"Python 3.14가 없고 Homebrew도 설치돼 있지 않습니다.
  https://brew.sh 에서 Homebrew를 설치한 뒤 다시 실행하거나, Python 3.14를
  직접 설치하고 'python3.14'가 PATH에 있게 하세요."
  say "Homebrew로 python@3.14 설치"
  brew install python@3.14
  PY314="$(command -v python3.14 || echo /opt/homebrew/bin/python3.14)"
fi
[ -x "$PY314" ] || die "쓸 수 있는 python3.14를 찾지 못했습니다"
echo "    $PY314 ($("$PY314" -V 2>&1))"

if ! "$PY314" -c 'import tkinter' >/dev/null 2>&1; then
  say "Python 3.14에 tkinter가 없음. python-tk@3.14 설치"
  command -v brew >/dev/null 2>&1 || die \
"tkinter가 없고 Homebrew도 설치돼 있지 않습니다.
  쓰고 있는 Python 3.14에 맞는 python-tk를 설치한 뒤 다시 실행하세요."
  brew install python-tk@3.14
  "$PY314" -c 'import tkinter' >/dev/null 2>&1 || die \
"python-tk@3.14를 설치했는데도 tkinter가 여전히 없습니다.
  Homebrew가 아닌 Python 3.14를 쓰고 있다면 그쪽의 Tk 바인딩을 설치하세요."
fi
echo "    tkinter 정상 ($("$PY314" -c 'import tkinter; print("Tk", tkinter.TkVersion)'))"

# --------------------------------------------------------------------------
# 2. virtualenv
# --------------------------------------------------------------------------
if [ "$FORCE" = "1" ] && [ -d "$VENV" ]; then
  say "기존 venv 삭제: $VENV"
  rm -rf "$VENV"
fi
if [ -d "$VENV" ]; then
  say "기존 venv 재사용: $VENV"
else
  say "venv 생성: $VENV"
  "$PY314" -m venv "$VENV"
fi

say "requirements 설치"
"$VENV/bin/python" -m pip install --quiet --upgrade pip
"$VENV/bin/python" -m pip install --quiet -r "$ROOT/requirements.txt"

# --------------------------------------------------------------------------
# 3. 에셋 링크
# --------------------------------------------------------------------------
# pet.pyc는 자기 디렉터리를 기준으로 에셋을 찾으므로 run/assets 등이 반드시
# 있어야 한다. 저장소에 심볼릭 링크로 커밋돼 있어 macOS에서는 clone 후에도
# 살아 있지만, 오래된 체크아웃에서는 잃어버릴 수 있다.
say "에셋 링크 점검"
for name in assets assets_v3 assets_v4 badges_trainer; do
  link="$ROOT/run/$name"
  if [ -d "$link" ]; then
    echo "    run/$name 정상"
  elif [ -d "$ROOT/$name" ]; then
    rm -f "$link"
    ln -s "../$name" "$link"
    echo "    run/$name 다시 연결"
  else
    warn "run/$name 이 없고 $ROOT/$name 도 없습니다 -- 에셋이 불완전합니다"
  fi
done

# --------------------------------------------------------------------------
# 4. 확인
# --------------------------------------------------------------------------
say "확인"
"$VENV/bin/python" "$ROOT/tools/doctor.py" || die "환경 점검 실패 (위 내용 참고)"

cat <<EOF

완료. 실행:

    ./run/pikapet.sh

런처는 기본으로 ./.venv 를 씁니다. 다른 곳을 쓰려면 PIKAPET_VENV를 지정하세요.
메뉴는 펫을 우클릭하면 나옵니다.

테스트: $VENV/bin/python -m unittest discover -s run
점검:   $VENV/bin/python tools/doctor.py
EOF
