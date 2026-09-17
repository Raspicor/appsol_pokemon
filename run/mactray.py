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
                label, b"invoke:", "")
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
            label, b"invoke:", "")
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


def install(app, root):
    """`app`(PetApp)의 트레이 전용 동작을 메뉴 바에 붙인다.

    우클릭 메뉴에 이미 있는 것은 넣지 않는다. 다만 '화면 중앙으로 부르기'는
    예외로 둔다. 펫이 화면 밖으로 걸어 나가면 우클릭할 수 없어서, 볼에 들어간
    것과 같은 막다른 길이 되기 때문이다.
    """
    def call(name):
        def run():
            fn = getattr(app, name, None)
            if fn is None:
                print(f"  PetApp에 {name} 이 없습니다", flush=True)
                return
            fn()
        return run

    def test_notification():
        """알림이 실제로 뜨는지, 그리고 누르면 어디로 가는지 확인하는 용도.

        알림은 조용히 실패하기 쉬운 영역이다 (권한, 집중 모드, 프레임워크가
        받아놓고 안 띄우는 경우). 눌러볼 수 있는 자리를 하나 두는 편이
        "왜 안 오지"를 훨씬 빨리 끝낸다.
        """
        icon = getattr(app, "tray_icon", None)
        if icon is None:
            print("  tray_icon이 없습니다", flush=True)
            return
        icon.notify("알림 테스트입니다. 이 배너를 눌러보세요.", "PikaPet")

    actions = [
        ("🔴 몬스터볼에서 꺼내기", call("exit_ball")),
        ("🌿 야생 포켓몬 확인", call("_open_pending_encounter")),
        ("⚔ 배틀 창 복구", call("_restore_battle_window")),
        (None, None),
        ("🎯 화면 중앙으로 부르기", call("force_recall")),
        ("🔔 알림 테스트", test_notification),
        (None, None),
        ("❌ 종료", call("quit_app")),
    ]
    return MenuBarItem(root, actions)
