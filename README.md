# PikaPet — 리버스 엔지니어링 및 macOS 포팅 분석

`~/Downloads/PikaPet.exe` (128 MB, PE32+ GUI, MD5 `74ff8b2ab58463f814bc5df28dc359ca`) 를 분해하고
macOS에서 실제로 구동시킨 결과 정리.

**결론부터: 재개발하지 않았고, 할 필요도 없었습니다. 원본 바이트코드가 macOS에서 돕니다.**
`run/pikapet.sh`로 실행합니다. 게임 로직 19,000줄은 한 줄도 건드리지 않았고,
Windows 가정이 새어나오는 네 지점만 런타임에 패치합니다.

---

## 1. 이게 뭔가

PyInstaller onefile로 묶인 **Python 3.14 데스크톱 펫 게임**입니다.

| 항목 | 값 |
|---|---|
| 런타임 | CPython 3.14 (`python314.dll`) |
| GUI | tkinter + Tcl/Tk 8.6.15 |
| 기타 의존성 | Pillow, numpy 2.5, pystray, websockets 16, werkzeug 3.1.8, watchdog |
| 메인 스크립트 | `pet.py` — **19,070 줄** |
| 코드 오브젝트 | 1,190개 (클래스/함수/컴프리헨션 포함) |
| 자체 모듈 | `spriteanim`, `winlayer` |
| 에셋 | 123 MB (`assets`, `assets_v3`, `assets_v4`, `badges_trainer`) |

내용물은 포켓몬풍 육성 게임입니다: 도감/진화, 체육관 8배지, 칭호 시스템, 메가진화,
무한모드, 채굴, 오목 AI(미니맥스), 배틀 코드 기반 비동기 PvP + websockets 실시간 PvP.
`PetApp` 클래스 하나가 소스 4,515~18,986줄을 차지합니다.

원본 docstring에 이런 문장이 남아 있습니다 —
*"이 프로젝트를 만든 샌드박스에는 Windows/tkinter가 없어 직접 실행 테스트를 하지 못했습니다."*
AI로 작성된 코드로 보이며, 그래서인지 모든 함수가 방어적으로 try/except 처리돼 있습니다.

## 2. Windows 의존성은 어디에 있나

**`pet.py`에는 Win32 API 직접 호출이 단 한 건도 없습니다.** `ctypes`/`windll`/`win32`/`winreg` 전무.
OS 의존성은 두 군데로만 들어갑니다.

### (a) `winlayer` 모듈 — 함수 10개짜리 얇은 계층

```
set_dpi_aware()                              flash_taskbar(hwnd, count, timeout)
stop_taskbar_flash(hwnd)                     hide_window_from_taskbar(hwnd)
get_virtual_screen_rect()   -> (l,t,w,h)     get_secondary_monitor_rect()
get_taskbar_rect()          -> (l,t,r,b)     acquire_single_instance_lock(name) -> bool
get_window_ledges(exclude, max) -> [{left,top,right,title}]   # 다른 창 윗면 = 펫이 올라타는 발판
get_desktop_icon_positions(max) -> [(x,y)]   # 바탕화면 아이콘 위 착지
```

**이 함수들은 전부 `if not IS_WINDOWS: return <안전한 기본값>` 으로 시작합니다.**
`IS_WINDOWS = sys.platform.startswith('win')` 이므로 macOS에서는 원본 `winlayer.pyc`를
**수정 없이 그대로** 쓸 수 있고, 관련 기능만 조용히 비활성화됩니다.

### (b) 저장 경로 — `%APPDATA%` / `%LOCALAPPDATA%`

`SAVE_DIR = $APPDATA/PikaPet`. macOS에선 환경변수를 직접 지정하면 됩니다
(`run/pikapet.sh`가 `~/Library/Application Support`로 설정).

## 3. macOS 구동 결과

**돌아갑니다.** 펫이 화면을 걸어다니고, 스프라이트 애니메이션이 재생되며, 상태가 저장됩니다.

### 그대로 동작한 것
- 19,070줄 모듈 초기화 (전역 425개, `PetApp` 로드)
- **Tcl/Tk 9.0.4** — 8.6.15로 빌드됐는데도 호환
- 펫 창 생성, 스프라이트 애니메이션, always-on-top (window layer 19), 이동
- 상태 저장/복구
- **우클릭 메뉴** — Tk 9는 맥에서도 우클릭이 `<Button-3>`이라(`tk.tcl`이 `<<ContextMenu>>`를
  플랫폼 구분 없이 Button-3에 매핑) 기존 바인딩이 그대로 먹습니다

### 고친 것 다섯 가지

`run/pikapet_mac.py`가 원본 바이트코드를 로드한 뒤 런타임에 패치합니다.
**`pet.pyc`는 건드리지 않습니다** — 디컴파일 품질과 무관하게 동작하고, 원본과 어긋날 일도 없습니다.

| # | 문제 | 해결 |
|---|---|---|
| 1 | `winlayer`가 Win32 전용 | `sys.modules["winlayer"] = maclayer` — Quartz/AppKit 구현으로 교체 |
| 2 | `-transparentcolor`는 Windows 전용 | Tk 레벨에서 맥의 `-transparent`로 번역 |
| 3 | `MAGIC = '#ff00ff'` 컬러키 | 폴백 경로에서만 `systemTransparent`로 교체 |
| 4 | pystray가 프로세스를 죽임 | `setup_tray`를 `MacTray` + 메뉴 바 항목으로 교체 |
| 5 | 스프라이트가 마젠타 판 위에 그려짐 | 판을 진짜 알파로 바꾸고 `run/overlay.py`가 네이티브로 그림 |

**트레이에만 있던 기능 셋**은 `run/mactray.py`가 메뉴 바(◓) 항목으로 되살립니다 —
`exit_ball`(몬스터볼에서 꺼내기), `_open_pending_encounter`(야생 포켓몬 조우),
`_restore_battle_window`(배틀 창 복구). 우클릭 메뉴에는 없는 것들입니다. 특히
`exit_ball`이 없으면 펫이 볼에 들어간 순간 창이 숨어서 우클릭할 대상이 사라지고
두 번 다시 꺼낼 수 없습니다. pystray를 되살리는 대신 NSStatusItem을 Tk의 메인
스레드에서 직접 만들기 때문에 별도 run loop가 필요 없습니다.

**오버레이 창 레벨은 23**입니다. 메뉴 바가 레이어 24에 합성되므로
`NSStatusWindowLevel`(25)로 두면 펫이 위로 걸어갈 때 메뉴 바를 덮고, 16ms마다
창을 재배치하는 탓에 그 띠가 계속 다시 합성돼 눈에 보이게 지직입니다. 23이면
원래 Tk 창처럼 메뉴 바 뒤로 지나가고, 펫의 Tk 창(레이어 19)보다는 위라서 클릭도
계속 오버레이가 받습니다.

**투명 배경은 Tk로는 불가능합니다.** Tk 9는 toplevel을 **알파 채널이 없는** 백킹 스토어에
렌더링합니다 — 콘텐트 뷰의 레이어가 `isOpaque = NO`이고 NSWindow가 이미 non-opaque에
clearColor인데도 `kCGImageAlphaNoneSkipLast` CGImage를 돌려줍니다. 그래서 `-transparent`,
`systemTransparent`, `NSWindow.setOpaque_(False)` 무엇을 해도 Tk가 그린 것은 꽉 찬
사각형으로 합성됩니다 (Tk 9.0.4 / macOS 26 실측. Tk 8.6.18은 반대로 창을 통째로 뚫어버립니다).

그래서 Tk의 렌더러와 싸우는 대신 빼버립니다. 컬러키를 요청한 창마다 그 위에 테두리 없는
NSWindow를 얹어 스프라이트를 **진짜 per-pixel 알파로** 그리고, Tk 창은 자리·드래그·우클릭
메뉴를 계속 맡은 채 보이지 않을 만큼 낮은 알파로 남습니다. 0이 아니라 0.004인 이유는
AppKit이 알파 0인 창을 클릭 히트테스트에서 건너뛰기 때문입니다.

오버레이가 실제로 무언가를 그리기 시작한 뒤에야 Tk 창을 투명하게 만들기 때문에,
판단이 틀린 창의 최악의 결과는 **예전 동작**이지 펫이 사라지는 것이 아닙니다.
`PIKAPET_OVERLAY=0`으로 예전 동작을 강제할 수 있습니다.

**2번이 왜 예외 처리만으로 부족한가**: `Companion.__init__`에서 라벨 생성이
`-transparentcolor` 호출과 **같은 try 블록 안**에 있습니다. 예외가 나면 동료 포켓몬 창에
스프라이트가 안 붙습니다. 그래서 예외를 내버려두지 않고 속성 자체를 번역합니다.

**4번의 정체**: `setup_tray()`가 `threading.Thread(target=icon.run).start()`로 pystray를
백그라운드 스레드에서 돌립니다. macOS pystray는 `NSApplication.run()`을 호출하는데 이건
메인 스레드 전용이라 `EXC_BREAKPOINT (SIGTRAP)`로 즉사합니다 (스택: AppKit ← libffi ← pyobjc).
다른 스레드의 네이티브 크래시라 `setup_tray`의 try/except로도 못 잡습니다.

트레이 메뉴는 **재구현하지 않았습니다**. `PetApp.build_menu`의 우클릭 메뉴가 트레이보다
완전하기 때문입니다 — 스킬·훈련·크기조절·도감·진화·일일퀘스트(광산/뽑기/수련/무한의돌/미니게임)·
메가진화·방향키조작·불러오기·설정·저장·종료가 전부 들어있습니다.
`MacTray`는 `notify()`를 알림 센터로 넘기고 `if self.tray_icon:` 가드를 통과시키는 역할만 합니다.

### `maclayer` — winlayer의 macOS 구현

10개 함수 전부 구현했고, 원본 `winlayer.pyc`와 시그니처가 일치하는지 테스트로 고정했습니다.

| 함수 | macOS 구현 |
|---|---|
| `get_virtual_screen_rect` | `CGGetActiveDisplayList` + `CGDisplayBounds` 합집합 |
| `get_secondary_monitor_rect` | `CGMainDisplayID`가 아닌 첫 디스플레이 |
| `get_taskbar_rect` | Dock — 각 화면의 `frame` vs `visibleFrame` 차이 |
| `get_window_ledges` | `CGWindowListCopyWindowInfo` — 다른 앱 창의 윗변 |
| `acquire_single_instance_lock` | `flock` (프로세스 종료 시 커널이 해제 → 죽은 락 없음) |
| `flash_taskbar` / `stop_taskbar_flash` | `requestUserAttention_` (Dock 아이콘 바운스) |
| `set_dpi_aware` | no-op — Tk는 이미 포인트 단위 |
| `hide_window_from_taskbar` | no-op — 맥은 프로세스당 Dock 타일 1개 |
| `get_desktop_icon_positions` | 기본 비활성 (아래 참조) |

**바탕화면 아이콘만 기본 꺼짐**입니다. 맥에는 Finder를 AppleScript로 조종하는 것 말고는
아이콘 위치를 읽을 방법이 없는데, 첫 호출 시 자동화 권한 프롬프트가 뜨고 응답할 때까지
블로킹됩니다. 타이머 콜백에서 할 짓이 아니라서요.
`PIKAPET_DESKTOP_ICONS=1`로 켤 수 있고, 결과는 캐시돼 프롬프트가 한 번만 뜹니다.

실측 확인 (듀얼 1920×1080):
```
virtual screen : (0, 0, 3840, 1080)
secondary      : (1920, 0, 1920, 1080)
dock (taskbar) : (1920, 991, 3840, 1080)     # Dock이 두 번째 화면에 있는 구성
ledges         : 9개 (다른 앱 창 윗변)
```

### AppKit 콜백에서 Tcl을 부르면 안 되는 이유

Tk의 mainloop가 macOS 런루프를 돌리기 때문에, NSView의 마우스 핸들러나 NSTimer
타깃은 **`Tcl_DoOneEvent` 안에서** 실행됩니다. 그 자리에서 `event_generate` 같은
Tcl 호출을 하면 Python thread state가 떨어져 나가고, 다음 `after` 타이머가

    Fatal Python error: PyEval_RestoreThread: ... the current Python thread state is NULL

로 프로세스를 abort시킵니다. 드문 경합이 아니라 몇 초 안에 재현됩니다 — 격리
실험 2/2 사망, 실제 앱 2/2 사망. 그래서 `overlay.py`의 마우스 핸들러는 deque에만
넣고, 이미 Tcl 컨텍스트인 `_Manager.tick`(16 ms)이 꺼내서 실제 Tk 이벤트를
만듭니다.

### Windows 화면과 어긋나던 네 가지

전부 Tk aqua가 Windows의 Tk와 다르게 굴어서 생긴 것이고, 전부 런처에서
고쳤습니다. 게임 바이트코드는 건드리지 않았습니다.

**(a) 장식을 뗐다 붙인 창은 다시 못 움직인다.** aqua의 Tk는
`overrideredirect(True)`로 장식을 떼어낸 창에서 그것을 다시 꺼도 NSWindow의
styleMask를 복원하지 않습니다. 실측: styleMask 78 → 14로 갈 뿐 titled 비트가
돌아오지 않고, `withdraw()`/`deiconify()`로 다시 매핑해도 마찬가지입니다.
그러면 타이틀바도 없고 게임이 compact 창에 걸어두는 드래그 바인딩도 없는 창이
되어 **아예 잡을 곳이 없습니다**. 로켓단 습격에서 "화면 키우기"를 누르면 정확히
그 상태가 됩니다. `install_titlebar_restore()`가 `wm_overrideredirect(False)`
뒤에 styleMask를 직접 복원합니다 (14 → 15, titled).

**(b) `⚔`가 `×`로 보인다.** macOS 시스템 폰트에는 U+2694의 쓸 만한 텍스트
글리프가 없습니다. Tk는 이걸 두부 박스로도 안 그리고 — 그랬으면 눈에 띄었을
텐데 — 머리카락처럼 가는 글리프로 떨어뜨려서, 게임이 쓰는 9px에서는
`⚔ Fight` 버튼이 `× Fight`로 보입니다. VS16(U+FE0F)을 붙이면 이모지 표현이
되어 Apple Color Emoji로 폴백합니다. 대상을 `⚔` 하나로 좁힌 근거는 실측입니다:
게임 문자열에 쓰인 기호 134종을 전부 9px bold로 그려 잉크 픽셀을 셌고, 망가지는
것은 `⚔` 뿐이었습니다 (잉크 20, VS16을 붙이면 65). `▶ ↩ ⚙ ⬇` 같은 것들은
모노크롬으로 멀쩡히 나오므로 건드리지 않습니다. 훅은
`tkinter.Misc._options` 한 군데에 겁니다 — `Widget.__init__`, `Misc.configure`,
`Menu.add`, `Canvas._create`가 전부 그 길목을 지나므로 위젯 종류마다 훅을 걸
필요가 없습니다.

**(c) 버튼 배경색이 통째로 무시된다.** aqua의 `tk.Button`은 `-background`를
**완전히 무시합니다**. 네이티브 버튼을 그리고 색은 버립니다.
`bd=0`, `relief=flat`, `highlightthickness=0`을 어떻게 섞어도 같고
(여섯 조합을 그려서 확인), `highlightbackground`는 버튼 둘레에 얇은 테를 두를
뿐 버튼 면은 여전히 흰색입니다. 게임의 버튼 181개 중 색을 주는 건 **8개뿐**이고
7개가 같은 노란색 `#ffd54a` 액션 버튼입니다(야생 포켓몬 토스트의 `⚔ Fight`,
`⚔ 스테이지 N 도전!`, 선물 `🎁 보러가기`, 확인 버튼들). 그 8개만
`MacColorButton`(배경색을 실제로 칠하는 `tk.Label` 기반)으로 바꾸고 나머지
173개는 진짜 `tk.Button`으로 둡니다. 게임은 위젯에 `isinstance`도
`winfo_class`도 쓰지 않으므로(disasm으로 확인) 바꿔치기가 보이지 않습니다.
여백은 네이티브 버튼과 요청 크기가 **픽셀 단위로 같아지도록** 맞췄습니다
(padx 17 / pady 5, 여섯 케이스에서 오차 0). 안 맞추면 색 버튼만 14×2 px 작아서
옆에 선 네이티브 버튼과 줄이 어긋납니다.

**(d) Dock 아이콘이 펫으로 바뀐다.** 게임은 시작하면서
`win.iconphoto(True, <펫 스프라이트>)`를 부릅니다(`_setup_taskbar_icon`,
pet.py:17476). Windows에서는 그 창의 작업표시줄 아이콘을 펫으로 바꾸는 의도한
동작이지만, aqua에서는 **앱 아이콘 자체**를 갈아치워서 Dock의 PikaPet이
몬스터볼에서 파이리가 됩니다. `-default`를 떼는 것으로는 못 막습니다 — 실측:

```
setApplicationIconImage_(447px)  ->  앱 아이콘 447x447
iconphoto(False, 32px)           ->  앱 아이콘 32x32   <- default 없이도 바뀐다
iconphoto(True,  32px)           ->  앱 아이콘 32x32
```

macOS 창에는 애초에 타이틀바 아이콘이 없으므로(문서 창의 프록시 아이콘을 빼면)
이 호출이 창에 해주는 일은 없습니다. 그래서 원본은 그대로 부르고 직후에 앱
아이콘만 되돌립니다.

### 다크 모드에서 깨지던 두 가지

macOS의 시스템 색은 다크 모드를 따라갑니다. 게임은 Windows의 밝은 기본값을
전제로 색을 고르므로 다크 모드에서 두 군데가 깨집니다. 둘 다
`install_contrast_fix()`가 메웁니다.

**(a) 위젯마다 검은 테두리.** aqua 위젯은 네이티브 베젤 바깥 영역을
`-highlightbackground`로 칠하는데, 기본값이 `systemWindowBackgroundColor` —
다크 모드에서 거의 검정입니다. 그래서 크림색(`#fff6e0`) 전투 창 위의 버튼마다
검은 사각형이 둘러집니다. 실측하면 위젯 경계에 `#1c1c1c`가 4px, 그 안쪽이 흰
베젤입니다. 옵션 조합을 그려서 비교했을 때 `bg`만 준 버튼은 검은 테가 남고
`highlightbackground`를 준 버튼만 그 테가 해당 색으로 바뀌었습니다. 부모의
배경색을 넣어주면 배경에 묻습니다.

**(b) 밝은 배경 위의 흰 글자.** `Label`의 기본 `fg`는 `systemTextColor`라
다크 모드에서 흰색입니다. 게임이 `bg`만 주고 `fg`를 안 준 라벨은 크림색 위의
흰 글자가 되어 사실상 안 보입니다. 실측: `야생 ？？？ Lv.2`의 글자가
(255,252,245), 배경이 (255,244,221). 바로 아래 `내 파이리`는 `fg`를 명시해서
멀쩡합니다.

`Button`에는 (b)를 적용하지 않습니다. aqua가 Button의 기본 글자색을 `Black`
으로 고정해 두고 베젤도 항상 밝아서, 어두운 창에 놓였다고 흰 글자를 주면 흰
베젤 위의 흰 글자가 됩니다. `Menu`에는 `-highlightbackground` 자체가 없어서
주면 위젯 생성이 실패합니다.

### 펫이 가만히 있는 이유

전투 창이 열려 있으면 펫은 움직이지 않습니다. `_update_walk`(pet.py:9279)의
첫 줄이 `if self.battle_open: return` 입니다. 반면 `Companion._step_free_roam`
에는 그 검사가 없어서 **동료만 계속 돌아다닙니다.** 그래서 펫이 멈춘 것처럼
보입니다. 게임 자체 동작이고 macOS 포팅과 무관합니다.

`open_battle`이 플래그를 세우면서 `WM_DELETE_WINDOW` → `_close_battle`을
등록하고 거기서 플래그가 풀립니다. `install_titlebar_restore()`가 붙여주는
네이티브 닫기 버튼도 그 경로를 타므로, 창을 닫으면 펫이 다시 움직입니다.

### 배포와 버전

저장소가 공개라 **GitHub Releases**가 배포처입니다. 파일당 2 GB까지라 115 MB
DMG에 여유가 있고, 받는 사람이 GitHub 계정 없이 받을 수 있고, 앱이 직접 읽을 수
있는 `releases/latest` API를 익명으로 제공합니다.

**버전은 태그 한 곳에만 적습니다.** 예전에는 `make_dmg.sh`에 손으로 적혀 있었고,
그래서 태그가 0.0.2인데 빌드된 앱은 0.0.1이라고 말하는 상태가 됐습니다. 지금은
`git describe --tags --abbrev=0`으로 읽어 `PIKAPET_VERSION`으로 넘기고, 그것이
`CFBundleShortVersionString`이 되며, `macupdate.app_version()`이 번들에서 그
값을 다시 읽습니다. 태그 → DMG 이름 → Info.plist → 업데이트 비교가 한 줄입니다.

HEAD가 태그 위에 정확히 있지 않으면 릴리스가 아니므로 `PikaPet-<버전>+<sha>.dmg`
로 이름이 붙습니다. 열어보지 않아도 배포본이 아님이 보이게. Info.plist에는
숫자만 들어갑니다 — `CFBundleShortVersionString`은 `x.y.z` 형태여야 합니다.

**태그는 `main`에만** 답니다. 지금 `0.0.1`은 develop 머지 커밋에, `0.0.2`는
main에 붙어 있어서 어느 브랜치에서 빌드하느냐에 따라 `git describe` 답이
달라집니다. 그리고 태그를 단 뒤에는 main을 develop으로 되돌려 받아야 합니다 —
지금 develop이 main보다 뒤라 다음 feature 브랜치가 옛 베이스에서 갈라집니다.

```
develop -> main 머지,  git tag 0.0.3,  git push --tags
tools/make_dmg.sh                      # 태그를 읽는다
dist/PikaPet-0.0.3.dmg 를 릴리스에 업로드
git checkout develop && git merge main
```

받는 쪽의 진짜 장벽은 다운로드가 아니라 **Gatekeeper**입니다. ad-hoc 서명이면
시스템 설정 > 개인정보 보호 및 보안 > "그래도 열기"를 눌러야 하고, macOS 15부터는
우클릭 > 열기로도 안 됩니다. Developer ID 서명 + 공증만이 이 단계를 없앱니다.

### 새 버전 확인

`run/macupdate.py`가 시작할 때 GitHub 릴리스 API를 한 번 읽고, 번들 버전보다
높으면 알림을 띄우고 메뉴 바 ◓ 맨 위에 "⬇ 새 버전 받기"를 붙입니다.

`--- 왜 SSE/WebSocket이 아닌가 ---`

둘 다 24시간 떠 있는 서버가 전제인데 이 앱에는 그런 게 없습니다 (PvP의 `ws://`
주소는 사용자가 직접 넣는 ngrok 주소입니다). 얻는 것은 지연 시간인데, "새 버전이
나왔다"는 사건은 잘해야 주 1회라 그 하나를 초 단위로 받으려고 소켓을 며칠씩
붙들고 잠자기·네트워크 전환마다 재연결하는 것은 값이 안 맞습니다. HTTPS GET
한 번이면 서버도 토큰도 필요 없습니다.

지키는 규칙 넷:

- **네트워크는 데몬 스레드, Tk는 큐를 통해서.** 스레드에서 Tcl을 건드리면
  프로세스가 abort합니다(아래 참조). overlay/mactray와 같은 방식입니다.
  실측: 스레드가 돈 뒤에도 `after` 타이머가 168회 정상 동작.
- **조용히 실패합니다.** 오프라인이든 API가 막혔든 릴리스가 0개(현재 상태, 404)든
  앱은 그냥 뜹니다.
- **소스 실행에서는 꺼집니다.** `PIKAPET_UPDATE_CHECK=1`로 켜고 `0`으로 끕니다.
- **번들일 때만 버전을 읽습니다.** 소스에서 `NSBundle.mainBundle()`은 Homebrew의
  `Python.app`이라 버전이 `3.14.7`로 나옵니다. 실측으로 확인했고, 그걸 앱 버전으로
  쓰면 비교가 통째로 엉뚱해집니다.

### 배포용 DMG 만들기

```bash
tools/make_dmg.sh                  # dist/PikaPet-0.0.1.dmg (아직 베타)
tools/make_dmg.sh --version 0.1.0  # 버전 지정
tools/make_dmg.sh --app-only       # .app 까지만
```

Python 3.14와 Tcl/Tk, 에셋 123 MB까지 전부 품은 `PikaPet.app`(173 MB)을 만들어
압축 디스크 이미지(114 MB)로 묶습니다. 받는 쪽에 아무것도 설치돼 있지 않아도
됩니다. 빌드용 venv를 `build/` 에 따로 만들어 쓰므로 실행용 `.venv` 는 건드리지
않습니다.

**PyInstaller가 이 앱의 원래 포장 방식입니다.** `PikaPet.exe`가 PyInstaller
onefile 번들이었고, 그 분기가 바이트코드에 아직 살아 있습니다 — `sys.frozen`이
켜지면 pet.pyc가 에셋을 `sys._MEIPASS`에서 읽고 세이브를 `$APPDATA/PikaPet`에
씁니다(pet.py:33~50). 덕분에 소스 실행에서 `run/pet_state.json`에 중복 저장되던
것도 번들에서는 일어나지 않습니다.

**`pet.pyc`는 데이터 파일이라 PyInstaller가 그 안의 import를 못 봅니다.**
`tools/pikapet.spec`의 `hiddenimports`가 그 목록을 손으로 들고 있고,
`disasm/pet.dis.txt`의 `IMPORT_NAME` 전부에서 뽑은 것입니다. 게임에 import가
늘어나면 여기에 추가해야 하며, 빠지면 빌드가 아니라 실행 시점에 터집니다.

앱 아이콘은 `tools/make_icon.py`가 `tools/icon.png`(몬스터볼)에서 만듭니다.
원본은 알파가 없는 RGB라 공 바깥이 흰색인데, 그대로 쓰면 Dock에 흰 사각형이
붙습니다. 공이 캔버스에 정확히 내접해 있어서 원형 마스크로 잘라냅니다 —
흰색을 지우는 방식은 못 씁니다. 공 아래쪽 절반과 하이라이트도 흰색이라
같이 지워집니다.

Apple Developer 인증서가 없으면 ad-hoc 서명만 붙으므로, 다른 맥에서 처음 열 때
**우클릭 > 열기**가 필요합니다. 인증서가 있으면
`PIKAPET_SIGN_ID="Developer ID Application: ..." tools/make_dmg.sh` 로 서명합니다.

### 테스트

```bash
cd ~/projects/pikapet && .venv/bin/python -m unittest discover -s run -v
```

131개 전부 통과합니다. 실제로 두 건의 버그를 잡았습니다:
- `flash_taskbar`의 세 번째 인자는 `timeout`이 아니라 `interval_ms`였고,
  `acquire_single_instance_lock`엔 기본 mutex 이름 `PikaPetSingleInstanceMutex_do_bro2`가
  있었습니다 (원본 `winlayer.pyc`와 시그니처를 대조하는 테스트가 잡아냄)
- Dock 탐지가 `screens()[0]`만 보느라, **Dock이 두 번째 화면에 있는** 이 장비 구성에서
  `None`을 반환했습니다

## 4. 설치와 실행

설치 스크립트가 파이썬·의존성·에셋 링크를 모두 처리합니다. 다시 실행해도 안전합니다.

**macOS**

```bash
./install.sh          # Homebrew 의존성 + .venv + 검증
./run/pikapet.sh
```

**Windows**

```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
run\pikapet.bat       # 콘솔 없이 실행, --debug 를 붙이면 콘솔 유지
```

펫을 **우클릭**하면 전체 메뉴가 나옵니다.

venv는 리포지터리 안 `.venv`에 만들어지고(재부팅에도 유지됨), `PIKAPET_VENV`로 다른
위치를 지정할 수 있습니다. 환경이 이상하면 진단부터 돌려보세요:

```bash
.venv/bin/python tools/doctor.py            # Windows: .venv\Scripts\python.exe tools\doctor.py
```

### 플랫폼별로 다른 점

`pet.pyc`는 **Python 3.14 바이트코드**라 버전이 협상 대상이 아닙니다. 다른 버전에서는
import 단계에서 실패하므로 두 설치 스크립트 모두 이걸 먼저 확인합니다.

| | macOS | Windows |
|---|---|---|
| 진입점 | `run/pikapet_mac.py` (패치 5종 적용 후 `pet.pyc` 로드) | `run/pet.pyc` 직접 실행 |
| 플랫폼 계층 | `run/maclayer.py` | `run/winlayer.pyc` (원본, `ctypes`만 사용) |
| tkinter | `python-tk@3.14` 별도 설치 필요 | python.org 설치본에 포함 |
| 추가 의존성 | pyobjc (requirements.txt에 마커로 분리) | 없음 |

Windows에서 특히 주의할 점은 **에셋 링크**입니다. `run/assets`, `run/assets_v3`,
`run/assets_v4`, `run/badges_trainer`는 git 심링크로 커밋돼 있는데, Windows 기본값인
`core.symlinks=false`에서는 `../assets` 같은 경로가 담긴 **텍스트 파일**로 체크아웃됩니다.
`pet.pyc`는 에셋을 자기 디렉터리 기준으로 찾으므로 이 상태면 스프라이트가 하나도 안 보입니다.
`install.ps1`이 이걸 감지해서 **junction**으로 바꿔줍니다(디렉터리 심링크와 달리 관리자
권한이나 개발자 모드가 필요 없습니다).

## 5. 디렉터리 구성

```
run/                 macOS 실행 환경
  pikapet.sh           실행 스크립트
  pikapet_mac.py       런처 — 원본 바이트코드에 런타임 패치 5종 적용
  overlay.py           스프라이트를 그리는 네이티브 AppKit 창
  maclayer.py          winlayer의 macOS 구현 (Quartz/AppKit)
  test_maclayer.py     계약 테스트 34개
  test_overlay.py      오버레이 추적 로직 테스트 17개
  test_macui.py        글리프 보정 / 색 버튼 / 대비 보정 테스트 45개
  macupdate.py         새 버전 확인 (GitHub Releases)
  test_macupdate.py    업데이트 확인 테스트 28개
  mactray.py           트레이 전용 기능을 되살린 메뉴 바 항목
  macnotify.py         알림 (UN 우선, osascript 폴백)
  pet.pyc / winlayer.pyc / spriteanim.pyc
bytecode/            원본 바이트코드
src/decompiled/      함수/메서드별 디컴파일 903개 + _INDEX.txt
src/winlayer.py      winlayer 전체 디컴파일
disasm/              CPython 3.14 dis 기반 전체 디스어셈블리 (100% 정확)
tools/               분해·디컴파일 도구 일체
assets*/             원본 에셋 123 MB
```

### 디컴파일 품질에 대한 주의

pycdc(Decompyle++)는 Python 3.13까지만 지원해서 3.14 지원을 직접 추가했습니다
(`tools/pycdc-python314.patch`, 692줄). 추가한 것:

- 3.14 opcode 맵 (`LOAD_SMALL_INT`, `LOAD_FAST_BORROW`, `NOT_TAKEN`, `POP_ITER`,
  `LOAD_COMMON_CONSTANT`, `LOAD_SPECIAL` 등)
- `CALL_KW`, `MAP_ADD`(딕셔너리 컴프리헨션), `SET_ADD`, `DICT_UPDATE`/`DICT_MERGE`,
  `FORMAT_SIMPLE`/`FORMAT_WITH_SPEC`(f-string), `LOAD_SUPER_ATTR`, `CALL_FUNCTION_EX`,
  `STORE_FAST_STORE_FAST` 등 미구현 opcode 핸들러
- marshal `TYPE_SLICE` (`':'`) — 3.14에서 slice 상수가 marshal 대상이 됨
- **inline cache 건너뛰기** — 3.14가 `POP_JUMP_IF_*`에 캐시를 추가해서
  상대 점프 기준점이 밀림. 이걸 안 고치면 모든 if문 본문이 한 명령어씩 어긋남

**남은 한계**: Python 3.11+ 는 예외 범위를 exception table로 표현하고 핸들러를 함수
끝에 배치하는데, pycdc는 try 블록의 끝을 핸들러 주소로 잘못 잡습니다. 그래서
**try/except가 있는 함수(전체의 약 35%)는 try 이후 코드가 깨집니다** —
`for None in (...)`, `'' = None`, 엉뚱한 `continue` 같은 형태로 나타납니다.
이건 pycdc의 구조적 한계이고 제가 새로 만든 버그가 아닙니다.

해당 함수는 `disasm/`의 디스어셈블리를 보세요. 그쪽은 CPython 자체 `dis`라 100% 정확합니다.
`src/decompiled/_INDEX.txt`에 함수별 소스 라인과 상태가 정리돼 있습니다.

## 6. 남은 것

포팅은 끝났지만 직접 눈으로 확인해볼 것들:

- **알림 센터** — `MacTray.notify()`는 `osascript`로 알림을 띄웁니다. 시스템 설정에서
  알림 권한을 한 번 허용해야 보입니다.

  **배너 클릭이 스크립트 편집기로 가는 것은 서명 문제입니다.** macOS는 ad-hoc
  서명 앱에 알림 권한을 전혀 주지 않습니다 — 프롬프트도 뜨지 않고 알림 설정에도
  등록되지 않으며 `UNErrorDomain Code=1`만 돌아옵니다(`dist/`, `~/Applications`
  동일). 그래서 배포 빌드는 늘 osascript로 떨어지고, 그 배너의 소유자는 스크립트
  편집기입니다. `run/macnotify.py`에 모던 `UNUserNotificationCenter` 경로와 클릭
  델리게이트가 이미 들어 있으니, Developer ID로 서명하면
  (`PIKAPET_SIGN_ID=...`) 그쪽으로 전환되고 배너를 누르면 야생 포켓몬 창이
  열립니다.

  `NSUserNotificationCenter`를 1순위로 쓰지 마세요. macOS 26에서 그 프레임워크는
  알림을 받아 `deliveredNotifications()` 목록에만 넣고 배너를 띄우지 않으며,
  예외도 내지 않습니다. "예외가 없으면 성공"으로 처리하면 알림이 전부 조용히
  사라집니다. 배너 소유자가 스크립트 편집기가 되는 단점은 남지만, 메뉴 바 ◓
  항목이 있어 알림이 안내하는 "트레이 아이콘을 클릭"을 실제로 따라갈 수 있습니다.
- **미확인 영역** — 전투 창, PvP(websockets), 미니게임, 오목은 아직 실행해보지 않았습니다.
  전부 순수 tkinter/Python이라 문제될 이유는 없지만 검증은 안 된 상태입니다.

### 나중에 할 만한 것

- **`.app` 번들로 패키징** — py2app이나 PyInstaller로 묶으면 더블클릭 실행이 되고,
  Dock 아이콘/알림 권한도 PikaPet 이름으로 제대로 잡힙니다.
- **바탕화면 아이콘 위 착지** — `PIKAPET_DESKTOP_ICONS=1`로 켜지만, Finder가 돌려주는
  좌표가 화면 좌표와 맞는지 검증이 필요합니다.
- **`pet.py` 소스 완전 복원** — try/except 있는 함수 약 420개를 디스어셈블리 보고
  손봐야 합니다. 런타임 패치로 충분한 한 굳이 할 이유는 없습니다.
