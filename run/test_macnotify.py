"""macnotify.py 테스트. 배너를 실제로 띄우지 않는다.

여기서 지키려는 것은 **기록**이다. 배포되는 ad-hoc 빌드는 알림을 늘 osascript로
보내는데, 그 배너의 소유자는 스크립트 편집기가 된다. 즉 사용자 쪽에서는 알림의
출처를 알 방법이 없다. 그래서 "이 알림이 왜 떴는가"에 답할 수 있는 유일한 자료가
notify.log 다. 실제로 이것이 없어서 새 사용자가 본 야생 조우 알림의 출처를 추적할
수 없었다.
"""

import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import macnotify


class FakePopen:
    """osascript를 실제로 돌리지 않는다."""

    calls = []

    def __init__(self, argv, **kw):
        FakePopen.calls.append(argv)


class LoggingWhatWeSent(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original_log = macnotify.LOG_PATH
        self.original_popen = macnotify.subprocess.Popen
        self.addCleanup(self._restore)
        macnotify.LOG_PATH = os.path.join(self.tmp, "notify.log")
        macnotify.subprocess.Popen = FakePopen
        FakePopen.calls = []

    def _restore(self):
        macnotify.LOG_PATH = self.original_log
        macnotify.subprocess.Popen = self.original_popen

    def logged(self):
        try:
            with open(macnotify.LOG_PATH, encoding="utf-8") as fh:
                return fh.read()
        except OSError:
            return ""

    def test_the_message_is_written_down(self):
        macnotify.post_with_osascript("야생 포켓몬이 나타난 것 같아요!", "PikaPet")
        written = self.logged()
        self.assertIn("야생 포켓몬이 나타난 것 같아요", written)
        self.assertIn("PikaPet", written)

    def test_the_line_carries_a_date(self):
        # 하루를 넘기면 시각만으로는 순서를 알 수 없다.
        macnotify.post_with_osascript("가", "PikaPet")
        self.assertRegex(self.logged(), r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_a_multiline_message_stays_on_one_line(self):
        # 한 줄이 한 알림이어야 읽을 수 있다.
        macnotify.post_with_osascript("첫 줄\n둘째 줄", "PikaPet")
        body = self.logged().strip()
        self.assertEqual(len(body.splitlines()), 1, body)
        self.assertIn("첫 줄 / 둘째 줄", body)

    def test_the_banner_still_goes_out(self):
        # 기록이 발송을 대신하는 것이 아니다.
        self.assertTrue(macnotify.post_with_osascript("가", "PikaPet"))
        self.assertEqual(len(FakePopen.calls), 1)
        self.assertEqual(FakePopen.calls[0][0], "osascript")
        self.assertIn("가", FakePopen.calls[0][-1])

    def test_a_failure_is_written_down_too(self):
        def boom(argv, **kw):
            raise OSError("osascript 없음")

        macnotify.subprocess.Popen = boom
        self.assertFalse(macnotify.post_with_osascript("가", "PikaPet"))
        self.assertIn("실패", self.logged())

    def test_an_unwritable_log_does_not_stop_the_notification(self):
        # 알림이 사라지는 것보다 기록이 없는 편이 낫다.
        macnotify.LOG_PATH = "/System/그럴수없는곳/notify.log"
        self.assertTrue(macnotify.post_with_osascript("가", "PikaPet"))


class EscapingForAppleScript(unittest.TestCase):
    """따옴표가 들어간 메시지가 스크립트를 깨뜨리지 않아야 한다."""

    def test_quotes_are_escaped(self):
        got = macnotify._applescript_string('그는 "안녕" 이라 했다')
        self.assertTrue(got.startswith('"') and got.endswith('"'))
        self.assertNotIn('"안녕"', got[1:-1])

    def test_backslashes_are_escaped(self):
        got = macnotify._applescript_string("경로\\여기")
        self.assertIn("\\\\", got)


if __name__ == "__main__":
    unittest.main()
