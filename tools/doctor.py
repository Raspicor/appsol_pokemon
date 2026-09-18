#!/usr/bin/env python3
"""이 인터프리터가 실제로 PikaPet을 돌릴 수 있는지 점검한다.

두 설치 스크립트가 마지막에 이걸 부르고, 앱이 이상하게 굴 때 따로 돌려볼 가치도
있다:

    .venv/bin/python tools/doctor.py          # macOS
    .venv\\Scripts\\python.exe tools\\doctor.py  # Windows

점검마다 ok/실패와 이유를 찍고, 종료 코드는 실패 개수다. 호출하는 쪽은 0인지만
보면 된다.
"""

import importlib.util
import os
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(ROOT, "run")

# run/ 안에 이것들을 가리키는 심볼릭 링크(macOS) 또는 junction(Windows)이 있다.
ASSET_LINKS = ("assets", "assets_v3", "assets_v4", "badges_trainer")

failures = []


def check(label, ok, detail=""):
    print(f"  [{'ok  ' if ok else '실패'}] {label}{'  -- ' + detail if detail else ''}")
    if not ok:
        failures.append(label)
    return ok


def pyc_magic(path):
    """해당 .pyc가 어떤 바이트코드 버전으로 쓰였는지."""
    with open(path, "rb") as fh:
        return struct.unpack("<H", fh.read(2))[0]


def main():
    print(f"PikaPet 환경 점검\n  python: {sys.version.split()[0]} ({sys.executable})\n")

    # 1. 인터프리터. pet.pyc는 바이트코드라서 버전에 협상의 여지가 없다.
    #    매직 넘버가 안 맞으면 import 시점에 맨 ValueError로 실패한다.
    is314 = sys.version_info[:2] == (3, 14)
    check("Python이 3.14", is314,
          "" if is314 else
          f"{sys.version_info.major}.{sys.version_info.minor} 발견. pet.pyc는 3.14 바이트코드")

    pet = os.path.join(RUN, "pet.pyc")
    if check("run/pet.pyc 존재", os.path.isfile(pet)):
        want = struct.unpack("<H", importlib.util.MAGIC_NUMBER[:2])[0]
        got = pyc_magic(pet)
        check("pet.pyc 바이트코드가 이 인터프리터와 일치", got == want,
              f"pet.pyc={got}, 인터프리터={want}")

    # 2. tkinter. Homebrew의 python@3.14는 python-tk@3.14를 따로 깔지 않으면
    #    tkinter 없이 온다. 그리고 이 앱은 전부 tkinter다.
    try:
        import tkinter
        check("tkinter import 가능", True, f"Tk {tkinter.TkVersion}")
    except Exception as exc:
        check("tkinter import 가능", False, f"{type(exc).__name__}: {exc}")

    # 3. 게임이 실제로 import하는 세 패키지
    for mod, pkg in (("PIL", "pillow"), ("pystray", "pystray"), ("websockets", "websockets")):
        try:
            __import__(mod)
            check(f"{pkg} 설치됨", True)
        except Exception as exc:
            check(f"{pkg} 설치됨", False, f"{type(exc).__name__}: {exc}")

    # 4. 플랫폼 계층
    if sys.platform == "darwin":
        for mod in ("Quartz", "AppKit"):
            try:
                __import__(mod)
                check(f"pyobjc {mod} import 가능", True)
            except Exception as exc:
                check(f"pyobjc {mod} import 가능", False, f"{type(exc).__name__}: {exc}")
        check("run/maclayer.py 존재", os.path.isfile(os.path.join(RUN, "maclayer.py")))
        check("run/pikapet_mac.py 존재", os.path.isfile(os.path.join(RUN, "pikapet_mac.py")))
        check("run/overlay.py 존재", os.path.isfile(os.path.join(RUN, "overlay.py")),
              "없으면 펫이 검은 판 위에 그려진다")
        check("run/mactray.py 존재", os.path.isfile(os.path.join(RUN, "mactray.py")),
              "없으면 몬스터볼에 들어간 펫을 꺼낼 수 없다")
        check("run/macnotify.py 존재", os.path.isfile(os.path.join(RUN, "macnotify.py")))
        check("run/macupdate.py 존재", os.path.isfile(os.path.join(RUN, "macupdate.py")),
              "없으면 새 버전이 나와도 알려주지 않는다")
        check("run/macupgrade.py 존재", os.path.isfile(os.path.join(RUN, "macupgrade.py")),
              "없으면 새 버전을 앱이 직접 설치하지 못하고 직접 내려받아야 한다")
        try:
            import UserNotifications  # noqa: F401
            check("pyobjc UserNotifications import 가능", True)
        except Exception as exc:
            check("pyobjc UserNotifications import 가능", False,
                  f"{type(exc).__name__}: 알림 배너가 스크립트 편집기 소유가 된다")
    elif os.name == "nt":
        check("run/winlayer.pyc 존재", os.path.isfile(os.path.join(RUN, "winlayer.pyc")),
              "Windows에서는 게임이 이걸 직접 import한다")

    # 5. 에셋. pet.pyc는 자기 디렉터리를 기준으로 에셋을 찾으므로 run/assets가
    #    실제 디렉터리로 이어져야 한다. Windows에서 그냥 `git clone`하면 심볼릭
    #    링크가 텍스트 파일로 풀리는데, 펫이 비어 보이는 가장 흔한 원인이다.
    for name in ASSET_LINKS:
        link = os.path.join(RUN, name)
        real = os.path.join(ROOT, name)
        if not os.path.exists(link):
            check(f"run/{name} 연결", False, "없음. 설치 스크립트를 다시 실행하세요")
        elif not os.path.isdir(link):
            size = os.path.getsize(link)
            check(f"run/{name} 연결", False,
                  f"디렉터리가 아니라 {size}바이트 파일임 -- git이 심볼릭 링크를 텍스트로 "
                  f"풀었다. 설치 스크립트를 다시 실행하세요")
        else:
            check(f"run/{name} 연결", True,
                  "" if os.path.isdir(real) else "경고: 원본 디렉터리가 없음")

    print()
    if failures:
        print(f"문제 {len(failures)}건: " + ", ".join(failures))
    else:
        print("전부 정상.")
    return len(failures)


if __name__ == "__main__":
    sys.exit(main())
