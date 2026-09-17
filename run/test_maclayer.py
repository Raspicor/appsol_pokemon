"""Contract tests for maclayer, the macOS stand-in for PikaPet's winlayer.

pet.pyc calls winlayer through ten functions and unpacks their return values
directly, so the shapes matter more than the values. These tests pin the shapes
against the real winlayer.pyc and against what the Win32 originals returned.

    cd ~/projects/pikapet && /tmp/pikaenv/bin/python -m unittest discover -s run -v
"""

import importlib.util
import inspect
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import maclayer  # noqa: E402


def _load_winlayer_pyc():
    """Load the shipped winlayer.pyc so we can compare public signatures.

    It imports cleanly off Windows -- every function short-circuits on
    IS_WINDOWS -- so this costs nothing.
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
    """Build one raw window record of the shape _list_windows() yields.

    `bottom` follows `top` unless given, so moving a window down the screen
    does not accidentally give it a negative height.
    """
    return {"pid": pid, "layer": layer, "title": title,
            "left": left, "top": top, "right": right,
            "bottom": top + 300 if bottom is None else bottom}


class TestParityWithWinlayer(unittest.TestCase):
    """maclayer must be a drop-in replacement for the module pet.pyc imports."""

    @classmethod
    def setUpClass(cls):
        cls.orig = _load_winlayer_pyc()

    def test_exports_every_public_function(self):
        for name in PUBLIC:
            with self.subTest(name=name):
                self.assertTrue(callable(getattr(maclayer, name, None)),
                                f"maclayer.{name} is missing")

    def test_signatures_match_the_original(self):
        if self.orig is None:
            self.skipTest("winlayer.pyc not present next to this test")
        for name in PUBLIC:
            with self.subTest(name=name):
                want = inspect.signature(getattr(self.orig, name))
                got = inspect.signature(getattr(maclayer, name))
                self.assertEqual(str(want), str(got),
                                 f"{name}{got} does not match winlayer's {name}{want}")


class TestRectShapes(unittest.TestCase):
    """The rect getters return plain int tuples or None -- never floats.

    pet.pyc feeds these into Tk geometry strings, where a float would produce
    '100.0x40.0+12.0+8.0' and raise TclError.
    """

    def _assert_int_tuple(self, value, length, label):
        if value is None:
            return
        self.assertIsInstance(value, tuple, f"{label} should be a tuple or None")
        self.assertEqual(len(value), length, f"{label} should have {length} items")
        for i, n in enumerate(value):
            self.assertIsInstance(n, int,
                                  f"{label}[{i}] should be int, got {type(n).__name__}")

    def test_virtual_screen_rect_is_left_top_width_height(self):
        r = maclayer.get_virtual_screen_rect()
        self._assert_int_tuple(r, 4, "get_virtual_screen_rect()")
        if r is not None:
            self.assertGreater(r[2], 0, "width must be positive")
            self.assertGreater(r[3], 0, "height must be positive")

    def test_virtual_screen_rect_covers_the_main_display(self):
        r = maclayer.get_virtual_screen_rect()
        if r is None:
            self.skipTest("no displays reported")
        left, top, width, height = r
        self.assertLessEqual(left, 0, "the main display sits at x=0, so the union starts at or left of it")
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
            self.assertGreater(right, left, "right must exceed left")
            self.assertGreater(bottom, top, "bottom must exceed top")


def frame(fx=0.0, fy=0.0, fw=1920.0, fh=1080.0,
          left=0.0, right=0.0, bottom=0.0, top=0.0):
    """One screen's (frame, visibleFrame) in AppKit's bottom-left coordinates.

    The insets are given the way macOS reports them: `top` is the menu bar,
    `bottom`/`left`/`right` is wherever the Dock sits.
    """
    return ((fx, fy, fw, fh),
            (fx + left, fy + bottom, fw - left - right, fh - bottom - top))


class TestDockDetection(unittest.TestCase):
    """The Dock is PikaPet's taskbar: a strip along a screen edge to stand on.

    It is found by comparing each screen's frame with its visibleFrame, then
    flipped into Tk's top-left coordinates.
    """

    def test_dock_along_the_bottom_of_a_single_screen(self):
        screens = [frame(top=30.0, bottom=89.0)]
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (0, 991, 1920, 1080))

    def test_dock_on_a_second_screen(self):
        """The Dock follows the user, not screen 0 -- which is exactly the
        layout this was first tested on: menu bar left, Dock right."""
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
        """A 30pt inset at the top is the menu bar; the pet must not mistake
        it for a ledge along the bottom."""
        self.assertIsNone(maclayer._dock_rect_from_frames([frame(top=30.0)], 1080.0))

    def test_no_insets_means_the_dock_is_hidden(self):
        self.assertIsNone(maclayer._dock_rect_from_frames([frame()], 1080.0))

    def test_no_screens(self):
        self.assertIsNone(maclayer._dock_rect_from_frames([], 1080.0))

    def test_screen_shorter_than_the_reference_is_flipped_correctly(self):
        """A second display of a different height still lands in the shared
        top-left coordinate space Tk uses."""
        screens = [frame(top=30.0), frame(fx=1920.0, fh=800.0, bottom=50.0)]
        # ref height 1080; the short screen's AppKit y range 0..50 becomes
        # 1030..1080 once flipped.
        self.assertEqual(maclayer._dock_rect_from_frames(screens, 1080.0),
                         (1920, 1030, 3840, 1080))


class TestLedgeFiltering(unittest.TestCase):
    """The ledge filter is pure, so it can be pinned without a screen."""

    def test_keeps_a_plain_window(self):
        out = maclayer._ledges_from_records([rec()], None, 40, own_pid=1)
        self.assertEqual(out, [{"left": 0, "top": 0, "right": 400, "title": "Some Window"}])

    def test_drops_our_own_windows(self):
        """The pet must not try to stand on itself."""
        out = maclayer._ledges_from_records([rec(pid=42)], None, 40, own_pid=42)
        self.assertEqual(out, [])

    def test_drops_non_normal_layers(self):
        """Layer 0 is ordinary app windows; the Dock, menu bar and our own
        always-on-top pet live above it and are not things to stand on."""
        for layer in (-1, 19, 20, 25):
            with self.subTest(layer=layer):
                self.assertEqual(maclayer._ledges_from_records([rec(layer=layer)], None, 40, 1), [])

    def test_drops_slivers(self):
        """Tk scatters 1px helper windows around; they are not ledges."""
        tiny = rec(left=0, top=0, right=1, bottom=33)   # 1px wide
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
        """Nearest-to-the-top-of-screen first, so the pet picks the highest
        ledge deterministically instead of whatever order Quartz returned."""
        records = [rec(title="low", top=800), rec(title="high", top=100)]
        out = maclayer._ledges_from_records(records, None, 40, 1)
        self.assertEqual([l["title"] for l in out], ["high", "low"])


class TestWindowLedgesLive(unittest.TestCase):
    def test_returns_well_formed_dicts(self):
        for led in maclayer.get_window_ledges():
            self.assertEqual(set(led), {"left", "top", "right", "title"},
                             "winlayer documents exactly these four keys")
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
        """Reading Finder's desktop needs an Automation prompt, so it stays off
        unless PIKAPET_DESKTOP_ICONS is set."""
        if os.environ.get("PIKAPET_DESKTOP_ICONS"):
            self.skipTest("explicitly enabled in this environment")
        self.assertEqual(maclayer.get_desktop_icon_positions(), [])


class TestSingleInstanceLock(unittest.TestCase):
    def test_first_caller_wins(self):
        self.assertIs(maclayer.acquire_single_instance_lock("pikapet-selftest"), True)

    def test_same_process_reacquire_is_idempotent(self):
        name = "pikapet-selftest-reentrant"
        self.assertIs(maclayer.acquire_single_instance_lock(name), True)
        self.assertIs(maclayer.acquire_single_instance_lock(name), True)

    def test_second_process_is_refused(self):
        """A live lock must refuse another process -- that is the whole point."""
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
        """flock dies with the process, so a crashed run must not lock us out."""
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
    """These have no macOS equivalent worth failing over.

    winlayer swallows every error rather than take the app down with it, and so
    must we -- they run inside Tk timer callbacks.
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
