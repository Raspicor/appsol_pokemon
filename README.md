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

### 고친 것 네 가지

`run/pikapet_mac.py`가 원본 바이트코드를 로드한 뒤 런타임에 패치합니다.
**`pet.pyc`는 건드리지 않습니다** — 디컴파일 품질과 무관하게 동작하고, 원본과 어긋날 일도 없습니다.

| # | 문제 | 해결 |
|---|---|---|
| 1 | `winlayer`가 Win32 전용 | `sys.modules["winlayer"] = maclayer` — Quartz/AppKit 구현으로 교체 |
| 2 | `-transparentcolor`는 Windows 전용 | Tk 레벨에서 맥의 `-transparent`로 번역 |
| 3 | `MAGIC = '#ff00ff'` 컬러키 | `systemTransparent`로 교체 (지원 여부 실측 후에만) |
| 4 | pystray가 프로세스를 죽임 | `setup_tray`를 `MacTray` 스텁으로 교체 |

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

### 테스트

```bash
cd ~/projects/pikapet && /tmp/pikaenv/bin/python -m unittest discover -s run -v
```

34개 전부 통과합니다. 실제로 두 건의 버그를 잡았습니다:
- `flash_taskbar`의 세 번째 인자는 `timeout`이 아니라 `interval_ms`였고,
  `acquire_single_instance_lock`엔 기본 mutex 이름 `PikaPetSingleInstanceMutex_do_bro2`가
  있었습니다 (원본 `winlayer.pyc`와 시그니처를 대조하는 테스트가 잡아냄)
- Dock 탐지가 `screens()[0]`만 보느라, **Dock이 두 번째 화면에 있는** 이 장비 구성에서
  `None`을 반환했습니다

## 4. 실행 방법

```bash
brew install python@3.14 python-tk@3.14
python3.14 -m venv /tmp/pikaenv
/tmp/pikaenv/bin/pip install pillow numpy pystray websockets werkzeug \
    watchdog six colorama packaging threadpoolctl typing_extensions \
    charset_normalizer markupsafe
~/projects/pikapet/run/pikapet.sh
```

펫을 **우클릭**하면 전체 메뉴가 나옵니다. 다른 venv를 쓰려면 `PIKAPET_VENV`로 지정하세요.

## 5. 디렉터리 구성

```
run/                 macOS 실행 환경
  pikapet.sh           실행 스크립트
  pikapet_mac.py       런처 — 원본 바이트코드에 런타임 패치 4종 적용
  maclayer.py          winlayer의 macOS 구현 (Quartz/AppKit)
  test_maclayer.py     계약 테스트 34개
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

- **투명 배경** — `-transparent`가 켜진 건 확인했지만, 스프라이트 주변이 실제로 깨끗하게
  비치는지는 화면으로 봐야 합니다. 어색하면 `PetApp.build_menu`의 `🔆 창 투명도 복구`를
  눌러보세요.
- **알림 센터** — `MacTray.notify()`는 `osascript`로 알림을 띄웁니다. 시스템 설정에서
  알림 권한을 한 번 허용해야 보입니다.
- **미확인 영역** — 전투 창, PvP(websockets), 미니게임, 오목은 아직 실행해보지 않았습니다.
  전부 순수 tkinter/Python이라 문제될 이유는 없지만 검증은 안 된 상태입니다.

### 나중에 할 만한 것

- **`.app` 번들로 패키징** — py2app이나 PyInstaller로 묶으면 더블클릭 실행이 되고,
  Dock 아이콘/알림 권한도 PikaPet 이름으로 제대로 잡힙니다.
- **바탕화면 아이콘 위 착지** — `PIKAPET_DESKTOP_ICONS=1`로 켜지만, Finder가 돌려주는
  좌표가 화면 좌표와 맞는지 검증이 필요합니다.
- **`pet.py` 소스 완전 복원** — try/except 있는 함수 약 420개를 디스어셈블리 보고
  손봐야 합니다. 런타임 패치로 충분한 한 굳이 할 이유는 없습니다.
