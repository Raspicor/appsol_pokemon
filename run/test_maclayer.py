"""PikaPet의 winlayer를 macOS에서 대신하는 maclayer의 계약 테스트.

pet.pyc는 winlayer를 함수 열 개로 부르고 반환값을 바로 풀어 쓴다. 그래서 값보다
모양이 더 중요하다. 이 테스트들은 그 모양을 실제 winlayer.pyc와, Win32 원본이
돌려주던 것에 맞춰 고정한다.

    cd ~/projects/pikapet && .venv/bin/python -m unittest discover -s run -v
"""

import importlib.util
import inspect
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import maclayer  # noqa: E402


# 락 테스트는 실제로 flock 을 잡는다. 그리고 `maclayer._lock_dir()` 은 APPDATA 를
# 읽으므로, 손대지 않으면 pikapet-selftest-*.lock 네 개가
# ~/Library/Application Support/PikaPet/ -- **실제 사용자의 폴더** -- 에 남는다.
# 실제로 남아 있었다. 여기서 APPDATA 를 임시 폴더로 돌린다. 교차 프로세스
# 테스트가 띄우는 자식도 환경을 물려받으므로 같은 임시 폴더를 본다.
_appdata_home = None


def setUpModule():
    global _appdata_home
    _appdata_home = (os.environ.get("APPDATA"), tempfile.mkdtemp())
    os.environ["APPDATA"] = _appdata_home[1]


def tearDownModule():
    original, tmp = _appdata_home
    if original is None:
        os.environ.pop("APPDATA", None)
    else:
        os.environ["APPDATA"] = original
    shutil.rmtree(tmp, ignore_errors=True)


def _load_winlayer_pyc():
    """공개 시그니처를 비교할 수 있도록 함께 배포된 winlayer.pyc를 로드한다.

    Windows가 아닌 곳에서도 문제없이 import된다 — 모든 함수가 IS_WINDOWS에서
    바로 빠져나간다 — 그래서 비용이 없다.
    """
    path = os.path.join(HERE, "winlayer.pyc")
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location("_orig_winlayer", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PUBLIC = [
    "set_dpi_aware",
    "flash_taskbar",
    "stop_taskbar_flash",
    "hide_window_from_taskbar",
    "get_virtual_screen_rect",
    "get_secondary_monitor_rect",
    "acquire_single_instance_lock",
    "get_taskbar_rect",
    "get_window_ledges",
    "get_desktop_icon_positions",
]


def rec(pid=999, layer=0, title="Some Window", left=0, top=0, right=400, bottom=None):
    """_list_windows()가 내주는 모양의 원시 창 레코드 하나를 만든다.

    `bottom`은 따로 주지 않으면 `top`을 따라간다. 창을 화면 아래로 옮겼을 때
    실수로 높이가 음수가 되지 않도록.
    """
    return {"pid": pid, "layer": layer, "title": title,
            "left": left, "top": top, "right": right,
            "bottom": top + 300 if bottom is None else bottom}


class TestParityWithWinlayer(unittest.TestCase):
    """maclayer는 pet.pyc가 import하는 모듈을 그대로 대체할 수 있어야 한다."""

    @classmethod
    def setUpClass(cls):
        cls.orig = _load_winlayer_pyc()

    def test_exports_every_public_function(self):
        for name in PUBLIC:
            with self.subTest(name=name):
                self.assertTrue(callable(getattr(maclayer, name, None)),
                                f"maclayer.{name} 이 없다")

    def test_signatures_match_the_original(self):
        if self.orig is None:
            self.skipTest("winlayer.pyc not present next to this test")
        for name in PUBLIC:
            with self.subTest(name=name):
                want = inspect.signature(getattr(self.orig, name))
                got = inspect.signature(getattr(maclayer, name))
                self.assertEqual(str(want), str(got),
                                 f"{name}{got} 가 winlayer의 {name}{want} 와 다르다")


class TestRectShapes(unittest.TestCase):
    """사각형을 돌려주는 함수들은 평범한 int 튜플이나 None만 준다 — float은 안 된다.

    pet.pyc가 이 값들을 Tk geometry 문자열에 넣는데, float이면
    '100.0x40.0+12.0+8.0' 이 되어 TclError가 난다.
    """

    def _assert_int_tuple(self, value, length, label):
        if value is None:
            return
        self.assertIsInstance(value, tuple, f"{label} 은 튜플이나 None이어야 한다")
        self.assertEqual(len(value), length, f"{label} 은 원소가 {length}개여야 한다")
        for i, n in enumerate(value):
            self.assertIsInstance(n, int,
                                  f"{label}[{i}] 은 int여야 하는데 {type(n).__name__} 이다")

    def test_virtual_screen_rect_is_left_top_width_height(self):
        r = maclayer.get_virtual_screen_rect()
        self._assert_int_tuple(r, 4, "get_virtual_screen_rect()")
        if r is not None:
            self.assertGreater(r[2], 0, "너비는 양수여야 한다")
            self.assertGreater(r[3], 0, "높이는 양수여야 한다")

    def test_virtual_screen_rect_covers_the_main_display(self):
        r = maclayer.get_virtual_screen_rect()
        if r is None:
            self.skipTest("보고된 디스플레이가 없음")
        left, top, width, height = r
        self.assertLessEqual(left, 0, "주 디스플레이가 x=0에 있으므로 합집합은 그 지점이나 그 왼쪽에서 시작한다")
        self.assertLessEqual(top, 0)
        self.assertGreaterEqual(width, 640)
        self.assertGreaterEqual(height, 480)

    def test_secondary_monitor_rect_is_left_top_width_height(self):
        r = maclayer.get_secondary_monitor_rect()
        self._assert_int_tuple(r, 4, "get_secondary_monitor_rect()")
        if r is not None:
            self.assertGreater(r[2], 0)
            self.assertGreater(r[3], 0)

    def test_taskbar_rect_is_left_top_right_bottom(self):
        r = maclayer.get_taskbar_rect()
        self._assert_int_tuple(r, 4, "get_taskbar_rect()")
        if r is not None:
            left, top, right, bottom = r
            self.assertGreater(right, left, "right는 left보다 커야 한다")
            self.assertGreater(bottom, top, "bottom은 top보다 커야 한다")


def frame(fx=0.0, fy=0.0, fw=1920.0, fh=1080.0,
          left=0.0, right=0.0, bottom=0.0, top=0.0):
    """화면 하나의 (frame, visibleFrame)을 AppKit의 왼쪽 아래 좌표로.

    여백은 macOS가 보고하는 방식대로 준다. `top`은 메뉴 바이고,
    `bottom`/`left`/`right`는 Dock이 있는 쪽이다.
    """
    return ((fx, fy, fw, fh),
            (fx + left, fy + bottom, fw - left - right, fh - bottom - top))


class TestDockDetection(unittest.TestCase):
    """Dock이 PikaPet의 작업 표시줄이다. 화면 가장자리를 따라 올라설 수 있는 띠.

    화면마다 frame과 visibleFrame을 비교해 찾아내고, Tk의 왼쪽 위 좌표로 뒤집는다.
    """

    def test_dock_along_the_bottom_of_a_single_screen(self):
        screens = [frame(top=30.0, bottom=89.0)]
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (0, 991, 1920, 1080))

    def test_dock_on_a_second_screen(self):
        """Dock은 screen 0이 아니라 사용자를 따라간다. 이걸 처음 테스트한 구성이
        정확히 그랬다: 메뉴 바는 왼쪽 화면, Dock은 오른쪽 화면."""
        screens = [frame(top=30.0), frame(fx=1920.0, bottom=89.0)]
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (1920, 991, 3840, 1080))

    def test_dock_on_the_left(self):
        screens = [frame(top=30.0, left=80.0)]
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (0, 30, 80, 1080))

    def test_dock_on_the_right(self):
        screens = [frame(top=30.0, right=80.0)]
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (1840, 30, 1920, 1080))

    def test_menu_bar_alone_is_not_a_dock(self):
        """위쪽 30pt 여백은 메뉴 바다. 펫이 그걸 아래쪽 선반으로 착각해서는 안 된다."""
        self.assertIsNone(maclayer._dock_rect_from_frames([frame(top=30.0)], 1080.0))

    def test_no_insets_means_the_dock_is_hidden(self):
        self.assertIsNone(maclayer._dock_rect_from_frames([frame()], 1080.0))

    def test_no_screens(self):
        self.assertIsNone(maclayer._dock_rect_from_frames([], 1080.0))

    def test_screen_shorter_than_the_reference_is_flipped_correctly(self):
        """높이가 다른 두 번째 디스플레이도 Tk가 쓰는 공통 왼쪽 위 좌표계에
        제대로 들어와야 한다."""
        screens = [frame(top=30.0), frame(fx=1920.0, fh=800.0, bottom=50.0)]
        # 기준 높이 1080. 낮은 화면의 AppKit y 범위 0..50은 뒤집으면
        # 1030..1080이 된다.
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (1920, 1030, 3840, 1080))


class TestLedgeFiltering(unittest.TestCase):
    """선반 필터는 순수 함수라서 화면 없이도 고정해둘 수 있다."""

    def test_keeps_a_plain_window(self):
        out = maclayer._ledges_from_records([rec()], None, 40, own_pid=1)
        self.assertEqual(out, [{"left": 0, "top": 0, "right": 400, "title": "Some Window"}])

    def test_drops_our_own_windows(self):
        """펫이 자기 자신 위에 올라서려 해서는 안 된다."""
        out = maclayer._ledges_from_records([rec(pid=42)], None, 40, own_pid=42)
        self.assertEqual(out, [])

    def test_drops_non_normal_layers(self):
        """layer 0이 평범한 앱 창이다. Dock, 메뉴 바, 그리고 항상 위에 있는 우리
        펫은 그보다 위에 있고 올라설 대상이 아니다."""
        for layer in (-1, 19, 20, 25):
            with self.subTest(layer=layer):
                self.assertEqual(maclayer._ledges_from_records([rec(layer=layer)], None, 40, 1), [])

    def test_drops_slivers(self):
        """Tk가 1px 보조 창을 흩뿌린다. 그건 선반이 아니다."""
        tiny = rec(left=0, top=0, right=1, bottom=33)   # 폭 1px
        self.assertEqual(maclayer._ledges_from_records([tiny], None, 40, 1), [])

    def test_honours_max_windows(self):
        many = [rec(title=f"w{i}", top=i * 50) for i in range(10)]
        self.assertEqual(len(maclayer._ledges_from_records(many, None, 3, 1)), 3)
        self.assertEqual(maclayer._ledges_from_records(many, None, 0, 1), [])

    def test_honours_exclude_titles_as_substrings(self):
        records = [rec(title="PikaPet"), rec(title="Safari", top=100)]
        out = maclayer._ledges_from_records(records, ["Pika"], 40, 1)
        self.assertEqual([l["title"] for l in out], ["Safari"])

    def test_exclude_titles_none_means_no_exclusions(self):
        self.assertEqual(len(maclayer._ledges_from_records([rec()], None, 40, 1)), 1)

    def test_sorted_topmost_first(self):
        """화면 위에 가까운 것이 먼저. 펫이 Quartz가 돌려준 순서가 아니라
        가장 높은 선반을 결정적으로 고르도록."""
        records = [rec(title="low", top=800), rec(title="high", top=100)]
        out = maclayer._ledges_from_records(records, None, 40, 1)
        self.assertEqual([l["title"] for l in out], ["high", "low"])


class TestWindowLedgesLive(unittest.TestCase):
    def test_returns_well_formed_dicts(self):
        for led in maclayer.get_window_ledges():
            self.assertEqual(set(led), {"left", "top", "right", "title"},
                             "winlayer가 문서화한 키는 정확히 이 네 개다")
            for k in ("left", "top", "right"):
                self.assertIsInstance(led[k], int)
            self.assertIsInstance(led["title"], str)
            self.assertGreater(led["right"], led["left"])

    def test_honours_max_windows(self):
        self.assertLessEqual(len(maclayer.get_window_ledges(None, 2)), 2)


class TestDesktopIcons(unittest.TestCase):
    def test_returns_list_of_xy_pairs(self):
        for pos in maclayer.get_desktop_icon_positions():
            self.assertIsInstance(pos, tuple)
            self.assertEqual(len(pos), 2)
            self.assertIsInstance(pos[0], int)
            self.assertIsInstance(pos[1], int)

    def test_honours_max_icons(self):
        self.assertLessEqual(len(maclayer.get_desktop_icon_positions(3)), 3)

    def test_disabled_by_default(self):
        """Finder 데스크톱을 읽으려면 자동화 프롬프트가 필요하므로,
        PIKAPET_DESKTOP_ICONS가 설정되지 않으면 꺼진 상태로 둔다."""
        if os.environ.get("PIKAPET_DESKTOP_ICONS"):
            self.skipTest("이 환경에서는 명시적으로 켜져 있음")
        self.assertEqual(maclayer.get_desktop_icon_positions(), [])


class TestSingleInstanceLock(unittest.TestCase):
    def test_first_caller_wins(self):
        self.assertIs(maclayer.acquire_single_instance_lock("pikapet-selftest"), True)

    def test_same_process_reacquire_is_idempotent(self):
        name = "pikapet-selftest-reentrant"
        self.assertIs(maclayer.acquire_single_instance_lock(name), True)
        self.assertIs(maclayer.acquire_single_instance_lock(name), True)

    def test_second_process_is_refused(self):
        """살아 있는 락은 다른 프로세스를 거절해야 한다. 그게 존재 이유다."""
        name = "pikapet-selftest-cross-process"
        self.assertIs(maclayer.acquire_single_instance_lock(name), True)
        code = (
            "import sys; sys.path.insert(0, %r); import maclayer;"
            "print(maclayer.acquire_single_instance_lock(%r))" % (HERE, name)
        )
        out = subprocess.run([sys.executable, "-c", code],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(out.stdout.strip(), "False", out.stderr)

    def test_released_when_the_holder_exits(self):
        """flock은 프로세스와 함께 죽으므로, 죽은 실행이 우리를 잠가버려서는 안 된다."""
        name = "pikapet-selftest-release"
        code = (
            "import sys; sys.path.insert(0, %r); import maclayer;"
            "print(maclayer.acquire_single_instance_lock(%r))" % (HERE, name)
        )
        first = subprocess.run([sys.executable, "-c", code],
                               capture_output=True, text=True, timeout=30)
        self.assertEqual(first.stdout.strip(), "True", first.stderr)
        second = subprocess.run([sys.executable, "-c", code],
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(second.stdout.strip(), "True", second.stderr)


class TestNoOpsAreSafe(unittest.TestCase):
    """이것들은 macOS에 대응물이 없고, 그 때문에 실패시킬 가치도 없다.

    winlayer는 오류로 앱을 죽이지 않고 전부 삼킨다. 우리도 그래야 한다 —
    Tk 타이머 콜백 안에서 도는 코드다.
    """

    def test_they_return_none(self):
        self.assertIsNone(maclayer.set_dpi_aware())
        self.assertIsNone(maclayer.hide_window_from_taskbar(0))
        self.assertIsNone(maclayer.stop_taskbar_flash(0))

    def test_flash_accepts_winlayer_defaults(self):
        self.assertIsNone(maclayer.flash_taskbar(0))
        self.assertIsNone(maclayer.flash_taskbar(0, 3, 250))

    def test_bogus_handles_do_not_raise(self):
        for bad in (None, -1, "not-a-window", 2 ** 62):
            with self.subTest(handle=bad):
                maclayer.hide_window_from_taskbar(bad)
                maclayer.flash_taskbar(bad)
                maclayer.stop_taskbar_flash(bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
