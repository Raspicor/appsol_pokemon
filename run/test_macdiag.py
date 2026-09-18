"""macdiag.py 테스트. 화면이 없어도 돌아야 한다.

여기서 지키려는 것은 **어느 단계를 탔는지 사후에 알 수 있는가** 다. 선택 창이
안 뜬다는 신고는 저장 파일이 있어서 원래 안 뜨는 것일 수도 있고, 창이 다른
Space에 생긴 것일 수도 있다. 로그가 그 둘을 구분해주지 못하면 있을 이유가 없다.
"""

import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import macdiag


# 이 모듈의 테스트는 런처를 그대로 부르므로, 손대지 않으면 `macdiag` 가
# ~/Library/Application Support/PikaPet/startup.log -- **실제 사용자의 기록** --
# 에 줄을 남긴다. 실제로 그렇게 됐다: StarterWindowFix 가 돌 때마다 select 단계
# 다섯 줄이 쌓여서, 신고를 받고 읽을 기록이 테스트 소음으로 덮였다. 개별 setUp
# 대신 모듈 단위로 막는다 -- 앞으로 추가되는 테스트까지 덮으려면 이쪽이어야 한다.
_log_home = None


def setUpModule():
    global _log_home
    import macdiag

    _log_home = (macdiag.LOG_PATH, tempfile.mkdtemp())
    macdiag.LOG_PATH = os.path.join(_log_home[1], "startup.log")


def tearDownModule():
    import macdiag

    original, tmp = _log_home
    macdiag.LOG_PATH = original
    shutil.rmtree(tmp, ignore_errors=True)


class FakeWindow:
    """Tk 없이 창 흉내만. winfo_geometry 만 있으면 된다."""

    def __init__(self, geometry="860x380+5+35", mapped=True, boom=False):
        self._geometry = geometry
        self._mapped = mapped
        self._boom = boom

    def update_idletasks(self):
        if self._boom:
            raise RuntimeError("창이 이미 사라졌다")

    def winfo_geometry(self):
        if self._boom:
            raise RuntimeError("창이 이미 사라졌다")
        return self._geometry

    def winfo_ismapped(self):
        return self._mapped


class WhereItGoes(unittest.TestCase):
    """기록은 자기가 설명하는 세이브 옆에 있어야 한다."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original = os.environ.get("APPDATA")
        self.addCleanup(self._restore)
        self.original_log = macdiag.LOG_PATH
        self.addCleanup(setattr, macdiag, "LOG_PATH", self.original_log)
        macdiag.LOG_PATH = None

    def _restore(self):
        if self.original is None:
            os.environ.pop("APPDATA", None)
        else:
            os.environ["APPDATA"] = self.original

    def test_it_sits_next_to_the_save_file(self):
        os.environ["APPDATA"] = self.tmp
        self.assertEqual(os.path.dirname(macdiag.log_path()),
                         os.path.dirname(macdiag.save_path()))

    def test_an_isolated_run_does_not_touch_the_real_log(self):
        # APPDATA 를 바꿔 띄운 시험 실행이 실제 기록을 덮으면 안 된다.
        os.environ["APPDATA"] = self.tmp
        macdiag.log("시험 실행")
        self.assertTrue(os.path.isfile(os.path.join(
            self.tmp, "PikaPet", "startup.log")))

    def test_the_usual_place_is_the_support_folder(self):
        os.environ.pop("APPDATA", None)
        self.assertEqual(
            macdiag.log_path(),
            os.path.expanduser(
                "~/Library/Application Support/PikaPet/startup.log"))


class WritingItDown(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original = macdiag.LOG_PATH
        self.addCleanup(setattr, macdiag, "LOG_PATH", self.original)
        macdiag.LOG_PATH = os.path.join(self.tmp, "startup.log")

    def logged(self):
        try:
            with open(macdiag.LOG_PATH, encoding="utf-8") as fh:
                return fh.read()
        except OSError:
            return ""

    def test_a_line_carries_the_date_and_time(self):
        macdiag.log("무슨 일")
        self.assertRegex(self.logged(), r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} 무슨 일")

    def test_lines_accumulate(self):
        macdiag.log("첫째")
        macdiag.log("둘째")
        self.assertEqual(len(self.logged().strip().splitlines()), 2)

    def test_an_unwritable_path_does_not_raise(self):
        macdiag.LOG_PATH = "/System/그럴수없는곳/startup.log"
        self.assertFalse(macdiag.log("무슨 일"))

    def test_an_oversized_log_keeps_the_newest_half(self):
        # 마지막 실행이 늘 궁금한 쪽이므로 꼬리를 남겨야 한다.
        with open(macdiag.LOG_PATH, "w", encoding="utf-8") as fh:
            for i in range(10000):
                fh.write(f"줄 {i}\n")
        self.assertGreater(os.path.getsize(macdiag.LOG_PATH), macdiag.MAX_BYTES)
        macdiag.log("마지막")
        body = self.logged()
        self.assertLess(os.path.getsize(macdiag.LOG_PATH), macdiag.MAX_BYTES)
        self.assertIn("마지막", body)
        self.assertIn("줄 9999", body)
        self.assertNotIn("줄 0\n", body)


class WhichPhaseItTook(unittest.TestCase):
    """로그를 읽는 사람이 제일 먼저 보는 줄."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original = macdiag.LOG_PATH
        self.addCleanup(setattr, macdiag, "LOG_PATH", self.original)
        macdiag.LOG_PATH = os.path.join(self.tmp, "startup.log")

    def logged(self):
        with open(macdiag.LOG_PATH, encoding="utf-8") as fh:
            return fh.read()

    def test_the_pet_phase_says_the_picker_is_skipped(self):
        # 이 한 줄이 "선택 창이 안 뜬다"가 버그인지 정상인지를 가른다.
        macdiag.log_phase("pet")
        written = self.logged()
        self.assertIn("pet 단계", written)
        self.assertIn("건너뜁니다", written)

    def test_the_select_phase_says_the_picker_is_shown(self):
        macdiag.log_phase("select")
        self.assertIn("고르는 창", self.logged())

    def test_an_unknown_phase_is_still_recorded(self):
        macdiag.log_phase("난생처음")
        self.assertIn("난생처음 단계", self.logged())


class LookingAtTheSaveFile(unittest.TestCase):
    """단계가 갈리는 지점. 저장 파일이 있으면 선택 창은 나오지 않는다."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def test_a_missing_save_explains_what_should_happen(self):
        got = macdiag.save_summary(os.path.join(self.tmp, "없는파일.json"))
        self.assertIn("없음", got)
        self.assertIn("선택 창", got)

    def test_an_existing_save_reports_size_and_time(self):
        path = os.path.join(self.tmp, "pet_state.json")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("PKPT1:xxxx")
        got = macdiag.save_summary(path)
        self.assertIn("있음", got)
        self.assertIn("10바이트", got)

    def test_the_path_follows_appdata(self):
        # install_save_paths()가 APPDATA를 정하고, 게임이 거기에 저장한다.
        original = os.environ.get("APPDATA")
        self.addCleanup(lambda: os.environ.__setitem__("APPDATA", original)
                        if original is not None
                        else os.environ.pop("APPDATA", None))
        os.environ["APPDATA"] = self.tmp
        self.assertEqual(macdiag.save_path(),
                         os.path.join(self.tmp, "PikaPet", "pet_state.json"))


class CanWeDrawImages(unittest.TestCase):
    """이미지만 안 나오고 나머지는 멀쩡한 증상이 여기서 갈린다."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original = macdiag.LOG_PATH
        self.addCleanup(setattr, macdiag, "LOG_PATH", self.original)
        macdiag.LOG_PATH = os.path.join(self.tmp, "startup.log")

    def logged(self):
        with open(macdiag.LOG_PATH, encoding="utf-8") as fh:
            return fh.read()

    def test_it_reports_the_pil_version(self):
        macdiag.log_images()
        self.assertIn("PIL", self.logged())

    def test_every_folder_present_is_counted(self):
        dirs = [os.path.join(self.tmp, n) for n in ("하나", "둘")]
        for d in dirs:
            os.makedirs(d)
        macdiag.log_images(dirs)
        self.assertIn("스프라이트 폴더 2/2 있음", self.logged())

    def test_a_missing_folder_is_named(self):
        # 심볼릭 링크가 사라진 번들이 정확히 이 모양이다.
        present = os.path.join(self.tmp, "있음")
        os.makedirs(present)
        missing = os.path.join(self.tmp, "없음")
        macdiag.log_images([present, missing])
        written = self.logged()
        self.assertIn("스프라이트 폴더 1/2 있음", written)
        self.assertIn(missing, written)

    def test_no_folder_list_is_said_so(self):
        macdiag.log_images([])
        self.assertIn("못 읽었습니다", self.logged())

    def test_it_stays_on_one_line(self):
        macdiag.log_images([self.tmp])
        self.assertEqual(len(self.logged().strip().splitlines()), 1)


class IsItActuallyOnScreen(unittest.TestCase):
    """창이 있는데 안 보이는 경우를 잡으려는 것이다."""

    def test_our_own_window_in_the_list_means_visible(self):
        mine = [{"kCGWindowOwnerPID": os.getpid(), "kCGWindowName": "PikaPet"}]
        self.assertTrue(macdiag.visible_here(lambda: mine))

    def test_only_other_apps_means_not_visible(self):
        others = [{"kCGWindowOwnerPID": os.getpid() + 1}]
        self.assertFalse(macdiag.visible_here(lambda: others))

    def test_an_empty_list_means_not_visible(self):
        self.assertFalse(macdiag.visible_here(lambda: None))

    def test_a_failure_is_unknown_not_false(self):
        # "모른다"를 "안 보인다"로 적으면 없는 문제를 쫓게 된다.
        def boom():
            raise OSError("Quartz 없음")

        self.assertIsNone(macdiag.visible_here(boom))

    def test_each_answer_reads_as_a_sentence(self):
        self.assertIn("이 화면에 있습니다", macdiag.visibility_note(True))
        self.assertIn("하나도 없습니다", macdiag.visibility_note(False))
        self.assertIn("확인하지 못했습니다", macdiag.visibility_note(None))

    def test_the_answer_is_about_the_app_not_one_window(self):
        # 내려간 창 하나를 두고 "보입니다"로 읽히면 오해를 준다.
        for answer in (True, False):
            self.assertIn("이 앱의 창", macdiag.visibility_note(answer))

    def test_not_visible_names_the_likely_cause(self):
        self.assertIn("전체화면", macdiag.visibility_note(False))


class RecordingAWindow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original = macdiag.LOG_PATH
        self.addCleanup(setattr, macdiag, "LOG_PATH", self.original)
        macdiag.LOG_PATH = os.path.join(self.tmp, "startup.log")

    def logged(self):
        with open(macdiag.LOG_PATH, encoding="utf-8") as fh:
            return fh.read()

    def test_the_geometry_is_written_down(self):
        macdiag.log_window("선택 창", FakeWindow("860x412+530+233"),
                           window_list=lambda: [])
        self.assertIn("선택 창 860x412+530+233", self.logged())

    def test_an_unmapped_window_is_called_out(self):
        # 몬스터볼에 들어가면 창이 내려간다. 펫이 사라졌다는 신고의 절반이 이것이다.
        macdiag.log_window("펫 창", FakeWindow(mapped=False),
                           window_list=lambda: [])
        self.assertIn("숨어 있습니다", self.logged())

    def test_a_dead_window_still_leaves_a_line(self):
        macdiag.log_window("펫 창", FakeWindow(boom=True), window_list=lambda: [])
        self.assertIn("위치 모름", self.logged())

    def test_the_visibility_is_on_the_same_line(self):
        macdiag.log_window("선택 창", FakeWindow(),
                           window_list=lambda: [{"kCGWindowOwnerPID": os.getpid()}])
        line = self.logged().strip()
        self.assertEqual(len(line.splitlines()), 1, line)
        self.assertIn("이 앱의 창이 이 화면에 있습니다", line)


class TheFirstLine(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.original = macdiag.LOG_PATH
        self.addCleanup(setattr, macdiag, "LOG_PATH", self.original)
        macdiag.LOG_PATH = os.path.join(self.tmp, "startup.log")

    def logged(self):
        with open(macdiag.LOG_PATH, encoding="utf-8") as fh:
            return fh.read()

    def test_it_names_the_version_and_the_save(self):
        macdiag.log_start(version="0.0.9")
        written = self.logged()
        self.assertIn("0.0.9", written)
        self.assertIn("저장 파일", written)

    def test_an_unknown_version_still_logs(self):
        macdiag.log_start(version="")
        self.assertIn("버전 모름", self.logged())

    def test_it_says_whether_this_is_a_bundle(self):
        macdiag.log_start(version="0.0.9")
        self.assertIn("소스 실행", self.logged())


if __name__ == "__main__":
    unittest.main()
