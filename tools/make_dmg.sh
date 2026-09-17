#!/bin/bash
# PikaPet.app을 만들고 배포용 .dmg로 묶는다. macOS 전용.
#
#   tools/make_dmg.sh                  dist/PikaPet-0.0.1.dmg 를 만든다
#   tools/make_dmg.sh --version 0.1.0  버전을 지정한다
#   tools/make_dmg.sh --app-only       .app 까지만 만들고 멈춘다
#   tools/make_dmg.sh --clean          빌드 캐시와 빌드용 venv를 먼저 지운다
#
# 빌드용 venv를 따로 만들어 쓰므로 실행용 ./.venv 는 건드리지 않는다. 결과물은
# 자기 안에 Python 3.14와 Tcl/Tk를 품고 있어서, 받는 쪽에 아무것도 설치돼 있지
# 않아도 된다.
#
# 서명에 대해: Apple Developer 인증서가 없으면 ad-hoc 서명(`codesign -s -`)만
# 붙는다. 그런 앱을 다른 맥에서 처음 열면 Gatekeeper가 막으므로, 받는 사람이
# 우클릭 > 열기를 한 번 해주어야 한다. 스크립트가 마지막에 그 안내를 찍는다.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/build"
BUILD_VENV="$BUILD/venv"
DIST="$ROOT/dist"
VERSION="0.0.1"   # 아직 베타
APP_ONLY=0
CLEAN=0

while [ $# -gt 0 ]; do
  case "$1" in
    --version)  VERSION="$2"; shift 2 ;;
    --app-only) APP_ONLY=1; shift ;;
    --clean)    CLEAN=1; shift ;;
    -h|--help)  sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "모르는 옵션: $1 (--help 참고)" >&2; exit 2 ;;
  esac
done

say()  { printf '\n==> %s\n' "$*"; }
warn() { printf '    !! %s\n' "$*" >&2; }
die()  { printf '\n오류: %s\n' "$*" >&2; exit 1; }

[ "$(uname -s)" = "Darwin" ] || die "make_dmg.sh는 macOS 전용입니다."
command -v hdiutil >/dev/null 2>&1 || die "hdiutil이 없습니다."

if [ "$CLEAN" = "1" ]; then
  say "빌드 산출물 정리"
  rm -rf "$BUILD" "$DIST"
fi

# --------------------------------------------------------------------------
# 1. 빌드용 venv
# --------------------------------------------------------------------------
# pet.pyc가 3.14 바이트코드라서 번들에 들어가는 Python도 3.14여야 한다. 그리고
# PyInstaller는 자기가 돌고 있는 인터프리터를 그대로 묶으므로, 빌드 venv의 버전이
# 곧 결과물의 버전이다.
say "빌드용 Python 3.14 찾는 중"
PY314=""
for c in python3.14 /opt/homebrew/bin/python3.14 /usr/local/bin/python3.14; do
  if command -v "$c" >/dev/null 2>&1; then PY314="$(command -v "$c")"; break; fi
done
[ -n "$PY314" ] || die "python3.14가 없습니다. 먼저 ./install.sh 를 실행하세요."
"$PY314" -c 'import tkinter' >/dev/null 2>&1 \
  || die "이 python3.14에 tkinter가 없습니다. ./install.sh 가 python-tk@3.14를 설치합니다."
echo "    $PY314 ($("$PY314" -V 2>&1))"

if [ ! -x "$BUILD_VENV/bin/python" ]; then
  say "빌드용 venv 생성: $BUILD_VENV"
  mkdir -p "$BUILD"
  "$PY314" -m venv "$BUILD_VENV"
fi
say "빌드 의존성 설치 (pyinstaller + 런타임)"
"$BUILD_VENV/bin/python" -m pip install --quiet --upgrade pip
"$BUILD_VENV/bin/python" -m pip install --quiet pyinstaller
# 게임이 실제로 import하는 것만. requirements.txt 전체를 넣으면 쓰지도 않는
# numpy 등이 따라 들어온다 (스펙의 excludes가 막아주긴 하지만 설치 시간이 아깝다).
"$BUILD_VENV/bin/python" -m pip install --quiet \
  pillow pystray websockets pyobjc-core pyobjc-framework-Cocoa pyobjc-framework-Quartz

# --------------------------------------------------------------------------
# 2. 아이콘
# --------------------------------------------------------------------------
# 저장소에 .icns가 없으므로 피카츄 스프라이트 첫 프레임으로 만든다. 실패해도
# 빌드는 계속한다. 아이콘이 없으면 기본 아이콘이 붙을 뿐이다.
ICNS="$BUILD/PikaPet.icns"
SPRITE="$ROOT/assets/sprites/pikachu/Idle-Anim.png"
if [ ! -f "$ICNS" ] && [ -f "$SPRITE" ] && command -v iconutil >/dev/null 2>&1; then
  say "아이콘 생성"
  ICONSET="$BUILD/PikaPet.iconset"
  rm -rf "$ICONSET"; mkdir -p "$ICONSET"
  if "$BUILD_VENV/bin/python" - "$SPRITE" "$ICONSET" <<'PY'
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
# 시트의 첫 프레임만 쓴다. AnimData.xml을 읽지 않고도 정사각 타일 하나를
# 떼어낼 수 있도록, 시트 높이를 타일 크기로 본다.
sheet = Image.open(src).convert("RGBA")
tile = min(sheet.width, sheet.height)
frame = sheet.crop((0, 0, tile, tile))
# 픽셀 아트라서 확대는 NEAREST로, 축소만 LANCZOS로 한다.
for size in (16, 32, 64, 128, 256, 512, 1024):
    for scale, suffix in ((1, ""), (2, "@2x")):
        px = size * scale
        if px > 1024:
            continue
        resample = Image.NEAREST if px >= tile else Image.LANCZOS
        img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
        pad = max(1, px // 10)          # 아이콘 그리드에 맞게 약간 여백
        inner = frame.resize((px - pad * 2, px - pad * 2), resample)
        img.paste(inner, (pad, pad), inner)
        img.save(f"{out}/icon_{size}x{size}{suffix}.png")
PY
  then
    iconutil -c icns "$ICONSET" -o "$ICNS" || warn "iconutil 실패. 아이콘 없이 진행합니다."
  else
    warn "아이콘 렌더 실패. 아이콘 없이 진행합니다."
  fi
fi
[ -f "$ICNS" ] && echo "    $ICNS" || ICNS=""

# --------------------------------------------------------------------------
# 3. .app 빌드
# --------------------------------------------------------------------------
say "PikaPet.app 빌드 (에셋 123 MB 복사에 시간이 걸립니다)"
rm -rf "$DIST/PikaPet.app" "$BUILD/pyinstaller"
PIKAPET_ICNS="$ICNS" PIKAPET_VERSION="$VERSION" \
  "$BUILD_VENV/bin/pyinstaller" \
    --noconfirm --clean \
    --distpath "$DIST" \
    --workpath "$BUILD/pyinstaller" \
    "$ROOT/tools/pikapet.spec"

APP="$DIST/PikaPet.app"
[ -d "$APP" ] || die "PikaPet.app이 만들어지지 않았습니다."

# PyInstaller는 COLLECT 출력(dist/PikaPet)과 .app 을 둘 다 남긴다. 같은 173 MB가
# 두 벌이 되므로 번들만 남긴다. 번들 안의 것은 COLLECT의 복사본이 아니라 같은
# 파일을 하드링크로 들고 있지 않으니, 지워도 .app 은 온전하다.
rm -rf "$DIST/PikaPet"

# 번들 안에 실제로 필요한 것이 들어갔는지 확인한다. 빠져도 빌드는 성공하고
# 실행할 때 비어 있는 펫이 나오므로, 여기서 잡는 편이 낫다.
say "번들 내용 확인"
missing=0
for path in pet.pyc spriteanim.pyc assets assets_v3 assets_v4 badges_trainer; do
  found=""
  for base in "$APP/Contents/Frameworks" "$APP/Contents/Resources"; do
    [ -e "$base/$path" ] && { found="$base/$path"; break; }
  done
  if [ -n "$found" ]; then
    echo "    $path 있음"
  else
    warn "$path 이 번들에 없습니다"
    missing=$((missing + 1))
  fi
done
[ "$missing" -eq 0 ] || die "번들에 $missing 개가 빠졌습니다."
echo "    크기: $(du -sh "$APP" | cut -f1)"

# --------------------------------------------------------------------------
# 4. 서명
# --------------------------------------------------------------------------
# Developer ID가 있으면 PIKAPET_SIGN_ID로 넘기고, 없으면 ad-hoc으로 서명한다.
# Apple Silicon에서는 서명이 아예 없는 바이너리는 실행조차 되지 않으므로
# ad-hoc 서명이라도 반드시 붙여야 한다.
SIGN_ID="${PIKAPET_SIGN_ID:--}"
say "코드 서명 (${SIGN_ID})"
codesign --force --deep --sign "$SIGN_ID" --timestamp=none "$APP" 2>&1 | sed 's/^/    /' || \
  warn "서명 실패. 앱이 실행되지 않을 수 있습니다."
codesign --verify --deep --strict "$APP" 2>&1 | sed 's/^/    /' || warn "서명 검증 실패"

if [ "$APP_ONLY" = "1" ]; then
  say "완료 (--app-only)"
  echo "    $APP"
  exit 0
fi

# --------------------------------------------------------------------------
# 5. .dmg 로 묶기
# --------------------------------------------------------------------------
# 스테이징 폴더에 앱과 /Applications 심볼릭 링크만 넣는다. 창 배경이나 아이콘
# 배치를 꾸미려면 Finder를 AppleScript로 조종해야 하는데, 그건 자동화 동의
# 프롬프트를 띄우고 멈춘다. 배포에는 이 정도가 필요하고 충분하다.
DMG="$DIST/PikaPet-$VERSION.dmg"
STAGE="$BUILD/dmg"
say "DMG 만들기"
rm -rf "$STAGE" "$DMG"
mkdir -p "$STAGE"
cp -R "$APP" "$STAGE/"
ln -s /Applications "$STAGE/Applications"

hdiutil create \
  -volname "PikaPet $VERSION" \
  -srcfolder "$STAGE" \
  -fs HFS+ \
  -format UDZO \
  -imagekey zlib-level=9 \
  -ov -quiet \
  "$DMG"

[ -f "$DMG" ] || die "DMG가 만들어지지 않았습니다."
hdiutil verify "$DMG" >/dev/null 2>&1 || warn "DMG 검증 실패"

cat <<EOF

완료.

    $DMG  ($(du -sh "$DMG" | cut -f1))

받는 사람 안내:

  1. DMG를 열고 PikaPet을 Applications로 끌어다 놓습니다.
  2. 처음 실행할 때는 **우클릭 > 열기**를 하고 한 번 더 확인해야 합니다.
     ad-hoc 서명이라 Gatekeeper가 막습니다. 터미널을 쓸 수 있다면 이것도 됩니다:
         xattr -dr com.apple.quarantine /Applications/PikaPet.app
  3. 메뉴는 펫을 우클릭하면 나옵니다.

공증(notarization)까지 하려면 Apple Developer 인증서로 다시 서명해야 합니다:

    PIKAPET_SIGN_ID="Developer ID Application: 이름 (TEAMID)" tools/make_dmg.sh
    xcrun notarytool submit "$DMG" --apple-id ... --team-id ... --password ... --wait
    xcrun stapler staple "$DMG"

세이브는 ~/Library/Application Support/PikaPet/ 에 저장됩니다.
EOF
