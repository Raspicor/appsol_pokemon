"""스프라이트를 네이티브 AppKit 창으로 그려서 진짜 투명하게 만든다.

Tk로는 안 된다. aqua에서 Tk 9는 toplevel을 **알파 채널이 없는** 백킹 스토어에
렌더링한다 — 콘텐트 뷰가 `isOpaque = NO`이고 NSWindow가 이미 non-opaque에
clearColor인데도, 레이어 내용이 `kCGImageAlphaNoneSkipLast` CGImage로 돌아온다.
그래서 Tk가 그리는 것은 무엇이든 꽉 찬 사각형으로 합성되고, `-transparent`,
`systemTransparent`, `NSWindow.setOpaque_(False)` 어느 것도 펫 주변을 비치게
하지 못한다. Tk 9.0.4 / macOS 26 실측.

그래서 Tk의 렌더러와 싸우는 대신 빼버린다. 컬러키를 요청한 창마다 그 위에
테두리 없는 NSWindow를 정확히 겹쳐 놓고, 그 창이 스프라이트를 진짜 per-pixel
알파로 그린다. Tk 창은 자리에 그대로 남아 창 위치를 계속 관장하되, 보이지 않을
만큼 낮은 알파로 내려간다.

마우스는 오버레이가 받아서 Tk로 넘긴다. 알파를 낮춘 Tk 창이 클릭을 계속 받는지는
macOS가 보장해주지 않고 (실제로 alpha 0.004로 내렸더니 드래그가 죽었다), 펫이
쓰는 이벤트는 다섯 개뿐이라 그대로 옮기는 편이 확실하다.

넘기는 방식에 한 가지 제약이 있다. **AppKit 콜백 안에서 Tcl을 부르면 프로세스가
죽는다.** Tk의 mainloop가 macOS 런루프를 돌리므로 마우스 콜백은 Tcl_DoOneEvent
안에서 AppKit을 거쳐 들어오는데, 그 자리에서 `event_generate`로 Tcl에 다시
들어가면 Python thread state가 떨어져 나가고 다음 Tk 타이머가
`PyEval_RestoreThread: the current Python thread state is NULL` 로 abort한다.
격리해서 재현했다: 직접 호출 2/2 사망, 큐 경유 2/2 생존. 그래서 콜백은 큐에만
넣고, 이미 Tcl 컨텍스트인 `tick`이 꺼내서 실제 이벤트를 만든다.

오버레이가 실제로 무언가를 그리기 시작한 뒤에야 Tk 창을 투명하게 만들기 때문에,
판단이 틀린 창의 최악의 결과는 예전 동작이지 펫이 사라지는 것이 아니다.

Tk 빌드에 아무것도 요구하지 않으므로 8.6이든 9든 똑같이 동작한다.
"""

import collections
import io
import re
import time

# 클릭 전달은 오버레이가 맡으므로 Tk 창은 눈에 안 보이기만 하면 된다.
# 0이 아니라 한 단계 위인 이유는, 알파가 정확히 0인 창을 AppKit이 아예 없는
# 것처럼 취급하는 경로가 있어서다.
INVISIBLE_ALPHA = 0.004

# 오버레이가 위치·매핑·생존을 다시 확인하고, 큐에 쌓인 마우스 이벤트를 꺼내는
# 주기. 창 이동은 geometry 훅에서 즉시 반영하므로 위치 갱신은 안전망이지만,
# 마우스 입력 지연은 이 값이 그대로 결정한다. 16 ms면 60 Hz다.
SYNC_MS = 16

# install()이 채운다. 하네스에서 오버레이 상태를 들여다볼 때 쓴다.
MANAGER = None

# PetApp.redraw가 내보내는 형식 (pet.py:7269): f"{w}x{h}+{left}+{top}".
# 두 번째 모니터로 넘어가 left가 음수가 되면 "+-55"로 나온다. 그 외 형식은
# Tk에서 위치를 직접 읽는 쪽으로 넘긴다.
_GEOMETRY = re.compile(r"^(?:(\d+)x(\d+))?\+(-?\d+)\+(-?\d+)$")

# 게임이 펫 라벨에 거는 마우스 이벤트 전부 (Companion.__init__ pet.py:4161~4164,
# PetApp도 같은 구성). 핸들러가 읽는 것은 x_root/y_root/x/y 뿐이라 그대로 만들어
# 넘길 수 있다.
_BUTTON1_MASK = 0x100


def available():
    """필요한 AppKit 조각들을 import할 수 있으면 True."""
    try:
        from AppKit import NSWindow, NSImage, NSImageView, NSColor  # noqa: F401
        from Foundation import NSData, NSMakeRect  # noqa: F401
    except Exception:
        return False
    return True


# --------------------------------------------------------------------------
# 좌표 변환
# --------------------------------------------------------------------------

_height = [0.0, 0.0]        # 캐시된 주 화면 높이와 그 값을 읽은 시각


def _primary_height():
    """Cocoa가 좌표를 재는 기준 화면의 높이.

    Tk는 주 디스플레이의 왼쪽 위를, Cocoa는 그 왼쪽 아래를 원점으로 삼는데 둘 다
    하나의 전역 좌표계라서, 모니터가 몇 개든 이 숫자 하나로 변환된다.
    """
    now = time.monotonic()
    if _height[0] and now - _height[1] < 2.0:
        return _height[0]
    from AppKit import NSScreen

    screens = NSScreen.screens()
    value = 0.0
    for screen in screens:
        frame = screen.frame()
        if frame.origin.x == 0 and frame.origin.y == 0:
            value = frame.size.height
            break
    else:
        if screens:
            value = screens[0].frame().size.height
    _height[0], _height[1] = value, now
    return value


def _mouse_in_tk_coords():
    """지금 마우스 위치를 Tk의 화면 좌표(왼쪽 위 원점)로."""
    from AppKit import NSEvent

    point = NSEvent.mouseLocation()
    return int(round(point.x)), int(round(_primary_height() - point.y))


# --------------------------------------------------------------------------
# 스프라이트 한 장을 그리는 네이티브 창
# --------------------------------------------------------------------------

def _ns_image(pil):
    from AppKit import NSImage
    from Foundation import NSData

    buf = io.BytesIO()
    pil.save(buf, "PNG")
    raw = buf.getvalue()
    return NSImage.alloc().initWithData_(NSData.dataWithBytes_length_(raw, len(raw)))


_view_class = None


def _sprite_view_class():
    """마우스를 Tk로 넘기는 NSImageView 서브클래스.

    ObjC 런타임에는 같은 이름의 클래스를 두 번 등록할 수 없으므로 한 번만 만들어
    캐시한다.
    """
    global _view_class
    if _view_class is not None:
        return _view_class

    import objc
    from AppKit import NSImageView, NSTrackingArea
    from Foundation import NSMakeRect

    # NSTrackingAreaOptions. InVisibleRect로 두면 뷰 크기가 바뀔 때마다 추적
    # 영역을 다시 만들 필요가 없고, ActiveAlways라서 앱이 맨 앞이 아니어도
    # 마우스가 올라온 것을 알 수 있다.
    MOUSE_ENTERED_AND_EXITED = 0x01
    ACTIVE_ALWAYS = 0x80
    IN_VISIBLE_RECT = 0x200

    class PikaPetSpriteView(NSImageView):
        """펫 그림을 그리고, 받은 마우스 이벤트를 Tk 라벨로 옮긴다."""

        def initWithFrame_(self, frame):
            self = objc.super(PikaPetSpriteView, self).initWithFrame_(frame)
            if self is None:
                return None
            self.sink = None            # (sequence, x, y, **kw) 를 받는 콜러블
            area = NSTrackingArea.alloc().initWithRect_options_owner_userInfo_(
                NSMakeRect(0, 0, 0, 0),
                MOUSE_ENTERED_AND_EXITED | ACTIVE_ALWAYS | IN_VISIBLE_RECT,
                self, None)
            self.addTrackingArea_(area)
            return self

        # 앱이 맨 앞에 있지 않아도 첫 클릭이 그대로 먹히게 한다. 이게 없으면
        # 첫 클릭은 앱을 활성화하는 데 쓰이고 펫에는 닿지 않는다.
        def acceptsFirstMouse_(self, event):
            return True

        @objc.python_method
        def _send(self, sequence, **kw):
            if self.sink is None:
                return
            x, y = _mouse_in_tk_coords()
            self.sink(sequence, x, y, **kw)

        def mouseDown_(self, event):
            self._send("<Button-1>")

        def mouseDragged_(self, event):
            self._send("<B1-Motion>", state=_BUTTON1_MASK)

        def mouseUp_(self, event):
            self._send("<ButtonRelease-1>")

        def rightMouseDown_(self, event):
            self._send("<Button-3>")

        def mouseEntered_(self, event):
            self._send("<Enter>")

    _view_class = PikaPetSpriteView
    return _view_class


class _Overlay:
    """스프라이트 하나를 그리는 테두리 없는 NSWindow."""

    def __init__(self, sink=None):
        import AppKit
        from AppKit import (NSWindow, NSColor,
                            NSWindowStyleMaskBorderless, NSBackingStoreBuffered)
        from Foundation import NSMakeRect

        window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(0, 0, 1, 1), NSWindowStyleMaskBorderless,
            NSBackingStoreBuffered, False)
        window.setOpaque_(False)
        window.setBackgroundColor_(NSColor.clearColor())
        window.setHasShadow_(False)
        # 이 창이 마우스를 받아 Tk로 넘긴다. 테두리 없는 창은 key window가 되지
        # 않으므로 클릭해도 다른 앱의 포커스를 빼앗지 않는다.
        window.setIgnoresMouseEvents_(False)
        # 펫의 topmost Tk 창(floating)보다 위, 네이티브 메뉴보다는 아래
        window.setLevel_(getattr(AppKit, "NSStatusWindowLevel", 25))
        window.setCollectionBehavior_(
            getattr(AppKit, "NSWindowCollectionBehaviorCanJoinAllSpaces", 1 << 0)
            | getattr(AppKit, "NSWindowCollectionBehaviorStationary", 1 << 4)
            | getattr(AppKit, "NSWindowCollectionBehaviorFullScreenAuxiliary", 1 << 8))

        view = _sprite_view_class().alloc().initWithFrame_(NSMakeRect(0, 0, 1, 1))
        view.setImageScaling_(1)          # NSImageScaleAxesIndependently
        view.setEditable_(False)
        view.sink = sink
        window.setContentView_(view)

        self.window = window
        self.view = view
        self.visible = False
        self._rect = None

    def show(self, x, y, w, h, ns_image=None):
        from Foundation import NSMakeRect

        if ns_image is not None:
            self.view.setImage_(ns_image)
        rect = (x, y, w, h)
        if rect != self._rect:
            if self._rect is None or (w, h) != self._rect[2:]:
                self.view.setFrame_(NSMakeRect(0, 0, w, h))
            self.window.setFrame_display_(
                NSMakeRect(x, _primary_height() - y - h, w, h), True)
            self._rect = rect
        if not self.visible:
            self.window.orderFrontRegardless()
            self.visible = True

    def set_alpha(self, value):
        self.window.setAlphaValue_(value)

    def hide(self):
        if self.visible:
            self.window.orderOut_(None)
            self.visible = False

    def close(self):
        try:
            self.hide()
            self.window.close()
        except Exception:
            pass


# --------------------------------------------------------------------------
# 오버레이를 Tk에 맞춰 붙들어두기
# --------------------------------------------------------------------------

class _Manager:
    """어느 Tk 창을 대신하고 있고, 어떤 오버레이가 그 역할인지를 들고 있다.

    위젯은 객체가 아니라 Tk 경로 이름으로 잡아둔다. 게임이 동료 창을 계속
    만들었다 없앴다 하는데, 이름은 위젯이 사라진 뒤에 남아 있어도 비용이 없다.
    """

    def __init__(self, root, raw_attributes):
        self.root = root
        self.raw_attributes = raw_attributes
        self.transparent = set()     # 컬러키를 받은 창들의 경로 이름
        self.dimmed = set()          # 그중 실제로 투명하게 만든 것들
        self.records = {}            # 라벨 경로 이름 -> 레코드
        self.pending = collections.deque()   # AppKit이 넣고 tick이 꺼내는 마우스 이벤트

    # -- 등록 ---------------------------------------------------------------

    def mark_transparent(self, toplevel):
        self.transparent.add(str(toplevel))

    def owns(self, widget):
        try:
            return str(widget.winfo_toplevel()) in self.transparent
        except Exception:
            return False

    def set_image(self, label, pil):
        """라벨에 스프라이트 한 장이 들어왔다. 그 라벨의 오버레이로 넘긴다."""
        if pil is None or not self.owns(label):
            return
        key = str(label)
        record = self.records.get(key)
        if record is None:
            record = {"label": label, "overlay": None, "pil": None, "opacity": 1.0}
            record["overlay"] = self.make_overlay(record)
            self.records[key] = record
        record["pil"] = pil
        self._place(record, fresh=True)
        if record["overlay"].visible:
            self._dim(label.winfo_toplevel())

    def make_overlay(self, record):
        """오버레이 하나를 만들고, 그 마우스 이벤트를 이 레코드로 연결한다."""
        return _Overlay(sink=lambda seq, x, y, **kw: self.enqueue(record, seq, x, y, **kw))

    def set_opacity(self, toplevel, value):
        """게임이 가진 창 투명도 설정을 오버레이 쪽으로 돌린다.

        Tk 창의 알파는 이미 '안 보이게 하는' 용도로 쓰고 있으므로, 설정값은
        네이티브 창에 적용해야 한다.
        """
        name = str(toplevel)
        for record in self.records.values():
            try:
                if str(record["label"].winfo_toplevel()) == name:
                    record["opacity"] = value
                    record["overlay"].set_alpha(value)
            except Exception:
                pass

    # -- 마우스 전달 ---------------------------------------------------------

    def enqueue(self, record, sequence, screen_x, screen_y, **kw):
        """AppKit 콜백에서 불린다. **여기서는 Tcl을 건드리지 않는다.**

        이 자리에서 `event_generate`를 부르면 Tcl에 재진입하게 되고 프로세스가
        abort한다 (모듈 독스트링 참고). 순수 Python 자료구조에만 넣고 끝낸다.
        좌표는 이벤트가 난 순간의 것을 써야 하므로 여기서 읽어 함께 넣는다.
        """
        self.pending.append((record, sequence, screen_x, screen_y, kw))

    def drain(self):
        """큐에 쌓인 마우스 이벤트를 Tk 이벤트로 만든다. tick에서만 부른다."""
        while self.pending:
            record, sequence, x, y, kw = self.pending.popleft()
            self.dispatch(record, sequence, x, y, **kw)

    def dispatch(self, record, sequence, screen_x, screen_y, **kw):
        """오버레이가 받은 마우스 이벤트를 Tk 라벨에서 다시 일으킨다.

        게임의 핸들러(PetApp.on_press/on_motion/on_release)가 읽는 것은
        x_root/y_root/x/y 네 개뿐이라, 그것만 채워주면 원래 클릭과 구분되지
        않는다.
        """
        label = record["label"]
        try:
            if not label.winfo_exists():
                return
            label.event_generate(sequence,
                                 x=screen_x - label.winfo_rootx(),
                                 y=screen_y - label.winfo_rooty(),
                                 rootx=screen_x, rooty=screen_y, **kw)
        except Exception:
            pass

    # -- Tk 창 자체 ----------------------------------------------------------

    def _dim(self, toplevel):
        name = str(toplevel)
        if name in self.dimmed:
            return
        try:
            self.raw_attributes(toplevel, "-alpha", INVISIBLE_ALPHA)
        except Exception:
            return
        self.dimmed.add(name)

    # -- 위치 ----------------------------------------------------------------

    def _place(self, record, fresh=False):
        """오버레이 하나를 라벨에 맞춘다. False면 라벨이 사라진 것."""
        label, overlay, pil = record["label"], record["overlay"], record["pil"]
        try:
            if not label.winfo_exists():
                return False
            if not label.winfo_ismapped() or pil is None:
                overlay.hide()
                return True
            x, y = label.winfo_rootx(), label.winfo_rooty()
        except Exception:
            return False
        overlay.show(x, y, pil.width, pil.height,
                     _ns_image(pil) if fresh else None)
        if fresh and record["opacity"] < 1.0:
            overlay.set_alpha(record["opacity"])
        return True

    def moved(self, toplevel, spec):
        """`geometry()` 호출을 같은 순간에 따라간다.

        여기서 `winfo_rootx`는 쓸 수 없다. 호출이 돌아온 시점에 창은 아직 안
        움직였고, 그래서 읽으면 옛 위치가 나오며 걷는 동안 스프라이트가 한 프레임씩
        뒤처지는 게 눈에 보인다. 요청한 위치는 geometry 문자열에 그대로 있고,
        라벨이 창 안에서 갖는 오프셋은 두 좌표가 똑같이 낡아 있으므로 살아남는다.
        """
        match = _GEOMETRY.match(spec.strip())
        if match is None:                     # 게임이 내보내지 않는 형식
            self.resync(toplevel)
            return
        x, y = int(match.group(3)), int(match.group(4))
        name = str(toplevel)
        for key, record in list(self.records.items()):
            label, overlay, pil = record["label"], record["overlay"], record["pil"]
            try:
                if str(label.winfo_toplevel()) != name:
                    continue
                if pil is None or not label.winfo_ismapped():
                    continue
                dx = label.winfo_rootx() - toplevel.winfo_rootx()
                dy = label.winfo_rooty() - toplevel.winfo_rooty()
            except Exception:
                continue
            overlay.show(x + dx, y + dy, pil.width, pil.height)

    def resync(self, toplevel=None):
        """Tk가 지금 보고하는 값으로 오버레이 위치를 다시 맞춘다.

        `moved` 뒤를 받치는 안전망. 창이 매핑/언매핑/파괴된 경우와, 다른 경로로
        움직인 경우를 잡는다.
        """
        name = str(toplevel) if toplevel is not None else None
        for key, record in list(self.records.items()):
            if name is not None:
                try:
                    if str(record["label"].winfo_toplevel()) != name:
                        continue
                except Exception:
                    pass
            if not self._place(record):
                record["overlay"].close()
                self.records.pop(key, None)
                self.dimmed.discard(key)

    def tick(self):
        # 이미 Tcl 콜백 안이므로 여기서 event_generate를 불러도 안전하다.
        try:
            if not self.root.winfo_exists():
                return
        except Exception:
            return
        self.drain()
        self.resync()
        try:
            self.root.after(SYNC_MS, self.tick)
        except Exception:
            pass


# --------------------------------------------------------------------------
# 설치
# --------------------------------------------------------------------------

def install(root, magic):
    """`magic` 배경을 요청한 창에 그려지는 스프라이트마다 오버레이가 붙도록 Tk를 훅한다.

    `magic`은 게임의 컬러키 색이다. 게임은 투명하게 만들고 싶은 창의 배경색으로
    그 색을 지정하는데, 여기서 필요한 신호가 정확히 그것이다. 게다가
    `systemTransparent`와 달리 Tk 빌드의 지원 여부에 전혀 기대지 않는다.
    """
    global MANAGER
    import tkinter as tk
    from PIL import Image, ImageTk

    manager = MANAGER = _Manager(root, tk.Wm.wm_attributes)

    # 1. 어떤 창이 투명해지고 싶은가: 컬러키를 배경으로 받은 창
    for cls in (tk.Tk, tk.Toplevel):
        original = cls.configure

        def configure(self, cnf=None, _original=original, **kw):
            colour = kw.get("bg", kw.get("background"))
            if colour is None and isinstance(cnf, dict):
                colour = cnf.get("bg", cnf.get("background"))
            if colour == magic:
                manager.mark_transparent(self)
            return _original(self, cnf, **kw)

        cls.configure = configure
        cls.config = configure

    # 2. PhotoImage 뒤의 PIL 이미지를 기억해둔다. Tk는 불투명한 핸들만 돌려주는데
    #    정작 필요한 건 알파다. PhotoImage 객체에 얹어두면 수명이 같이 가므로,
    #    게임이 매 프레임 버리는 이미지는 그것과 함께 해제된다.
    photo_init = ImageTk.PhotoImage.__init__

    def __init__(self, image=None, size=None, **kw):
        photo_init(self, image, size, **kw)
        if isinstance(image, Image.Image):
            self._pikapet_source = image

    ImageTk.PhotoImage.__init__ = __init__

    # 3. 그런 창 안의 라벨에 들어가는 스프라이트는 전부 오버레이로 간다
    label_init = tk.Label.__init__
    label_configure = tk.Label.configure

    def label__init__(self, master=None, cnf={}, **kw):
        label_init(self, master, cnf, **kw)
        image = kw.get("image")
        if image is None and isinstance(cnf, dict):
            image = cnf.get("image")
        if image is not None:
            manager.set_image(self, getattr(image, "_pikapet_source", None))

    def label_config(self, cnf=None, **kw):
        result = label_configure(self, cnf, **kw)
        image = kw.get("image")
        if image is None and isinstance(cnf, dict):
            image = cnf.get("image")
        if image is not None:
            manager.set_image(self, getattr(image, "_pikapet_source", None))
        return result

    tk.Label.__init__ = label__init__
    tk.Label.configure = label_config
    tk.Label.config = label_config

    # 4. 창이 움직이는 즉시 따라간다. 한 틱 뒤가 아니라.
    wm_geometry = tk.Wm.wm_geometry

    def geometry(self, newGeometry=None):
        result = wm_geometry(self, newGeometry)
        if newGeometry is not None:
            manager.moved(self, newGeometry)
        return result

    tk.Wm.wm_geometry = geometry
    tk.Wm.geometry = geometry

    # 5. 게임의 창 투명도 설정은 이제 오버레이 몫이다
    wm_attributes = tk.Wm.wm_attributes

    def attributes(self, *args, **kwargs):
        if len(args) >= 2 and args[0] == "-alpha" and manager.owns(self):
            try:
                manager.set_opacity(self.winfo_toplevel(), float(args[1]))
                return None
            except (TypeError, ValueError):
                pass
        return wm_attributes(self, *args, **kwargs)

    tk.Wm.wm_attributes = attributes
    tk.Wm.attributes = attributes

    root.after(SYNC_MS, manager.tick)
    return manager
