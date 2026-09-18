#!/bin/bash
# PikaPet.app을 만들고 배포용 .dmg로 묶는다. macOS 전용.
#
#   tools/make_dmg.sh                  태그에서 버전을 읽어 dist/PikaPet-<ver>.dmg
#   tools/make_dmg.sh --version 0.1.0  버전을 직접 지정한다
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
VERSION=""        # 비어 있으면 git 태그에서 읽는다 (아래)
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

# --------------------------------------------------------------------------
# 버전: 태그가 유일한 출처
# --------------------------------------------------------------------------
# 예전에는 이 파일에 손으로 적혀 있었고, 그래서 태그가 0.0.2인데 빌드된 앱은
# 0.0.1이라고 말하는 상태가 됐다. 버전이 두 군데 적혀 있으면 반드시 어긋난다.
#
# 태그 위에 정확히 서 있지 않으면 릴리스가 아니다. 그때는 이름에 커밋을 붙여서
# "이건 배포본이 아니다"가 파일명만 봐도 보이게 한다. Info.plist에 들어가는
# 값은 숫자만 남긴다 -- CFBundleShortVersionString 은 x.y.z 형태여야 한다.
if [ -z "$VERSION" ]; then
  if ! command -v git >/dev/null 2>&1 || ! git -C "$ROOT" rev-parse --git-dir >/dev/null 2>&1; then
    die "git 저장소가 아니라 태그에서 버전을 읽을 수 없습니다. --version 으로 지정하세요."
  fi
  VERSION="$(git -C "$ROOT" describe --tags --abbrev=0 2>/dev/null || true)"
  [ -n "$VERSION" ] || die "태그가 하나도 없습니다. 태그를 만들거나 --version 으로 지정하세요."
  VERSION="${VERSION#v}"                      # v0.0.2 로 달아도 받아준다
fi

# 배포본인지 아닌지는 VERSION 을 어떻게 얻었는지와 무관하다. 태그 위에 정확히
# 서 있고, 커밋되지 않은 변경이 하나도 없을 때만 릴리스다. 둘 중 하나라도
# 어긋나면 파일 이름에 그 사실을 적는다 -- 이름이 릴리스와 같으면 나중에 어느
# 쪽인지 알 방법이 없고, 실제로 그렇게 섞인 번들을 한 번 배포했다.
#
# --version 으로 숫자를 직접 준 경우에도 똑같이 본다. 릴리스는 태그에서 나오고
# (CLAUDE.md), --version 은 그 밖의 빌드를 위한 것이다.
LABEL="$VERSION"
if command -v git >/dev/null 2>&1 && git -C "$ROOT" rev-parse --git-dir >/dev/null 2>&1; then
  DIRTY="$(git -C "$ROOT" status --porcelain 2>/dev/null)"
  if git -C "$ROOT" describe --tags --exact-match >/dev/null 2>&1 && [ -z "$DIRTY" ]; then
    :                                          # 릴리스. 이름은 숫자만
  else
    SUFFIX="$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo nogit)"
    [ -z "$DIRTY" ] || SUFFIX="$SUFFIX-dirty"
    LABEL="$VERSION+$SUFFIX"
    if [ -n "$DIRTY" ]; then
      warn "커밋되지 않은 변경이 있습니다. 배포본이 아닌 빌드로 표시합니다: $LABEL"
    else
      warn "HEAD가 태그 위에 정확히 서 있지 않습니다. 배포본이 아닌 빌드로 표시합니다: $LABEL"
    fi
  fi
fi
echo "    버전 $VERSION (빌드 이름: $LABEL)"

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
  pillow pystray websockets pyobjc-core pyobjc-framework-Cocoa \
  pyobjc-framework-Quartz pyobjc-framework-UserNotifications

# --------------------------------------------------------------------------
# 2. 아이콘
# --------------------------------------------------------------------------
# .icns는 tools/make_icon.py 가 tools/icon.png 에서 만든다. 매번 다시 만든다
# -- 원본이나 스크립트를 고쳤는데 예전 아이콘이 그대로 붙는 일이 없도록.
ICNS="$BUILD/PikaPet.icns"
if command -v iconutil >/dev/null 2>&1; then
  say "아이콘 생성 (몬스터볼)"
  ICONSET="$BUILD/PikaPet.iconset"
  rm -rf "$ICONSET" "$ICNS"
  if "$BUILD_VENV/bin/python" "$ROOT/tools/make_icon.py" --iconset "$ICONSET"; then
    iconutil -c icns "$ICONSET" -o "$ICNS" || warn "iconutil 실패. 아이콘 없이 진행합니다."
  else
    warn "아이콘 렌더 실패. 아이콘 없이 진행합니다."
  fi
else
  warn "iconutil이 없습니다. 아이콘 없이 진행합니다."
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

# pet.pyc 는 sys._MEIPASS(= Contents/Frameworks) 아래에서 에셋을 찾는데, 거기의
# assets 는 ../Resources/assets 를 가리키는 심볼릭 링크다. 링크가 끊기면 앱은
# 멀쩡히 돌면서 스프라이트만 하나도 안 읽힌다 -- 선택 창에 '(이미지 없음)' 이
# 뜨고 펫이 안 보인다. 실제로 신고된 증상이라 여기서 실물까지 확인한다.
for path in assets/sprites assets_v3 assets_v4 badges_trainer; do
  [ -d "$APP/Contents/Frameworks/$path" ] || \
    die "Frameworks/$path 가 풀리지 않습니다 (심볼릭 링크 끊김). 이미지가 안 나옵니다."
done
echo "    Frameworks 에서 에셋 링크 4개 정상"

# XML 파서가 모듈로 수집됐는지 본다. spriteanim 은 스프라이트마다 AnimData.xml
# 을 읽으므로, pyexpat 이 빠지면 이미지가 전부 사라진다 -- 그런데 앱은 멀쩡히
# 돌아서 빌드도 실행도 성공으로 보인다. 실제로 그렇게 배포했다.
if ! ls "$APP/Contents/Frameworks"/pyexpat*.so >/dev/null 2>&1; then
  die "pyexpat 이 번들 최상위에 없습니다. XML 을 못 읽어 이미지가 전부 안 나옵니다."
fi
echo "    XML 파서(pyexpat) 수집됨"

# pyexpat 은 /usr/lib/libexpat.1.dylib 에 링크돼 있다. 그 시스템 라이브러리는
# macOS 버전마다 내용이 다르다 -- 26.5 에서 빌드하면 expat 2.7.2+ 의
# _XML_SetAllocTracker* 심볼을 요구하는데 macOS 26.2 의 것에는 없다. 그러면
# dyld 가 적재를 거부하고 ElementTree 가 그 실패를 "No module named expat" 으로
# 덮어써서, 게임의 **모든 이미지가 사라진다**. 앱의 나머지는 멀쩡히 돌아서
# 빌드도 실행도 성공으로 보인다. 실제로 그렇게 배포했다.
#
# 그래서 우리 expat 을 들고 가고, 참조를 번들 안으로 돌린다. PyInstaller 는
# /usr/lib 의존성을 시스템 것으로 보고 손대지 않으므로 여기서 해야 한다.
say "expat 링크를 번들 것으로 돌리기"
EXPAT="$APP/Contents/Frameworks/libexpat.1.dylib"
[ -f "$EXPAT" ] || die "libexpat.1.dylib 이 번들에 없습니다. spec 의 binaries 를 확인하세요."
chmod u+w "$EXPAT"
install_name_tool -id "@loader_path/libexpat.1.dylib" "$EXPAT" || \
  die "libexpat 의 install name 을 바꾸지 못했습니다."

find "$APP" -type f \( -name "*.so" -o -name "*.dylib" \) | while IFS= read -r bin; do
  if otool -L "$bin" 2>/dev/null | grep -q "/usr/lib/libexpat"; then
    chmod u+w "$bin"
    install_name_tool -change /usr/lib/libexpat.1.dylib \
      "@loader_path/libexpat.1.dylib" "$bin" || true
  fi
done

# 하나도 남아 있으면 안 된다. 남으면 그 기계에서만 되는 빌드가 된다.
LEFT=0
while IFS= read -r bin; do
  otool -L "$bin" 2>/dev/null | grep -q "/usr/lib/libexpat" && LEFT=$((LEFT + 1))
done < <(find "$APP" -type f \( -name "*.so" -o -name "*.dylib" \))
[ "$LEFT" -eq 0 ] || die "$LEFT 개가 아직 시스템 expat 을 참조합니다."

# pyexpat 이 필요로 하는 XML_ 심볼이 번들 expat 에 모두 있는지 본다. 버전이
# 어긋나면 여기서 잡힌다 -- 심볼 이름을 손으로 적어두면 다음 번에 또 어긋난다.
NEED="$(nm -u "$APP/Contents/Frameworks/pyexpat"*.so | grep '^_XML_' | sort -u)"
HAVE="$(nm -g "$EXPAT" | awk '$2 == "T" { print $3 }' | grep '^_XML_' | sort -u)"
MISSING="$(comm -23 <(printf '%s\n' "$NEED") <(printf '%s\n' "$HAVE"))"
[ -z "$MISSING" ] || die "번들 expat 에 없는 심볼: $(printf '%s' "$MISSING" | tr '\n' ' ')"
echo "    expat 을 번들 것으로 연결 (심볼 $(printf '%s\n' "$NEED" | wc -l | tr -d ' ')개 확인)"
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
DMG="$DIST/PikaPet-$LABEL.dmg"
STAGE="$BUILD/dmg"
say "DMG 만들기"
rm -rf "$STAGE" "$DMG"
mkdir -p "$STAGE"
# ditto 로 복사한다. cp -R 은 확장 속성을 떨어뜨려서 서명 검증이 깨질 수 있고,
# 여기서 만들어지는 사본이 곧 사람들이 받는 것이다. (에셋은 Frameworks 에서
# ../Resources 를 가리키는 상대 심볼릭 링크로 연결돼 있는데, 그 링크가 사라지면
# 앱은 멀쩡히 돌면서 이미지만 전부 사라진다. 실측으로 재현했다.)
ditto "$APP" "$STAGE/PikaPet.app"
ln -s /Applications "$STAGE/Applications"

hdiutil create \
  -volname "PikaPet $LABEL" \
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
  3. 메뉴는 펫을 우클릭하면 나옵니다. 메뉴 바의 ◓ 에는 우클릭 메뉴에 없는
     항목(몬스터볼에서 꺼내기, 야생 포켓몬 확인, 배틀 창 복구, 화면 중앙으로
     부르기, 새 버전 확인)이 있습니다.

알림에 대해: ad-hoc 서명 빌드는 알림을 osascript로 띄우므로 배너의 소유자가
스크립트 편집기가 되고, 배너를 클릭하면 스크립트 편집기가 열립니다. macOS는
ad-hoc 서명 앱에 알림 권한을 주지 않아서 (프롬프트조차 뜨지 않습니다) 우회할 수
없습니다. Developer ID로 서명하면 run/macnotify.py 가 모던 API로 전환되고,
배너가 PikaPet 소유가 되어 클릭 시 야생 포켓몬 창이 열립니다.

공증(notarization)까지 하려면 Apple Developer 인증서로 다시 서명해야 합니다:

    PIKAPET_SIGN_ID="Developer ID Application: 이름 (TEAMID)" tools/make_dmg.sh
    xcrun notarytool submit "$DMG" --apple-id ... --team-id ... --password ... --wait
    xcrun stapler staple "$DMG"

세이브는 ~/Library/Application Support/PikaPet/ 에 저장됩니다.
EOF
