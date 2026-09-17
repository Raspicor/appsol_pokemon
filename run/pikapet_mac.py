#!/usr/bin/env python3
"""PikaPet를 macOS에서 실행한다.

pet.pyc는 Windows에서 빌드된 바이트코드지만 Windows 전용은 아니다. 자기가 직접
Win32를 부르는 곳이 없고, 플랫폼에 의존하는 것은 전부 `winlayer` 모듈로 보낸다.
그래서 게임을 다시 쓰는 대신, 이 런처가 원본 바이트코드를 그대로 로드한 뒤
Windows 가정이 새어나오는 다섯 곳만 런타임에 패치한다:

  1. `winlayer`        -> 옆에 있는 Quartz/AppKit 구현인 maclayer로 교체.
  2. `-transparentcolor` -> macOS에는 컬러키 투명도가 없으므로, 실제로 존재하는
                          `-transparent` 창 속성으로 번역한다.
  3. `MAGIC`           -> 마젠타 컬러키를 `systemTransparent`로. 번역된 속성이
                          기대하는 값이다. 폴백 경로에서만 적용한다. 아래 오버레이는
                          그 색을 표식으로 읽으므로 손대지 않는다.
  4. `PetApp.setup_tray` -> pystray의 macOS 백엔드는 `NSApplication.run()`을
                          부르는데 이건 메인 스레드 전용이다. PikaPet은 이를 데몬
                          스레드에서 시작해 프로세스가 즉사한다. 알림을 살린 대역과,
                          트레이에만 있던 동작을 담은 메뉴 바 항목(mactray.py)으로
                          교체.
  5. 스프라이트 프레임이 올라가는 마젠타 판 -> 창이 실제로 그리는 색으로. 색이
                          렌더 경로의 리터럴이라 패치 3으로는 닿지 않는다.

투명도는 이 패치들에 들어가지 않는다. aqua의 Tk로는 불가능하기 때문이다. Tk 9는
모든 toplevel을 알파 채널 없는 백킹 스토어에 렌더링하므로 `-transparent`,
`systemTransparent`, non-opaque NSWindow 어느 것도 결국 꽉 찬 사각형으로 합성된다.
그래서 스프라이트는 Tk 창 위에 겹쳐놓은 네이티브 AppKit 창이 그린다 — 측정 근거는
overlay.py에 있다. 패치 5가 그 오버레이에 진짜 알파를 가진 판을 넘긴다. AppKit을
쓸 수 없으면 불투명 창 위의 검은 판으로 되돌아가고, 그게 이 포팅의 예전 동작이다.

pet.pyc에 아무것도 되쓰지 않으므로 패치가 게임과 어긋날 수 없고, 디컴파일 결과가
완벽한지에도 의존하지 않는다.

    ./pikapet_mac.py
"""

import importlib.util
import os
import subprocess
import sys
import tkinter as tk

def _here():
    """pet.pyc와 에셋이 있는 디렉터리.

    소스에서 돌 때는 이 파일이 있는 run/ 이다. .app으로 묶으면 PyInstaller가
    데이터 파일을 풀어놓은 곳(`sys._MEIPASS`)이 되는데, 그건 pet.pyc 자신이
    frozen일 때 RESOURCE_DIR로 쓰는 값과 같다. 이 앱은 원래 PyInstaller
    onefile 번들이었으므로 그 분기가 바이트코드에 그대로 살아 있다.
    """
    if getattr(sys, "frozen", False):
        return getattr(sys, "_MEIPASS",
                       os.path.dirname(os.path.abspath(sys.executable)))
    return os.path.dirname(os.path.abspath(__file__))


HERE = _here()


# --------------------------------------------------------------------------
# 1. 환경: PikaPet은 Windows 프로필 환경변수를 찾는다
# --------------------------------------------------------------------------

def install_save_paths():
    """%APPDATA%/%LOCALAPPDATA%를 macOS의 통상 위치로 돌린다.

    pet.pyc는 이 값들로 저장 디렉터리를 만든다. 둘 다 비어 있을 때의 폴백은
    pet_state.json을 실행 파일 옆 — 즉 앱 폴더 안 — 에 두는데, 거기 두면 쉽게
    잃어버린다.
    """
    default = os.path.expanduser("~/Library/Application Support")
    os.environ.setdefault("APPDATA", default)
    os.environ.setdefault("LOCALAPPDATA", default)


# --------------------------------------------------------------------------
# 2. 투명도
# --------------------------------------------------------------------------

def install_transparency_shim():
    """Windows 컬러키 투명도를 macOS의 대응물로 번역한다.

    Windows에서 펫은 마젠타 픽셀을 전부 뚫어달라고 Tk에 요청한다:

        win.attributes('-transparentcolor', '#ff00ff')
        win.config(bg='#ff00ff')

    macOS Tk에는 그런 속성이 없어서 TclError가 난다. PikaPet이 그걸 잡기는 하는데,
    `Companion.__init__`에서는 라벨 생성이 같은 try 블록 안에 있다. 그래서 예외가
    나면 동료 창에 스프라이트가 붙지 않는다. 예외를 내버려두지 않고 호출 자체를
    번역하면 그 경로들이 전부 온전히 남는다.
    """
    original = tk.Wm.wm_attributes

    def wm_attributes(self, *args, **kwargs):
        if args and args[0] == "-transparentcolor":
            try:
                return original(self, "-transparent", True)
            except tk.TclError:
                return None
        return original(self, *args, **kwargs)

    tk.Wm.wm_attributes = wm_attributes
    tk.Wm.attributes = wm_attributes


TRANSPARENCY_NOTES = {
    "native": "켜짐 (스프라이트를 AppKit이 그림, 배경이 비침)",
    "opaque": "꺼짐 (AppKit 없음, 펫이 검은 판 위에 놓임)",
    "none": "꺼짐 (불투명 펫 창)",
}


def transparency_mode(master):
    """이 machine에서 펫의 배경을 어떻게 처리할지.

    "native" -- overlay.py가 AppKit 창으로 스프라이트를 그린다. 여기서 진짜
                투명도를 얻는 유일한 방법이다. aqua의 Tk는 무엇을 요청해도
                toplevel을 꽉 찬 사각형으로 합성한다 (Tk 9.0.4 / macOS 26에서
                위젯 종류, override-redirect, `-alpha`, `-stylemask`,
                `MacWindowStyle`, non-opaque NSWindow 전부 실측. Tk 8.6.18은
                반대로 창을 통째로 뚫어버린다).
    "opaque" -- pyobjc가 없어서, 스프라이트 판을 창이 그리는 검정과 같은 색으로
                칠하고 펫은 사각형 위에 놓인다.
    "none"   -- Tk가 투명도 속성 자체를 거부한다.

    PIKAPET_OVERLAY=0으로 예전 동작을 강제할 수 있다. 아직 본 적 없는 디스플레이
    구성에서 오버레이가 말썽을 부릴 때를 위한 탈출구다.
    """
    if not transparency_is_available(master):
        return "none"
    if os.environ.get("PIKAPET_OVERLAY") == "0":
        return "opaque"
    try:
        import overlay
    except Exception:
        return "opaque"
    return "native" if overlay.available() else "opaque"


def transparency_is_available(master):
    """이 Tk가 투명도 속성과 색을 애초에 받아주는지.

    가정하지 않고 버릴 창으로 직접 찔러본다. 거부하는 Tk에서 MAGIC을
    `systemTransparent`로 바꿔버리면 모든 펫 창의 설정이 실패하기 때문이다.
    """
    probe = None
    try:
        probe = tk.Toplevel(master)
        probe.withdraw()
        probe.wm_attributes("-transparent", True)
        probe.config(bg="systemTransparent")
        return True
    except Exception:
        return False
    finally:
        if probe is not None:
            try:
                probe.destroy()
            except Exception:
                pass


# 스프라이트를 네이티브로 그릴 수 없을 때 배경이 되는 색. Tk는 투명 창의 배경을
# 불투명한 검정으로 칠하고, 아래의 판은 그 색과 정확히 같아야 한다. 아니면 펫이
# 눈에 보이는 다른 색 사각형 안에 앉는다.
BACKDROP = (0, 0, 0)


def install_sprite_alpha_patch(transparent=False):
    """스프라이트 판을 마젠타에서 창이 실제로 보여주는 색으로 바꾼다.

    `Companion.step`과 `PetApp.redraw`는 둘 다 프레임을 Windows 방식으로 만든다
    (pet.py:4264, pet.py:7252):

        resized.putalpha(alpha)                       # 0 또는 255로 이진화
        bg = Image.new('RGB', (w, h), (255, 0, 255))
        bg.paste(resized, (0, 0), resized)
        ImageTk.PhotoImage(bg)

    Windows에서는 창의 `-transparentcolor` 키가 합성 시점에 그 마젠타 픽셀을
    지워버리므로 판이 보일 일이 없다. macOS에는 컬러키가 없고 — `-transparent`는
    위젯 배경만 비운다 — 판이 그대로 살아남아 펫이 마젠타 상자 안에 앉는다.

    패치 3으로는 여기 닿지 못한다. 색이 `MAGIC` 전역이 아니라 바이트코드 안의
    리터럴 `(255, 0, 255)` 튜플이기 때문이다. 이 두 곳이 pet.pyc에 있는
    `(255, 0, 255)` 상수 전부이므로, 모드와 색으로 거르면 다른 것이 걸릴 수 없다.

    `transparent`를 주면 판이 아무것도 없는 진짜 RGBA가 되어, 합성된 프레임이
    스프라이트의 알파를 overlay.py까지 그대로 들고 간다. 그게 정상 경로다.

    이 옵션이 없으면 판은 **불투명**이어야 한다. 투명 판만으로도 마젠타는 사라지지만,
    Tk가 직접 그리는 경우에는 애니메이션이 깨진다. 그때는 프레임이 자기 불투명
    픽셀만 쓰고, Tk는 non-opaque 창을 지우지 않으므로, 매 프레임이 이전 프레임 위에
    합성돼 펫이 지난 자세들의 뭉개짐으로 번진다. 판을 BACKDROP — 창이 이미 그리는
    바로 그 색 — 으로 채우면 매 프레임 위젯 전체를 다시 칠하게 되고, 사각형은 자기
    배경에 묻혀 보이지 않는다.
    """
    from PIL import Image

    original = Image.new

    def new(mode, size, color=0, *args, **kwargs):
        if mode == "RGB" and color == (255, 0, 255):
            if transparent:
                return original("RGBA", size, (0, 0, 0, 0), *args, **kwargs)
            return original(mode, size, BACKDROP, *args, **kwargs)
        return original(mode, size, color, *args, **kwargs)

    Image.new = new


# --------------------------------------------------------------------------
# 3. 트레이 아이콘
# --------------------------------------------------------------------------

class MacTray:
    """PetApp이 기대하는 pystray 아이콘 자리를 대신한다.

    PikaPet이 실제로 건드리는 멤버는 `notify`, `update_menu`, `icon`, `stop`
    네 개뿐이고, 호출마다 `if self.tray_icon:`으로 감싼다. 그래서 속성을 None으로
    두면 모든 알림이 조용히 사라진다. 이 객체는 truthy를 유지하면서 알림을 알림
    센터로 넘긴다.

    메뉴는 여기서 다시 구현하지 않는다. PikaPet은 이미 `PetApp.build_menu`에서
    완전한 우클릭 메뉴 — 스킬, 훈련, 도감, 일일 퀘스트, 설정, 종료 — 를 만들어
    펫 자신에게 붙이므로, macOS에서 트레이 사본은 군더더기였다.
    """

    def __init__(self, app):
        self._app = app
        self.icon = None            # PetApp이 PIL 이미지를 넣는 자리. 쓰이지 않음
        self.visible = False

    def notify(self, message, title="PikaPet"):
        """Tk 이벤트 루프를 막지 않고 알림 센터에 띄운다."""
        try:
            if _deliver_notification(message, title):
                return
        except Exception:
            pass
        try:
            script = 'display notification {} with title {}'.format(
                _applescript_string(message), _applescript_string(title))
            subprocess.Popen(["osascript", "-e", script],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    def update_menu(self):
        """할 일 없음. 우클릭 메뉴는 클릭마다 처음부터 다시 만들어진다."""

    def stop(self):
        """할 일 없음. 내려야 할 백그라운드 트레이 스레드가 없다."""


def _deliver_notification(message, title):
    """이 프로세스 소유의 배너를 띄운다. 나갔으면 True.

    `osascript -e 'display notification'`이 뻔한 방법이지만, 그렇게 띄운 배너는
    스크립트 편집기 소유가 된다. 그래서 하나를 클릭하면 — 야생 포켓몬 알림 같은
    것 — 펫이 아니라 스크립트 편집기가 올라온다. 프레임워크를 직접 거치면 배너가
    실행 중인 인터프리터에 귀속되므로, 클릭했을 때 우리만 활성화된다.

    NSUserNotificationCenter는 macOS 11부터 deprecated지만 아직 배달된다.
    `MacTray.notify`의 osascript 경로는 이게 끝내 멈추는 릴리스를 위한 폴백으로
    남겨둔다.
    """
    from Foundation import NSUserNotification, NSUserNotificationCenter

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    if center is None:
        return False
    note = NSUserNotification.alloc().init()
    note.setTitle_(str(title))
    note.setInformativeText_(str(message))
    center.deliverNotification_(note)
    return True


def _applescript_string(text):
    """AppleScript 소스에 끼워 넣을 수 있게 파이썬 문자열을 인용한다."""
    escaped = str(text).replace("\\", "\\\\").replace('"', '\\"')
    escaped = escaped.replace("\r", " ").replace("\n", " ")
    return '"' + escaped + '"'


def install_window_patch(pet):
    """PikaPet이 진짜 루트 창을 만든 뒤에 투명도를 결정한다.

    main()은 PetApp을 만들기 바로 전에 setup_pet_window(root)를 부른다. Tk 루트가
    처음 존재하는 순간이면서, bg=MAGIC으로 위젯이 만들어지기 전 마지막 순간이다.
    """
    original = pet.setup_pet_window

    def setup_pet_window(root):
        mode = transparency_mode(root)
        if mode == "native":
            # MAGIC은 게임 본래의 '#ff00ff'로 일부러 남겨둔다. 오버레이가 그것을
            # "이 창은 투명해지고 싶다"는 표식으로 쓰는데, 거기엔 Tk의 지원이
            # 전혀 필요하지 않다. 두 훅 모두 원본이 돌기 전에 걸려 있어야 한다.
            # 원본의 마지막 줄이 root.config(bg=MAGIC), 바로 그 감시 대상이다.
            import overlay

            install_sprite_alpha_patch(transparent=True)
            overlay.install(root, pet.MAGIC)
        elif mode != "none":
            pet.MAGIC = "systemTransparent"
            install_sprite_alpha_patch(transparent=False)
        print(f"  투명도: {TRANSPARENCY_NOTES[mode]}", flush=True)
        return original(root)

    pet.setup_pet_window = setup_pet_window


def install_tray_replacement(pet):
    def setup_tray(self):
        self._pystray = None
        self.tray_icon = MacTray(self)
        install_menu_bar(self)

    setup_tray.__doc__ = MacTray.__doc__
    pet.PetApp.setup_tray = setup_tray


def install_menu_bar(app):
    """트레이에만 있던 동작을 메뉴 바 항목으로 되살린다.

    `PetApp.build_menu`의 우클릭 메뉴가 트레이를 거의 다 덮지만, 셋이 빠진다:
    `exit_ball`, `_open_pending_encounter`, `_restore_battle_window`. 그중
    `exit_ball`이 없으면 펫이 몬스터볼에 들어간 순간 창이 숨어서 우클릭할 대상이
    사라지고, 두 번 다시 꺼낼 수 없다. 야생 포켓몬 알림은 아예 트레이 아이콘을
    클릭하라고 안내한다.

    실패해도 게임은 그대로 돌아간다. setup_tray 안에서 예외가 나가면 PetApp 생성이
    깨지므로 여기서 삼킨다.
    """
    root = getattr(app, "root", None)
    if root is None:
        print("  메뉴 바: self.root가 아직 없어 건너뜀", flush=True)
        return None
    try:
        import mactray

        if not mactray.available():
            print("  메뉴 바: AppKit을 쓸 수 없어 건너뜀", flush=True)
            return None
        app._pikapet_menu_bar = mactray.install(app, root)
        print("  메뉴 바: ◓ 항목 추가 (몬스터볼 꺼내기 / 야생 포켓몬 / 배틀 복구)",
              flush=True)
        return app._pikapet_menu_bar
    except Exception as exc:
        print(f"  메뉴 바 생성 실패: {type(exc).__name__}: {exc}", flush=True)
        return None


# --------------------------------------------------------------------------
# 4. 우클릭
# --------------------------------------------------------------------------

def install_right_click_fallback():
    """오른쪽이 버튼 2인 Tk 빌드에서도 <Button-3> 바인딩이 먹게 한다.

    Tk 9는 플랫폼별 마우스 버튼을 통일했다 — `tk.tcl`이 모든 윈도잉 시스템에서
    <<ContextMenu>>를 <Button-3>으로 매핑한다 — 그래서 PikaPet의 기존 바인딩이
    그대로 동작한다. aqua의 Tk 8.6은 우클릭을 버튼 2로 보고했으므로, 그런 빌드에서는
    메뉴가 아예 열리지 않는다.
    """
    if tk.TkVersion >= 9.0:
        return False

    original = tk.Misc.bind

    def bind(self, sequence=None, func=None, add=None):
        result = original(self, sequence, func, add)
        if isinstance(sequence, str) and "Button-3" in sequence:
            original(self, sequence.replace("Button-3", "Button-2"), func, "+")
        return result

    tk.Misc.bind = bind
    return True


# --------------------------------------------------------------------------
# pet.pyc 로드
# --------------------------------------------------------------------------

def load_pet():
    """pet.pyc를 __main__ 블록 실행 없이 모듈로 import한다."""
    path = os.path.join(HERE, "pet.pyc")
    if not os.path.exists(path):
        sys.exit(f"{__file__} 옆에 pet.pyc가 없습니다")
    spec = importlib.util.spec_from_file_location("pet", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["pet"] = module
    spec.loader.exec_module(module)
    return module


def main():
    if sys.platform != "darwin":
        sys.exit("pikapet_mac.py는 macOS용입니다. 다른 곳에서는 pet.pyc를 직접 실행하세요.")

    sys.path.insert(0, HERE)        # pet.pyc가 spriteanim.pyc를 찾도록
    install_save_paths()

    import maclayer
    sys.modules["winlayer"] = maclayer   # pet.pyc가 `import winlayer`를 돌기 전에

    install_transparency_shim()
    remapped_buttons = install_right_click_fallback()

    pet = load_pet()
    install_window_patch(pet)
    install_tray_replacement(pet)

    print(f"macOS PikaPet | Tk {tk.TkVersion} | 메뉴: 펫을 우클릭"
          + (" | Button-3을 Button-2에도 연결" if remapped_buttons else ""),
          flush=True)

    pet.main()


if __name__ == "__main__":
    main()
