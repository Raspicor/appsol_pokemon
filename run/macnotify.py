"""알림을 이 앱 소유로 띄운다. 클릭하면 PikaPet이 올라오도록.

경로가 왜 두 개인지:

* `osascript -e 'display notification'` 은 배너를 확실히 띄우지만, 그 배너의
  소유자가 **스크립트 편집기**다. 그래서 야생 포켓몬 알림을 눌러도 스크립트
  편집기가 열린다.
* `NSUserNotificationCenter` 는 쓰지 않는다. macOS 26에서 알림을 받아
  `deliveredNotifications()` 목록에만 넣고 배너를 띄우지 않으면서 예외도 내지
  않는다. 실측으로 확인했다.
* `UNUserNotificationCenter` (모던 API) 는 앱 번들의 신원으로 알림을 보내므로
  배너가 PikaPet 소유가 되고, 눌렀을 때 PikaPet이 활성화된다. 대신 번들
  식별자와 사용자 허용이 필요하다. `.app` 으로 묶으면 둘 다 충족되고, 소스에서
  그냥 실행하면 번들이 Homebrew의 `org.python.python` 이라 거부된다
  (`UNErrorDomain Code=1`).

**ad-hoc 서명으로는 UN을 쓸 수 없다.** 실측: `codesign -s -` 로 서명한 번들에
대해 macOS는 권한 프롬프트를 띄우지도, 알림 설정에 등록하지도 않고 그냥
`UNErrorDomain Code=1 "Notifications are not allowed for this application"` 을
돌려준다. 앱을 ~/Applications 에 두어도 같다. Developer ID로 서명해야
(`PIKAPET_SIGN_ID=...`) 열린다. 그때는 이 코드가 그대로 동작하고 배너 클릭이
야생 포켓몬 창을 연다.

그래서 UN을 먼저 시도하고, 거부되면 osascript로 떨어진다. 알림이 사라지는 것보다
소유자가 엉뚱한 편이 낫다. 지금 배포되는 ad-hoc 빌드는 항상 osascript 경로다.

**콜백 주의**: UN의 완료 핸들러와 델리게이트는 AppKit 컨텍스트에서 불린다.
거기서 Tcl을 건드리면 프로세스가 abort한다 (overlay.py 참고). 그래서 배너 클릭은
큐에만 넣고, Tk 타이머가 꺼내서 처리한다.
"""

import collections
import os
import subprocess
import time

# 배너를 누른 것을 처리하기까지의 최대 지연.
DRAIN_MS = 120

_delegate_class = None

# 번들로 묶으면 stdout이 없다. 알림은 조용히 실패하기 쉬운 영역이라, 어디까지
# 갔는지 남길 곳이 필요하다.
LOG_PATH = os.path.expanduser("~/Library/Application Support/PikaPet/notify.log")


def _log(message):
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as fh:
            fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")
    except Exception:
        pass


def available():
    """모던 알림 API를 쓸 수 있으면 True."""
    try:
        from UserNotifications import UNUserNotificationCenter  # noqa: F401
    except Exception:
        return False
    return True


def _applescript_string(text):
    escaped = str(text).replace("\\", "\\\\").replace('"', '\\"')
    escaped = escaped.replace("\r", " ").replace("\n", " ")
    return '"' + escaped + '"'


def post_with_osascript(message, title):
    """확실히 뜨는 폴백. 배너 소유자는 스크립트 편집기가 된다.

    **보낸 것을 기록한다.** 배포되는 ad-hoc 빌드는 늘 이 경로를 타는데, 기록이
    없으면 "이 알림이 왜 떴지"에 나중에 답할 방법이 없다. 배너 소유자가 스크립트
    편집기라서 사용자 쪽에서도 출처를 알 수 없기 때문에 더 그렇다. 한 줄이 한
    알림이고, 줄바꿈은 눕혀서 한 줄로 만든다.
    """
    flat = " / ".join(part.strip() for part in str(message).splitlines()
                      if part.strip())
    try:
        script = "display notification {} with title {}".format(
            _applescript_string(message), _applescript_string(title))
        subprocess.Popen(["osascript", "-e", script],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        _log(f"osascript 알림: [{title}] {flat}")
        return True
    except Exception as exc:
        _log(f"osascript 알림 실패: {type(exc).__name__}: {exc} / {flat}")
        return False


def _delegate_cls():
    """배너 클릭을 큐에 넣는 UNUserNotificationCenterDelegate."""
    global _delegate_class
    if _delegate_class is not None:
        return _delegate_class

    from Foundation import NSObject

    class PikaPetNotificationDelegate(NSObject):
        def initWithQueue_(self, queue):
            self = self.init()
            if self is None:
                return None
            self.queue = queue
            return self

        # 앱이 앞에 있어도 배너를 보여준다. 기본값은 조용히 삼키는 것이다.
        def userNotificationCenter_willPresentNotification_withCompletionHandler_(
                self, center, notification, handler):
            try:
                handler(1 << 2 | 1 << 3)   # UNNotificationPresentationOptionSound | .Banner
            except Exception:
                pass

        def userNotificationCenter_didReceiveNotificationResponse_withCompletionHandler_(
                self, center, response, handler):
            # AppKit 컨텍스트다. Tcl은 건드리지 않고 큐에만 넣는다.
            try:
                self.queue.append("clicked")
            except Exception:
                pass
            try:
                handler()
            except Exception:
                pass

    _delegate_class = PikaPetNotificationDelegate
    return _delegate_class


class Notifier:
    """UN으로 먼저 보내고, 거부되면 osascript로 떨어진다.

    `on_click`은 배너를 눌렀을 때 Tk 타이머 안에서 불린다. 없으면 클릭은
    앱을 앞으로 가져오는 것까지만 한다.
    """

    def __init__(self, root, on_click=None):
        self.root = root
        self.on_click = on_click
        self.clicks = collections.deque()
        self.center = None
        self.delegate = None
        self.authorized = None      # None = 아직 모름
        self._counter = 0

        try:
            from UserNotifications import (UNUserNotificationCenter,
                                           UNAuthorizationOptionAlert,
                                           UNAuthorizationOptionSound)

            self.center = UNUserNotificationCenter.currentNotificationCenter()
            self.delegate = _delegate_cls().alloc().initWithQueue_(self.clicks)
            self.center.setDelegate_(self.delegate)
            self.center.requestAuthorizationWithOptions_completionHandler_(
                UNAuthorizationOptionAlert | UNAuthorizationOptionSound,
                self._authorized)
        except Exception as exc:
            print(f"  알림: 모던 API 사용 불가 ({type(exc).__name__}), "
                  f"osascript로 보냅니다", flush=True)
            self.center = None

        self.root.after(DRAIN_MS, self._drain)

    # -- AppKit 콜백. Tcl 금지 -------------------------------------------------

    def _authorized(self, granted, error):
        self.authorized = bool(granted)
        _log(f"권한 요청 결과: granted={bool(granted)} error={error}")
        if not granted:
            print(f"  알림: 이 번들에는 허용되지 않음 ({error}). "
                  f"osascript로 보냅니다", flush=True)

    def _added(self, error):
        _log(f"발송 결과: error={error}")
        if error is not None:
            # UN이 거부했다. 여기서 폴백을 쏜다 (subprocess라 Tcl과 무관하다).
            self.authorized = False
            pending = getattr(self, "_last", None)
            if pending:
                post_with_osascript(*pending)

    # -- 보내기 ---------------------------------------------------------------

    def notify(self, message, title="PikaPet"):
        if self.center is None or self.authorized is False:
            return post_with_osascript(message, title)
        try:
            from UserNotifications import (UNMutableNotificationContent,
                                           UNNotificationRequest)

            content = UNMutableNotificationContent.alloc().init()
            content.setTitle_(str(title))
            content.setBody_(str(message))
            self._counter += 1
            self._last = (message, title)
            request = UNNotificationRequest.requestWithIdentifier_content_trigger_(
                f"pikapet-{self._counter}", content, None)
            self.center.addNotificationRequest_withCompletionHandler_(
                request, self._added)
            return True
        except Exception:
            return post_with_osascript(message, title)

    # -- 클릭 처리. Tk 타이머 안 --------------------------------------------

    def _drain(self):
        while self.clicks:
            self.clicks.popleft()
            if self.on_click is None:
                continue
            try:
                self.on_click()
            except Exception as exc:
                print(f"  알림 클릭 처리 실패: {type(exc).__name__}: {exc}",
                      flush=True)
        try:
            if self.root.winfo_exists():
                self.root.after(DRAIN_MS, self._drain)
        except Exception:
            pass
