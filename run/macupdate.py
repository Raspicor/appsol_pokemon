"""새 버전이 나왔는지 확인한다.

저장소가 공개라 GitHub의 릴리스 API를 **토큰 없이** 읽을 수 있다. 그래서 서버를
따로 둘 필요가 없다.

왜 SSE나 WebSocket이 아닌가: 둘 다 24시간 떠 있는 서버가 전제인데 이 앱에는
그런 게 없다 (PvP의 `ws://` 주소는 사용자가 직접 넣는 ngrok 주소다). 게다가
'새 버전이 나왔다'는 사건은 잘해야 주 1회라, 그 하나를 초 단위로 받으려고
소켓을 며칠씩 붙들고 잠자기·네트워크 전환마다 재연결하는 것은 값이 안 맞는다.
시작할 때 HTTPS GET 한 번이면 충분하다.

**스레드 주의**: 네트워크는 데몬 스레드에서 한다. 그 스레드에서 Tk를 건드리면
프로세스가 abort한다 (overlay.py의 모듈 독스트링 참고). 그래서 결과는 큐에만
넣고, Tk 타이머가 꺼내서 콜백을 부른다. overlay/mactray와 같은 방식이다.

조용히 실패하는 것이 원칙이다. 오프라인이든, API가 막혔든, 릴리스가 하나도
없든 앱은 그냥 떠야 한다. 업데이트 안내는 있으면 좋은 것이지 앱의 기능이 아니다.
"""

import collections
import json
import os
import sys
import threading
import urllib.request

OWNER_REPO = "Raspicor/appsol_pokemon"
API_URL = f"https://api.github.com/repos/{OWNER_REPO}/releases/latest"
RELEASES_URL = f"https://github.com/{OWNER_REPO}/releases/latest"

# 응답을 기다리는 시간. 길게 잡을 이유가 없다 -- 실패하면 그냥 넘어간다.
TIMEOUT_SEC = 6

# 결과를 꺼내보는 주기.
DRAIN_MS = 500


def app_version():
    """실행 중인 앱의 버전. 알 수 없으면 None.

    번들의 Info.plist가 유일한 출처다. 그 값은 빌드할 때 git 태그에서 왔으므로
    (tools/make_dmg.sh) 태그 -> 번들 -> 이 비교가 한 줄로 이어진다.

    **번들일 때만 읽는다.** 소스에서 그냥 실행하면 `NSBundle.mainBundle()` 이
    Homebrew의 Python.app 이라 CFBundleShortVersionString 이 파이썬 버전
    (3.14.7)으로 나온다. 실측으로 확인했다. 그걸 앱 버전으로 쓰면 비교가
    통째로 엉뚱해진다. 시험용으로는 PIKAPET_VERSION 으로 넣어줄 수 있다.
    """
    override = os.environ.get("PIKAPET_VERSION")
    if override:
        return override
    if not getattr(sys, "frozen", False):
        return None
    try:
        import AppKit

        value = AppKit.NSBundle.mainBundle().objectForInfoDictionaryKey_(
            "CFBundleShortVersionString")
        return str(value) if value else None
    except Exception:
        return None


def parse_version(text):
    """'v0.0.2' / '0.0.2' -> (0, 0, 2). 못 읽으면 None.

    숫자가 아닌 꼬리표(0.1.0-beta, 0.0.2+abc)는 떼고 숫자만 본다. 비교에 쓰는
    값이라, 읽을 수 없으면 비교를 포기하는 편이 틀리게 비교하는 것보다 낫다.
    """
    if not isinstance(text, str):
        return None
    text = text.strip().lstrip("vV")
    for sep in ("-", "+", " "):
        text = text.split(sep)[0]
    parts = text.split(".")
    if not parts or len(parts) > 4:
        return None
    numbers = []
    for part in parts:
        if not part.isdigit():
            return None
        numbers.append(int(part))
    return tuple(numbers)


def is_newer(latest, current):
    """`latest`가 `current`보다 높은가. 한쪽이라도 못 읽으면 False."""
    a, b = parse_version(latest), parse_version(current)
    if a is None or b is None:
        return False
    length = max(len(a), len(b))
    return a + (0,) * (length - len(a)) > b + (0,) * (length - len(b))


def fetch_latest_tag(url=API_URL, timeout=TIMEOUT_SEC, opener=None):
    """최신 릴리스의 태그 이름. 없거나 실패하면 None.

    릴리스가 하나도 없으면 GitHub는 404를 준다. 오류가 아니라 '아직 없다'는
    뜻이므로 조용히 None을 돌려준다.
    """
    try:
        request = urllib.request.Request(
            url, headers={"Accept": "application/vnd.github+json",
                          "User-Agent": "PikaPet"})
        open_url = opener or urllib.request.urlopen
        with open_url(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        tag = payload.get("tag_name")
        return tag if isinstance(tag, str) else None
    except Exception:
        return None


def enabled():
    """이 실행에서 업데이트 확인을 할 것인가.

    소스에서 돌릴 때는 끈다 -- 개발 중에 '새 버전이 있어요'가 뜨면 방해만 된다.
    번들에서도 PIKAPET_UPDATE_CHECK=0 으로 끌 수 있다.
    """
    flag = os.environ.get("PIKAPET_UPDATE_CHECK")
    if flag is not None:
        return flag not in ("0", "false", "no", "")
    return bool(getattr(sys, "frozen", False))


class UpdateCheck:
    """백그라운드로 확인하고, 결과를 Tk 타이머에서 콜백으로 넘긴다.

    `on_update(latest_tag, url)` 은 새 버전이 있을 때만 불린다. Tk 메인 스레드
    안이므로 위젯을 건드려도 된다.

    `on_result(latest_tag, is_new)` 를 주면 그것이 대신 불리고, **결과가 무엇이든
    한 번 불린다** (최신일 때도, 조회에 실패해 tag 가 None 일 때도). 사람이 메뉴에서
    직접 확인을 눌렀을 때 쓴다 -- 눌렀는데 아무 반응이 없으면 고장으로 보인다.
    """

    def __init__(self, root, current_version, on_update, fetch=None,
                 on_result=None):
        self.root = root
        self.current = current_version
        self.on_update = on_update
        self.on_result = on_result
        self.fetch = fetch or fetch_latest_tag
        self.results = collections.deque()
        self.done = False

    def start(self):
        """확인을 시작한다. 바로 돌아온다."""
        thread = threading.Thread(target=self._work, name="pikapet-update",
                                  daemon=True)
        thread.start()
        self._schedule()
        return thread

    # -- 네트워크 스레드. Tcl 금지 ------------------------------------------

    def _work(self):
        tag = self.fetch()
        # 여기서는 큐에 넣기만 한다. Tk를 건드리면 프로세스가 죽는다.
        self.results.append(tag)

    # -- Tk 타이머 안 --------------------------------------------------------

    def _schedule(self):
        try:
            self.root.after(DRAIN_MS, self.drain)
        except Exception:
            pass

    def drain(self):
        """결과가 왔으면 처리한다. 안 왔으면 다시 예약한다."""
        if not self.results:
            if not self.done:
                self._schedule()
            return
        self.done = True
        tag = self.results.popleft()
        newer = is_newer(tag, self.current)
        try:
            if self.on_result is not None:
                self.on_result(tag, newer)
            elif newer:
                self.on_update(tag, RELEASES_URL)
        except Exception as exc:
            print(f"  업데이트 안내 실패: {type(exc).__name__}: {exc}", flush=True)


def open_releases_page(url=RELEASES_URL):
    """받는 곳을 브라우저로 연다."""
    try:
        import subprocess

        subprocess.Popen(["open", url],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False
