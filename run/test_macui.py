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
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk

import pikapet_mac as L


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

if __name__ == "__main__":
    unittest.main()
