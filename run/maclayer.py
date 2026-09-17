"""PikaPet의 `winlayer` API를 macOS로 구현한 것.

winlayer.py는 펫이 다른 창 위에 앉고, 작업 표시줄을 따라 걷고, 주의를 끌려고
깜빡이는 데 필요한 Win32 호출들을 감싼다. 그쪽 함수는 전부
`if not IS_WINDOWS: return <안전한 기본값>`으로 시작하므로, 게임은 이것 없이도
macOS에서 돌아간다 — 그 동작들만 잃는다. 이 모듈이 Quartz와 AppKit으로 그것들을
되돌려준다.

런처가 pet.pyc를 로드하기 전에 이 모듈을 `sys.modules["winlayer"]`로 심어두므로,
앱 자신의 `import winlayer`가 이걸 집어간다. pet.pyc는 `winlayer.IS_WINDOWS`를
전혀 건드리지 않고 공개 함수 열 개만 부르는데, 그래서 통째로 바꿔치기해도 안전하다.

좌표는 macOS의 Tk가 보고하는 것과 같다. 픽셀이 아니라 포인트이고, 원점은 메뉴 바가
있는 디스플레이의 왼쪽 위이며, y는 아래로 자란다. AppKit의 원점은 왼쪽 아래이므로
NSScreen에서 읽은 값은 내보내기 전에 뒤집는다.

winlayer처럼 여기서는 아무것도 예외를 던지지 않는다. 이 함수들은 Tk 타이머 콜백
안에서 돌고, 권한이 없거나 모니터가 뽑혔다고 해서 펫이 죽어서는 안 된다.
"""

import fcntl
import os
import subprocess
import sys
import threading

IS_MACOS = sys.platform == "darwin"

try:
    import Quartz
    from AppKit import NSApplication, NSCriticalRequest, NSScreen
    _HAVE_PYOBJC = True
except Exception:                                           # pragma: no cover
    Quartz = None
    _HAVE_PYOBJC = False

# Windows는 작업 표시줄 크기를 정수 픽셀로 재고, pet.pyc는 이 숫자들을 Tk geometry
# 문자열에 그대로 끼워 넣는다. 그래서 모든 사각형은 int로 내보낸다.
_MIN_LEDGE_WIDTH = 80
_MIN_LEDGE_HEIGHT = 40


# --------------------------------------------------------------------------
# 디스플레이
# --------------------------------------------------------------------------

def _display_bounds():
    """활성 디스플레이 전부를 (left, top, width, height)로. 원점은 왼쪽 위.

    CGDisplayBounds는 이미 Tk가 쓰는 전역 디스플레이 좌표계로 동작하므로 여기서는
    뒤집을 필요가 없다.
    """
    if not _HAVE_PYOBJC:
        return []
    try:
        err, ids, _count = Quartz.CGGetActiveDisplayList(16, None, None)
        if err:
            return []
        out = []
        for did in ids:
            r = Quartz.CGDisplayBounds(did)
            out.append((did, int(r.origin.x), int(r.origin.y),
                        int(r.size.width), int(r.size.height)))
        return out
    except Exception:
        return []


def get_virtual_screen_rect():
    """모든 디스플레이를 감싸는 사각형을 (left, top, width, height)로."""
    try:
        rects = _display_bounds()
        if not rects:
            return None
        left = min(x for _, x, _, _, _ in rects)
        top = min(y for _, _, y, _, _ in rects)
        right = max(x + w for _, x, _, w, _ in rects)
        bottom = max(y + h for _, _, y, _, h in rects)
        if right <= left or bottom <= top:
            return None
        return (left, top, right - left, bottom - top)
    except Exception:
        return None


def get_secondary_monitor_rect():
    """주 디스플레이가 아닌 첫 번째 디스플레이를 (left, top, width, height)로."""
    try:
        if not _HAVE_PYOBJC:
            return None
        main = Quartz.CGMainDisplayID()
        for did, x, y, w, h in _display_bounds():
            if did != main and w > 0 and h > 0:
                return (x, y, w, h)
        return None
    except Exception:
        return None


def _dock_rect_from_frames(frames, ref_height):
    """화면마다의 (frame, visibleFrame) 쌍에서 Dock을 찾아낸다.

    `frames`는 AppKit 좌표 — 왼쪽 아래 원점, y가 위로 자람 — 를 화면당
    ((fx, fy, fw, fh), (vx, vy, vw, vh)) 로 담는다. `ref_height`는 그 좌표계의
    원점인 screens()[0]의 높이이고, 결과를 Tk의 왼쪽 위 좌표로 뒤집는 기준이 된다.

    모니터를 뽑지 않고도 다중 모니터 경우를 테스트할 수 있도록 순수 함수로 두었다.
    (left, top, right, bottom) 또는 Dock이 숨어 있을 때 None을 돌려준다. 위쪽에만
    여백이 있으면 그건 Dock이 아니라 메뉴 바다.
    """
    for (fx, fy, fw, fh), (vx, vy, vw, vh) in frames:
        left_inset = vx - fx
        right_inset = (fx + fw) - (vx + vw)
        bottom_inset = vy - fy
        top_inset = (fy + fh) - (vy + vh)

        def flip(y):
            """AppKit의 y(아래부터) -> Tk의 y(위부터)."""
            return int(round(ref_height - y))

        if bottom_inset > 1:
            return (int(fx), flip(fy + bottom_inset), int(fx + fw), flip(fy))
        if left_inset > 1:
            return (int(fx), flip(fy + fh - top_inset),
                    int(fx + left_inset), flip(fy))
        if right_inset > 1:
            return (int(fx + fw - right_inset), flip(fy + fh - top_inset),
                    int(fx + fw), flip(fy))
    return None


def get_taskbar_rect():
    """Dock의 사각형을 (left, top, right, bottom)로.

    Dock은 macOS에서 Windows 작업 표시줄에 가장 가까운 것이다. 펫이 올라설 수 있는
    예약된 띠. Dock이 자동 숨김으로 설정돼 있으면 None을 돌려주는데, winlayer가
    Shell_TrayWnd를 못 찾았을 때와 같은 동작이다.
    """
    try:
        if not _HAVE_PYOBJC:
            return None
        screens = NSScreen.screens()
        if not screens:
            return None
        # screens()[0]이 AppKit 좌표계의 원점을 정한다. Dock 자체는 어느 화면에나
        # 있을 수 있으므로 전부 확인한다.
        ref_height = screens[0].frame().size.height
        frames = []
        for s in screens:
            f, v = s.frame(), s.visibleFrame()
            frames.append(((f.origin.x, f.origin.y, f.size.width, f.size.height),
                           (v.origin.x, v.origin.y, v.size.width, v.size.height)))
        return _dock_rect_from_frames(frames, ref_height)
    except Exception:
        return None


# --------------------------------------------------------------------------
# 다른 앱의 창 -- 펫이 걸어 다니는 선반
# --------------------------------------------------------------------------

def _list_windows():
    """화면에 있는 창들을 pid/layer/title/left/top/right/bottom 딕셔너리로.

    `kCGWindowName`은 화면 기록 권한이 필요하다. 권한이 없으면 macOS가 그 키를
    그냥 빼버리므로 대신 소유 애플리케이션 이름을 쓴다. 제외 목록과 펫이 보여주는
    툴팁에는 그 정도면 충분하다.
    """
    if not _HAVE_PYOBJC:
        return []
    try:
        options = (Quartz.kCGWindowListOptionOnScreenOnly
                   | Quartz.kCGWindowListExcludeDesktopElements)
        infos = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID) or []
    except Exception:
        return []

    out = []
    for info in infos:
        try:
            bounds = info.get("kCGWindowBounds") or {}
            x, y = float(bounds.get("X", 0)), float(bounds.get("Y", 0))
            w, h = float(bounds.get("Width", 0)), float(bounds.get("Height", 0))
            title = info.get("kCGWindowName") or info.get("kCGWindowOwnerName") or ""
            out.append({
                "pid": int(info.get("kCGWindowOwnerPID", -1)),
                "layer": int(info.get("kCGWindowLayer", 0)),
                "title": str(title),
                "left": int(x), "top": int(y),
                "right": int(x + w), "bottom": int(y + h),
            })
        except Exception:
            continue
    return out


def _ledges_from_records(records, exclude_titles, max_windows, own_pid):
    """원시 창 레코드를 winlayer의 선반 딕셔너리로 바꾼다.

    화면이나 권한 프롬프트 없이 필터 규칙을 테스트할 수 있도록 Quartz 호출과
    분리해 두었다.
    """
    if max_windows is not None and max_windows <= 0:
        return []
    excludes = [t for t in (exclude_titles or []) if t]

    kept = []
    for r in records:
        if r["pid"] == own_pid:
            continue                                  # 자기 자신 위에는 올라서지 않는다
        if r["layer"] != 0:
            continue                                  # Dock, 메뉴 바, 우리 자신의 topmost 펫
        if r["right"] - r["left"] < _MIN_LEDGE_WIDTH:
            continue                                  # Tk가 1px 보조 창을 흩뿌린다
        if r["bottom"] - r["top"] < _MIN_LEDGE_HEIGHT:
            continue
        title = r["title"]
        if any(x in title for x in excludes):
            continue
        kept.append({"left": r["left"], "top": r["top"],
                     "right": r["right"], "title": title})

    # 가장 높은 선반이 먼저 오게 한다. 펫의 선택이 Quartz가 우연히 돌려준 창 순서에
    # 좌우되지 않도록.
    kept.sort(key=lambda l: (l["top"], l["left"]))
    return kept[:max_windows] if max_windows is not None else kept


def get_window_ledges(exclude_titles=None, max_windows=40):
    """다른 앱 창들의 윗변을 [{left, top, right, title}, ...] 로."""
    try:
        return _ledges_from_records(_list_windows(), exclude_titles,
                                    max_windows, os.getpid())
    except Exception:
        return []


# --------------------------------------------------------------------------
# 데스크톱 아이콘
# --------------------------------------------------------------------------

_ICON_SCRIPT = 'tell application "Finder" to get desktop position of every item of desktop window'
_icon_cache = None


def get_desktop_icon_positions(max_icons=60):
    """Finder 데스크톱 아이콘들의 화면 위치를 [(x, y), ...] 로.

    기본은 꺼짐. Windows와 달리 macOS에는 AppleScript로 Finder를 조종하지 않고
    이걸 읽는 방법이 없다. 그런데 그 호출은 처음에 자동화 동의 프롬프트를 띄우고
    사용자가 답할 때까지 멈춘다 — 타이머 콜백에서 할 일이 아니다.
    PIKAPET_DESKTOP_ICONS=1로 켤 수 있고, 결과는 실행이 끝날 때까지 캐시되므로
    프롬프트는 한 번만 나올 수 있다.
    """
    global _icon_cache
    try:
        if max_icons is not None and max_icons <= 0:
            return []
        if not os.environ.get("PIKAPET_DESKTOP_ICONS"):
            return []
        if _icon_cache is None:
            _icon_cache = _read_desktop_icons()
        return _icon_cache[:max_icons] if max_icons is not None else list(_icon_cache)
    except Exception:
        return []


def _read_desktop_icons():
    try:
        out = subprocess.run(["osascript", "-e", _ICON_SCRIPT],
                             capture_output=True, text=True, timeout=5)
        if out.returncode != 0:
            return []
        # osascript는 평평한 목록을 찍는다: "12, 34, 12, 120, ..."
        nums = [int(float(p)) for p in out.stdout.replace("\n", "").split(",") if p.strip()]
        return list(zip(nums[0::2], nums[1::2]))
    except Exception:
        return []


# --------------------------------------------------------------------------
# 단일 인스턴스
# --------------------------------------------------------------------------

# winlayer가 쓰는 것과 같은 기본값. 두 계층이 락의 정체에 대해 합의하도록.
_DEFAULT_MUTEX = "PikaPetSingleInstanceMutex_do_bro2"

_locks = {}
_lock_guard = threading.Lock()


def _lock_dir():
    base = os.environ.get("APPDATA") or os.path.expanduser("~/Library/Application Support")
    path = os.path.join(base, "PikaPet")
    os.makedirs(path, exist_ok=True)
    return path


def acquire_single_instance_lock(name=_DEFAULT_MUTEX):
    """이 프로세스가 실행해도 되면 True, 다른 인스턴스가 이미 쥐고 있으면 False.

    flock을 쓴다. 커널이 프로세스 종료 시 알아서 풀어주므로, 죽은 실행이
    사용자를 잠가버릴 수 없다 — 남아 있는 락 파일 방식이라면 그렇게 된다.
    오류가 나면 True를 돌려준다. 락 자체가 깨졌다고 실행을 거부하는 것이 펫이
    잠깐 둘이 되는 것보다 나쁘고, winlayer도 그렇게 동작한다.
    """
    try:
        with _lock_guard:
            if name in _locks:
                return True                       # 이미 우리가 쥐고 있다
            safe = "".join(c if c.isalnum() or c in "-._" else "_" for c in str(name))
            fd = os.open(os.path.join(_lock_dir(), safe + ".lock"),
                         os.O_CREAT | os.O_RDWR, 0o644)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os.close(fd)
                return False
            _locks[name] = fd                     # 실행 동안 fd를 살려둔다
            return True
    except Exception:
        return True


# --------------------------------------------------------------------------
# 주의 끌기와 Dock
# --------------------------------------------------------------------------

_attention_request = None


def set_dpi_aware():
    """할 일 없음. macOS의 Tk는 이미 포인트 단위로 동작하고 Retina를 스스로 처리한다."""
    return None


def flash_taskbar(hwnd, count=8, interval_ms=500):
    """Dock 아이콘을 튀게 해서 사용자의 주의를 끈다.

    얼마나 튈지는 macOS가 정하므로 `count`와 `interval_ms`는 시그니처를 맞추려고
    받기만 하고 무시한다. AppKit은 메인 스레드에서 건드려야 한다. pet.pyc는 이걸
    Tk 콜백에서 부르지만, 가드가 있어야 엉뚱한 백그라운드 호출이 pystray처럼
    프로세스를 트랩에 빠뜨리지 않는다.
    """
    global _attention_request
    try:
        if not _HAVE_PYOBJC or threading.current_thread() is not threading.main_thread():
            return None
        _attention_request = NSApplication.sharedApplication().requestUserAttention_(
            NSCriticalRequest)
    except Exception:
        pass
    return None


def stop_taskbar_flash(hwnd):
    """flash_taskbar가 시작한 Dock 튀기를 멈춘다."""
    global _attention_request
    try:
        if _HAVE_PYOBJC and _attention_request is not None \
                and threading.current_thread() is threading.main_thread():
            NSApplication.sharedApplication().cancelUserAttentionRequest_(_attention_request)
    except Exception:
        pass
    _attention_request = None
    return None


def hide_window_from_taskbar(hwnd):
    """할 일 없음. macOS는 창마다가 아니라 프로세스 전체에 Dock 타일 하나를 준다.
    그래서 winlayer가 펫의 보조 창을 작업 표시줄에서 빼려고 쓰는
    WS_EX_TOOLWINDOW 수법에 대응하는, 창 단위의 방법이 없다.
    """
    return None
