"""macupdate.py 테스트. 디스플레이도 네트워크도 쓰지 않는다.

여기서 지키려는 것은 세 가지다:

  * 버전 비교가 틀리지 않을 것 -- 틀리면 최신인데 업데이트하라고 뜨거나,
    새 버전이 나왔는데 조용하다.
  * 어떤 실패에도 앱이 멈추지 않을 것. 업데이트 안내는 있으면 좋은 것이지
    앱의 기능이 아니다.
  * **네트워크 스레드가 Tk를 건드리지 않을 것.** 건드리면 다음 `after` 타이머가
    프로세스를 abort시킨다 (overlay.py 참고). 이건 실제로 두 번 당한 문제다.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import macupdate


class ParsingVersions(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(macupdate.parse_version("0.0.2"), (0, 0, 2))

    def test_a_leading_v_is_accepted(self):
        # 태그를 v0.1.0 으로 달 수도 있다.
        self.assertEqual(macupdate.parse_version("v0.1.0"), (0, 1, 0))

    def test_suffixes_are_dropped(self):
        # make_dmg.sh 는 태그 위가 아닌 빌드에 +sha 를 붙인다.
        self.assertEqual(macupdate.parse_version("0.0.2+f81bdd5"), (0, 0, 2))
        self.assertEqual(macupdate.parse_version("0.1.0-beta"), (0, 1, 0))

    def test_short_and_long_forms(self):
        self.assertEqual(macupdate.parse_version("1"), (1,))
        self.assertEqual(macupdate.parse_version("1.2.3.4"), (1, 2, 3, 4))

    def test_nonsense_gives_none(self):
        for text in ("", "latest", "0.0.x", "1.2.3.4.5", None, 3):
            self.assertIsNone(macupdate.parse_version(text), text)


class ComparingVersions(unittest.TestCase):
    def test_newer(self):
        self.assertTrue(macupdate.is_newer("0.0.3", "0.0.2"))
        self.assertTrue(macupdate.is_newer("0.1.0", "0.0.9"))
        self.assertTrue(macupdate.is_newer("1.0.0", "0.9.9"))

    def test_same_is_not_newer(self):
        self.assertFalse(macupdate.is_newer("0.0.2", "0.0.2"))

    def test_older_is_not_newer(self):
        self.assertFalse(macupdate.is_newer("0.0.1", "0.0.2"))

    def test_different_lengths_compare_by_value(self):
        # 0.1 과 0.1.0 은 같은 버전이다. 자릿수로 비교하면 안 된다.
        self.assertFalse(macupdate.is_newer("0.1", "0.1.0"))
        self.assertTrue(macupdate.is_newer("0.1.1", "0.1"))

    def test_unreadable_versions_never_claim_an_update(self):
        # 틀리게 비교하느니 비교를 포기한다.
        self.assertFalse(macupdate.is_newer("최신", "0.0.2"))
        self.assertFalse(macupdate.is_newer("0.0.3", None))

    def test_a_dev_build_is_not_told_to_update_to_its_own_tag(self):
        # 0.0.2+sha 로 빌드된 것에 릴리스 0.0.2 는 새 버전이 아니다.
        self.assertFalse(macupdate.is_newer("0.0.2", "0.0.2+f81bdd5"))


class Fetching(unittest.TestCase):
    def test_the_tag_is_returned(self):
        def opener(request, timeout=None):
            return FakeResponse(b'{"tag_name": "0.0.3"}')

        self.assertEqual(macupdate.fetch_latest_tag(opener=opener), "0.0.3")

    def test_no_releases_yet_is_silent(self):
        # 릴리스가 하나도 없으면 GitHub는 404를 준다. 오류가 아니라 '아직 없다'다.
        def opener(request, timeout=None):
            raise OSError("HTTP Error 404: Not Found")

        self.assertIsNone(macupdate.fetch_latest_tag(opener=opener))

    def test_being_offline_is_silent(self):
        def opener(request, timeout=None):
            raise OSError("nodename nor servname provided")

        self.assertIsNone(macupdate.fetch_latest_tag(opener=opener))

    def test_garbage_json_is_silent(self):
        def opener(request, timeout=None):
            return FakeResponse("<html>없음</html>".encode("utf-8"))

        self.assertIsNone(macupdate.fetch_latest_tag(opener=opener))

    def test_a_missing_tag_field_is_silent(self):
        def opener(request, timeout=None):
            return FakeResponse(b'{"name": "0.0.3"}')

        self.assertIsNone(macupdate.fetch_latest_tag(opener=opener))


class FakeResponse:
    def __init__(self, body):
        self.body = body

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakeRoot:
    """Tk 루트 자리. 예약된 콜백을 손으로 돌릴 수 있게 들고만 있는다."""

    def __init__(self):
        self.scheduled = []
        self.touched_from = []

    def after(self, _ms, fn):
        self.touched_from.append("after")
        self.scheduled.append(fn)

    def run_pending(self):
        pending, self.scheduled = self.scheduled, []
        for fn in pending:
            fn()


class Reporting(unittest.TestCase):
    def setUp(self):
        self.root = FakeRoot()
        self.told = []

    def make(self, latest, current="0.0.2"):
        return macupdate.UpdateCheck(
            self.root, current,
            lambda tag, url: self.told.append((tag, url)),
            fetch=lambda: latest)

    def test_a_newer_release_is_reported(self):
        check = self.make("0.0.3")
        check.start()
        for _ in range(20):
            self.root.run_pending()
            if self.told:
                break
        self.assertEqual(self.told[0][0], "0.0.3")
        self.assertIn("releases", self.told[0][1])

    def test_the_same_version_is_not_reported(self):
        check = self.make("0.0.2")
        check.start()
        for _ in range(20):
            self.root.run_pending()
        self.assertEqual(self.told, [])

    def test_a_failed_fetch_is_not_reported(self):
        check = self.make(None)
        check.start()
        for _ in range(20):
            self.root.run_pending()
        self.assertEqual(self.told, [])

    def test_the_network_thread_never_touches_tk(self):
        # 이게 이 파일에서 가장 중요한 테스트다. 스레드가 Tk를 부르면 다음
        # after 타이머에서 프로세스가 abort한다.
        calls = []

        class Trap:
            def after(self, _ms, fn):
                calls.append(fn)

            def __getattr__(self, name):
                raise AssertionError(f"네트워크 스레드가 Tk의 {name} 을 불렀다")

        check = macupdate.UpdateCheck(Trap(), "0.0.2", lambda *a: None,
                                      fetch=lambda: "0.0.3")
        check._work()                       # 스레드가 하는 일 그대로
        self.assertEqual(list(check.results), ["0.0.3"])
        self.assertEqual(calls, [])

    def test_the_callback_runs_on_the_tk_side(self):
        check = self.make("0.0.3")
        check._work()                       # 결과만 큐에 넣고
        self.assertEqual(self.told, [])     # 아직 아무에게도 알리지 않았다
        check.drain()                       # Tk 타이머가 꺼낼 때 알린다
        self.assertEqual(len(self.told), 1)

    def test_a_broken_callback_does_not_escape(self):
        def explode(tag, url):
            raise RuntimeError("안 됨")

        check = macupdate.UpdateCheck(self.root, "0.0.2", explode,
                                      fetch=lambda: "0.0.3")
        check._work()
        check.drain()                       # 예외가 새어 나오면 실패

    def test_it_stops_scheduling_once_the_answer_arrives(self):
        check = self.make("0.0.3")
        check._work()
        check.drain()
        self.assertTrue(check.done)
        self.assertEqual(self.root.scheduled, [])


class Switch(unittest.TestCase):
    def setUp(self):
        self.original = os.environ.get("PIKAPET_UPDATE_CHECK")
        self.addCleanup(self._restore)
        self.frozen = getattr(sys, "frozen", None)
        self.addCleanup(self._restore_frozen)

    def _restore(self):
        if self.original is None:
            os.environ.pop("PIKAPET_UPDATE_CHECK", None)
        else:
            os.environ["PIKAPET_UPDATE_CHECK"] = self.original

    def _restore_frozen(self):
        if self.frozen is None:
            if hasattr(sys, "frozen"):
                del sys.frozen
        else:
            sys.frozen = self.frozen

    def test_off_when_running_from_source(self):
        os.environ.pop("PIKAPET_UPDATE_CHECK", None)
        if hasattr(sys, "frozen"):
            del sys.frozen
        self.assertFalse(macupdate.enabled())

    def test_on_in_a_bundle(self):
        os.environ.pop("PIKAPET_UPDATE_CHECK", None)
        sys.frozen = True
        self.assertTrue(macupdate.enabled())

    def test_the_environment_variable_wins_both_ways(self):
        sys.frozen = True
        os.environ["PIKAPET_UPDATE_CHECK"] = "0"
        self.assertFalse(macupdate.enabled())
        if hasattr(sys, "frozen"):
            del sys.frozen
        os.environ["PIKAPET_UPDATE_CHECK"] = "1"
        self.assertTrue(macupdate.enabled())


class ReadingOurOwnVersion(unittest.TestCase):
    def setUp(self):
        self.version = os.environ.get("PIKAPET_VERSION")
        self.frozen = getattr(sys, "frozen", None)
        self.addCleanup(self._restore)

    def _restore(self):
        if self.version is None:
            os.environ.pop("PIKAPET_VERSION", None)
        else:
            os.environ["PIKAPET_VERSION"] = self.version
        if self.frozen is None:
            if hasattr(sys, "frozen"):
                del sys.frozen
        else:
            sys.frozen = self.frozen

    def test_source_runs_have_no_version(self):
        # 소스에서 NSBundle 을 읽으면 Homebrew Python.app 의 3.14.7 이 나온다.
        # 그걸 앱 버전으로 쓰면 비교가 통째로 엉뚱해진다.
        os.environ.pop("PIKAPET_VERSION", None)
        if hasattr(sys, "frozen"):
            del sys.frozen
        self.assertIsNone(macupdate.app_version())

    def test_the_override_wins(self):
        os.environ["PIKAPET_VERSION"] = "0.0.9"
        self.assertEqual(macupdate.app_version(), "0.0.9")


if __name__ == "__main__":
    unittest.main()
