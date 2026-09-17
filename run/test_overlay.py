"""overlay.py의 장부 관리에 대한 테스트.

여기 있는 것은 전부 디스플레이 없이 돈다. AppKit 쪽은 앱을 실제로 돌려서
확인했고, 여기서 테스트하는 것은 실제로 틀렸던 부분이다 — 어느 창을 대신할지
정하는 것, 그리고 네이티브 창을 Tk 창에 맞춰 붙들어두는 것.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import overlay


class FakeOverlay:
    """NSWindow 자리를 대신하면서, 무엇을 요청받았는지 기록한다."""

    def __init__(self):
        self.shown = []
        self.visible = False
        self.alpha = 1.0
        self.closed = False

    def show(self, x, y, w, h, ns_image=None):
        self.shown.append((x, y, w, h))
        self.visible = True

    def set_alpha(self, value):
        self.alpha = value

    def hide(self):
        self.visible = False

    def close(self):
        self.closed = True


class FakeImage:
    def __init__(self, width=32, height=40):
        self.width = width
        self.height = height


class FakeWidget:
    """매니저가 건드리는 Tk 위젯 API의 일부만."""

    def __init__(self, name, top=None, rootx=0, rooty=0, mapped=True, exists=True):
        self.name = name
        self.top = top if top is not None else self
        self.rootx, self.rooty = rootx, rooty
        self.mapped, self.exists = mapped, exists

    def __str__(self):
        return self.name

    def winfo_toplevel(self):
        return self.top

    def winfo_rootx(self):
        return self.rootx

    def winfo_rooty(self):
        return self.rooty

    def winfo_ismapped(self):
        return self.mapped

    def winfo_exists(self):
        return self.exists


def make_manager():
    calls = []
    manager = overlay._Manager(root=None,
                               raw_attributes=lambda *a: calls.append(a))
    return manager, calls


def attach(manager, top, label, pil=None, at=(0, 0)):
    """set_image가 하는 것처럼, 가짜 오버레이와 함께 라벨을 등록한다."""
    label.rootx, label.rooty = at
    record = {"label": label, "overlay": FakeOverlay(),
              "pil": pil or FakeImage(), "opacity": 1.0}
    manager.records[str(label)] = record
    manager.transparent.add(str(top))
    return record


class GeometryParsing(unittest.TestCase):
    """오버레이가 따라가는 것이 geometry 문자열이므로, PetApp.redraw가 쓰는
    방식 그대로 읽어야 한다."""

    def parse(self, spec):
        match = overlay._GEOMETRY.match(spec)
        return None if match is None else (int(match.group(3)), int(match.group(4)))

    def test_size_and_position(self):
        self.assertEqual(self.parse("32x40+600+300"), (600, 300))

    def test_position_only(self):
        self.assertEqual(self.parse("+600+300"), (600, 300))

    def test_negative_left_is_written_as_plus_minus(self):
        # f"{w}x{h}+{left}+{top}" 에서 left가 음수인 경우. 펫이 주 화면 왼쪽에
        # 있는 화면으로 걸어가면 이렇게 된다
        self.assertEqual(self.parse("32x40+-55+951"), (-55, 951))

    def test_size_only_is_not_a_move(self):
        self.assertIsNone(self.parse("32x40"))

    def test_edge_relative_form_is_refused(self):
        # Tk의 "-5-5"는 "오른쪽/아래 가장자리로부터"를 뜻한다. 게임은 이 형식을
        # 내보내지 않고, 추측하면 스프라이트가 틀린 자리에 놓인다
        self.assertIsNone(self.parse("32x40-5-5"))


class Ownership(unittest.TestCase):
    def test_only_windows_given_the_chroma_key_are_owned(self):
        manager, _ = make_manager()
        pet = FakeWidget(".")
        dialog = FakeWidget(".!toplevel")
        manager.mark_transparent(pet)

        self.assertTrue(manager.owns(FakeWidget(".!label", top=pet)))
        self.assertFalse(manager.owns(FakeWidget(".!toplevel.!label", top=dialog)))

    def test_a_widget_that_cannot_answer_is_not_owned(self):
        manager, _ = make_manager()

        class Broken(FakeWidget):
            def winfo_toplevel(self):
                raise RuntimeError("destroyed")

        self.assertFalse(manager.owns(Broken(".x")))


class FollowingAMove(unittest.TestCase):
    """`moved`가 존재하는 이유: `geometry()` 뒤에 위치를 읽으면 *옛* 값이 나온다.
    그 시점에 창은 아직 움직이지 않았다."""

    def test_uses_the_requested_position_not_the_stale_one(self):
        manager, _ = make_manager()
        top = FakeWidget(".", rootx=1904, rooty=951)
        label = FakeWidget(".!label", top=top)
        record = attach(manager, top, label, at=(1904, 951))

        manager.moved(top, "32x40+600+300")

        self.assertEqual(record["overlay"].shown[-1], (600, 300, 32, 40))

    def test_keeps_the_label_offset_inside_its_window(self):
        manager, _ = make_manager()
        top = FakeWidget(".", rootx=1000, rooty=500)
        label = FakeWidget(".!label", top=top)
        record = attach(manager, top, label, at=(1004, 508))   # 4,8 만큼 안쪽

        manager.moved(top, "32x40+600+300")

        self.assertEqual(record["overlay"].shown[-1], (604, 308, 32, 40))

    def test_ignores_labels_in_other_windows(self):
        manager, _ = make_manager()
        pet = FakeWidget(".", rootx=0, rooty=0)
        companion = FakeWidget(".!toplevel", rootx=0, rooty=0)
        mine = attach(manager, pet, FakeWidget(".!label", top=pet))
        theirs = attach(manager, companion,
                        FakeWidget(".!toplevel.!label", top=companion))

        manager.moved(pet, "32x40+600+300")

        self.assertEqual(len(mine["overlay"].shown), 1)
        self.assertEqual(theirs["overlay"].shown, [])

    def test_an_unmapped_label_is_left_alone(self):
        manager, _ = make_manager()
        top = FakeWidget(".")
        label = FakeWidget(".!label", top=top, mapped=False)
        record = attach(manager, top, label)

        manager.moved(top, "32x40+600+300")

        self.assertEqual(record["overlay"].shown, [])

    def test_an_unparseable_spec_falls_back_to_reading_tk(self):
        manager, _ = make_manager()
        top = FakeWidget(".", rootx=700, rooty=400)
        label = FakeWidget(".!label", top=top)
        record = attach(manager, top, label, at=(700, 400))

        manager.moved(top, "32x40-5-5")

        self.assertEqual(record["overlay"].shown[-1], (700, 400, 32, 40))


class ForwardingTheMouse(unittest.TestCase):
    """오버레이가 마우스를 받아 Tk로 넘긴다. 알파를 낮춘 Tk 창이 클릭을 계속
    받을지는 macOS가 보장하지 않고, 실제로 받지 못했다."""

    def setUp(self):
        self.manager, _ = make_manager()
        self.top = FakeWidget(".")
        self.label = FakeWidget(".!label", top=self.top, rootx=600, rooty=300)
        self.record = attach(self.manager, self.top, self.label, at=(600, 300))
        self.sent = []
        self.label.event_generate = lambda seq, **kw: self.sent.append((seq, kw))

    def test_enqueue_does_not_touch_tk(self):
        """AppKit 콜백이 부르는 자리다. 여기서 Tcl에 재진입하면 다음 Tk 타이머가
        `PyEval_RestoreThread: thread state is NULL` 로 프로세스를 죽인다.
        격리 재현: 직접 호출 2/2 사망, 큐 경유 2/2 생존."""
        def explode(seq, **kw):
            raise AssertionError("enqueue가 Tk를 건드렸다")
        self.label.event_generate = explode

        self.manager.enqueue(self.record, "<Button-1>", 616, 320)

        self.assertEqual(len(self.manager.pending), 1)

    def test_drain_delivers_in_order(self):
        for seq in ("<Button-1>", "<B1-Motion>", "<ButtonRelease-1>"):
            self.manager.enqueue(self.record, seq, 616, 320)

        self.manager.drain()

        self.assertEqual([s for s, _ in self.sent],
                         ["<Button-1>", "<B1-Motion>", "<ButtonRelease-1>"])
        self.assertEqual(len(self.manager.pending), 0)

    def test_drain_empties_the_queue_even_if_one_fails(self):
        calls = []

        def flaky(seq, **kw):
            calls.append(seq)
            if seq == "<B1-Motion>":
                raise RuntimeError("nope")
        self.label.event_generate = flaky
        for seq in ("<Button-1>", "<B1-Motion>", "<ButtonRelease-1>"):
            self.manager.enqueue(self.record, seq, 616, 320)

        self.manager.drain()

        self.assertEqual(calls, ["<Button-1>", "<B1-Motion>", "<ButtonRelease-1>"])
        self.assertEqual(len(self.manager.pending), 0)

    def test_screen_position_becomes_both_widget_and_root_coordinates(self):
        # on_press는 x/y를 라벨 안 오프셋으로, on_motion은 x_root/y_root를
        # 화면 좌표로 읽는다 (pet.py:11657, 11669)
        self.manager.dispatch(self.record, "<Button-1>", 616, 320)

        sequence, kw = self.sent[0]
        self.assertEqual(sequence, "<Button-1>")
        self.assertEqual((kw["x"], kw["y"]), (16, 20))
        self.assertEqual((kw["rootx"], kw["rooty"]), (616, 320))

    def test_extra_arguments_are_passed_through(self):
        self.manager.dispatch(self.record, "<B1-Motion>", 600, 300, state=0x100)

        self.assertEqual(self.sent[0][1]["state"], 0x100)

    def test_a_destroyed_label_is_not_written_to(self):
        self.label.exists = False

        self.manager.dispatch(self.record, "<Button-1>", 616, 320)

        self.assertEqual(self.sent, [])

    def test_a_failing_generate_does_not_escape(self):
        # 이 경로는 AppKit 콜백 안에서 돈다. 여기서 예외가 나가면 Tk가 아니라
        # ObjC 런타임으로 올라간다.
        def boom(seq, **kw):
            raise RuntimeError("gone")
        self.label.event_generate = boom

        self.manager.dispatch(self.record, "<Button-1>", 616, 320)


class Lifecycle(unittest.TestCase):
    def test_a_destroyed_label_drops_its_overlay(self):
        manager, _ = make_manager()
        top = FakeWidget(".")
        label = FakeWidget(".!label", top=top, exists=False)
        record = attach(manager, top, label)

        manager.resync()

        self.assertTrue(record["overlay"].closed)
        self.assertEqual(manager.records, {})

    def test_an_unmapped_label_hides_rather_than_closing(self):
        manager, _ = make_manager()
        top = FakeWidget(".")
        label = FakeWidget(".!label", top=top, mapped=False)
        record = attach(manager, top, label)
        record["overlay"].visible = True

        manager.resync()

        self.assertFalse(record["overlay"].visible)
        self.assertFalse(record["overlay"].closed)
        self.assertIn(".!label", manager.records)


class WindowOpacity(unittest.TestCase):
    """Tk 창의 알파는 이미 쓰임새가 정해져 있다 — 그게 창을 안 보이게 만드는
    수단이다 — 그래서 게임 자신의 투명도 설정은 오버레이에 적용해야 한다."""

    def test_opacity_reaches_the_overlay(self):
        manager, _ = make_manager()
        top = FakeWidget(".")
        record = attach(manager, top, FakeWidget(".!label", top=top))

        manager.set_opacity(top, 0.5)

        self.assertEqual(record["overlay"].alpha, 0.5)
        self.assertEqual(record["opacity"], 0.5)

    def test_a_window_is_dimmed_once_only(self):
        manager, calls = make_manager()
        top = FakeWidget(".")

        manager._dim(top)
        manager._dim(top)

        self.assertEqual(calls, [(top, "-alpha", overlay.INVISIBLE_ALPHA)])

    def test_the_dimmed_alpha_stays_hit_testable(self):
        # AppKit은 알파가 0인 창을 클릭 경로에서 건너뛴다. 그러면 펫이 드래그와
        # 우클릭 메뉴를 잃는다
        self.assertGreater(overlay.INVISIBLE_ALPHA, 0)
        self.assertLess(overlay.INVISIBLE_ALPHA, 0.01)


if __name__ == "__main__":
    unittest.main()
