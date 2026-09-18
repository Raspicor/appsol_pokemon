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


# Windows Tk의 TkDefaultFont는 {Segoe UI} 9 인데, aqua에서는 시스템 폰트 10이다.
# 더 크고 더 넓다. PikaPet은 버튼 폭을 `width=N` 으로 주고 Tk에서 그 단위는
# 픽셀이 아니라 **문자 수**이므로, 기본 폰트가 넓어지면 버튼 줄이 통째로 넓어진다.
# compact 전투 창은 게임이 300x380으로 하드코딩해서 여유가 없다. 실측(전투 창의
# 내용 프레임 요청 폭 대 캔버스 292px):
#
#     시스템 폰트 10  ->  309px  (17px 넘침, 내용이 x=-17 로 밀려 왼쪽이 잘린다)
#     시스템 폰트  9  ->  295px  ( 3px 넘침)
#     시스템 폰트  8  ->  281px  (넘치지 않음)
#
# 그래서 8로 내린다. 게임은 글자 있는 라벨 대부분에 ('맑은 고딕', N) 을 직접
# 지정하므로 이 값이 닿는 곳은 사실상 폰트를 안 준 위젯 — 즉 버튼 — 뿐이고,
# 그게 정확히 넘치던 자리다.
DEFAULT_FONT_SIZE = 8


def install_font_defaults(root):
    """기본 폰트를 Windows 레이아웃이 가정하는 비율로 맞춘다.

    게임이 위젯을 만들기 전에 불러야 한다. 실패해도 그냥 넘어간다. 레이아웃이
    조금 넘치는 것이 앱이 안 뜨는 것보다 낫다.
    """
    try:
        from tkinter import font as tkfont

        current = tkfont.nametofont("TkDefaultFont", root=root)
        before = current.actual("size")
        if before <= DEFAULT_FONT_SIZE:
            return before
        current.configure(size=DEFAULT_FONT_SIZE)
        return before
    except Exception as exc:
        print(f"  기본 폰트 조정 실패: {type(exc).__name__}: {exc}", flush=True)
        return None


def install_font_defaults_everywhere():
    """새 Tk 루트가 생길 때마다 기본 폰트를 맞춘다.

    `setup_pet_window` 에서만 부르면 **스타터 선택 창을 놓친다.** 게임은 세이브가
    없을 때 `PetApp` 보다 먼저 별도의 `tk.Tk()` 를 만들어 거기에 선택 창을 그린다
    (pet.py:19067). 그 창은 `geometry('860x380')` 로 크기가 고정돼 있는데, 실측하면
    내용이 **930x262** 를 요구한다 -- 가로 70px 이 넘쳐서 다섯 번째 포켓몬(이브이)
    의 시작 버튼이 오른쪽에서 잘린다. 폰트를 맞추면 790x260 이 되어 들어간다.

    `TkDefaultFont` 는 인터프리터마다 따로 있으므로 루트마다 걸어야 한다.
    `install_font_defaults` 는 이미 작아져 있으면 그냥 돌아오니 여러 번 불려도
    괜찮다.
    """
    original = tk.Tk.__init__

    def __init__(self, *args, **kw):
        original(self, *args, **kw)
        try:
            install_font_defaults(self)
        except Exception:
            # 폰트가 조금 넘치는 것이 앱이 안 뜨는 것보다 낫다.
            pass

    tk.Tk.__init__ = __init__
    return original


def _restore_titlebar(win):
    """overrideredirect를 끈 Tk 창에 macOS 타이틀바를 돌려준다.

    aqua의 Tk는 `overrideredirect(True)` 로 장식을 떼어낸 창에서 그것을 다시
    끄면 Tk 쪽 플래그만 바뀌고 NSWindow의 styleMask는 그대로 둔다. 실측:
    styleMask 78 -> 14 로 갈 뿐 titled 비트가 돌아오지 않고, withdraw/deiconify
    로 다시 매핑해도 마찬가지다. 그러면 타이틀바도 없고 게임이 compact 창에
    걸어두는 드래그 바인딩도 없는 창이 되어 **아예 움직일 수 없다**. 로켓단
    습격에서 "화면 키우기"를 누르면 정확히 그 상태가 된다.

    그래서 styleMask를 직접 복원한다. Windows에서 이 창이 갖는 것과 같은,
    끌 수 있는 네이티브 타이틀바가 생긴다.
    """
    try:
        import AppKit

        titled = getattr(AppKit, "NSWindowStyleMaskTitled", 1)
        closable = getattr(AppKit, "NSWindowStyleMaskClosable", 2)
        mini = getattr(AppKit, "NSWindowStyleMaskMiniaturizable", 4)

        width, height = win.winfo_width(), win.winfo_height()
        if width < 40 or height < 40:
            return
        best = None
        for ns in AppKit.NSApp().windows():
            frame = ns.frame()
            if (abs(int(frame.size.width) - width) <= 6
                    and abs(int(frame.size.height) - height) <= 6):
                gap = abs(int(frame.origin.x) - win.winfo_rootx())
                if best is None or gap < best[0]:
                    best = (gap, ns)
        if best is None:
            return
        ns = best[1]
        if ns.styleMask() & titled:
            return
        ns.setStyleMask_(ns.styleMask() | titled | closable | mini)
        try:
            ns.setTitle_(win.title())
        except Exception:
            pass
    except Exception:
        pass


def install_titlebar_restore():
    """`overrideredirect(False)` 뒤에 타이틀바를 되살리도록 Tk를 훅한다.

    창이 다시 매핑된 뒤에 손대야 하므로 after_idle로 미룬다. 실패해도 조용히
    넘어간다. 창을 못 옮기는 것이 앱이 죽는 것보다는 낫다.
    """
    original = tk.Wm.wm_overrideredirect

    def wm_overrideredirect(self, boolean=None):
        result = original(self, boolean)
        if boolean is not None and not boolean:
            try:
                self.after_idle(lambda: _restore_titlebar(self))
            except Exception:
                pass
        return result

    tk.Wm.wm_overrideredirect = wm_overrideredirect
    tk.Wm.overrideredirect = wm_overrideredirect


# --------------------------------------------------------------------------
# 2-c. 기호 글리프
# --------------------------------------------------------------------------
# macOS 시스템 폰트에는 U+2694(⚔)의 쓸 만한 텍스트 글리프가 없다. Tk는 이걸
# 두부 박스로도 안 그리고 -- 그랬으면 눈에 띄었을 텐데 -- 머리카락처럼 가는
# 글리프로 떨어뜨린다. 게임이 쓰는 9px에서는 그냥 작은 × 하나로 보여서
# '⚔ Fight' 버튼이 '× Fight' 가 된다. Windows에서는 맑은 고딕의 폰트 링크가
# 이걸 제대로 된 칼 그림으로 그린다.
#
# VS16(U+FE0F)을 붙이면 이모지 표현이 되고, 그러면 Tk가 Apple Color Emoji로
# 폴백해서 칼 두 자루가 제대로 나온다. 게임 코드에도 이미 한 군데
# ('⚔️\nVS') 는 VS16이 붙어 있다 -- 원작자도 알고 있었던 것 같다.
#
# 대상을 ⚔ 하나로 좁힌 근거: 게임 문자열에 쓰인 기호 134종을 전부 9px bold로
# 그려서 잉크 픽셀을 셌다. 망가지는 건 ⚔ 뿐이다 (잉크 20, VS16을 붙이면 65).
# ▶ ↩ ⚙ ⬇ 같은 것들은 모노크롬으로 멀쩡히 나오므로 건드리지 않는다 -- 그걸
# 이모지로 바꾸는 건 고치는 게 아니라 취향을 바꾸는 것이다.
BROKEN_GLYPHS = {"\u2694": "\u2694\ufe0f"}

# 사람이 읽는 글자가 들어가는 옵션만 손댄다. 다른 옵션에 저 문자가 들어갈 일은
# 없지만, 폭이 좁을수록 사고가 적다.
TEXT_OPTIONS = frozenset(("text", "label", "title"))


def _fix_glyphs(value):
    """표시용 문자열에서 macOS가 못 그리는 기호를 이모지 표현으로 바꾼다."""
    for bad, good in BROKEN_GLYPHS.items():
        if bad in value and good not in value:
            value = value.replace(bad, good)
    return value


def install_glyph_fix():
    """모든 위젯의 텍스트 옵션에 글리프 보정을 건다.

    `Misc._options` 는 tkinter가 파이썬 키워드를 Tcl 옵션으로 바꾸는 단 하나의
    길목이다. Widget.__init__, Misc.configure, Menu.add, Canvas._create 가 전부
    여기를 지난다. 그래서 위젯 종류마다 훅을 거는 대신 이 하나만 감싼다.
    ⚔ 는 버튼 10곳, 라벨 6곳, 메뉴 항목에도 나오므로 그 전부가 필요하다.
    """
    original = tk.Misc._options

    def _options(self, cnf, kw=None):
        try:
            if kw:
                for key in TEXT_OPTIONS:
                    v = kw.get(key)
                    if isinstance(v, str):
                        kw[key] = _fix_glyphs(v)
            if isinstance(cnf, dict):
                for key in TEXT_OPTIONS:
                    v = cnf.get(key)
                    if isinstance(v, str):
                        cnf[key] = _fix_glyphs(v)
        except Exception:
            pass
        return original(self, cnf, kw)

    tk.Misc._options = _options


# --------------------------------------------------------------------------
# 2-d. 색 있는 버튼
# --------------------------------------------------------------------------
# aqua의 tk.Button은 -background 를 **완전히 무시한다**. 네이티브 버튼을 그리고
# 색은 버린다. bd=0, relief=flat, highlightthickness=0 을 어떻게 섞어도 같다
# (여섯 조합을 그려서 확인했다). highlightbackground 는 버튼 둘레에 얇은 테를
# 두를 뿐 버튼 면은 여전히 하얗다.
#
# 게임에서 버튼은 181개인데 그중 색을 주는 건 8개뿐이고, 7개가 같은 노란색
# '#ffd54a' 액션 버튼이다 -- 야생 포켓몬 토스트의 '⚔ Fight', 배틀의 '⚔ 공격',
# '⚔ 스테이지 N 도전!', 선물 '🎁 보러가기', 확인 버튼들. Windows에서는 노란
# 버튼이고 macOS에서는 다른 버튼과 구별되지 않는 흰 버튼이 된다.
#
# 그래서 색을 준 버튼만 Label로 흉내 낸다. Label은 배경색을 그대로 칠한다.
# 나머지 173개는 진짜 tk.Button 그대로 두어 네이티브 모양을 지킨다. 게임은
# 위젯에 isinstance 도 winfo_class 도 쓰지 않으므로 (disasm으로 확인) 바꿔치기가
# 보이지 않는다.

# 눌렀을 때 얼마나 어두워지는가. 값이 클수록 눌린 티가 난다.
PRESS_DARKEN = 0.82
HOVER_LIGHTEN = 1.06

# 실측: 이 여백을 주면 같은 text/font/width 로 만든 네이티브 버튼과
# 요청 크기가 정확히 같아진다.
BUTTON_PADX = 17
BUTTON_PADY = 5


def _shade(color, factor):
    """#rrggbb 를 factor 배로 밝게/어둡게. 실패하면 원래 색."""
    try:
        if not (isinstance(color, str) and color.startswith("#") and len(color) == 7):
            return color
        parts = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
        return "#%02x%02x%02x" % tuple(
            max(0, min(255, int(round(p * factor)))) for p in parts)
    except Exception:
        return color


def _is_light(color):
    """#rgb / #rrggbb 가 밝은 색인가. 판단할 수 없으면 밝다고 본다.

    판단이 안 될 때 밝다고 보는 이유: 그러면 검은 글자가 나오고, 게임이 쓰는
    배경은 대부분 밝다. 반대로 틀리면 흰 배경에 흰 글자가 된다.
    """
    try:
        if not (isinstance(color, str) and color.startswith("#")):
            return True
        if len(color) == 4:                       # #eee -> #eeeeee
            color = "#" + "".join(ch * 2 for ch in color[1:])
        if len(color) != 7:
            return True
        r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
        return (0.299 * r + 0.587 * g + 0.114 * b) > 140
    except Exception:
        return True


class MacColorButton(tk.Label):
    """배경색을 실제로 칠하는 버튼. aqua의 tk.Button 대용.

    tk.Button과 Label은 옵션이 거의 같다 (text/font/bg/fg/width/state/anchor/
    justify/wraplength/relief/bd/padx/pady/image/compound). 다른 것은 `command`와
    `invoke()`/`flash()` 뿐이라, 그 셋만 얹으면 게임 쪽에서는 버튼과 구별되지
    않는다.
    """

    def __init__(self, master=None, cnf=None, **kw):
        kw = dict(cnf or {}, **kw)
        self._command = kw.pop("command", None)
        # Button에만 있고 Label에는 없는 옵션들. 조용히 버린다.
        for gone in ("default", "overrelief", "repeatdelay", "repeatinterval"):
            kw.pop(gone, None)

        bg = kw.get("bg", kw.get("background"))
        # 진짜 tk.Button의 기본 글자색은 검정이다. Label의 기본은
        # systemTextColor 라서, 그냥 두면 다크 모드에서 노란 버튼 위에 흰
        # 글자가 찍혀 읽을 수 없게 된다. 배경 밝기를 보고 정한다.
        if "fg" not in kw and "foreground" not in kw:
            kw["fg"] = "#111111" if _is_light(bg) else "#ffffff"
        # 네이티브 aqua 버튼과 같은 자리를 차지하게 맞춘 값이다. 안 맞추면
        # 색 버튼만 14x2 px 작아서, 옆에 선 네이티브 버튼과 줄이 어긋난다.
        kw.setdefault("padx", BUTTON_PADX)
        kw.setdefault("pady", BUTTON_PADY)
        kw.setdefault("relief", "flat")
        kw.setdefault("bd", 0)
        kw.setdefault("cursor", "pointinghand")
        kw.setdefault("highlightthickness", 1)
        kw.setdefault("highlightbackground", _shade(bg, 0.78))
        super().__init__(master, **kw)

        self._base_bg = bg
        self.bind("<Enter>", self._on_enter, add="+")
        self.bind("<Leave>", self._on_leave, add="+")
        self.bind("<ButtonPress-1>", self._on_press, add="+")
        self.bind("<ButtonRelease-1>", self._on_release, add="+")

    # -- 눌린 느낌 ---------------------------------------------------------

    def _enabled(self):
        try:
            return str(self.cget("state")) != "disabled"
        except Exception:
            return True

    def _paint(self, factor):
        if self._base_bg and self._enabled():
            try:
                tk.Label.configure(self, bg=_shade(self._base_bg, factor))
            except Exception:
                pass

    def _on_enter(self, _event=None):
        self._paint(HOVER_LIGHTEN)

    def _on_leave(self, _event=None):
        self._paint(1.0)

    def _on_press(self, _event=None):
        self._paint(PRESS_DARKEN)

    def _on_release(self, event=None):
        self._paint(HOVER_LIGHTEN)
        # 버튼 밖에서 손을 떼면 취소. 진짜 버튼과 같은 동작이다.
        if event is not None:
            if not (0 <= event.x < self.winfo_width()
                    and 0 <= event.y < self.winfo_height()):
                self._paint(1.0)
                return
        self.invoke()

    # -- 버튼 API ----------------------------------------------------------

    def invoke(self):
        if self._command is None or not self._enabled():
            return None
        return self._command()

    def flash(self):
        for factor in (PRESS_DARKEN, 1.0, PRESS_DARKEN, 1.0):
            self._paint(factor)
            self.update_idletasks()

    def configure(self, cnf=None, **kw):
        kw = dict(cnf or {}, **kw)
        if "command" in kw:
            self._command = kw.pop("command")
        for gone in ("default", "overrelief", "repeatdelay", "repeatinterval"):
            kw.pop(gone, None)
        new_bg = kw.get("bg", kw.get("background"))
        if new_bg:
            self._base_bg = new_bg
        if not kw:
            return None
        return tk.Label.configure(self, **kw)

    config = configure

    def cget(self, key):
        if key == "command":
            return self._command
        return tk.Label.cget(self, key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def __getitem__(self, key):
        return self.cget(key)


def install_button_colors():
    """배경색을 준 tk.Button만 MacColorButton으로 바꿔치기한다.

    게임은 `tk.Button(...)` 으로 부르고 이름은 호출할 때 tkinter 모듈에서
    찾으므로, 모듈 속성을 갈아끼우면 그대로 걸린다. 색을 안 주는 버튼은
    진짜 tk.Button을 돌려줘서 네이티브 모양을 지킨다.
    """
    original = tk.Button

    def Button(master=None, cnf=None, **kw):
        merged = dict(cnf or {}, **kw)
        bg = merged.get("bg", merged.get("background"))
        if isinstance(bg, str) and bg.startswith("#"):
            try:
                return MacColorButton(master, **merged)
            except Exception:
                pass
        return original(master, cnf or {}, **kw)

    Button.__doc__ = MacColorButton.__doc__
    tk.Button = Button
    return original

# --------------------------------------------------------------------------
# 2-e. 앱(Dock) 아이콘
# --------------------------------------------------------------------------
# 게임은 시작할 때 `win.iconphoto(True, <펫 스프라이트>)` 를 부른다
# (`_setup_taskbar_icon`, pet.py:17476). Windows에서는 그 창의 작업표시줄
# 아이콘을 펫으로 바꾸는, 의도한 동작이다.
#
# aqua에서는 그게 **앱 아이콘 자체**를 갈아치운다. 그래서 Dock의 PikaPet이
# 몬스터볼에서 파이리가 된다. `-default` 를 떼는 것으로는 못 막는다 -- 실측:
#
#     setApplicationIconImage_(447px)  ->  앱 아이콘 447x447
#     iconphoto(False, 32px)           ->  앱 아이콘 32x32   <- default 없이도 바뀐다
#     iconphoto(True,  32px)           ->  앱 아이콘 32x32
#
# macOS 창에는 애초에 타이틀바 아이콘이 없으므로 (문서 창의 프록시 아이콘을
# 빼면) 이 호출이 창에 해주는 일은 없다. 그래서 원본은 그대로 부르고, 직후에
# 앱 아이콘만 우리 것으로 되돌린다.

# 소스에서 그냥 실행할 때 쓸 아이콘. 번들에서는 .icns가 이미 붙어 있지만,
# 게임이 덮어쓴 뒤 되돌리려면 어차피 이미지가 필요하다.
ICON_CANDIDATES = (
    os.path.join(HERE, "..", "Resources", "PikaPet.icns"),   # .app 안
    os.path.join(HERE, "..", "tools", "icon.png"),           # 저장소에서 실행
)

_app_icon = None            # 한 번 읽어서 들고 있는 NSImage


def app_icon_image():
    """앱 아이콘 NSImage. 못 찾으면 None."""
    global _app_icon
    if _app_icon is not None:
        return _app_icon
    try:
        import AppKit

        for path in ICON_CANDIDATES:
            path = os.path.abspath(path)
            if not os.path.exists(path):
                continue
            image = AppKit.NSImage.alloc().initWithContentsOfFile_(path)
            if image is not None:
                _app_icon = image
                return image
    except Exception as exc:
        print(f"  앱 아이콘 읽기 실패: {type(exc).__name__}: {exc}", flush=True)
    return None


def set_app_icon():
    """Dock 아이콘을 몬스터볼로 맞춘다. 아이콘이 없으면 그냥 넘어간다."""
    image = app_icon_image()
    if image is None:
        return False
    try:
        import AppKit

        AppKit.NSApp().setApplicationIconImage_(image)
        return True
    except Exception:
        return False


def install_app_icon_guard():
    """`iconphoto` 가 Dock 아이콘을 갈아치우면 곧바로 되돌린다."""
    original = tk.Wm.wm_iconphoto

    def wm_iconphoto(self, *args, **kw):
        result = original(self, *args, **kw)
        set_app_icon()
        return result

    tk.Wm.wm_iconphoto = wm_iconphoto
    tk.Wm.iconphoto = wm_iconphoto

# --------------------------------------------------------------------------
# 2-f. 검은 테두리와 안 보이는 글자
# --------------------------------------------------------------------------
# macOS의 시스템 색은 다크 모드를 따라간다. 게임은 Windows의 밝은 기본값을
# 전제로 색을 고르므로, 다크 모드에서 두 가지가 깨진다.
#
# **(1) 위젯마다 검은 테두리.** aqua 위젯은 네이티브 베젤 바깥 영역을
# `-highlightbackground` 로 칠하는데, 기본값이 systemWindowBackgroundColor,
# 즉 다크 모드에서 거의 검정이다. 그래서 크림색(#fff6e0) 전투 창 위의 버튼마다
# 검은 사각형이 둘러진다. 실측: 버튼 경계에 #1c1c1c 가 4px, 그 안쪽이 흰 베젤.
# 옵션 조합을 그려서 확인했을 때, `bg` 만 준 버튼은 검은 테가 남고
# `highlightbackground` 를 준 버튼만 그 테가 해당 색으로 바뀌었다. 그러니
# **그 옵션이 그 띠를 칠한다**. 부모의 배경색을 넣어주면 띠가 배경에 묻는다.
#
# **(2) 밝은 배경 위의 흰 글자.** Label의 기본 `fg` 는 systemTextColor 라서
# 다크 모드에서 흰색이 된다. 게임이 bg만 주고 fg를 안 준 라벨은 크림색 위의
# 흰 글자가 되어 사실상 안 보인다. 실측: '야생 ？？？ Lv.2' 글자 (255,252,245),
# 배경 (255,244,221). 바로 아래 '내 파이리'는 fg를 명시해서 멀쩡하다.
# Button은 해당 없다 -- aqua가 Button의 기본 fg를 'Black' 으로 고정해 두고
# 베젤도 항상 밝기 때문에, 여기서 건드리면 오히려 흰 베젤에 흰 글자가 된다.

# 이 띠를 칠할 수 있는 위젯들. Menu에는 -highlightbackground 가 없어서 넣으면
# Tcl이 생성 자체를 거부한다.
RING_WIDGETS = frozenset((
    "button", "label", "frame", "canvas", "checkbutton", "radiobutton",
    "entry", "listbox", "text", "scale", "spinbox", "message",
    "labelframe", "scrollbar", "menubutton",
))

# 자기 배경 위에 자기 글자를 그리는 위젯들. 여기만 fg를 보정한다.
TEXT_WIDGETS = frozenset(("label", "message", "checkbutton", "radiobutton"))


def _explicit_color(value):
    """#rrggbb 형태면 그 값, 아니면 None.

    'systemWindowBackgroundColor' 같은 이름은 aqua가 알아서 다루므로 건드리지
    않는다. 우리가 손댈 것은 게임이 직접 고른 색뿐이다.
    """
    if isinstance(value, str) and value.startswith("#") and len(value) in (4, 7):
        return value
    return None


def _parent_background(master):
    """부모 위젯의 배경색. 명시적으로 칠해져 있지 않으면 None."""
    try:
        return _explicit_color(str(master.cget("bg")))
    except Exception:
        return None


def install_contrast_fix():
    """생성되는 모든 위젯에 테두리색과 글자색을 보정한다.

    `BaseWidget.__init__` 은 모든 위젯이 지나가는 자리이고, 여기서는 위젯 종류
    (`widgetName`)와 부모를 둘 다 알 수 있다. 게임이 명시한 옵션은 그대로 둔다 --
    보정은 **비어 있는 자리**만 채운다.
    """
    original = tk.BaseWidget.__init__

    def __init__(self, master, widgetName, cnf={}, kw={}, extra=()):
        try:
            options = kw if kw else cnf
            if isinstance(options, dict) and widgetName != "toplevel":
                if widgetName in RING_WIDGETS and not (
                        "highlightbackground" in options
                        or "highlightthickness" in options):
                    behind = _parent_background(master)
                    if behind:
                        options["highlightbackground"] = behind
                if widgetName in TEXT_WIDGETS and not (
                        "fg" in options or "foreground" in options):
                    own = _explicit_color(options.get("bg", options.get("background")))
                    if own:
                        options["fg"] = "#111111" if _is_light(own) else "#f0f0f0"
                # 창 모서리의 크기 조절 손잡이. 주황 사각형이 둥근 모서리에
                # 잘려서 조각처럼 보이므로, 배경에 맞추고 글리프만 남긴다.
                if options.get("text") == CORNER_GRIP:
                    behind = _parent_background(master)
                    if behind:
                        options["bg"] = behind
                        options["fg"] = (_shade(behind, 0.62) if _is_light(behind)
                                         else _shade(behind, 1.8))
        except Exception:
            pass
        return original(self, master, widgetName, cnf, kw, extra)

    tk.BaseWidget.__init__ = __init__

# --------------------------------------------------------------------------
# 2-g. 체력바와 모서리 손잡이
# --------------------------------------------------------------------------
# **체력바.** 게임은 체력/경험치를 `ttk.Progressbar` 로 그린다. aqua의 그
# 위젯은 네이티브 트랙을 6px 높이로만 그리고, 위젯의 남은 높이(16px 중 10px)를
# 시스템 색으로 채운다. 다크 모드에서 그 색이 거의 검정이라, 크림색 창 위에
# **얇은 파란 선 위아래로 검은 띠가 5px씩** 남는다. 실측한 세로 단면:
#
#     -1px (255,244,221)  <- 창 배경
#     +0..+4px ( 28, 28, 28)   <- 검은 띠
#     +5..+10px (  0,115,251)  <- 실제 게이지
#     +11..+15px ( 28, 28, 28) <- 검은 띠
#
# ttk 스타일로는 못 고친다. background / troughcolor / bordercolor 를 어떻게
# 조합해도 aqua는 전부 무시했다 (5가지 조합을 그려서 확인, 모두 동일한
# (28,28,28)). 테마를 clam 으로 바꾸면 색이 먹지만 그러면 게임이 쓰는
# `ttk.Combobox` 2개까지 네이티브 드롭다운을 잃는다. 그래서 Progressbar만
# Tk로 직접 그리는 것으로 바꿔치운다. 게임이 쓰는 API는 length/maximum/value
# 뿐이다 (11곳 전부 확인).
#
# **모서리 손잡이.** compact 전투 창 오른쪽 아래의 `⇲` 는 크기 조절 핸들이다
# (pet.py:10070, cursor='sizing'). 헤더와 같은 주황(#e8a53a)인데, macOS는
# 창 모서리를 둥글게 깎아서 그 주황 사각형이 잘려 나간 조각처럼 보인다.
# Windows는 모서리가 각져서 깔끔하게 맞물린다. 기능은 그대로 두고 색만 창
# 배경에 맞춰, 글리프만 은은하게 남긴다.

BAR_HEIGHT = 16          # 네이티브와 같은 높이. 바꾸면 레이아웃이 밀린다.
BAR_FILL = "#0073fb"     # 지금 화면에 나오던 그 파란색
CORNER_GRIP = "\u21f2"   # ⇲

# 업데이트 창 배경. 시스템 색을 쓰면 다크 모드에서 글자가 사라진다 (2-f 참고).
UPGRADE_BG = "#f2f2f2"


def _bar_fraction(value, maximum):
    """게이지가 찬 비율. 0.0 ~ 1.0.

    게임은 체력을 그대로 넣기 때문에 음수나 최대 초과가 들어올 수 있다.
    (전투 중 과damage, 회복 아이템 등) 잘라내지 않으면 채움 막대가 바 밖으로
    삐져나간다.
    """
    try:
        maximum = float(maximum)
        if maximum <= 0:
            return 0.0
        return max(0.0, min(1.0, float(value) / maximum))
    except Exception:
        return 0.0


class MacProgressBar(tk.Frame):
    """ttk.Progressbar 대용. aqua가 ttk 색을 무시해서 직접 그린다.

    게임 쪽에서는 구별되지 않아야 하므로 length/maximum/value 와
    step()/start()/stop() 을 그대로 받는다.
    """

    def __init__(self, master=None, length=100, maximum=100, value=0,
                 mode="determinate", orient="horizontal", style=None, **kw):
        behind = _parent_background(master) or "#f2f2f2"
        trough = _shade(behind, 0.90)
        kw.pop("style", None)
        kw.pop("variable", None)
        super().__init__(master, width=int(length), height=BAR_HEIGHT,
                         bg=trough, bd=0,
                         highlightthickness=1,
                         highlightbackground=_shade(behind, 0.72), **kw)
        # 자식 때문에 크기가 변하지 않게 고정한다. 이게 없으면 채움 막대가
        # 프레임 크기를 끌고 다닌다.
        self.pack_propagate(False)
        self.grid_propagate(False)

        self._maximum = float(maximum) or 100.0
        self._value = float(value)
        self._length = int(length)
        self._mode = mode
        self._job = None

        self._fill = tk.Frame(self, bg=BAR_FILL, bd=0, highlightthickness=0)
        self._paint()

    # -- 그리기 -------------------------------------------------------------

    def _paint(self):
        try:
            fraction = _bar_fraction(self._value, self._maximum)
            if fraction <= 0:
                self._fill.place_forget()
            else:
                self._fill.place(x=0, y=0, relheight=1.0, relwidth=fraction)
        except Exception:
            pass

    # -- ttk.Progressbar API ------------------------------------------------

    def configure(self, cnf=None, **kw):
        kw = dict(cnf or {}, **kw)
        touched = False
        if "value" in kw:
            self._value = float(kw.pop("value") or 0); touched = True
        if "maximum" in kw:
            self._maximum = float(kw.pop("maximum") or 100); touched = True
        if "mode" in kw:
            self._mode = kw.pop("mode")
        if "length" in kw:
            self._length = int(kw.pop("length"))
            tk.Frame.configure(self, width=self._length)
            touched = True
        for gone in ("style", "orient", "variable", "phase"):
            kw.pop(gone, None)
        if kw:
            tk.Frame.configure(self, **kw)
        if touched:
            self._paint()
        return None

    config = configure

    def cget(self, key):
        if key == "value":
            return self._value
        if key == "maximum":
            return self._maximum
        if key == "mode":
            return self._mode
        if key == "length":
            return self._length
        return tk.Frame.cget(self, key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def __getitem__(self, key):
        return self.cget(key)

    def step(self, amount=1.0):
        self._value = (self._value + float(amount)) % (self._maximum or 100.0)
        self._paint()

    def start(self, interval=50):
        """determinate 바를 스스로 채운다. ttk의 같은 이름과 같은 역할."""
        self.stop()

        def tick():
            self.step(1.0)
            try:
                self._job = self.after(interval, tick)
            except Exception:
                self._job = None

        try:
            self._job = self.after(interval, tick)
        except Exception:
            self._job = None

    def stop(self):
        if self._job is not None:
            try:
                self.after_cancel(self._job)
            except Exception:
                pass
            self._job = None


def install_progressbar_fix():
    """`ttk.Progressbar` 를 직접 그리는 것으로 바꿔치운다.

    게임은 `from tkinter import ttk` 뒤에 `ttk.Progressbar(...)` 로 부르므로,
    모듈 속성을 갈아끼우면 호출 시점에 그대로 걸린다. `ttk.Combobox` 는
    건드리지 않는다 -- 그쪽은 네이티브 드롭다운이 제대로 동작한다.
    """
    from tkinter import ttk

    original = ttk.Progressbar

    def Progressbar(master=None, **kw):
        try:
            return MacProgressBar(master, **kw)
        except Exception as exc:
            print(f"  체력바 대체 실패, 기본 것으로 갑니다: "
                  f"{type(exc).__name__}: {exc}", flush=True)
            return original(master, **kw)

    Progressbar.__doc__ = MacProgressBar.__doc__
    ttk.Progressbar = Progressbar
    return original

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
        self._notifier = _make_notifier(app)

    def notify(self, message, title="PikaPet"):
        """Tk 이벤트 루프를 막지 않고 알림을 띄운다.

        실제 발송은 macnotify가 한다. 번들로 묶였으면 모던 API로 이 앱 소유의
        배너를 띄우고(눌렀을 때 PikaPet이 올라온다), 그게 거부되면 osascript로
        떨어진다. 자세한 근거는 macnotify.py 참고.
        """
        if self._notifier is not None:
            try:
                self._notifier.notify(message, title)
                return
            except Exception:
                pass
        try:
            import macnotify

            macnotify.post_with_osascript(message, title)
        except Exception:
            pass

    def update_menu(self):
        """할 일 없음. 우클릭 메뉴는 클릭마다 처음부터 다시 만들어진다."""

    def stop(self):
        """할 일 없음. 내려야 할 백그라운드 트레이 스레드가 없다."""


def _make_notifier(app):
    """이 앱 소유로 알림을 띄우는 객체. 실패하면 None (osascript로 떨어진다)."""
    root = getattr(app, "root", None)
    if root is None:
        return None
    try:
        import macnotify

        def on_click():
            """배너를 눌렀을 때. Tk 타이머 안이라 게임을 직접 건드려도 된다."""
            opener = getattr(app, "_open_pending_encounter", None)
            if opener is not None and getattr(app, "_pending_encounter", None):
                opener()
                return
            try:
                app.root.deiconify()
            except Exception:
                pass

        return macnotify.Notifier(root, on_click=on_click)
    except Exception as exc:
        print(f"  알림 초기화 실패: {type(exc).__name__}: {exc}", flush=True)
        return None


def _centre_window(win):
    """창을 주 화면 가운데 위쪽에 놓는다. 크기는 건드리지 않는다."""
    win.update_idletasks()
    width = win.winfo_width() or win.winfo_reqwidth()
    height = win.winfo_height() or win.winfo_reqheight()
    x = max(0, (win.winfo_screenwidth() - width) // 2)
    y = max(0, (win.winfo_screenheight() - height) // 3)
    win.geometry(f"+{x}+{y}")


def bring_to_front(win):
    """앱을 활성 앱으로 만들고 창을 맨 앞으로 올린다. 활성화됐으면 True.

    `lift()` 만으로는 부족하다. 방금 띄운 프로세스는 아직 활성 앱이 아니고,
    그 상태에서는 창이 다른 Space 에 머무를 수 있다.
    """
    activated = False
    try:
        import AppKit

        AppKit.NSApp().activateIgnoringOtherApps_(True)
        activated = True
    except Exception:
        pass
    try:
        win.lift()
        win.focus_force()
    except Exception:
        pass
    return activated


def install_starter_window_fix(pet):
    """세이브가 없을 때 뜨는 스타터 선택 창을 찾을 수 있게 만든다.

    두 가지를 한다.

    **앞으로 끌어온다.** 이 창은 게임이 `PetApp` 보다 먼저 만드는 별도의
    `tk.Tk()` 위에 있고 (pet.py:19067), 막 띄운 프로세스는 아직 활성 앱이 아니다.
    실측: 전체화면 앱이 떠 있는 상태에서 백그라운드로 실행하면 창은 제대로
    만들어지는데 (860x412+34+64, alpha 1.0) CGWindowList 가 `onscreen` 을
    돌려주지 않는다 -- 전체화면 앱은 자기 Space 를 쓰고 새 창은 원래 Space 로
    가기 때문이다. 같은 코드를 포그라운드로 띄우면 `visible=True` 로 잘 보인다.
    사용자 눈에는 앱을 눌렀는데 아무 일도 안 일어난 것으로 보인다.

    **가운데로 놓는다.** 게임은 `geometry('860x380')` 으로 크기만 정하고 위치는
    말하지 않아서 Tk 가 화면 왼쪽 위 구석 (+5+35) 에 붙인다. 정해지지 않은 값을
    채우는 것이라 게임의 선택을 덮어쓰는 것이 아니다.

    `PetApp` 의 펫 창에는 이것을 하지 않는다. 그 창은 `overrideredirect` 이고,
    켤 때마다 작업 중인 앱에서 포커스를 훔쳐가면 안 된다. 선택 창은 반대로
    사용자의 입력을 반드시 받아야 하는 창이다.

    실패해도 창은 그대로 뜬다. 위치가 어정쩡한 것이 앱이 안 뜨는 것보다 낫다.
    """
    original = getattr(pet, "show_starter_select", None)
    if original is None:
        print("  스타터 선택 창 보정 건너뜀: show_starter_select 가 없습니다",
              flush=True)
        return None

    def show_starter_select(root, on_pick, *args, **kw):
        result = original(root, on_pick, *args, **kw)
        for step in (_centre_window, bring_to_front):
            try:
                step(root)
            except Exception as exc:
                print(f"  선택 창 {step.__name__} 실패: "
                      f"{type(exc).__name__}: {exc}", flush=True)
        # 창이 매핑된 뒤 한 번 더. 첫 시도는 매핑 전에 묻힐 수 있다.
        try:
            root.after(300, lambda: bring_to_front(root))
        except Exception:
            pass
        return result

    pet.show_starter_select = show_starter_select
    return original


def install_window_patch(pet):
    """PikaPet이 진짜 루트 창을 만든 뒤에 투명도를 결정한다.

    main()은 PetApp을 만들기 바로 전에 setup_pet_window(root)를 부른다. Tk 루트가
    처음 존재하는 순간이면서, bg=MAGIC으로 위젯이 만들어지기 전 마지막 순간이다.
    """
    original = pet.setup_pet_window

    def setup_pet_window(root):
        set_app_icon()
        before = install_font_defaults(root)
        if before and before != DEFAULT_FONT_SIZE:
            print(f"  기본 폰트: {before} -> {DEFAULT_FONT_SIZE} "
                  f"(버튼 폭이 문자 수 단위라 창이 넘치는 것을 막는다)", flush=True)
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
        install_update_check(self)

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
        app._pikapet_menu_bar = mactray.install(
            app, root, version_check=make_version_check(app))
        print("  메뉴 바: ◓ 항목 추가 (몬스터볼 꺼내기 / 야생 포켓몬 / 배틀 복구"
              " / 버전 확인)", flush=True)
        return app._pikapet_menu_bar
    except Exception as exc:
        print(f"  메뉴 바 생성 실패: {type(exc).__name__}: {exc}", flush=True)
        return None


class UpgradeWindow(tk.Toplevel):
    """내려받는 동안 보여주는 작은 창.

    게임의 창들과 달리 제목 줄을 그대로 둔다 -- 사용자가 옮길 수 있어야 하고,
    overrideredirect 를 걸면 aqua 에서 다시 되돌릴 수 없다 (2-b 참고).
    """

    def __init__(self, master, tag, on_cancel=None):
        super().__init__(master)
        self.on_cancel = on_cancel
        self.title("PikaPet 업데이트")
        self.resizable(False, False)
        self.configure(bg=UPGRADE_BG)
        self.protocol("WM_DELETE_WINDOW", self._cancel)

        self._label = tk.Label(self, text=f"새 버전 {tag} 내려받는 중…",
                               bg=UPGRADE_BG, anchor="w")
        self._label.pack(fill="x", padx=16, pady=(16, 8))

        self._bar = MacProgressBar(self, length=320, maximum=100, value=0)
        self._bar.pack(padx=16)

        self._note = tk.Label(self, text="", bg=UPGRADE_BG, anchor="w")
        self._note.pack(fill="x", padx=16, pady=(6, 0))

        self._button = tk.Button(self, text="취소", command=self._cancel)
        self._button.pack(pady=(10, 14))

        self.update_idletasks()
        self._centre_on(master)
        try:
            self.transient(master)
        except Exception:
            pass

    def _centre_on(self, master):
        try:
            w, h = self.winfo_reqwidth(), self.winfo_reqheight()
            sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
            self.geometry(f"+{(sw - w) // 2}+{(sh - h) // 3}")
        except Exception:
            pass

    def _cancel(self):
        self._button.configure(state="disabled")
        self._note.configure(text="취소하고 있습니다…")
        if self.on_cancel is not None:
            self.on_cancel()

    def set_progress(self, got, total):
        """`got` 이 None 이면 '꺼내는 중' 단계다. Tk 메인 스레드 안이다."""
        try:
            if got is None:
                self._bar.configure(value=100)
                self._label.configure(text="새 버전을 설치할 준비를 하고 있습니다…")
                self._note.configure(text="")
                self._button.configure(state="disabled")
                return
            if total:
                self._bar.configure(value=got * 100.0 / total)
                self._note.configure(
                    text=f"{got / 1048576:.0f} / {total / 1048576:.0f} MB")
            else:
                self._note.configure(text=f"{got / 1048576:.0f} MB")
        except Exception:
            pass


def _finish_upgrade(app, window, tag, result):
    """내려받기가 끝난 뒤. Tk 메인 스레드 안이다."""
    from tkinter import messagebox

    import macupgrade

    try:
        window.destroy()
    except Exception:
        pass

    if result.cancelled:
        return
    if not result.ok:
        macupgrade.log(f"실패 {tag}: {result.error}")
        if messagebox.askyesno(
                "PikaPet",
                "업데이트를 받지 못했습니다.\n\n"
                f"{result.error}\n\n"
                "받는 곳을 열어서 직접 내려받을까요?"):
            import macupdate
            macupdate.open_releases_page()
        return

    started, reason = macupgrade.apply_and_relaunch(result.staged)
    if not started:
        macupgrade.log(f"교체 시작 실패 {tag}: {reason}")
        messagebox.showwarning(
            "PikaPet", f"업데이트를 적용할 수 없습니다.\n\n{reason}")
        return

    macupgrade.log(f"교체 스크립트 시작 {tag}, 앱을 종료합니다")
    # 교체는 우리가 끝난 뒤에 일어난다. 스크립트가 pid 를 지켜보고 있다.
    quit_app = getattr(app, "quit_app", None)
    if callable(quit_app):
        quit_app()
    else:
        try:
            app.root.destroy()
        except Exception:
            pass
        os._exit(0)


def _start_upgrade(app, tag):
    """내려받기를 시작하고 진행률 창을 띄운다."""
    import macupgrade

    root = app.root
    window = UpgradeWindow(root, tag)
    job = macupgrade.Upgrade(
        root, tag,
        on_progress=window.set_progress,
        on_done=lambda result: _finish_upgrade(app, window, tag, result))
    window.on_cancel = job.cancel
    job.start()
    return job


def _offer_upgrade(app, current, tag):
    """앱이 직접 설치하겠다고 제안한다. 이 자리에서 처리했으면 True.

    False 를 돌려주면 위쪽이 기존 방식(받는 곳 열기)으로 넘어간다. 소스에서
    실행 중이거나 dmg 안에서 실행 중이면 교체할 수 없기 때문이다.
    """
    from tkinter import messagebox

    import macupgrade

    ok, reason = macupgrade.can_replace()
    if not ok:
        return False
    if not messagebox.askyesno(
            "PikaPet",
            # 조사를 쓰지 않는다 -- 버전 숫자를 읽는 방식에 따라 이/가가 갈린다.
            "새 버전이 나왔습니다.\n\n"
            f"지금 쓰는 것: {current}\n"
            f"가장 최신: {tag}\n\n"
            "지금 설치할까요? PikaPet이 잠시 닫히고 다시 열립니다.\n"
            "키우던 포켓몬은 그대로 유지됩니다."):
        return True                     # 나중에 하겠다고 했다
    _start_upgrade(app, tag)
    return True


def _show_version_result(app, current, tag, newer):
    """수동 확인의 결과를 알린다. Tk 메인 스레드 안이므로 위젯을 써도 된다.

    알림 배너가 아니라 대화상자를 쓴다. ad-hoc 서명에서는 배너가 스크립트 편집기
    소유로 떠서 눌러도 엉뚱한 곳이 열리기 때문이다 (macnotify.py 참고).
    """
    from tkinter import messagebox

    import macupdate

    if tag is None:
        messagebox.showwarning(
            "PikaPet",
            "새 버전을 확인할 수 없습니다.\n\n"
            "인터넷 연결을 확인하고 잠시 뒤에 다시 시도해 주세요.")
        return

    if newer:
        # 앱이 직접 설치할 수 있으면 그쪽이 낫다 -- 브라우저로 받으면
        # quarantine 이 붙어서 '그래도 열기'를 또 거쳐야 한다 (macupgrade 참고).
        if not _offer_upgrade(app, current, tag):
            if messagebox.askyesno(
                    "PikaPet",
                    # 조사를 쓰지 않는다. '0.0.5 이/가', '0.0.1 이/가' 처럼
                    # 버전 숫자를 읽는 방식에 따라 갈려서 어느 쪽도 늘 맞지 않는다.
                    "새 버전이 나왔습니다.\n\n"
                    f"지금 쓰는 것: {current}\n"
                    f"가장 최신: {tag}\n\n"
                    "받는 곳을 열까요?"):
                macupdate.open_releases_page()
            menu = getattr(app, "_pikapet_menu_bar", None)
            if menu is not None:
                menu.add_action(f"⬇ 새 버전 {tag} 받기",
                                lambda: macupdate.open_releases_page())
        return

    if current is None:
        # 번들이 아니면 자기 버전을 못 읽는다 -- NSBundle이 Homebrew의 Python.app
        # 을 가리켜서 3.14.7 이 나온다 (macupdate.app_version 참고).
        messagebox.showinfo(
            "PikaPet",
            f"가장 최신 릴리스는 {tag} 입니다.\n\n"
            "실행 중인 버전은 읽을 수 없습니다.")
        return

    messagebox.showinfo("PikaPet", f"최신 버전입니다. ({current})")


def make_version_check(app):
    """메뉴 바의 '🔄 새 버전 확인'이 부를 함수. 만들 수 없으면 None.

    자동 확인(`install_update_check`)과 다른 점이 셋이다:

      * **번들이 아니어도 동작한다.** 사람이 직접 누른 것이라 방해가 아니다.
      * **최신이거나 실패했을 때도 결과를 보여준다.** 눌렀는데 아무 일도
        일어나지 않으면 고장난 것으로 보인다.
      * 알림이 아니라 대화상자로 알린다.

    **네트워크는 데몬 스레드가 한다.** 이 함수는 mactray의 Tk 타이머 안에서
    불리므로, 여기서 응답을 기다리면 그 몇 초 동안 게임이 멈춘다.
    """
    root = getattr(app, "root", None)
    if root is None:
        return None
    try:
        import macupdate
    except Exception as exc:
        print(f"  수동 버전 확인 불가: {type(exc).__name__}: {exc}", flush=True)
        return None

    busy = []

    def run():
        if busy:                      # 여러 번 눌러도 조회는 하나만
            return
        busy.append(True)
        current = macupdate.app_version()

        def finished(tag, newer):
            busy.clear()
            _show_version_result(app, current, tag, newer)

        try:
            macupdate.UpdateCheck(root, current, None,
                                  on_result=finished).start()
        except Exception as exc:
            busy.clear()
            print(f"  버전 확인 실패: {type(exc).__name__}: {exc}", flush=True)

    return run


def install_update_check(app):
    """새 버전이 나왔는지 배경에서 확인한다.

    번들에서만 돈다 (소스 실행에서 '새 버전이 있어요'는 방해일 뿐이다).
    확인은 데몬 스레드가 하고, 결과는 큐를 통해 Tk 타이머로 넘어온다 --
    스레드에서 Tk를 건드리면 프로세스가 abort하기 때문이다.

    알림 배너는 ad-hoc 서명에서 스크립트 편집기 소유가 되어 눌러도 엉뚱한 곳이
    열린다. 그래서 안내는 알림으로 하되, **받으러 가는 길은 메뉴 바에** 둔다.
    """
    root = getattr(app, "root", None)
    if root is None:
        return None
    try:
        import macupdate

        if not macupdate.enabled():
            return None
        current = macupdate.app_version()
        if current is None:
            print("  업데이트 확인: 번들 버전을 못 읽어 건너뜀", flush=True)
            return None

        # 지난 업데이트가 중간에 끊겼다면 170MB 가 임시 폴더에 남아 있다.
        try:
            import macupgrade

            swept = macupgrade.sweep_stale_work()
            if swept:
                print(f"  남아 있던 업데이트 임시 폴더 {swept}개 정리", flush=True)
        except Exception:
            pass

        def on_update(tag, url):
            print(f"  새 버전 {tag} (현재 {current})", flush=True)
            menu = getattr(app, "_pikapet_menu_bar", None)
            if menu is not None:
                import macupgrade

                # 직접 설치할 수 있으면 메뉴 항목도 '설치'가 된다. 브라우저를
                # 거치지 않으면 quarantine 이 안 붙어서 보안 단계가 사라진다.
                if macupgrade.can_replace()[0]:
                    menu.add_action(f"⬇ 새 버전 {tag} 설치",
                                    lambda: _offer_upgrade(app, current, tag))
                else:
                    menu.add_action(f"⬇ 새 버전 {tag} 받기",
                                    lambda: macupdate.open_releases_page(url))
            icon = getattr(app, "tray_icon", None)
            if icon is not None:
                icon.notify(f"새 버전이 나왔어요: {tag}. "
                            f"메뉴 바 ◓ 에서 설치할 수 있어요.", "PikaPet")

        check = macupdate.UpdateCheck(root, current, on_update)
        check.start()
        print(f"  업데이트 확인: {current} 기준으로 조회 중", flush=True)
        return check
    except Exception as exc:
        print(f"  업데이트 확인 실패: {type(exc).__name__}: {exc}", flush=True)
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

    install_font_defaults_everywhere()
    install_transparency_shim()
    install_titlebar_restore()
    install_glyph_fix()
    install_button_colors()
    install_contrast_fix()
    install_progressbar_fix()
    install_app_icon_guard()
    remapped_buttons = install_right_click_fallback()

    pet = load_pet()
    install_window_patch(pet)
    install_tray_replacement(pet)
    install_starter_window_fix(pet)

    print(f"macOS PikaPet | Tk {tk.TkVersion} | 메뉴: 펫을 우클릭"
          + (" | Button-3을 Button-2에도 연결" if remapped_buttons else ""),
          flush=True)

    pet.main()


if __name__ == "__main__":
    main()
