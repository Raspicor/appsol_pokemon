"""새 버전을 앱이 직접 받아서 스스로 교체한다.

`macupdate.py` 는 "새 버전이 있는가"만 답한다. 이 파일은 그 다음, 실제로
바꿔치우는 일을 한다.

## 왜 이게 되는가 (전부 실측)

  * `/Applications` 는 `drwxrwxr-x root:admin` 이고 설치한 사용자가 admin 이라
    **관리자 암호가 필요 없다.** 번들 자신도 사용자 소유다.
  * urllib 로 받은 파일에는 `com.apple.provenance` 만 붙고
    **`com.apple.quarantine` 은 붙지 않는다.** 브라우저로 받으면 Chrome 이
    quarantine 을 붙이기 때문에 사용자가 시스템 설정에서 '그래도 열기'를
    눌러야 하는데(현재 설치본에 실제로 붙어 있다), 앱이 직접 받으면 그 단계가
    사라진다. 자동 업데이트가 수동보다 **덜** 번거로운 이유가 이것이다.
  * `ditto` 는 ad-hoc 서명을 보존한다 -- 복사본이
    `codesign --verify --deep --strict` 를 통과한다. `cp -R` 는 확장 속성을
    흘리므로 쓰지 않는다.
  * `hdiutil attach -nobrowse -readonly` 도 권한 없이 된다.

## 실행 중인 번들은 스스로를 교체할 수 없다

그래서 교체는 **분리된 셸 스크립트**가 한다. 앱이 끝나기를 기다렸다가, 기존
번들을 옆으로 치우고, 새 번들을 제자리에 놓고, 검증하고, 어긋나면 되돌린다.
성공하면 다시 실행한다. 스크립트는 `start_new_session=True` 로 띄워서 우리가
죽어도 살아남는다.

**어느 단계에서 실패해도 기존 앱이 남는다.** 그게 이 파일의 유일한 불변식이다.
그러니 새 번들을 검증하기 전에는 기존 것을 절대 지우지 않는다.

## 스레드 주의

네트워크와 `hdiutil`/`ditto` 는 데몬 스레드에서 돈다. 그 스레드에서 Tk를
건드리면 프로세스가 abort한다 (overlay.py 의 모듈 독스트링 참고). 그래서
진행률과 결과는 큐에만 넣고 Tk 타이머가 꺼낸다. macupdate 와 같은 방식이다.
"""

import collections
import json
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request

OWNER_REPO = "Raspicor/appsol_pokemon"
API_LATEST = f"https://api.github.com/repos/{OWNER_REPO}/releases/latest"
API_BY_TAG = f"https://api.github.com/repos/{OWNER_REPO}/releases/tags/"

# 내려받기 한 덩어리. 115MB 를 256KB 씩 나누면 진행률이 450번 정도 갱신된다 --
# 눈에 부드럽고 큐가 넘치지도 않는다.
CHUNK = 256 * 1024

# 응답을 기다리는 시간. 내려받기 자체는 이것과 무관하게 오래 걸려도 된다.
CONNECT_TIMEOUT_SEC = 15

# 진행률/결과를 꺼내보는 주기.
DRAIN_MS = 120

LOG_PATH = os.path.expanduser(
    "~/Library/Application Support/PikaPet/update.log")


# --------------------------------------------------------------------------
# 어디에 설치돼 있는가

def bundle_path():
    """실행 중인 .app 의 경로. 번들이 아니면 None.

    PyInstaller 번들에서 `sys.executable` 은
    `/Applications/PikaPet.app/Contents/MacOS/PikaPet` 이다. 세 단계 위가
    번들이다. 구조를 확인하고서야 돌려준다 -- 엉뚱한 경로를 지우는 일은
    절대 없어야 한다.
    """
    if not getattr(sys, "frozen", False):
        return None
    try:
        macos = os.path.dirname(os.path.abspath(sys.executable))   # Contents/MacOS
        contents = os.path.dirname(macos)                          # Contents
        app = os.path.dirname(contents)                            # X.app
        if (app.endswith(".app")
                and os.path.basename(contents) == "Contents"
                and os.path.isfile(os.path.join(contents, "Info.plist"))):
            return app
    except Exception:
        pass
    return None


def can_replace(app=None):
    """이 자리에서 번들을 바꿔칠 수 있는가. `(가능한가, 이유)`.

    이유는 사람에게 보여줄 문장이다. 못 하는 경우에도 기존 방식(브라우저로
    내려받기)으로 넘어가면 되므로, 여기서는 판단만 하고 아무것도 하지 않는다.
    """
    app = app or bundle_path()
    if app is None:
        return False, "설치된 앱이 아니라 소스에서 실행 중입니다."
    if app.startswith("/Volumes/"):
        # dmg 안에서 그냥 실행한 경우. 읽기 전용이라 교체할 수 없다.
        return False, "PikaPet을 먼저 Applications 폴더로 옮겨주세요."
    parent = os.path.dirname(app)
    if not os.access(parent, os.W_OK):
        return False, f"{parent} 에 쓸 수 없습니다."
    if not os.access(app, os.W_OK):
        return False, f"{app} 에 쓸 수 없습니다."
    return True, ""


def installed_version(app=None):
    """설치된 번들의 버전. 못 읽으면 None."""
    app = app or bundle_path()
    if app is None:
        return None
    try:
        with open(os.path.join(app, "Contents", "Info.plist"), "rb") as f:
            return plistlib.load(f).get("CFBundleShortVersionString")
    except Exception:
        return None


# --------------------------------------------------------------------------
# 무엇을 받을 것인가

def find_asset(tag=None, timeout=CONNECT_TIMEOUT_SEC, opener=None):
    """릴리스에서 dmg 자산을 찾는다. `(주소, 크기, 이름)` 또는 None.

    `tag` 를 주면 그 릴리스를, 없으면 최신을 본다. dmg 가 여러 개면 첫 번째를
    쓴다 -- 이 저장소는 릴리스마다 dmg 하나다.
    """
    url = (API_BY_TAG + tag) if tag else API_LATEST
    try:
        request = urllib.request.Request(
            url, headers={"Accept": "application/vnd.github+json",
                          "User-Agent": "PikaPet"})
        open_url = opener or urllib.request.urlopen
        with open_url(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        for asset in payload.get("assets") or ():
            name = asset.get("name") or ""
            if name.endswith(".dmg") and asset.get("browser_download_url"):
                return (asset["browser_download_url"],
                        int(asset.get("size") or 0), name)
    except Exception:
        pass
    return None


# --------------------------------------------------------------------------
# 받고, 검증하고, 옮겨 놓기

def download(url, dest, size=0, on_chunk=None, cancel=None,
             timeout=CONNECT_TIMEOUT_SEC, opener=None):
    """`url` 을 `dest` 로 내려받는다. 받은 바이트 수를 돌려준다.

    `on_chunk(받은 바이트, 전체 바이트)` 는 덩어리마다 불린다. **네트워크
    스레드에서 불리므로 Tk를 건드려선 안 된다.**

    `cancel` 은 `threading.Event` 다. set 되면 받다 말고 KeyboardInterrupt 가
    아니라 `Cancelled` 를 낸다 -- 취소는 오류가 아니라서 위쪽에서 구분해야 한다.
    """
    request = urllib.request.Request(url, headers={"User-Agent": "PikaPet"})
    open_url = opener or urllib.request.urlopen
    got = 0
    with open_url(request, timeout=timeout) as response, open(dest, "wb") as out:
        total = size or int(response.headers.get("Content-Length") or 0)
        while True:
            if cancel is not None and cancel.is_set():
                raise Cancelled()
            chunk = response.read(CHUNK)
            if not chunk:
                break
            out.write(chunk)
            got += len(chunk)
            if on_chunk is not None:
                on_chunk(got, total)
    return got


class Cancelled(Exception):
    """사용자가 취소했다. 오류가 아니다."""


def _run(argv, timeout=180):
    """조용히 실행하고 `(성공했나, 출력)`. 예외를 내지 않는다."""
    try:
        done = subprocess.run(argv, capture_output=True, text=True,
                              timeout=timeout)
        return done.returncode == 0, (done.stdout or "") + (done.stderr or "")
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def verify_bundle(app, expected_version=None):
    """새 번들이 정말 쓸 만한가. `(괜찮은가, 이유)`.

    두 가지를 본다. 버전이 기대한 것과 같은가 -- 엉뚱한 릴리스를 받아놓고
    교체하면 되돌릴 근거가 없다. 그리고 서명이 온전한가 -- ad-hoc 이라
    신원은 확인할 수 없지만, 번들이 전송 중에 깨졌는지는 잡을 수 있다.
    """
    if not os.path.isdir(app):
        return False, "새 번들이 없습니다."
    got = installed_version(app)
    if expected_version and got != expected_version:
        return False, f"버전이 맞지 않습니다: {got} (기대한 것 {expected_version})"
    ok, output = _run(["codesign", "--verify", "--deep", "--strict", app])
    if not ok:
        return False, f"서명 검증에 실패했습니다: {output.strip()[:200]}"
    return True, ""


def stage_from_dmg(dmg, workdir, expected_version=None):
    """dmg 를 마운트해 .app 을 `workdir` 로 꺼내 놓는다. 꺼낸 경로를 돌려준다.

    마운트는 반드시 풀고 나온다 -- 실패해도 `/Volumes` 에 쓰레기를 남기지
    않는다. `ditto` 를 쓰는 이유는 확장 속성과 서명을 보존하기 때문이다.
    """
    mount = os.path.join(workdir, "mnt")
    os.makedirs(mount, exist_ok=True)
    ok, output = _run(["hdiutil", "attach", dmg, "-nobrowse", "-readonly",
                       "-mountpoint", mount])
    if not ok:
        raise RuntimeError(f"디스크 이미지를 열 수 없습니다: {output.strip()[:200]}")
    try:
        apps = [n for n in sorted(os.listdir(mount)) if n.endswith(".app")]
        if not apps:
            raise RuntimeError("디스크 이미지 안에 앱이 없습니다.")
        staged = os.path.join(workdir, apps[0])
        ok, output = _run(["ditto", os.path.join(mount, apps[0]), staged])
        if not ok:
            raise RuntimeError(f"새 앱을 꺼낼 수 없습니다: {output.strip()[:200]}")
    finally:
        _run(["hdiutil", "detach", mount, "-quiet"], timeout=60)
    good, reason = verify_bundle(staged, expected_version)
    if not good:
        raise RuntimeError(reason)
    return staged


# --------------------------------------------------------------------------
# 교체는 우리가 죽은 뒤에 일어난다

# 스크립트가 지워도 되는 작업 폴더의 표식. 이 이름이 안 들어 있으면 지우지
# 않는다 -- 생성한 스크립트 안의 rm -rf 는 경로를 의심해야 한다.
WORK_MARK = "pikapet-update-"

SWAP_SCRIPT = r"""#!/bin/sh
# PikaPet 업데이트 적용. 앱이 끝난 뒤에 돌아간다.
#
# 불변식: 새 번들을 검증하기 전에는 기존 것을 지우지 않는다. 어느 단계에서
# 실패해도 기존 앱이 제자리에 남아야 한다.
set -u

PID="$1"; NEW="$2"; TARGET="$3"; LOG="$4"; WORK="$5"

log() { printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG" 2>/dev/null; }

cleanup_work() {
  # 대상이 작업 폴더 안에 있으면 손대지 않는다. 정상적인 설치에서는 일어나지
  # 않지만, 여기서 틀리면 앱을 지우게 된다.
  case "$TARGET" in
    "$WORK"/*)
      log "작업 폴더 정리 건너뜀 (대상이 그 안에 있습니다): $WORK"
      return ;;
  esac
  case "$WORK" in
    *__MARK__*) rm -rf "$WORK" ;;
    *) log "작업 폴더 정리 건너뜀 (예상하지 않은 경로): $WORK" ;;
  esac
}

log "시작: pid=$PID target=$TARGET"

# 앱이 끝나기를 기다린다. 60초를 넘기면 포기한다 -- 억지로 죽이면 세이브가
# 깨질 수 있고, 업데이트는 다음 기회에 하면 된다.
i=0
while kill -0 "$PID" 2>/dev/null; do
  i=$((i + 1))
  if [ "$i" -gt 120 ]; then
    log "실패: 앱이 60초 안에 끝나지 않았습니다. 교체하지 않습니다"
    cleanup_work
    exit 1
  fi
  sleep 0.5
done
log "앱 종료 확인"

BACKUP="$TARGET.pikapet-old"
rm -rf "$BACKUP"

if [ -e "$TARGET" ]; then
  if ! mv "$TARGET" "$BACKUP"; then
    log "실패: 기존 번들을 옮길 수 없습니다"
    cleanup_work
    exit 1
  fi
fi

restore() {
  rm -rf "$TARGET"
  if [ -e "$BACKUP" ]; then
    mv "$BACKUP" "$TARGET" && log "되돌렸습니다" || log "되돌리기도 실패했습니다"
  fi
}

if ! ditto "$NEW" "$TARGET" 2>>"$LOG"; then
  log "실패: 새 번들 복사"
  restore
  cleanup_work
  exit 1
fi

if ! codesign --verify --deep --strict "$TARGET" 2>>"$LOG"; then
  log "실패: 교체한 번들의 서명 검증"
  restore
  cleanup_work
  exit 1
fi

VER=$(/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' \
        "$TARGET/Contents/Info.plist" 2>/dev/null)
log "성공: $TARGET 이 $VER 이 되었습니다"

rm -rf "$BACKUP"
cleanup_work

if ! open -a "$TARGET"; then
  log "경고: 다시 실행하지 못했습니다. 직접 열어주세요"
fi
"""


def write_swap_script(workdir):
    """교체 스크립트를 `workdir` 에 써 놓고 경로를 돌려준다."""
    path = os.path.join(workdir, "swap.sh")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SWAP_SCRIPT.replace("__MARK__", WORK_MARK))
    os.chmod(path, 0o755)
    return path


def launch_swap(script, new_app, target, workdir, pid=None):
    """교체 스크립트를 떼어내서 띄운다. Popen 을 돌려준다.

    `start_new_session=True` 가 핵심이다. 우리 프로세스 그룹에서 빠져나가야
    앱이 종료된 뒤에도 살아남는다.
    """
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    return subprocess.Popen(
        ["/bin/sh", script, str(pid or os.getpid()), new_app, target,
         LOG_PATH, workdir],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, start_new_session=True,
        close_fds=True)


# --------------------------------------------------------------------------
# Tk 쪽에서 쓰는 얼굴

class Result:
    """업그레이드 시도의 결과. 하나만 참이다."""

    def __init__(self, staged=None, error=None, cancelled=False):
        self.staged = staged
        self.error = error
        self.cancelled = cancelled

    @property
    def ok(self):
        return self.staged is not None


class Upgrade:
    """받아서 꺼내 놓기까지를 배경에서 한다. 교체는 아직 하지 않는다.

    `on_progress(받은 바이트, 전체 바이트)` 와 `on_done(Result)` 는 둘 다 Tk
    메인 스레드에서 불린다. 그래서 위젯을 건드려도 된다.

    교체를 여기서 하지 않는 이유: 앱을 끝내는 결정은 사용자에게 보여주고
    나서 해야 하고, 그건 Tk 쪽 일이다. 이 클래스는 '언제든 버려도 되는'
    단계까지만 진행한다.
    """

    def __init__(self, root, tag, on_progress=None, on_done=None,
                 find=None, fetch=None, stage=None):
        self.root = root
        self.tag = tag
        self.on_progress = on_progress
        self.on_done = on_done
        self.find = find or find_asset
        self.fetch = fetch or download
        self.stage = stage or stage_from_dmg
        self.events = collections.deque()
        self.cancel_flag = threading.Event()
        self.workdir = None
        self.done = False

    def start(self):
        thread = threading.Thread(target=self._work, name="pikapet-upgrade",
                                  daemon=True)
        thread.start()
        self._schedule()
        return thread

    def cancel(self):
        """받는 것을 그만둔다. 이미 끝났으면 아무 일도 없다."""
        self.cancel_flag.set()

    # -- 배경 스레드. Tcl 금지 ----------------------------------------------

    def _work(self):
        try:
            found = self.find(self.tag)
            if not found:
                self.events.append(("done", Result(
                    error="받을 파일을 찾을 수 없습니다.")))
                return
            url, size, name = found
            self.workdir = tempfile.mkdtemp(prefix=WORK_MARK)
            dmg = os.path.join(self.workdir, name)
            self.fetch(url, dmg, size=size,
                       on_chunk=lambda got, total: self.events.append(
                           ("progress", (got, total))),
                       cancel=self.cancel_flag)
            if self.cancel_flag.is_set():
                raise Cancelled()
            self.events.append(("stage", None))
            staged = self.stage(dmg, self.workdir, self.tag)
            try:
                os.remove(dmg)                  # 115MB 를 들고 있을 이유가 없다
            except OSError:
                pass                            # 정리 실패로 업그레이드를 버릴 이유는 없다
            self.events.append(("done", Result(staged=staged)))
        except Cancelled:
            self._discard()
            self.events.append(("done", Result(cancelled=True)))
        except Exception as exc:
            self._discard()
            self.events.append(("done", Result(
                error=f"{type(exc).__name__}: {exc}")))

    def _discard(self):
        if self.workdir and WORK_MARK in self.workdir:
            shutil.rmtree(self.workdir, ignore_errors=True)
            self.workdir = None

    # -- Tk 타이머 안 --------------------------------------------------------

    def _schedule(self):
        try:
            self.root.after(DRAIN_MS, self.drain)
        except Exception:
            pass

    def drain(self):
        """쌓인 진행률과 결과를 처리한다."""
        last_progress = None
        finished = None
        while self.events:
            kind, value = self.events.popleft()
            if kind == "progress":
                last_progress = value           # 중간 것은 버린다. 최신만 보면 된다
            elif kind == "stage":
                last_progress = ("stage", None)
            elif kind == "done":
                finished = value
        try:
            if last_progress is not None and self.on_progress is not None:
                if last_progress[0] == "stage":
                    self.on_progress(None, None)
                else:
                    self.on_progress(*last_progress)
            if finished is not None:
                self.done = True
                if self.on_done is not None:
                    self.on_done(finished)
                return
        except Exception as exc:
            print(f"  업데이트 진행 표시 실패: {type(exc).__name__}: {exc}",
                  flush=True)
        if not self.done:
            self._schedule()


def apply_and_relaunch(staged, target=None, workdir=None):
    """교체 스크립트를 띄운다. 돌려준 뒤 **앱을 종료해야** 실제로 바뀐다.

    `(성공했나, 이유)`. 스크립트를 띄우는 것까지만 책임진다 -- 그 뒤의 일은
    우리가 죽은 다음에 일어나므로 여기서 결과를 알 수 없다. 남는 기록은
    update.log 다.
    """
    target = target or bundle_path()
    if target is None:
        return False, "설치된 앱을 찾을 수 없습니다."
    workdir = workdir or os.path.dirname(staged)
    try:
        script = write_swap_script(workdir)
        launch_swap(script, staged, target, workdir)
        return True, ""
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def log(message):
    """update.log 에 한 줄 남긴다. 실패해도 조용히 넘어간다."""
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"{stamp} {message}\n")
    except Exception:
        pass
