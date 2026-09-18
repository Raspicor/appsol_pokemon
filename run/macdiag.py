"""시작이 어떻게 흘러갔는지 한 줄씩 남긴다.

**왜 있는가.** "포켓몬 선택 창이 안 뜬다"는 신고를 받았을 때, 그 Mac에서 무슨
일이 있었는지 알 수 있는 자료가 하나도 없었다. 번들에는 stdout이 없다. 게다가
선택 창은 저장 파일에 고른 포켓몬이 없을 때만 나오므로(pet.py:19063), "안 뜬다"는
말이 전혀 다른 두 상태를 뜻할 수 있다.

* 이미 고른 포켓몬이 저장돼 있어서 **원래 뜨지 않는 것.** 게임은 곧바로 펫 단계로
  간다. 이때 화면에 있어야 할 것은 선택 창이 아니라 펫이다.
* 창은 만들어졌는데 사용자가 보는 화면에 없는 것. 전체화면 앱이 앞에 있으면
  실측으로 `kCGWindowIsOnscreen`이 아예 잡히지 않는다 -- 전체화면 앱은 자기만의
  Space를 가지고, 아직 활성화되지 않은 새 창은 원래 Space에 생긴다.

둘을 구분할 방법이 없어 추측만 했다. 그래서 어느 단계를 탔는지, 창이 실제로 어디에
어떤 크기로 생겼는지, 그것이 지금 화면에 보이는지를 남긴다. `macnotify`가 보낸
알림을 남기는 것과 같은 이유다.

읽는 사람이 개발자가 아닐 수 있으므로 한 줄이 그대로 문장이 되게 쓴다. 그리고
**아무것도 실패시키지 않는다** -- 기록은 게임보다 덜 중요하다.
"""

import os
import sys
import time

# 기록은 자기가 설명하는 세이브 옆에 둔다. 평소에는
# ~/Library/Application Support/PikaPet/startup.log 이고, APPDATA 를 바꿔 띄운
# 시험 실행은 자기 폴더에 남아 실제 기록을 건드리지 않는다.
LOG_PATH = None

# 한 번 실행에 세 줄쯤 쓴다. 이 크기면 수백 번의 기록이 남고, 넘으면 오래된 절반을
# 버린다. 신고를 받고 물어보는 것은 늘 '마지막 실행'이다.
MAX_BYTES = 64 * 1024

PHASE_NOTES = {
    "select": "select 단계 -- 시작할 포켓몬을 고르는 창을 띄웁니다",
    "pet": "pet 단계 -- 저장된 포켓몬이 있어 선택 창은 건너뜁니다",
}


def _base_dir():
    return os.environ.get("APPDATA") or os.path.expanduser(
        "~/Library/Application Support")


def log_path():
    """기록을 남길 곳. `LOG_PATH` 를 정해두면 그것을 쓴다 (테스트)."""
    return LOG_PATH or os.path.join(_base_dir(), "PikaPet", "startup.log")


def log(message):
    """한 줄 남긴다. 실패하면 조용히 넘어간다."""
    try:
        path = log_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")
        _trim()
        return True
    except Exception:
        return False


def _trim():
    """로그가 계속 커지지 않게 오래된 절반을 버린다."""
    try:
        path = log_path()
        if os.path.getsize(path) <= MAX_BYTES:
            return
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(lines[len(lines) // 2:])
    except Exception:
        pass


def save_path():
    """게임이 세이브를 두는 곳. `install_save_paths()` 가 정한 APPDATA를 따른다."""
    return os.path.join(_base_dir(), "PikaPet", "pet_state.json")


def save_summary(path=None):
    """저장 파일이 있는지. **어느 단계를 탈지가 여기서 갈린다.**"""
    path = path or save_path()
    try:
        info = os.stat(path)
    except OSError:
        return "없음 (그래서 선택 창이 나와야 합니다)"
    when = time.strftime("%m-%d %H:%M", time.localtime(info.st_mtime))
    return f"있음 ({info.st_size}바이트, {when} 저장)"


def screen_size():
    """주 화면 크기. 선택 창은 860x380을 요구하므로 들어가는지가 중요하다."""
    try:
        import AppKit

        frame = AppKit.NSScreen.mainScreen().frame()
        return f"{int(frame.size.width)}x{int(frame.size.height)}"
    except Exception:
        return None


def visible_here(window_list=None):
    """이 앱의 창이 지금 이 화면에 **하나라도** 있으면 True. 모르면 None.

    창 하나를 지목하지 않는다. CGWindowList 의 좌표를 Tk 의 geometry 와 맞추려면
    타이틀 바 높이와 Retina 배율까지 따라가야 하는데, 정작 쫓는 고장은 "창이
    분명히 있는데 사용자 화면에는 하나도 없다" 쪽이라 앱 단위로 충분하다.

    창이 있는데도 안 보이는 경우를 잡으려는 것이다. 전체화면 앱이 앞에 있을 때
    실측으로 우리 창은 목록에서 아예 빠진다.
    """
    if window_list is None:
        try:
            import Quartz

            def window_list():
                return Quartz.CGWindowListCopyWindowInfo(
                    Quartz.kCGWindowListOptionOnScreenOnly
                    | Quartz.kCGWindowListExcludeDesktopElements,
                    Quartz.kCGNullWindowID)
        except Exception:
            return None
    try:
        mine = os.getpid()
        for info in window_list() or []:
            if info.get("kCGWindowOwnerPID") == mine:
                return True
        return False
    except Exception:
        return None


def visibility_note(visible):
    """`visible_here` 의 답을 문장으로. 앱 단위임이 드러나게 쓴다."""
    if visible is None:
        return "화면에 보이는지는 확인하지 못했습니다"
    if visible:
        return "이 앱의 창이 이 화면에 있습니다"
    return ("이 앱의 창이 이 화면에 하나도 없습니다"
            " (다른 Space거나 전체화면 앱 뒤)")


def log_start(version=None):
    """실행 한 번의 첫 줄. 버전, 번들 여부, 화면, 저장 파일."""
    if version is None:
        try:
            import macupdate

            version = macupdate.app_version()
        except Exception:
            version = None
    parts = [f"── 시작 {version or '버전 모름'}",
             "번들" if getattr(sys, "frozen", False) else "소스 실행"]
    screen = screen_size()
    if screen:
        parts.append(f"화면 {screen}")
    parts.append(f"저장 파일 {save_summary()}")
    return log(" | ".join(parts))


def log_phase(name):
    """게임이 어느 단계로 갔는지. 신고를 읽을 때 가장 먼저 보는 줄이다."""
    return log(PHASE_NOTES.get(name, f"{name} 단계"))


def log_window(label, win, window_list=None):
    """창이 실제로 어디에 생겼고 보이는지."""
    geometry = "위치 모름"
    hidden = ""
    try:
        win.update_idletasks()
        geometry = win.winfo_geometry()
    except Exception:
        pass
    try:
        if not win.winfo_ismapped():
            hidden = " | 창이 숨어 있습니다 (몬스터볼?)"
    except Exception:
        pass
    note = visibility_note(visible_here(window_list))
    return log(f"{label} {geometry}{hidden} | {note}")
