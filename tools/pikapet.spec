# -*- mode: python ; coding: utf-8 -*-
"""PikaPet.app을 만드는 PyInstaller 스펙. tools/make_dmg.sh가 이걸 쓴다.

여기서 손으로 챙겨야 하는 것이 두 가지다.

1. **pet.pyc는 데이터 파일이다.** 게임 본체는 19,070줄의 3.14 바이트코드이고
   런처가 importlib으로 직접 로드한다. PyInstaller의 정적 분석은 그 안을 들여다볼
   수 없으므로, pet.pyc가 import하는 모듈을 바이트코드에서 뽑아 hiddenimports에
   손으로 적는다 (disasm/pet.dis.txt의 IMPORT_NAME 전부).

2. **에셋은 저장소 루트에서 가져온다.** run/assets 등은 ../assets를 가리키는
   심볼릭 링크다. 링크가 아니라 원본을 넣는다.

frozen이 되면 pet.pyc가 스스로 RESOURCE_DIR = sys._MEIPASS, SAVE_DIR =
$APPDATA/PikaPet 로 전환한다 (pet.py:33~50). 원래 이 앱이 PyInstaller 번들이었기
때문이다. 그래서 에셋은 번들에서 읽고 세이브는 사용자 폴더로 가며, 소스 실행에서
run/pet_state.json 에 중복 저장되던 문제도 여기서는 일어나지 않는다.
"""

import glob
import os
import sysconfig

ROOT = os.path.abspath(os.path.join(SPECPATH, os.pardir))
RUN = os.path.join(ROOT, "run")

# 게임 본체와 스프라이트 시트 파서. 둘 다 바이트코드이고 번들 루트에 놓아야
# 런처의 sys.path.insert(0, HERE) 가 `import spriteanim` 을 풀 수 있다.
datas = [
    (os.path.join(RUN, "pet.pyc"), "."),
    (os.path.join(RUN, "spriteanim.pyc"), "."),
]

# 에셋 123 MB. RESOURCE_DIR 기준의 상대 경로 이름을 그대로 유지해야 한다.
for name in ("assets", "assets_v3", "assets_v4", "badges_trainer"):
    datas.append((os.path.join(ROOT, name), name))

# **C 확장은 최상위에 직접 넣어야 하는 것이 있다.** hiddenimports 에 적어도
# PyInstaller 는 pyexpat 을 CArchive TOC 에 등록하지 않고, 프레임워크 트리의
# python3__dot__14/lib-dynload 안에만 둔다. 그 폴더 이름은 PyInstaller 가 바꿔
# 놓은 것이라 파이썬의 정상 탐색 경로가 아니어서 `import pyexpat` 이 기계에 따라
# 실패한다 -- 빌드한 맥(26.5)에서는 되고 macOS 26.2 에서는 안 됐다.
#
# 번들 최상위(= sys._MEIPASS)는 sys.path 에 들어 있고 표준 확장 로더가 거기서
# .so 를 읽는다. `_tkinter.so` 가 이미 그렇게 놓여 정상 동작하는 것이 근거다.
binaries = []
_dynload = sysconfig.get_config_var("DESTSHARED")
for _name in ("pyexpat", "_elementtree"):
    _found = glob.glob(os.path.join(_dynload or "", _name + "*.so"))
    if not _found:
        raise SystemExit(
            f"{_name} 확장을 찾을 수 없습니다 ({_dynload}). "
            "이게 없으면 AnimData.xml 을 못 읽어 이미지가 전부 안 나옵니다.")
    binaries.append((_found[0], "."))

# **expat 은 우리 것을 들고 간다.** Homebrew 의 python@3.14 는
# --with-system-expat 으로 빌드돼서 pyexpat 이 /usr/lib/libexpat.1.dylib 에
# 링크하는데, 그 시스템 라이브러리는 macOS 버전마다 내용이 다르다. 실측:
# 26.5 에서 빌드한 pyexpat 은 _XML_SetAllocTrackerActivationThreshold 와
# _XML_SetAllocTrackerMaximumAmplification (expat 2.7.2+ API) 을 요구하는데
# macOS 26.2 의 시스템 expat 에는 그 심볼이 없다. 그러면 dyld 가 적재를
# 거부하고, ElementTree 가 그 실패를 "No module named expat" 로 덮어써서
# 게임의 모든 이미지가 사라진다 -- 원인을 찾는 데 한참 걸렸다.
#
# 여기서 파일만 넣고, 참조를 @loader_path 로 돌리는 것은 make_dmg.sh 가 한다
# (PyInstaller 는 /usr/lib 의존성을 시스템 것으로 보고 손대지 않는다).
_expat = "/opt/homebrew/opt/expat/lib/libexpat.1.dylib"
if not os.path.exists(_expat):
    raise SystemExit(
        f"{_expat} 가 없습니다. `brew install expat` 이 필요합니다 -- "
        "시스템 expat 에 링크된 채로 배포하면 다른 macOS 버전에서 "
        "이미지가 전부 사라집니다.")
binaries.append((_expat, "."))

hiddenimports = [
    # pet.pyc가 import하는 것 전부 (disasm/pet.dis.txt의 IMPORT_NAME)
    "asyncio", "base64", "colorsys", "json", "math", "queue", "random",
    "shutil", "subprocess", "threading", "time", "traceback", "webbrowser",
    "tkinter", "tkinter.ttk", "tkinter.messagebox",
    "PIL", "PIL.Image", "PIL.ImageTk", "PIL.ImageDraw", "PIL.ImageFont",
    "pystray", "websockets",
    # spriteanim.pyc가 추가로 쓰는 것. **expat 까지 손으로 적어야 한다.**
    # ElementTree 는 `from xml.parsers import expat` 을 try 안에서 늦게 하므로
    # PyInstaller 의 정적 분석이 따라가지 못하고, pyexpat 이 CArchive TOC 에
    # 등록되지 않는다. 그러면 번들 안에 .so 파일이 프레임워크 트리로 딸려오기는
    # 하지만 (python3__dot__14/lib-dynload -- 이름이 바뀌어 있어 파이썬의 정상
    # 탐색 경로가 아니다) `import pyexpat` 이 기계에 따라 실패한다.
    #
    # 실제로 그렇게 됐다. 빌드한 맥(26.5)에서는 되고 macOS 26.2 에서는
    #   ImportError: No module named expat; use SimpleXMLTreeBuilder instead
    # 가 나면서 스프라이트가 하나도 안 읽혔다 -- 모든 스프라이트 폴더가
    # AnimData.xml 로 시작하기 때문에 이미지가 전부 사라진다. 앱의 나머지는
    # 멀쩡하게 돌아서 고장으로 보이지도 않는다.
    "xml.etree.ElementTree", "xml.parsers.expat", "pyexpat", "_elementtree",
    # 우리 쪽 모듈. winlayer 자리에 들어가는 maclayer는 런처가 import하므로
    # 분석에 잡히지만, 명시해두는 편이 안전하다.
    "maclayer", "overlay", "mactray", "macnotify", "macupdate", "macupgrade",
    "macdiag",
    # maclayer와 overlay가 쓰는 pyobjc
    "Quartz", "AppKit", "Foundation", "objc", "UserNotifications",
]

# requirements.txt는 원본 .exe가 묶고 있던 것들을 함께 적어두지만, 게임이 실제로
# import하지는 않는다. 번들에 들어가면 numpy만으로도 수십 MB가 늘어난다.
excludes = [
    "numpy", "werkzeug", "Werkzeug", "watchdog", "markupsafe", "MarkupSafe",
    "colorama", "charset_normalizer", "threadpoolctl",
    "pytest", "setuptools", "pip", "wheel",
]

analysis = Analysis(
    [os.path.join(RUN, "pikapet_mac.py")],
    pathex=[RUN],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    [],
    exclude_binaries=True,
    name="PikaPet",
    debug=False,
    strip=False,
    upx=False,
    console=False,          # GUI 앱. 콘솔 창을 띄우지 않는다
)

collect = COLLECT(
    exe,
    analysis.binaries,
    analysis.datas,
    strip=False,
    upx=False,
    name="PikaPet",
)

# onefile이 아니라 onedir 안의 .app 이다. onefile은 실행할 때마다 에셋 123 MB를
# 임시 폴더에 풀어서 시작이 눈에 띄게 느려진다.
app = BUNDLE(
    collect,
    name="PikaPet.app",
    icon=os.environ.get("PIKAPET_ICNS") or None,
    bundle_identifier="com.raspicor.pikapet",
    version=os.environ.get("PIKAPET_VERSION", "0.0.0"),
    info_plist={
        "CFBundleName": "PikaPet",
        "CFBundleDisplayName": "PikaPet",
        "CFBundleShortVersionString": os.environ.get("PIKAPET_VERSION", "0.0.0"),
        "NSHighResolutionCapable": True,
        # LSUIElement로 두지 않는다. winlayer의 flash_taskbar가 주의를 끌 때
        # Dock 아이콘을 튀게 하는데, Dock 타일이 없으면 그게 아무 일도 하지 않는다.
        # 실측한 하한이다. 번들 바이너리 60개(Homebrew python@3.14 와 tcl-tk
        # 병에서 온 _json, _ctypes, libtcl9tk 등)가 LC_BUILD_VERSION minos 26.0
        # 을 달고 있어서, macOS 25 이하에서는 파이썬 자체가 뜨지 않는다. 여기에
        # 11.0 을 적어두면 돌지도 못하는 맥에서 설치가 열려 "안 켜진다"가 된다.
        # 확인: find dist/PikaPet.app -name '*.so' -o -name '*.dylib' 에
        #       otool -l | grep minos 를 돌려 가장 높은 값.
        "LSMinimumSystemVersion": "26.0",
        "NSAppleEventsUsageDescription":
            "데스크톱 아이콘 위치를 읽을 때 Finder에 물어봅니다 "
            "(PIKAPET_DESKTOP_ICONS=1 일 때만).",
    },
)
