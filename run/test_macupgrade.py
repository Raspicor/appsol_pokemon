"""macupgrade.py 테스트. 네트워크도 디스플레이도 쓰지 않는다.

여기서 지키려는 것은 하나로 요약된다: **어느 단계에서 실패해도 기존 앱이
제자리에 남아야 한다.** 업데이트가 실패하는 것은 불편이지만, 앱이 사라지는
것은 사용자의 손으로 복구할 수 없는 사고다.

교체 스크립트는 실제 셸로 돌린다. 되돌리기 로직이 이 파일에서 가장 중요한
부분인데, 그것을 파이썬으로 흉내 내서는 검증이 되지 않는다.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import macupgrade

# Request() 는 가짜 opener 를 쓰더라도 URL 문법은 검사한다.
URL = "https://example.invalid/PikaPet.dmg"


def make_app(path, version="0.0.1", executable=True):
    """최소한의 .app 을 만든다. 서명은 없다."""
    contents = os.path.join(path, "Contents")
    os.makedirs(os.path.join(contents, "MacOS"), exist_ok=True)
    with open(os.path.join(contents, "Info.plist"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
                '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
                '<plist version="1.0"><dict>'
                '<key>CFBundleShortVersionString</key>'
                f'<string>{version}</string>'
                '</dict></plist>\n')
    if executable:
        exe = os.path.join(contents, "MacOS", "PikaPet")
        with open(exe, "w", encoding="utf-8") as f:
            f.write("#!/bin/sh\nexit 0\n")
        os.chmod(exe, 0o755)
    return path


class FindingWhereWeAre(unittest.TestCase):
    def setUp(self):
        self.frozen = getattr(sys, "frozen", None)
        self.addCleanup(self._restore)

    def _restore(self):
        if self.frozen is None:
            if hasattr(sys, "frozen"):
                del sys.frozen
        else:
            sys.frozen = self.frozen

    def test_source_runs_have_no_bundle(self):
        if hasattr(sys, "frozen"):
            del sys.frozen
        self.assertIsNone(macupgrade.bundle_path())

    def test_a_source_run_cannot_replace(self):
        if hasattr(sys, "frozen"):
            del sys.frozen
        ok, reason = macupgrade.can_replace()
        self.assertFalse(ok)
        self.assertIn("소스", reason)

    def test_running_from_a_dmg_cannot_replace(self):
        # /Volumes 는 읽기 전용으로 마운트된 dmg 다. 여기서 교체를 시도하면
        # 실패하는데, 사용자에게는 'Applications 로 옮기세요'가 답이다.
        ok, reason = macupgrade.can_replace("/Volumes/PikaPet 0.0.6/PikaPet.app")
        self.assertFalse(ok)
        self.assertIn("Applications", reason)

    def test_an_unwritable_place_cannot_replace(self):
        ok, reason = macupgrade.can_replace("/System/PikaPet.app")
        self.assertFalse(ok)

    def test_a_writable_place_can_replace(self):
        base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, base, True)
        app = make_app(os.path.join(base, "PikaPet.app"))
        ok, reason = macupgrade.can_replace(app)
        self.assertTrue(ok, reason)


class ReadingVersions(unittest.TestCase):
    def test_the_version_comes_from_info_plist(self):
        base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, base, True)
        app = make_app(os.path.join(base, "PikaPet.app"), version="9.9.9")
        self.assertEqual(macupgrade.installed_version(app), "9.9.9")

    def test_a_broken_bundle_gives_none(self):
        base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, base, True)
        self.assertIsNone(macupgrade.installed_version(
            os.path.join(base, "없는것.app")))


class ChoosingTheAsset(unittest.TestCase):
    def opener(self, payload):
        class Response:
            def __init__(self, body):
                self.body = body

            def read(self):
                return self.body

            def __enter__(self):
                return self

            def __exit__(self, *exc):
                return False

        import json

        def open_url(request, timeout=None):
            return Response(json.dumps(payload).encode("utf-8"))
        return open_url

    def test_the_dmg_is_picked(self):
        found = macupgrade.find_asset(opener=self.opener({"assets": [
            {"name": "notes.txt", "browser_download_url": "u1", "size": 1},
            {"name": "PikaPet-0.0.6.dmg", "browser_download_url": "u2",
             "size": 120},
        ]}))
        self.assertEqual(found, ("u2", 120, "PikaPet-0.0.6.dmg"))

    def test_no_dmg_gives_none(self):
        self.assertIsNone(macupgrade.find_asset(
            opener=self.opener({"assets": [{"name": "a.zip",
                                            "browser_download_url": "u"}]})))

    def test_no_assets_gives_none(self):
        self.assertIsNone(macupgrade.find_asset(opener=self.opener({})))

    def test_a_network_failure_gives_none(self):
        def boom(request, timeout=None):
            raise OSError("offline")
        self.assertIsNone(macupgrade.find_asset(opener=boom))


class Downloading(unittest.TestCase):
    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.dest = os.path.join(self.base, "out.bin")

    def opener(self, body):
        class Response:
            def __init__(self):
                self.rest = body
                self.headers = {"Content-Length": str(len(body))}

            def read(self, n=None):
                if n is None:
                    chunk, self.rest = self.rest, b""
                else:
                    chunk, self.rest = self.rest[:n], self.rest[n:]
                return chunk

            def __enter__(self):
                return self

            def __exit__(self, *exc):
                return False

        return lambda request, timeout=None: Response()

    def test_the_body_lands_on_disk(self):
        body = b"x" * (macupgrade.CHUNK * 2 + 7)
        got = macupgrade.download(URL, self.dest, opener=self.opener(body))
        self.assertEqual(got, len(body))
        with open(self.dest, "rb") as f:
            self.assertEqual(f.read(), body)

    def test_progress_is_reported(self):
        body = b"y" * (macupgrade.CHUNK * 3)
        seen = []
        macupgrade.download(URL, self.dest, size=len(body),
                            on_chunk=lambda got, total: seen.append((got, total)),
                            opener=self.opener(body))
        self.assertEqual(seen[-1], (len(body), len(body)))
        self.assertTrue(all(t == len(body) for _, t in seen))

    def test_cancelling_raises_cancelled_not_an_error(self):
        # 취소는 오류가 아니다. 위쪽이 둘을 구분해서 다르게 보여준다.
        body = b"z" * (macupgrade.CHUNK * 4)
        flag = threading.Event()
        flag.set()
        with self.assertRaises(macupgrade.Cancelled):
            macupgrade.download(URL, self.dest, cancel=flag,
                                opener=self.opener(body))


class VerifyingTheNewBundle(unittest.TestCase):
    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)

    def test_a_missing_bundle_is_rejected(self):
        ok, reason = macupgrade.verify_bundle(os.path.join(self.base, "x.app"))
        self.assertFalse(ok)

    def test_a_wrong_version_is_rejected(self):
        # 엉뚱한 릴리스를 받아놓고 교체하면 사용자가 영문을 모른다.
        app = make_app(os.path.join(self.base, "PikaPet.app"), version="0.0.1")
        ok, reason = macupgrade.verify_bundle(app, expected_version="0.0.6")
        self.assertFalse(ok)
        self.assertIn("0.0.6", reason)

    def test_an_unsigned_bundle_is_rejected(self):
        # 우리가 만드는 번들은 최소한 ad-hoc 서명이 붙어 있다. 서명이 아예
        # 없으면 전송 중에 깨졌거나 우리 것이 아니다.
        app = make_app(os.path.join(self.base, "PikaPet.app"), version="0.0.6")
        ok, reason = macupgrade.verify_bundle(app, expected_version="0.0.6")
        self.assertFalse(ok)
        self.assertIn("서명", reason)


class TheSwapScript(unittest.TestCase):
    """실제 셸로 돌린다. 되돌리기가 이 파일에서 가장 중요한 부분이다."""

    def setUp(self):
        # 실제 설치와 같은 배치: 작업 폴더와 설치 위치는 다른 곳이다. 둘을
        # 겹쳐 두면 정리 단계가 앱을 지우는데, 그건 스크립트가 막아야 하는
        # 별도의 경우라서 따로 시험한다.
        self.root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.root, True)
        self.work = os.path.join(self.root, macupgrade.WORK_MARK + "abc")
        os.makedirs(self.work)
        self.installed = os.path.join(self.root, "Applications")
        os.makedirs(self.installed)
        self.log = os.path.join(self.root, "update.log")
        self.target = make_app(os.path.join(self.installed, "PikaPet.app"),
                               version="0.0.5")
        self.new = make_app(os.path.join(self.work, "PikaPet.app"),
                            version="0.0.6")
        self.script = macupgrade.write_swap_script(self.work)

    def run_script(self, pid="1", new=None, target=None, work=None):
        # pid 1 은 launchd -- 절대 끝나지 않으므로 '기다리는' 경우에 쓴다.
        done = subprocess.run(
            ["/bin/sh", self.script, pid, new or self.new,
             target or self.target, self.log, work or self.work],
            capture_output=True, text=True, timeout=120)
        return done

    def logged(self):
        try:
            with open(self.log, encoding="utf-8") as f:
                return f.read()
        except OSError:
            return ""

    def test_it_waits_for_the_app_and_gives_up_rather_than_killing_it(self):
        # 억지로 죽이면 세이브가 깨질 수 있다. 업데이트는 다음 기회에 하면 된다.
        # 0.5초 * 120 = 60초를 기다리므로 대기 상한을 줄여서 돌린다.
        #
        # 기다릴 pid 로는 **우리 자신**을 쓴다. pid 1(launchd)은 우리 소유가
        # 아니라서 `kill -0` 이 권한 오류를 내고, 스크립트가 그것을 '이미
        # 끝났다'로 읽어 그냥 진행해 버린다.
        quick = os.path.join(self.work, "quick.sh")
        with open(self.script, encoding="utf-8") as f:
            body = f.read().replace('-gt 120', '-gt 2')
        with open(quick, "w", encoding="utf-8") as f:
            f.write(body)
        os.chmod(quick, 0o755)
        done = subprocess.run(
            ["/bin/sh", quick, str(os.getpid()), self.new, self.target,
             self.log, self.work],
            capture_output=True, text=True, timeout=60)
        self.assertNotEqual(done.returncode, 0)
        self.assertTrue(os.path.isdir(self.target), "기존 앱이 사라졌다")
        self.assertEqual(macupgrade.installed_version(self.target), "0.0.5")
        self.assertIn("교체하지 않습니다", self.logged())

    def test_an_unverifiable_new_bundle_leaves_the_old_one_in_place(self):
        # 서명이 없는 번들은 검증을 통과하지 못한다. 그때 기존 앱이 남아야 한다.
        # 이것이 이 파일에서 가장 중요한 테스트다.
        dead = str(os.getpid() + 999999)      # 존재하지 않는 pid -> 즉시 진행
        done = self.run_script(pid=dead)
        self.assertNotEqual(done.returncode, 0)
        self.assertTrue(os.path.isdir(self.target), "기존 앱이 사라졌다")
        self.assertEqual(macupgrade.installed_version(self.target), "0.0.5",
                         "기존 앱이 되돌려지지 않았다")
        self.assertIn("되돌렸습니다", self.logged())

    def test_a_missing_new_bundle_leaves_the_old_one_in_place(self):
        dead = str(os.getpid() + 999999)
        done = self.run_script(pid=dead,
                               new=os.path.join(self.work, "없는것.app"))
        self.assertNotEqual(done.returncode, 0)
        self.assertTrue(os.path.isdir(self.target))
        self.assertEqual(macupgrade.installed_version(self.target), "0.0.5")

    def test_it_refuses_to_delete_an_unexpected_work_directory(self):
        # 생성한 스크립트 안의 rm -rf 는 경로를 의심해야 한다.
        outside = tempfile.mkdtemp()           # WORK_MARK 가 없는 이름
        self.addCleanup(shutil.rmtree, outside, True)
        keep = os.path.join(outside, "지우면안됨.txt")
        with open(keep, "w", encoding="utf-8") as f:
            f.write("x")
        dead = str(os.getpid() + 999999)
        self.run_script(pid=dead, work=outside)
        self.assertTrue(os.path.exists(keep), "예상하지 않은 폴더를 지웠다")
        self.assertIn("정리 건너뜀", self.logged())

    def test_it_refuses_to_clean_a_work_directory_holding_the_target(self):
        # 정상적인 설치에서는 겹치지 않지만, 여기서 틀리면 앱을 지운다.
        inside = make_app(os.path.join(self.work, "Applications", "PikaPet.app"),
                          version="0.0.5")
        dead = str(os.getpid() + 999999)
        self.run_script(pid=dead, target=inside)
        self.assertTrue(os.path.isdir(inside), "작업 폴더를 지우며 앱까지 지웠다")
        self.assertIn("대상이 그 안에 있습니다", self.logged())

    def test_the_backup_is_not_left_behind_on_the_failure_path(self):
        dead = str(os.getpid() + 999999)
        self.run_script(pid=dead)
        self.assertFalse(os.path.exists(self.target + ".pikapet-old"),
                         "되돌린 뒤에도 백업이 남았다")


class OrchestratingIt(unittest.TestCase):
    """Upgrade 클래스. 스레드가 Tk를 건드리지 않는 것이 핵심이다."""

    def setUp(self):
        self.root = FakeRoot()

    def test_the_worker_thread_never_touches_tk(self):
        # 건드리면 다음 after 타이머에서 프로세스가 abort한다.
        calls = []

        class Trap:
            def after(self, _ms, fn):
                calls.append(fn)

            def __getattr__(self, name):
                raise AssertionError(f"작업 스레드가 Tk의 {name} 을 불렀다")

        job = macupgrade.Upgrade(
            Trap(), "0.0.6",
            find=lambda tag: ("u", 10, "a.dmg"),
            fetch=lambda *a, **k: 10,
            stage=lambda dmg, work, ver: dmg + ".app")
        self.addCleanup(self._clean, job)
        job._work()
        self.assertEqual(calls, [])
        kinds = [k for k, _ in job.events]
        self.assertIn("done", kinds)

    def test_a_successful_run_reports_the_staged_app(self):
        job = self.make(stage=lambda dmg, work, ver: "/tmp/staged.app")
        job._work()
        job.drain()
        self.assertTrue(self.result.ok)
        self.assertEqual(self.result.staged, "/tmp/staged.app")

    def test_a_missing_asset_is_an_error_not_a_crash(self):
        job = self.make(find=lambda tag: None)
        job._work()
        job.drain()
        self.assertFalse(self.result.ok)
        self.assertFalse(self.result.cancelled)
        self.assertIn("찾을 수 없습니다", self.result.error)

    def test_a_staging_failure_is_reported(self):
        def boom(dmg, work, ver):
            raise RuntimeError("서명 검증에 실패했습니다")
        job = self.make(stage=boom)
        job._work()
        job.drain()
        self.assertFalse(self.result.ok)
        self.assertIn("서명", self.result.error)

    def test_cancelling_is_not_an_error(self):
        def cancelling(*a, **k):
            raise macupgrade.Cancelled()
        job = self.make(fetch=cancelling)
        job._work()
        job.drain()
        self.assertTrue(self.result.cancelled)
        self.assertIsNone(self.result.error)

    def test_progress_is_collapsed_to_the_latest(self):
        # 450번쯤 오는 진행률을 전부 그리면 Tk가 밀린다. 최신만 본다.
        seen = []
        job = macupgrade.Upgrade(self.root, "0.0.6",
                                 on_progress=lambda g, t: seen.append((g, t)))
        for i in range(1, 6):
            job.events.append(("progress", (i, 5)))
        job.drain()
        self.assertEqual(seen, [(5, 5)])

    def test_the_staging_step_shows_as_indeterminate(self):
        seen = []
        job = macupgrade.Upgrade(self.root, "0.0.6",
                                 on_progress=lambda g, t: seen.append((g, t)))
        job.events.append(("stage", None))
        job.drain()
        self.assertEqual(seen, [(None, None)])

    def test_a_broken_callback_does_not_escape(self):
        def explode(result):
            raise RuntimeError("안 됨")
        job = macupgrade.Upgrade(self.root, "0.0.6", on_done=explode)
        job.events.append(("done", macupgrade.Result(staged="/tmp/x.app")))
        job.drain()                            # 예외가 새어 나오면 실패

    def test_the_work_directory_is_cleaned_up_on_failure(self):
        job = self.make(stage=lambda *a: (_ for _ in ()).throw(RuntimeError("x")))
        job._work()
        self.assertIsNone(job.workdir, "실패했는데 작업 폴더가 남았다")

    def make(self, find=None, fetch=None, stage=None):
        self.result = None

        def done(result):
            self.result = result

        job = macupgrade.Upgrade(
            self.root, "0.0.6", on_done=done,
            find=find or (lambda tag: ("u", 10, "a.dmg")),
            fetch=fetch or (lambda *a, **k: 10),
            stage=stage or (lambda dmg, work, ver: "/tmp/staged.app"))
        # 성공 경로에서는 _discard 가 불리지 않는다 (교체 스크립트가 치운다).
        # 테스트에서는 그 스크립트가 없으므로 여기서 치운다.
        self.addCleanup(self._clean, job)
        return job

    def _clean(self, job):
        if job.workdir and macupgrade.WORK_MARK in job.workdir:
            shutil.rmtree(job.workdir, ignore_errors=True)


class FakeRoot:
    def __init__(self):
        self.scheduled = []

    def after(self, _ms, fn):
        self.scheduled.append(fn)


class SweepingStaleWork(unittest.TestCase):
    """끊긴 업데이트가 남긴 임시 폴더 치우기.

    나이를 보는 것이 핵심이다. 앱이 시작될 때 교체 스크립트가 아직 돌고 있을
    수 있고, 그 폴더를 지우면 진행 중인 교체가 깨진다.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def make_dir(self, name, age_sec=0):
        path = os.path.join(self.tmp, name)
        os.makedirs(path)
        if age_sec:
            old = time.time() - age_sec
            os.utime(path, (old, old))
        return path

    def test_an_old_work_directory_is_removed(self):
        path = self.make_dir(macupgrade.WORK_MARK + "old", age_sec=7 * 3600)
        self.assertEqual(macupgrade.sweep_stale_work(tmpdir=self.tmp), 1)
        self.assertFalse(os.path.exists(path))

    def test_a_fresh_one_is_left_alone(self):
        # 교체가 진행 중일 수 있다. 지우면 그것을 깨뜨린다.
        path = self.make_dir(macupgrade.WORK_MARK + "busy")
        self.assertEqual(macupgrade.sweep_stale_work(tmpdir=self.tmp), 0)
        self.assertTrue(os.path.exists(path))

    def test_other_directories_are_never_touched(self):
        other = self.make_dir("무관한폴더", age_sec=99 * 3600)
        macupgrade.sweep_stale_work(tmpdir=self.tmp)
        self.assertTrue(os.path.exists(other))

    def test_a_missing_directory_is_not_an_error(self):
        self.assertEqual(
            macupgrade.sweep_stale_work(tmpdir=os.path.join(self.tmp, "없음")), 0)


class ApplyingIt(unittest.TestCase):
    def test_it_refuses_without_a_target(self):
        ok, reason = macupgrade.apply_and_relaunch("/tmp/staged.app", target=None)
        self.assertFalse(ok)
        self.assertIn("찾을 수 없습니다", reason)


if __name__ == "__main__":
    unittest.main()
