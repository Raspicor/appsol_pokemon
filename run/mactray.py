"""메뉴 바 항목. 트레이에만 있던 기능을 macOS에서 되살린다.

PikaPet의 `PetApp.setup_tray`는 pystray로 트레이 메뉴를 만들고, 그 안에만 있는
동작이 셋 있다. 우클릭 메뉴(`PetApp.build_menu`)에는 없다:

  * `exit_ball`               몬스터볼에서 꺼내기
  * `_open_pending_encounter` 야생 포켓몬 조우 열기
  * `_restore_battle_window`  배틀 창 복구

패치 4가 pystray를 걷어내면서 이 셋이 닿을 수 없게 됐고, 그중 `exit_ball`은
치명적이다. 펫이 볼에 들어가면 창이 숨어서 우클릭할 대상 자체가 사라지므로,
한번 들어가면 두 번 다시 꺼낼 수 없다. 야생 포켓몬 알림은 아예 "트레이 아이콘을
클릭해 확인해보세요"라고 안내한다.

pystray를 되살리는 것이 답은 아니다. pystray의 macOS 백엔드는
`NSApplication.run()`을 부르고 PikaPet은 그것을 데몬 스레드에서 시작해
`SIGTRAP`으로 즉사한다. 여기서는 NSStatusItem을 Tk의 메인 스레드에서 직접 만든다.
Tk가 이미 macOS 런루프를 돌리고 있으므로 별도의 run loop가 필요 없다.

**메뉴 항목의 동작은 AppKit 콜백이다.** 그 자리에서 Tcl을 부르면 프로세스가
abort한다 (overlay.py의 모듈 독스트링 참고). 그래서 콜백은 큐에만 넣고, Tk 타이머가
꺼내서 실제로 게임 함수를 부른다.
"""

import collections

# 메뉴를 고른 뒤 실제로 실행되기까지의 최대 지연. 사람이 메뉴를 누르는 동작이라
# 100 ms면 즉각적으로 느껴지고, 틱 비용도 무시할 수 있다.
DRAIN_MS = 100

# macOS 시스템 폰트에는 U+2694(⚔)의 쓸 만한 텍스트 글리프가 없다. 실측(메뉴 폰트
# .AppleSystemUIFont 13pt): 그냥 ⚔ 는 잉크 26px / 폭 7.8pt 로 × 의 26px / 8.1pt 와
# 사실상 같아서 '⚔ 배틀 창 복구'가 '× 배틀 창 복구'로 읽힌다. VS16(U+FE0F)을 붙이면
# Apple Color Emoji 가 받아 77px / 19.0pt 가 된다.
#
# pikapet_mac 의 install_glyph_fix 는 `tkinter.Misc._options` 에 걸려 있어 여기까지
# 닿지 않는다 -- NSMenuItem 의 제목은 tkinter 를 거치지 않는다. 그래서 메뉴 제목을
# 만드는 이 한 곳에서 따로 고친다.
BROKEN_GLYPHS = {"\u2694": "\u2694\ufe0f"}


# 수동 버전 확인 항목의 이름. 런처와 테스트가 같은 문자열을 봐야 하므로 여기 둔다.
VERSION_CHECK_LABEL = "🔄 새 버전 확인"


def menu_title(label):
    """메뉴에 실제로 넣을 제목. 깨져 보이는 기호만 고친다."""
    for bad, good in BROKEN_GLYPHS.items():
        if bad in label and good not in label:
            label = label.replace(bad, good)
    return label


_target_class = None


def available():
    """메뉴 바 항목을 만들 수 있으면 True."""
    try:
        from AppKit import NSStatusBar, NSMenu, NSMenuItem  # noqa: F401
    except Exception:
        return False
    return True


def _menu_target_class():
    """메뉴 선택을 큐에 넣는 ObjC 타깃.

    ObjC 런타임에 같은 이름을 두 번 등록할 수 없으므로 한 번만 만들어 캐시한다.
    """
    global _target_class
    if _target_class is not None:
        return _target_class

    from Foundation import NSObject

    class PikaPetMenuTarget(NSObject):
        def initWithQueue_(self, queue):
            self = self.init()
            if self is None:
                return None
            self.queue = queue
            return self

        def invoke_(self, sender):
            # AppKit 콜백. Tcl은 절대 건드리지 않고 큐에만 넣는다.
            try:
                self.queue.append(int(sender.tag()))
            except Exception:
                pass

    _target_class = PikaPetMenuTarget
    return _target_class


class MenuBarItem:
    """메뉴 바에 붙는 항목 하나와 그 메뉴.

    `actions`는 (표시할 이름, 부를 함수) 목록이다. 함수는 Tk 타이머 안에서
    불리므로 게임 코드를 자유롭게 건드려도 된다.
    """

    def __init__(self, root, actions, title="◓"):
        from AppKit import (NSStatusBar, NSMenu, NSMenuItem,
                            NSVariableStatusItemLength)

        self.root = root
        self.actions = list(actions)
        self.queue = collections.deque()

        # ObjC 쪽에서만 참조하는 객체들이므로 파이썬 쪽에서 강한 참조를 들고
        # 있어야 한다. 놓으면 수거되고 메뉴가 죽는다.
        self.target = _menu_target_class().alloc().initWithQueue_(self.queue)
        self.menu = NSMenu.alloc().init()
        self.menu.setAutoenablesItems_(False)

        for index, (label, _fn) in enumerate(self.actions):
            if label is None:                      # 구분선
                self.menu.addItem_(NSMenuItem.separatorItem())
                continue
            entry = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
                menu_title(label), b"invoke:", "")
            entry.setTarget_(self.target)
            entry.setTag_(index)
            entry.setEnabled_(True)
            self.menu.addItem_(entry)

        self.item = NSStatusBar.systemStatusBar().statusItemWithLength_(
            NSVariableStatusItemLength)
        self.item.button().setTitle_(title)
        self.item.button().setToolTip_("PikaPet")
        self.item.setMenu_(self.menu)

        self.root.after(DRAIN_MS, self._drain)

    def add_action(self, label, fn, index=0):
        """메뉴에 항목을 하나 더 붙인다. **Tk 타이머 안에서 부를 것.**

        업데이트 안내처럼 실행 중에야 생기는 항목을 위한 것이다. 기본값은 맨
        위(index 0) -- 평소에 없던 항목이라 눈에 띄어야 의미가 있다.

        같은 이름이 이미 있으면 아무것도 하지 않는다. 확인을 여러 번 돌려도
        메뉴가 불어나지 않게.
        """
        from AppKit import NSMenuItem

        if any(existing == label for existing, _ in self.actions):
            return None
        self.actions.append((label, fn))
        entry = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            menu_title(label), b"invoke:", "")
        entry.setTarget_(self.target)
        entry.setTag_(len(self.actions) - 1)
        entry.setEnabled_(True)
        self.menu.insertItem_atIndex_(entry, index)
        return entry

    def _drain(self):
        """큐에 쌓인 메뉴 선택을 실행한다. Tk 타이머 안이라 Tcl 호출이 안전하다."""
        while self.queue:
            try:
                index = self.queue.popleft()
                label, fn = self.actions[index]
            except Exception:
                continue
            try:
                fn()
            except Exception as exc:
                print(f"  메뉴 '{label}' 실행 실패: "
                      f"{type(exc).__name__}: {exc}", flush=True)
        try:
            if self.root.winfo_exists():
                self.root.after(DRAIN_MS, self._drain)
        except Exception:
            pass

    def close(self):
        try:
            from AppKit import NSStatusBar
            NSStatusBar.systemStatusBar().removeStatusItem_(self.item)
        except Exception:
            pass


def menu_actions(app, version_check=None):
    """메뉴에 넣을 (이름, 함수) 목록. `None` 이름은 구분선이다.

    목록을 만드는 일만 한다 -- AppKit 없이 테스트할 수 있게. 메뉴에 무엇이
    들어가고 무엇이 빠지는지가 이 파일에서 가장 자주 틀리는 부분이다.

    우클릭 메뉴에 이미 있는 것은 넣지 않는다. 다만 '화면 중앙으로 부르기'는
    예외로 둔다. 펫이 화면 밖으로 걸어 나가면 우클릭할 수 없어서, 볼에 들어간
    것과 같은 막다른 길이 되기 때문이다.

    `version_check` 는 런처가 넘겨준다 (macupdate 를 아는 쪽이 거기라서).
    없으면 그 항목은 빠진다.

    '알림 테스트'는 뺐다. ad-hoc 서명에서는 배너가 늘 스크립트 편집기 소유로
    뜨기 때문에, 눌러봐도 "PikaPet 알림이 되는가"에 답을 주지 못한다. 진단에는
    도움이 됐지만 쓰는 사람에게는 잘못된 결과를 보여주는 항목이었다.
    """
    def call(name):
        def run():
            fn = getattr(app, name, None)
            if fn is None:
                print(f"  PetApp에 {name} 이 없습니다", flush=True)
                return
            fn()
        return run

    actions = [
        ("🔴 몬스터볼에서 꺼내기", call("exit_ball")),
        ("🌿 야생 포켓몬 확인", call("_open_pending_encounter")),
        ("⚔ 배틀 창 복구", call("_restore_battle_window")),
        (None, None),
        ("🎯 화면 중앙으로 부르기", call("force_recall")),
    ]
    if version_check is not None:
        actions.append((VERSION_CHECK_LABEL, version_check))
    actions += [
        (None, None),
        ("❌ 종료", call("quit_app")),
    ]
    return actions


def install(app, root, version_check=None):
    """`app`(PetApp)의 트레이 전용 동작을 메뉴 바에 붙인다."""
    return MenuBarItem(root, menu_actions(app, version_check))
