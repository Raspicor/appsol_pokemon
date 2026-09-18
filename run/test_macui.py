"""pikapet_mac.py의 UI 보정에 대한 테스트.

디스플레이 없이 돈다. 여기서 검증하는 것은 실제로 잘못됐던 두 가지다:

  * macOS가 못 그리는 기호를 이모지 표현으로 바꾸는 것 ('⚔ Fight'가 화면에
    '× Fight'로 보이던 문제),
  * 색을 준 버튼만 Label로 바꿔치기하는 것 (aqua가 tk.Button의 배경색을
    무시하는 문제).

두 번째는 **범위가 핵심**이다. 색을 안 준 버튼까지 바꿔버리면 게임의 버튼
181개가 전부 네이티브 모양을 잃는다. 그래서 고르는 규칙을 직접 테스트한다.
실제 그려지는 모습은 앱을 돌려서 확인했다.
"""

import os
import sys
import shutil
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk

import mactray
import pikapet_mac as L


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


class FakeMisc:
    """Misc._options가 기대하는 최소한의 것. 콜백 등록만 흉내 낸다."""

    def _register(self, func):
        return "cmd0"


class GlyphSubstitution(unittest.TestCase):
    def test_crossed_swords_gets_the_emoji_selector(self):
        self.assertEqual(L._fix_glyphs("⚔ Fight"), "⚔️ Fight")

    def test_already_fixed_text_is_left_alone(self):
        # 게임 코드에 이미 VS16이 붙어 있는 자리가 한 군데 있다 ('⚔️\nVS').
        # 두 번 붙이면 글자가 깨진다.
        already = "⚔️\nVS"
        self.assertEqual(L._fix_glyphs(already), already)

    def test_every_occurrence_is_replaced(self):
        self.assertEqual(L._fix_glyphs("⚔ 공격 ⚔"), "⚔️ 공격 ⚔️")

    def test_other_symbols_are_untouched(self):
        # 이것들은 9px에서 멀쩡히 그려진다. 이모지로 바꾸면 고치는 게 아니라
        # 게임의 모양을 마음대로 바꾸는 것이 된다.
        for text in ("▶ 시작", "⚙ 설정", "⬇ 내려받기", "↩ 되돌리기", "⚠ 주의", "✨ 이로치"):
            self.assertEqual(L._fix_glyphs(text), text)

    def test_plain_text_is_returned_unchanged(self):
        self.assertEqual(L._fix_glyphs("야생 포켓몬이 나타났어요!"), "야생 포켓몬이 나타났어요!")


class GlyphHook(unittest.TestCase):
    """Misc._options 훅. 모든 위젯의 옵션이 여기를 지난다."""

    def setUp(self):
        self.original = tk.Misc._options
        self.addCleanup(setattr, tk.Misc, "_options", self.original)
        L.install_glyph_fix()

    def _options(self, **kw):
        return dict(zip(*[iter(tk.Misc._options(FakeMisc(), {}, kw))] * 2))

    def test_text_option_is_fixed(self):
        self.assertEqual(self._options(text="⚔ Fight")["-text"], "⚔️ Fight")

    def test_menu_label_is_fixed(self):
        # 우클릭 메뉴의 '⚔ 전투 창 다시 열기'가 이 경로로 간다.
        self.assertEqual(self._options(label="⚔ 전투 창 다시 열기")["-label"],
                         "⚔️ 전투 창 다시 열기")

    def test_non_text_options_are_not_touched(self):
        # 폰트 이름이나 색에 손대면 Tcl이 그대로 거부한다.
        got = self._options(bg="#ffd54a", font="{맑은 고딕} 9 bold")
        self.assertEqual(got["-bg"], "#ffd54a")
        self.assertEqual(got["-font"], "{맑은 고딕} 9 bold")

    def test_cnf_dict_is_fixed_too(self):
        # Widget.__init__은 kw가 아니라 cnf로 넘긴다.
        pairs = tk.Misc._options(FakeMisc(), {"text": "⚔ 공격"})
        self.assertEqual(dict(zip(*[iter(pairs)] * 2))["-text"], "⚔️ 공격")

    def test_non_string_values_survive(self):
        # text=None 은 Tcl로 안 넘어가고, 숫자는 숫자 그대로 넘어간다.
        got = self._options(text=None, width=12)
        self.assertEqual(got.get("-width"), 12)
        self.assertNotIn("-text", got)

    def test_callables_are_still_registered(self):
        self.assertEqual(self._options(command=lambda: None)["-command"], "cmd0")


class Shading(unittest.TestCase):
    def test_darkening(self):
        self.assertEqual(L._shade("#ffd54a", 0.5), "#806a25")

    def test_lightening_clamps_at_white(self):
        self.assertEqual(L._shade("#ffd54a", 5.0), "#ffffff")

    def test_named_colours_are_returned_as_is(self):
        # 게임은 'systemWindowBackgroundColor' 같은 이름도 쓴다.
        self.assertEqual(L._shade("systemTextColor", 0.8), "systemTextColor")
        self.assertEqual(L._shade(None, 0.8), None)

    def test_light_and_dark(self):
        self.assertTrue(L._is_light("#ffd54a"))       # 노란 액션 버튼
        self.assertTrue(L._is_light("#f5f5f5"))
        self.assertFalse(L._is_light("#1a1a1a"))
        self.assertTrue(L._is_light("systemTextColor"))   # 모르면 검정 글자

    def test_three_digit_hex(self):
        # 게임은 '#eee' 같은 짧은 표기도 쓴다. 펼쳐서 보지 않으면 어두운 '#111'
        # 까지 밝다고 판정해서 검은 배경에 검은 글자가 된다.
        self.assertTrue(L._is_light("#eee"))
        self.assertFalse(L._is_light("#111"))


class ButtonRouting(unittest.TestCase):
    """색을 준 버튼만 바꿔치기해야 한다. 나머지는 네이티브 그대로."""

    def setUp(self):
        self.made = []
        original = tk.Button

        def fake_native(master=None, cnf=None, **kw):
            self.made.append(("네이티브", dict(cnf or {}, **kw)))
            return "네이티브 버튼"

        def fake_colored(master=None, **kw):
            self.made.append(("색칠", kw))
            return "색칠 버튼"

        tk.Button = fake_native
        self.addCleanup(setattr, tk, "Button", original)
        self.addCleanup(setattr, L, "MacColorButton", L.MacColorButton)
        L.MacColorButton = fake_colored
        L.install_button_colors()

    def test_button_with_a_hex_background_is_replaced(self):
        tk.Button(None, text="⚔ Fight", bg="#ffd54a", command=lambda: None)
        self.assertEqual(self.made[0][0], "색칠")

    def test_background_keyword_spelling_also_counts(self):
        tk.Button(None, text="확인", background="#ffd54a")
        self.assertEqual(self.made[0][0], "색칠")

    def test_button_without_a_background_stays_native(self):
        # 게임의 버튼 181개 중 173개가 여기에 해당한다.
        tk.Button(None, text="닫기", command=lambda: None)
        self.assertEqual(self.made[0][0], "네이티브")

    def test_system_colour_names_stay_native(self):
        # 이름 있는 색은 aqua가 알아서 처리한다. Label로 바꿀 이유가 없다.
        tk.Button(None, text="닫기", bg="systemWindowBackgroundColor")
        self.assertEqual(self.made[0][0], "네이티브")

    def test_options_are_passed_through(self):
        tk.Button(None, text="⚔ 스테이지 3 도전!", bg="#ffd54a", width=12)
        kind, kw = self.made[0]
        self.assertEqual(kind, "색칠")
        self.assertEqual(kw["width"], 12)
        self.assertEqual(kw["text"], "⚔ 스테이지 3 도전!")

    def test_cnf_dict_positional_form_works(self):
        tk.Button(None, {"text": "확인", "bg": "#ffd54a"})
        self.assertEqual(self.made[0][0], "색칠")

    def test_a_broken_replacement_falls_back_to_native(self):
        # 색이 빠진 버튼이 앱이 안 뜨는 것보다 낫다.
        def explode(master=None, **kw):
            raise RuntimeError("안 됨")

        L.MacColorButton = explode
        tk.Button(None, text="확인", bg="#ffd54a")
        self.assertEqual(self.made[0][0], "네이티브")


class AppIconGuard(unittest.TestCase):
    """aqua의 `iconphoto` 는 -default 없이도 앱 아이콘을 갈아치운다.

    그래서 인자를 손보는 것으로는 못 막고, 부르고 나서 되돌려야 한다.
    """

    def setUp(self):
        self.calls = []
        self.restored = []
        original = tk.Wm.wm_iconphoto

        def fake(this, *args, **kw):
            self.calls.append(args)
            return "원본 결과"

        tk.Wm.wm_iconphoto = fake
        self.addCleanup(setattr, tk.Wm, "wm_iconphoto", original)
        self.addCleanup(setattr, tk.Wm, "iconphoto", original)
        self.addCleanup(setattr, L, "set_app_icon", L.set_app_icon)
        L.set_app_icon = lambda: self.restored.append(True) or True
        L.install_app_icon_guard()

    def test_the_original_call_is_not_altered(self):
        # 게임은 pet.py:17476 에서 이 형태로 부른다. 인자는 그대로 넘어가야 한다.
        tk.Wm.wm_iconphoto(object(), True, "펫 스프라이트")
        self.assertEqual(self.calls, [(True, "펫 스프라이트")])

    def test_the_app_icon_is_restored_afterwards(self):
        tk.Wm.wm_iconphoto(object(), True, "펫 스프라이트")
        self.assertEqual(len(self.restored), 1)

    def test_the_return_value_is_passed_through(self):
        self.assertEqual(tk.Wm.wm_iconphoto(object(), False, "이미지"), "원본 결과")

    def test_the_alias_is_patched_too(self):
        # 게임은 iconphoto 라는 이름으로 부른다.
        tk.Wm.iconphoto(object(), True, "이미지")
        self.assertEqual(len(self.restored), 1)


class AppIconLookup(unittest.TestCase):
    def test_the_repo_copy_is_found_when_not_bundled(self):
        # 소스에서 실행할 때 쓰는 경로. 번들 경로가 먼저지만 그건 .app 안에만 있다.
        found = [p for p in L.ICON_CANDIDATES if os.path.exists(p)]
        self.assertTrue(found, f"아이콘 후보가 하나도 없다: {L.ICON_CANDIDATES}")
        self.assertTrue(found[0].endswith("icon.png"))

class FakeParent:
    """부모 위젯 자리. cget('bg') 만 답한다."""

    def __init__(self, bg):
        self.bg = bg

    def cget(self, key):
        if key in ("bg", "background"):
            if self.bg is None:
                raise RuntimeError("배경 없음")
            return self.bg
        raise KeyError(key)


class ContrastFix(unittest.TestCase):
    """다크 모드에서 생기는 검은 테두리와 안 보이는 글자를 메운다."""

    def setUp(self):
        self.made = []
        original = tk.BaseWidget.__init__

        def recorder(this, master, widgetName, cnf={}, kw={}, extra=()):
            self.made.append((widgetName, dict(kw if kw else cnf)))

        tk.BaseWidget.__init__ = recorder
        self.addCleanup(setattr, tk.BaseWidget, "__init__", original)
        L.install_contrast_fix()

    def make(self, widget, parent_bg="#fff6e0", **kw):
        tk.BaseWidget.__init__(object(), FakeParent(parent_bg), widget, {}, kw)
        return self.made[-1][1]

    # -- 검은 테두리 -------------------------------------------------------

    def test_a_button_gets_the_parents_colour_for_its_ring(self):
        # 이게 전투 창 버튼마다 검은 사각형이 둘러지던 것이다.
        self.assertEqual(self.make("button", text="⚔ 공격")["highlightbackground"],
                         "#fff6e0")

    def test_labels_and_frames_get_it_too(self):
        for widget in ("label", "frame", "canvas", "entry", "scrollbar"):
            self.assertEqual(self.make(widget)["highlightbackground"], "#fff6e0",
                             widget)

    def test_a_system_coloured_parent_is_left_alone(self):
        # 부모가 시스템 색이면 테두리도 같은 시스템 색이라 이미 맞는다.
        self.assertNotIn("highlightbackground",
                         self.make("button", parent_bg="systemWindowBackgroundColor"))

    def test_a_parent_without_a_background_is_left_alone(self):
        self.assertNotIn("highlightbackground", self.make("button", parent_bg=None))

    def test_the_games_own_choice_wins(self):
        got = self.make("button", highlightbackground="#123456")
        self.assertEqual(got["highlightbackground"], "#123456")

    def test_an_explicit_thickness_is_respected(self):
        # 게임이 테두리를 직접 다루고 있으면 끼어들지 않는다.
        self.assertNotIn("highlightbackground", self.make("button", highlightthickness=0))

    def test_menus_are_never_touched(self):
        # Menu에는 -highlightbackground 가 없어서 주면 생성이 통째로 실패한다.
        self.assertNotIn("highlightbackground", self.make("menu"))

    def test_toplevels_are_never_touched(self):
        self.assertNotIn("highlightbackground", self.make("toplevel"))

    # -- 안 보이는 글자 ----------------------------------------------------

    def test_a_label_on_a_light_background_gets_dark_text(self):
        # '야생 ？？？ Lv.2' 가 크림색 위에 흰 글자로 찍히던 것이다.
        got = self.make("label", text="야생 ？？？ Lv.2", bg="#fff6e0")
        self.assertEqual(got["fg"], "#111111")

    def test_a_label_on_a_dark_background_gets_light_text(self):
        self.assertEqual(self.make("label", text="상태", bg="#1a1a1a")["fg"], "#f0f0f0")

    def test_an_explicit_foreground_wins(self):
        got = self.make("label", text="내 파이리", bg="#fff6e0", fg="#1a4a8a")
        self.assertEqual(got["fg"], "#1a4a8a")

    def test_a_label_without_its_own_background_is_left_alone(self):
        self.assertNotIn("fg", self.make("label", text="무엇"))

    def test_buttons_never_get_a_derived_foreground(self):
        # aqua 버튼의 베젤은 부모 색과 무관하게 항상 밝다. 어두운 창에 놓였다고
        # 흰 글자를 주면 흰 베젤에 흰 글자가 된다.
        self.assertNotIn("fg", self.make("button", text="확인", bg="#1a1a1a",
                                         parent_bg="#1a1a1a"))

    # -- 안전 --------------------------------------------------------------

    def test_the_cnf_dict_form_is_handled(self):
        tk.BaseWidget.__init__(object(), FakeParent("#fff6e0"), "button",
                               {"text": "확인"}, {})
        self.assertEqual(self.made[-1][1]["highlightbackground"], "#fff6e0")

    def test_a_broken_parent_does_not_stop_the_widget(self):
        class Exploding:
            def cget(self, key):
                raise RuntimeError("안 됨")

        tk.BaseWidget.__init__(object(), Exploding(), "button", {}, {"text": "확인"})
        self.assertEqual(self.made[-1][0], "button")


class ColourHelpers(unittest.TestCase):
    def test_hex_colours_are_recognised(self):
        self.assertEqual(L._explicit_color("#fff6e0"), "#fff6e0")
        self.assertEqual(L._explicit_color("#eee"), "#eee")

    def test_system_names_are_not(self):
        for name in ("systemWindowBackgroundColor", "systemTextColor", "white", "", None):
            self.assertIsNone(L._explicit_color(name), name)


class BarFraction(unittest.TestCase):
    """체력바가 찬 비율. 게임이 넣는 값을 그대로 믿으면 막대가 삐져나간다."""

    def test_normal(self):
        self.assertAlmostEqual(L._bar_fraction(50, 100), 0.5)
        self.assertAlmostEqual(L._bar_fraction(0, 100), 0.0)
        self.assertAlmostEqual(L._bar_fraction(100, 100), 1.0)

    def test_over_and_under_are_clamped(self):
        # 과damage 로 음수가, 회복으로 최대 초과가 들어올 수 있다.
        self.assertEqual(L._bar_fraction(-20, 100), 0.0)
        self.assertEqual(L._bar_fraction(150, 100), 1.0)

    def test_zero_maximum_does_not_divide(self):
        self.assertEqual(L._bar_fraction(10, 0), 0.0)

    def test_garbage_gives_empty(self):
        for value, maximum in ((None, 100), ("얼마", 100), (10, None), (10, "많이")):
            self.assertEqual(L._bar_fraction(value, maximum), 0.0, (value, maximum))


class ProgressbarRouting(unittest.TestCase):
    """aqua는 ttk Progressbar 의 색을 전부 무시하므로 직접 그리는 것으로 바꾼다.

    다만 `ttk.Combobox` 는 건드리면 안 된다 -- 네이티브 드롭다운이 제대로
    동작하고 있고, 테마를 바꾸면 그것까지 잃는다.
    """

    def setUp(self):
        from tkinter import ttk

        self.ttk = ttk
        self.made = []
        self.original = ttk.Progressbar
        self.original_combo = ttk.Combobox

        def fake_native(master=None, **kw):
            self.made.append(("네이티브", kw))
            return "네이티브 바"

        def fake_ours(master=None, **kw):
            self.made.append(("직접 그림", kw))
            return "우리 바"

        ttk.Progressbar = fake_native
        self.addCleanup(setattr, ttk, "Progressbar", self.original)
        self.addCleanup(setattr, L, "MacProgressBar", L.MacProgressBar)
        L.MacProgressBar = fake_ours
        L.install_progressbar_fix()

    def test_progressbars_are_replaced(self):
        self.ttk.Progressbar(None, length=210, maximum=39, value=39)
        self.assertEqual(self.made[0][0], "직접 그림")

    def test_the_options_are_passed_through(self):
        self.ttk.Progressbar(None, length=210, maximum=39, value=12)
        kw = self.made[0][1]
        self.assertEqual((kw["length"], kw["maximum"], kw["value"]), (210, 39, 12))

    def test_combobox_is_left_native(self):
        self.assertIs(self.ttk.Combobox, self.original_combo)

    def test_a_failure_falls_back_to_the_native_one(self):
        # 검은 띠가 남은 체력바가, 앱이 안 뜨는 것보다 낫다.
        def explode(master=None, **kw):
            raise RuntimeError("안 됨")

        L.MacProgressBar = explode
        self.ttk.Progressbar(None, length=210)
        self.assertEqual(self.made[0][0], "네이티브")


class CornerGrip(unittest.TestCase):
    """compact 전투 창 오른쪽 아래의 크기 조절 손잡이."""

    def setUp(self):
        self.made = []
        original = tk.BaseWidget.__init__

        def recorder(this, master, widgetName, cnf={}, kw={}, extra=()):
            self.made.append((widgetName, dict(kw if kw else cnf)))

        tk.BaseWidget.__init__ = recorder
        self.addCleanup(setattr, tk.BaseWidget, "__init__", original)
        L.install_contrast_fix()

    def make(self, parent_bg, **kw):
        tk.BaseWidget.__init__(object(), FakeParent(parent_bg), "label", {}, kw)
        return self.made[-1][1]

    def test_it_blends_into_a_light_window(self):
        # 주황 사각형이 둥근 모서리에 잘려 조각처럼 보이던 것.
        got = self.make("#fff6e0", text=L.CORNER_GRIP, bg="#e8a53a", fg="white")
        self.assertEqual(got["bg"], "#fff6e0")
        self.assertNotEqual(got["fg"], "white")

    def test_the_glyph_stays(self):
        # 기능이 있는 손잡이다. 지우면 창 크기를 못 바꾼다.
        self.assertEqual(self.make("#fff6e0", text=L.CORNER_GRIP, bg="#e8a53a")["text"],
                         L.CORNER_GRIP)

    def test_a_dark_window_gets_a_lighter_glyph(self):
        got = self.make("#1a1a1a", text=L.CORNER_GRIP, bg="#e8a53a", fg="white")
        self.assertEqual(got["bg"], "#1a1a1a")
        self.assertTrue(L._is_light(got["fg"]) is False or got["fg"] != "#1a1a1a")

    def test_other_labels_keep_their_colour(self):
        got = self.make("#fff6e0", text="야생 포켓몬", bg="#e8a53a", fg="white")
        self.assertEqual(got["bg"], "#e8a53a")


class MenuBarGlyphs(unittest.TestCase):
    """메뉴 바 항목의 ⚔.

    install_glyph_fix 는 `tkinter.Misc._options` 에 걸려 있어서 NSMenuItem 의
    제목에는 닿지 않는다. 실제로 메뉴 바의 '⚔ 배틀 창 복구'가 '× 배틀 창 복구'로
    보였다. mactray 가 제목을 만드는 자리에서 따로 고친다.
    """

    def test_the_sword_gets_the_emoji_selector(self):
        self.assertEqual(mactray.menu_title("⚔ 배틀 창 복구"),
                         "\u2694\ufe0f 배틀 창 복구")

    def test_it_is_not_applied_twice(self):
        once = mactray.menu_title("⚔ 배틀 창 복구")
        self.assertEqual(mactray.menu_title(once), once)

    def test_other_labels_are_untouched(self):
        # ⬇ ◓ 🔴 🌿 🎯 🔔 은 그냥 그려진다. 이모지로 바꾸면 모양만 달라진다.
        for label in ("🔴 몬스터볼에서 꺼내기", "🌿 야생 포켓몬 확인",
                      "🎯 화면 중앙으로 부르기", "🔔 알림 테스트", "❌ 종료",
                      "⬇ 새 버전 0.0.5 받기"):
            self.assertEqual(mactray.menu_title(label), label)

    def test_every_shipped_menu_label_survives(self):
        # 실제로 쓰는 이름들이 그대로 통과하는지. 빈 문자열이 나오면 메뉴가 빈다.
        for label in ("⚔ 배틀 창 복구", "🔴 몬스터볼에서 꺼내기", "❌ 종료"):
            self.assertTrue(mactray.menu_title(label).strip())


class MenuBarContents(unittest.TestCase):
    """◓ 메뉴에 무엇이 들어가고 무엇이 빠지는가.

    이 파일에서 가장 자주 틀리는 부분이라 목록을 직접 본다. `menu_actions` 는
    AppKit을 쓰지 않으므로 화면 없이 확인할 수 있다.
    """

    class FakeApp:
        def __init__(self):
            self.called = []

        def __getattr__(self, name):
            def fn():
                self.called.append(name)
            return fn

    def labels(self, **kw):
        app = self.FakeApp()
        return [label for label, _ in mactray.menu_actions(app, **kw)]

    def test_the_three_tray_only_actions_are_there(self):
        # 이 셋이 빠지면 포트가 기능을 잃는다. exit_ball 은 특히 치명적이다.
        labels = self.labels()
        for needle in ("몬스터볼에서 꺼내기", "야생 포켓몬 확인", "배틀 창 복구"):
            self.assertTrue(any(l and needle in l for l in labels), needle)

    def test_the_notification_test_is_gone(self):
        # ad-hoc 서명에서는 배너가 늘 스크립트 편집기 소유라, 눌러봐도
        # 'PikaPet 알림이 되는가'에 답을 주지 못했다.
        self.assertFalse(any(l and "알림 테스트" in l for l in self.labels()))

    def test_the_version_check_appears_only_when_given(self):
        self.assertIn(mactray.VERSION_CHECK_LABEL,
                      self.labels(version_check=lambda: None))
        self.assertNotIn(mactray.VERSION_CHECK_LABEL, self.labels())

    def test_quit_is_last(self):
        labels = [l for l in self.labels(version_check=lambda: None) if l]
        self.assertIn("종료", labels[-1])

    def test_separators_never_sit_next_to_each_other(self):
        # version_check 가 없으면 구분선 두 개가 붙을 수 있다.
        for kw in ({}, {"version_check": lambda: None}):
            labels = self.labels(**kw)
            self.assertIsNotNone(labels[0], kw)
            self.assertIsNotNone(labels[-1], kw)
            for a, b in zip(labels, labels[1:]):
                self.assertFalse(a is None and b is None, kw)

    def test_the_actions_call_the_game(self):
        app = self.FakeApp()
        for label, fn in mactray.menu_actions(app):
            if label is not None:
                fn()
        self.assertIn("exit_ball", app.called)
        self.assertIn("_restore_battle_window", app.called)

    def test_a_missing_game_method_does_not_raise(self):
        class Bare:
            pass

        for label, fn in mactray.menu_actions(Bare()):
            if label is not None:
                fn()                        # 예외가 나가면 메뉴가 죽는다


class FontOnEveryRoot(unittest.TestCase):
    """폰트 보정이 스타터 선택 창까지 닿는가.

    게임은 세이브가 없을 때 PetApp 보다 먼저 별도의 `tk.Tk()` 를 만들어 거기에
    선택 창을 그린다 (pet.py:19067). `setup_pet_window` 에서만 폰트를 맞추면 그
    창을 놓치는데, 그 창은 크기가 860x380 으로 고정돼 있고 내용은 실측 930x262 를
    요구한다 -- 다섯 번째 포켓몬의 시작 버튼이 오른쪽에서 잘린다.
    """

    def setUp(self):
        self.original_init = tk.Tk.__init__
        self.original_apply = L.install_font_defaults
        self.addCleanup(self._restore)
        self.seen = []
        tk.Tk.__init__ = lambda self, *a, **k: None
        L.install_font_defaults = lambda root: self.seen.append(root)

    def _restore(self):
        tk.Tk.__init__ = self.original_init
        L.install_font_defaults = self.original_apply

    def make_root(self, *args, **kw):
        root = tk.Tk.__new__(tk.Tk)
        tk.Tk.__init__(root, *args, **kw)
        return root

    def test_a_new_root_gets_the_font_fix(self):
        L.install_font_defaults_everywhere()
        root = self.make_root()
        self.assertEqual(self.seen, [root])

    def test_every_root_gets_it_not_just_the_first(self):
        # TkDefaultFont 는 인터프리터마다 따로 있으므로 루트마다 걸어야 한다.
        L.install_font_defaults_everywhere()
        a, b = self.make_root(), self.make_root()
        self.assertEqual(self.seen, [a, b])

    def test_the_original_init_still_runs_with_its_arguments(self):
        calls = []
        tk.Tk.__init__ = lambda self, *a, **k: calls.append((a, k))
        L.install_font_defaults_everywhere()
        self.make_root("screenname", useTk=1)
        self.assertEqual(calls, [(("screenname",), {"useTk": 1})])

    def test_a_font_failure_does_not_stop_the_window(self):
        # 레이아웃이 조금 넘치는 것이 앱이 안 뜨는 것보다 낫다.
        def boom(root):
            raise RuntimeError("폰트 없음")

        L.install_font_defaults = boom
        L.install_font_defaults_everywhere()
        self.make_root()                    # 예외가 새어 나오면 실패


class StarterWindowFix(unittest.TestCase):
    """세이브가 없을 때 뜨는 선택 창을 찾을 수 있게 만드는 보정.

    실측한 고장: 전체화면 앱이 떠 있을 때 백그라운드로 띄우면 창이 제대로
    만들어지는데도 (860x412+34+64, alpha 1.0) CGWindowList 가 onscreen 을
    돌려주지 않는다. 막 띄운 프로세스는 활성 앱이 아니고, 전체화면 앱이 쓰는
    Space 가 아닌 원래 Space 로 창이 가기 때문이다. 사용자에게는 앱이 아무
    반응도 없는 것으로 보인다. 보정 후 onscreen=True, +530+233.
    """

    class FakePet:
        def __init__(self, fn=None):
            if fn is not None:
                self.show_starter_select = fn

    class FakeRoot:
        def __init__(self):
            self.scheduled = []

        def after(self, _ms, fn):
            self.scheduled.append(fn)

    def setUp(self):
        self.centred = []
        self.fronted = []
        self.original_centre = L._centre_window
        self.original_front = L.bring_to_front
        self.addCleanup(self._restore)
        L._centre_window = lambda win: self.centred.append(win)
        L.bring_to_front = lambda win: self.fronted.append(win)

    def _restore(self):
        L._centre_window = self.original_centre
        L.bring_to_front = self.original_front

    def test_the_window_is_centred_and_raised(self):
        calls = []

        def show(root, cb):
            calls.append((root, cb))
            return "속값"

        pet = self.FakePet(show)
        L.install_starter_window_fix(pet)
        root, cb = self.FakeRoot(), (lambda name: None)
        got = pet.show_starter_select(root, cb)
        self.assertEqual(calls, [(root, cb)])
        self.assertEqual(got, "속값", "원본의 반환값을 그대로 넘겨야 한다")
        self.assertEqual(self.centred, [root])
        self.assertEqual(self.fronted, [root])

    def test_it_tries_again_once_the_window_is_mapped(self):
        # 첫 시도는 매핑 전이라 묻힐 수 있다.
        pet = self.FakePet(lambda root, cb: None)
        L.install_starter_window_fix(pet)
        root = self.FakeRoot()
        pet.show_starter_select(root, lambda name: None)
        self.assertEqual(len(root.scheduled), 1)
        self.fronted.clear()
        root.scheduled[0]()
        self.assertEqual(self.fronted, [root])

    def test_extra_arguments_are_passed_through(self):
        seen = []
        pet = self.FakePet(lambda root, cb, *a, **k: seen.append((a, k)))
        L.install_starter_window_fix(pet)
        pet.show_starter_select(self.FakeRoot(), None, "더", key=1)
        self.assertEqual(seen, [(("더",), {"key": 1})])

    def test_a_failure_does_not_stop_the_window(self):
        # 위치가 어정쩡한 것이 앱이 안 뜨는 것보다 낫다.
        def boom(win):
            raise RuntimeError("화면 정보 없음")

        L._centre_window = boom
        L.bring_to_front = boom
        pet = self.FakePet(lambda root, cb: "떴다")
        L.install_starter_window_fix(pet)
        self.assertEqual(
            pet.show_starter_select(self.FakeRoot(), None), "떴다")

    def test_a_game_without_the_function_is_left_alone(self):
        pet = self.FakePet()
        self.assertIsNone(L.install_starter_window_fix(pet))
        self.assertFalse(hasattr(pet, "show_starter_select"))


class StartupLogWiring(unittest.TestCase):
    """시작 기록이 실제로 걸려 있는가.

    이것이 없으면 "선택 창이 안 뜬다"는 신고에 답할 수 없다. 선택 창은 저장
    파일에 고른 포켓몬이 없을 때만 나오므로(pet.py:19063), 안 뜨는 것이 정상일
    수도 있고 창이 다른 Space 에 생긴 것일 수도 있다. 단계 이름이 그 둘을
    가른다.
    """

    class FakeRoot:
        def __init__(self):
            self.scheduled = []

        def after(self, _ms, fn):
            self.scheduled.append(fn)

    def setUp(self):
        self.diag = []
        self.original_diag = L._diag
        self.addCleanup(setattr, L, "_diag", self.original_diag)
        self.addCleanup(setattr, L, "_centre_window", L._centre_window)
        self.addCleanup(setattr, L, "bring_to_front", L.bring_to_front)
        L._diag = lambda action, *a, **k: self.diag.append((action,) + a)
        # 위치 보정 자체는 StarterWindowFix 가 본다. 여기서는 기록만 본다.
        L._centre_window = lambda win: None
        L.bring_to_front = lambda win: None

    def test_the_select_phase_is_recorded_before_the_window_opens(self):
        opened = []

        def show(root, cb):
            # 원본이 돌기 전에 이미 남아 있어야 한다. 원본이 예외를 내도
            # 어느 단계였는지는 알 수 있어야 하기 때문이다.
            opened.append(list(self.diag))

        pet = type("P", (), {"show_starter_select": staticmethod(show)})()
        L.install_starter_window_fix(pet)
        pet.show_starter_select(self.FakeRoot(), lambda name: None)
        self.assertEqual(opened, [[("log_phase", "select")]])

    def test_the_window_position_is_recorded_once_it_settles(self):
        pet = type("P", (), {"show_starter_select": staticmethod(
            lambda root, cb: None)})()
        L.install_starter_window_fix(pet)
        root = self.FakeRoot()
        pet.show_starter_select(root, None)
        self.diag.clear()
        root.scheduled[0]()
        self.assertEqual(self.diag, [("log_window", "선택 창", root)])

    def test_the_pet_phase_is_recorded_too(self):
        # 이 줄이 있으면 "선택 창을 건너뛴 것"이 저장 파일 때문임을 알 수 있다.
        self.addCleanup(setattr, L, "set_app_icon", L.set_app_icon)
        self.addCleanup(setattr, L, "install_font_defaults",
                        L.install_font_defaults)
        self.addCleanup(setattr, L, "transparency_mode", L.transparency_mode)
        L.set_app_icon = lambda: None
        L.install_font_defaults = lambda root: None
        L.transparency_mode = lambda root: "none"

        called = []
        pet = type("P", (), {})()
        pet.MAGIC = "#ff00ff"
        pet.setup_pet_window = lambda root: called.append(root) or "속값"
        L.install_window_patch(pet)
        root = self.FakeRoot()
        got = pet.setup_pet_window(root)
        self.assertEqual(got, "속값", "원본의 반환값을 그대로 넘겨야 한다")
        self.assertEqual(called, [root])
        self.assertIn(("log_phase", "pet"), self.diag)
        # 펫의 위치는 나중에 정해진다. 바로 읽으면 아직 자리를 안 잡은 값이다.
        self.assertEqual(len(root.scheduled), 1)
        root.scheduled[0]()
        self.assertIn(("log_window", "펫 창", root), self.diag)
        # 펫이 안 보인다는 신고는 스프라이트 문제와 오버레이 문제로 갈린다.
        self.assertTrue(any("오버레이" in str(d) for d in self.diag), self.diag)
        self.assertTrue(any("투명도 none" in str(d) for d in self.diag), self.diag)

    def test_a_broken_logger_cannot_break_the_game(self):
        L._diag = self.original_diag
        import macdiag

        original = macdiag.log_phase
        self.addCleanup(setattr, macdiag, "log_phase", original)

        def boom(name):
            raise OSError("디스크가 꽉 찼다")

        macdiag.log_phase = boom
        pet = type("P", (), {"show_starter_select": staticmethod(
            lambda root, cb: "떴다")})()
        L.install_starter_window_fix(pet)
        self.assertEqual(pet.show_starter_select(self.FakeRoot(), None), "떴다")

    def test_an_unknown_action_is_swallowed(self):
        L._diag = self.original_diag
        L._diag("그런함수없음", 1, 2)


class FindingTheAssets(unittest.TestCase):
    """에셋이 심볼릭 링크 뒤에 있다. 링크가 사라지면 이미지만 전부 사라진다.

    번들 구조 (실측):

        sys._MEIPASS = Contents/Frameworks          <- pet.pyc 가 RESOURCE_DIR 로 쓴다
        Contents/Frameworks/assets -> ../Resources/assets
        Contents/Resources/assets                   <- 실물

    링크 네 개를 지운 번들로 신고를 그대로 재현했다: 선택 창에 '(이미지 없음)'
    다섯 개. 코드는 Frameworks 안에 실물로 있으니 창·메뉴·알림은 전부 정상이다.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.had_frozen = hasattr(sys, "frozen")
        self.frozen = getattr(sys, "frozen", None)
        self.had_meipass = hasattr(sys, "_MEIPASS")
        self.meipass = getattr(sys, "_MEIPASS", None)
        self.addCleanup(self._restore)
        self.diag = []
        self.original_diag = L._diag
        self.addCleanup(setattr, L, "_diag", self.original_diag)
        L._diag = lambda action, *a, **k: self.diag.append((action,) + a)

    def _restore(self):
        for name, had, value in (("frozen", self.had_frozen, self.frozen),
                                 ("_MEIPASS", self.had_meipass, self.meipass)):
            if had:
                setattr(sys, name, value)
            else:
                try:
                    delattr(sys, name)
                except AttributeError:
                    pass

    def _bundle(self, link=True, assets=True):
        """Contents/{Frameworks,Resources} 를 만든다. `link` 가 False 면 링크 없음."""
        contents = os.path.join(self.tmp, "PikaPet.app", "Contents")
        frameworks = os.path.join(contents, "Frameworks")
        resources = os.path.join(contents, "Resources")
        os.makedirs(frameworks)
        os.makedirs(resources)
        if assets:
            os.makedirs(os.path.join(resources, "assets", "sprites"))
            if link:
                os.symlink("../Resources/assets",
                           os.path.join(frameworks, "assets"))
        sys.frozen = True
        sys._MEIPASS = frameworks
        return frameworks, resources

    def test_a_healthy_bundle_is_left_alone(self):
        frameworks, _ = self._bundle(link=True)
        self.assertIsNone(L.fix_resource_dir())
        self.assertEqual(sys._MEIPASS, frameworks)
        self.assertEqual(self.diag, [])

    def test_a_missing_link_is_routed_to_the_real_folder(self):
        frameworks, resources = self._bundle(link=False)
        self.assertEqual(L.fix_resource_dir(), resources)
        self.assertEqual(sys._MEIPASS, resources,
                         "pet.pyc 가 이 값으로 RESOURCE_DIR 을 정한다")

    def test_the_repair_is_written_down(self):
        self._bundle(link=False)
        L.fix_resource_dir()
        self.assertEqual(len(self.diag), 1)
        self.assertIn("에셋 링크가 없어", self.diag[0][1])

    def test_assets_nowhere_says_images_will_not_appear(self):
        frameworks, _ = self._bundle(link=False, assets=False)
        self.assertIsNone(L.fix_resource_dir())
        self.assertEqual(sys._MEIPASS, frameworks, "옮길 곳이 없으면 그대로 둔다")
        self.assertIn("이미지가 나오지 않습니다", self.diag[0][1])

    def test_running_from_source_is_not_touched(self):
        # 소스 실행은 RESOURCE_DIR 이 run/ 이고 거기 링크가 실제로 있다.
        self._bundle(link=False)
        sys.frozen = False
        self.assertIsNone(L.fix_resource_dir())

    def test_a_bundle_without_meipass_is_not_touched(self):
        self._bundle(link=False)
        del sys._MEIPASS
        self.assertIsNone(L.fix_resource_dir())


class SpriteLoadLog(unittest.TestCase):
    """스프라이트 로드 실패는 게임이 삼킨다. 이유를 남겨야 한다."""

    class FakeSpriteanim:
        def __init__(self, boom=None):
            self.boom = boom
            self.calls = []

        def AnimSet(self, folder):
            self.calls.append(folder)
            if self.boom is not None:
                raise self.boom
            return f"애니메이션({folder})"

    def setUp(self):
        self.diag = []
        self.original_diag = L._diag
        self.addCleanup(setattr, L, "_diag", self.original_diag)
        L._diag = lambda action, *a, **k: self.diag.append((action,) + a)
        self.original_module = sys.modules.get("spriteanim")
        self.addCleanup(self._restore)

    def _restore(self):
        if self.original_module is None:
            sys.modules.pop("spriteanim", None)
        else:
            sys.modules["spriteanim"] = self.original_module

    def _install(self, boom=None, dirs=()):
        fake = self.FakeSpriteanim(boom)
        sys.modules["spriteanim"] = fake
        pet = type("P", (), {"SPRITE_SEARCH_DIRS": dirs})()
        L.install_sprite_load_log(pet)
        return fake

    def test_the_search_dirs_are_logged_at_startup(self):
        self._install(dirs=("/한/곳", "/또/한/곳"))
        self.assertIn(("log_images", ("/한/곳", "/또/한/곳")), self.diag)

    def test_one_sprite_set_is_probed_at_startup(self):
        # 선택 창을 다시 볼 수 없는 사람에게서도 이미지 상태를 알아야 한다.
        fake = self.FakeSpriteanim()
        sys.modules["spriteanim"] = fake
        pet = type("P", (), {"SPRITE_SEARCH_DIRS": (),
                             "sprite_folder_path": staticmethod(
                                 lambda name: f"/에셋/sprites/{name}")})()
        L.install_sprite_load_log(pet)
        self.assertIn(("log_sprite_probe", "/에셋/sprites/charmander"), self.diag)

    def test_a_game_without_sprite_folder_path_still_installs(self):
        fake = self.FakeSpriteanim()
        sys.modules["spriteanim"] = fake
        pet = type("P", (), {"SPRITE_SEARCH_DIRS": ()})()
        self.assertIsNotNone(L.install_sprite_load_log(pet))
        self.assertTrue(any("이미지 시험을 시작하지 못했습니다" in str(d)
                            for d in self.diag))

    def test_a_failure_carries_the_traceback(self):
        # 예외 이름만으로는 XML 쪽인지 디코딩 쪽인지 갈리지 않는다.
        fake = self._install(boom=OSError("Truncated File Read"))
        self.diag.clear()
        with self.assertRaises(OSError):
            fake.AnimSet("/어딘가/charmander")
        message = self.diag[0][1]
        self.assertIn("Truncated File Read", message)
        self.assertIn("AnimSet", message, "어느 줄에서 났는지 보여야 한다")
        self.assertEqual(len(message.splitlines()), 1, "한 줄이어야 한다")

    def test_a_success_logs_nothing_extra(self):
        fake = self._install()
        self.diag.clear()
        self.assertEqual(fake.AnimSet("/어딘가/pikachu"), "애니메이션(/어딘가/pikachu)")
        self.assertEqual(self.diag, [])

    def test_a_failure_names_the_reason_and_the_path(self):
        fake = self._install(boom=FileNotFoundError("AnimData.xml 없음"))
        self.diag.clear()
        with self.assertRaises(FileNotFoundError):
            fake.AnimSet("/어딘가/charmander")
        self.assertEqual(len(self.diag), 1)
        message = self.diag[0][1]
        self.assertIn("charmander", message)
        self.assertIn("FileNotFoundError", message)
        self.assertIn("폴더 없음", message)

    def test_the_failure_is_re_raised(self):
        # 게임의 '(이미지 없음)' 폴백이 그대로 살아 있어야 한다.
        fake = self._install(boom=ValueError("XML 깨짐"))
        with self.assertRaises(ValueError):
            fake.AnimSet("/어딘가/eevee")

    def test_the_same_folder_is_logged_once(self):
        # 스프라이트 로드는 프레임마다 일어나기도 한다.
        fake = self._install(boom=OSError("안 됨"))
        self.diag.clear()
        for _ in range(5):
            with self.assertRaises(OSError):
                fake.AnimSet("/어딘가/squirtle")
        self.assertEqual(len(self.diag), 1)

    def test_different_folders_are_each_logged(self):
        fake = self._install(boom=OSError("안 됨"))
        self.diag.clear()
        for name in ("pikachu", "charmander"):
            with self.assertRaises(OSError):
                fake.AnimSet(f"/어딘가/{name}")
        self.assertEqual(len(self.diag), 2)

    def test_a_missing_spriteanim_is_reported_not_raised(self):
        sys.modules["spriteanim"] = None      # import 가 실패하게
        self.assertIsNone(L.install_sprite_load_log(type("P", (), {})()))
        self.assertIn("스프라이트 모듈", self.diag[0][1])


class WindowsWording(unittest.TestCase):
    """게임의 안내 문구는 macOS 에 없는 것을 가리킨다.

    실제 신고: 야생 포켓몬 알림을 받은 사람이 "트레이 아이콘"을 찾다가 포기했다.
    macOS 에는 작업표시줄도 트레이도 없다. 그런데 이 문구들은 하필 **펫을
    잃어버린 사람에게 어디를 보라고 알려주는** 말이라서, 틀리면 그 사람이 갈 곳이
    없어진다.
    """

    # 게임 바이트코드에 실제로 들어 있는 문자열 (disasm/pet.dis.txt).
    GAME_STRINGS = [
        "PikaPet이 이미 실행 중이에요!\n작업표시줄 오른쪽 트레이 아이콘을 확인해보세요.",
        "야생 포켓몬이 나타난 것 같아요!\n트레이 아이콘을 클릭해 확인해보세요.",
        "몬스터볼 안에서 계속 자라고 있어요.\n트레이 아이콘에서 다시 꺼낼 수 있어요.",
        "전투가 계속되고 있어요. 트레이 아이콘을 눌러 다시 열 수 있어요.",
        "조용히 트레이 아이콘 깜빡이기 (추천)",
    ]

    def test_no_game_message_still_mentions_a_tray(self):
        for text in self.GAME_STRINGS:
            got = L.retarget_wording(text)
            self.assertNotIn("트레이", got, text)
            self.assertNotIn("작업표시줄", got, text)

    def test_every_message_points_at_the_menu_bar(self):
        for text in self.GAME_STRINGS[:4]:
            self.assertIn("◓", L.retarget_wording(text), text)

    def test_the_body_of_the_message_is_kept(self):
        # 부분 문자열만 갈아끼운다. 앞의 설명은 게임의 말 그대로 남아야 한다.
        got = L.retarget_wording(
            "몬스터볼 안에서 계속 자라고 있어요.\n트레이 아이콘에서 다시 꺼낼 수 있어요.")
        self.assertTrue(got.startswith("몬스터볼 안에서 계속 자라고 있어요."), got)

    def test_each_message_names_the_menu_item_that_fixes_it(self):
        pairs = [("야생 포켓몬이 나타난 것 같아요!\n트레이 아이콘을 클릭해 확인해보세요.",
                  "야생 포켓몬 확인"),
                 ("몬스터볼 안에서 계속 자라고 있어요.\n트레이 아이콘에서 다시 꺼낼 수 있어요.",
                  "몬스터볼에서 꺼내기"),
                 ("전투가 계속되고 있어요. 트레이 아이콘을 눌러 다시 열 수 있어요.",
                  "배틀 창 복구")]
        for text, item in pairs:
            self.assertIn(item, L.retarget_wording(text), text)

    def test_an_unrelated_message_is_untouched(self):
        for text in ("격투 스트레이트", "레벨이 올랐어요!", ""):
            self.assertEqual(L.retarget_wording(text), text)

    def test_widget_text_goes_through_it_too(self):
        # 설정 창의 라디오 버튼 이름은 위젯 옵션으로 들어온다.
        got = L._fix_text("조용히 트레이 아이콘 깜빡이기 (추천)")
        self.assertIn("메뉴 바 아이콘", got)

    def test_the_glyph_fix_still_applies_to_widget_text(self):
        self.assertEqual(L._fix_text("\u2694 배틀"), "\u2694\ufe0f 배틀")


class MessageBoxWording(unittest.TestCase):
    """대화상자 문구는 `Misc._options` 를 지나지 않는다."""

    class FakeBox:
        def __init__(self):
            self.calls = []

        def _make(self, name):
            def fn(title=None, message=None, **kw):
                self.calls.append((name, title, message, kw))
                return "눌렀음"
            return fn

    def setUp(self):
        self.box = self.FakeBox()
        for name in L.MESSAGE_FUNCTIONS:
            setattr(self.box, name, self.box._make(name))

    def test_the_already_running_message_is_translated(self):
        # 앱을 눌러도 아무 일이 없어 보이는 사람이 받는 유일한 설명이다.
        L.install_message_wording(self.box)
        self.box.showinfo(
            "PikaPet",
            "PikaPet이 이미 실행 중이에요!\n작업표시줄 오른쪽 트레이 아이콘을 확인해보세요.")
        name, title, message, _ = self.box.calls[0]
        self.assertEqual(title, "PikaPet")
        self.assertIn("메뉴 바의 ◓", message)
        self.assertNotIn("작업표시줄", message)

    def test_every_dialog_function_is_covered(self):
        swapped = L.install_message_wording(self.box)
        self.assertEqual(set(swapped), set(L.MESSAGE_FUNCTIONS))

    def test_the_return_value_is_passed_back(self):
        # askyesno 의 답이 사라지면 게임의 분기가 전부 망가진다.
        L.install_message_wording(self.box)
        self.assertEqual(self.box.askyesno("PikaPet", "할까요?"), "눌렀음")

    def test_other_arguments_survive(self):
        L.install_message_wording(self.box)
        self.box.showwarning("PikaPet", "조심", icon="warning", parent=None)
        _, _, _, kw = self.box.calls[0]
        self.assertEqual(kw, {"icon": "warning", "parent": None})

    def test_a_missing_function_is_skipped(self):
        del self.box.askretrycancel
        swapped = L.install_message_wording(self.box)
        self.assertNotIn("askretrycancel", swapped)


class SingleInstanceLog(unittest.TestCase):
    """이미 돌고 있어서 그냥 끝나는 실행.

    이 검사는 `load_state()` 앞이라 (pet.py:19049 대 19062) 세이브를 지우든 앱을
    다시 설치하든 결과가 같다. 기록이 없으면 "지우고 새로 설치해도 안 뜬다"에
    답할 수 없다.
    """

    class FakeLayer:
        def __init__(self, got):
            self._got = got
            self.calls = []

        def acquire_single_instance_lock(self, name="기본"):
            self.calls.append(name)
            return self._got

    def setUp(self):
        self.diag = []
        self.original = L._diag
        self.addCleanup(setattr, L, "_diag", self.original)
        L._diag = lambda action, *a, **k: self.diag.append((action,) + a)

    def test_a_blocked_launch_is_written_down(self):
        layer = self.FakeLayer(False)
        L.install_single_instance_log(layer)
        self.assertFalse(layer.acquire_single_instance_lock())
        self.assertEqual(len(self.diag), 1)
        action, message = self.diag[0]
        self.assertEqual(action, "log")
        self.assertIn("이미 실행 중", message)
        self.assertIn("◓", message, "어디를 보라고 알려줘야 한다")

    def test_a_normal_launch_logs_nothing_here(self):
        layer = self.FakeLayer(True)
        L.install_single_instance_log(layer)
        self.assertTrue(layer.acquire_single_instance_lock())
        self.assertEqual(self.diag, [])

    def test_the_answer_is_not_changed(self):
        # 락 판정을 뒤집으면 펫이 둘이 된다.
        for got in (True, False):
            layer = self.FakeLayer(got)
            L.install_single_instance_log(layer)
            self.assertEqual(layer.acquire_single_instance_lock(), got)

    def test_the_mutex_name_is_passed_through(self):
        layer = self.FakeLayer(True)
        L.install_single_instance_log(layer)
        layer.acquire_single_instance_lock("PikaPetSingleInstanceMutex")
        self.assertEqual(layer.calls, ["PikaPetSingleInstanceMutex"])


if __name__ == "__main__":
    unittest.main()
