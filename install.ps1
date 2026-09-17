<#
.SYNOPSIS
    Windows에서 PikaPet 환경을 준비한다.

.DESCRIPTION
    Python 3.14 virtualenv를 만들고, requirements.txt를 설치하고, Windows에서
    git이 망가뜨리는 run\assets 링크를 고친 뒤 tools\doctor.py를 돌린다.
    여러 번 실행해도 안전하다.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File install.ps1
    powershell -ExecutionPolicy Bypass -File install.ps1 -Force
    powershell -ExecutionPolicy Bypass -File install.ps1 -Venv D:\envs\pikapet

.NOTES
    이 파일은 한글 주석이 있으므로 UTF-8 BOM으로 저장해야 한다. PowerShell 5.1은
    BOM이 없는 .ps1을 ANSI로 읽어서 한글이 깨지고, 따옴표 안의 글자가 깨지면
    파싱까지 어긋난다.
#>
[CmdletBinding()]
param(
    [switch] $Force,
    [string] $Venv
)

$ErrorActionPreference = 'Stop'

# PowerShell 7.3 이상은 ErrorActionPreference가 Stop인 동안, 네이티브 명령이
# stderr에 쓴 것을 전부 종료 오류로 승격시킨다. pip와 python은 평범한 안내에도
# stderr를 쓰므로 이 동작을 끄고 $LASTEXITCODE를 직접 본다.
if (Test-Path variable:PSNativeCommandUseErrorActionPreference) {
    $PSNativeCommandUseErrorActionPreference = $false
}

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $Venv) { $Venv = Join-Path $Root '.venv' }

function Say  ($m) { Write-Host "`n==> $m" -ForegroundColor Cyan }
function Warn ($m) { Write-Host "    !! $m" -ForegroundColor Yellow }
function Die  ($m) { Write-Host "`n오류: $m" -ForegroundColor Red; exit 1 }

# $IsWindows는 PowerShell 6+에만 있으므로 5.1을 위해 $env:OS도 같이 본다.
if (-not $IsWindows -and $env:OS -ne 'Windows_NT') {
    Die 'install.ps1은 Windows용입니다. macOS에서는 ./install.sh를 쓰세요.'
}

# ---------------------------------------------------------------------------
# 1. Python 3.14
# ---------------------------------------------------------------------------
# pet.pyc는 3.14 바이트코드다. 다른 버전에서는 import 시점에 실패하므로 이건
# 취향이 아니라 강제 조건이다. python.org 설치본은 tkinter를 포함하므로 macOS와
# 달리 GUI를 위해 따로 설치할 것이 없다.
Say 'Python 3.14 찾는 중'
$PyExe = $null
$PyArgs = @()

# 여러 버전이 깔려 있을 때 `py -3.14`가 가장 확실한 경로다.
$launcher = Get-Command py -ErrorAction SilentlyContinue
if ($launcher) {
    try {
        $v = & py -3.14 -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>$null
        if ($LASTEXITCODE -eq 0 -and $v.Trim() -eq '3.14') {
            $PyExe = 'py'; $PyArgs = @('-3.14')
        }
    } catch { }
}
if (-not $PyExe) {
    foreach ($cand in @('python3.14', 'python')) {
        $c = Get-Command $cand -ErrorAction SilentlyContinue
        if ($c) {
            $v = & $c.Source -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>$null
            if ($v -and $v.Trim() -eq '3.14') { $PyExe = $c.Source; break }
        }
    }
}
if (-not $PyExe) {
    Die @'
Python 3.14를 찾을 수 없습니다.

  pet.pyc는 Python 3.14 바이트코드이고 다른 버전에서는 로드되지 않습니다.
  https://www.python.org/downloads/ 에서 설치하세요. 설치 시 "Add python.exe to
  PATH"를 켜고 기본 구성요소인 "tcl/tk and IDLE"을 그대로 두어야 합니다.
  설치한 뒤 다시 실행하세요.
'@
}
$shown = if ($PyArgs) { "$PyExe $PyArgs" } else { $PyExe }
Write-Host "    $shown ($(& $PyExe @PyArgs -V))"

& $PyExe @PyArgs -c 'import tkinter' 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Die @'
이 Python 3.14에는 tkinter가 없습니다.

  python.org 설치 프로그램을 다시 실행해 "Modify"를 고르고
  "tcl/tk and IDLE" 옵션을 켜세요. 이 앱은 전부 tkinter입니다.
'@
}
Write-Host "    tkinter 정상"

# ---------------------------------------------------------------------------
# 2. virtualenv
# ---------------------------------------------------------------------------
if ($Force -and (Test-Path $Venv)) {
    Say "기존 venv 삭제: $Venv"
    Remove-Item -Recurse -Force $Venv
}
if (Test-Path $Venv) {
    Say "기존 venv 재사용: $Venv"
} else {
    Say "venv 생성: $Venv"
    & $PyExe @PyArgs -m venv $Venv
    if ($LASTEXITCODE -ne 0) { Die 'venv 생성 실패' }
}

$VPy = Join-Path $Venv 'Scripts\python.exe'
if (-not (Test-Path $VPy)) { Die "venv가 깨진 것 같습니다: $VPy 없음" }

Say 'requirements 설치'
& $VPy -m pip install --quiet --upgrade pip
& $VPy -m pip install --quiet -r (Join-Path $Root 'requirements.txt')
if ($LASTEXITCODE -ne 0) { Die 'pip install 실패' }

# ---------------------------------------------------------------------------
# 3. 에셋 링크 -- Windows에서 언제나 깨지는 그 하나
# ---------------------------------------------------------------------------
# run\assets, run\assets_v3, run\assets_v4, run\badges_trainer는 git 심볼릭
# 링크로 커밋돼 있다. 기본값인 core.symlinks=false 에서는 git이 각각을
# "../assets" 라는 내용의 작은 텍스트 파일로 풀어놓고, 에셋을 run\ 기준으로
# 찾는 게임은 아무것도 못 찾아 빈 펫을 그린다.
#
# 심볼릭 링크 대신 junction을 쓰는 것은 의도적이다. 디렉터리 심볼릭 링크는
# 관리자 권한이나 개발자 모드가 필요한데, junction은 둘 다 필요 없다.
Say '에셋 링크 점검'
foreach ($name in @('assets', 'assets_v3', 'assets_v4', 'badges_trainer')) {
    $link   = Join-Path $Root "run\$name"
    $target = Join-Path $Root $name

    if (-not (Test-Path $target)) {
        Warn "$name 이 저장소 루트에 없습니다 -- 에셋이 불완전합니다"
        continue
    }
    $item = Get-Item $link -ErrorAction SilentlyContinue
    if ($item -and $item.PSIsContainer) {
        Write-Host "    run\$name 정상"
        continue
    }
    if ($item) {
        # git이 남긴 텍스트 파일이거나 깨진 링크
        Remove-Item -Force -Recurse $link
    }
    New-Item -ItemType Junction -Path $link -Target $target | Out-Null
    Write-Host "    run\$name 연결 (junction -> $name)"
}

# ---------------------------------------------------------------------------
# 4. 확인
# ---------------------------------------------------------------------------
Say '확인'
& $VPy (Join-Path $Root 'tools\doctor.py')
if ($LASTEXITCODE -ne 0) { Die '환경 점검 실패 (위 내용 참고)' }

Write-Host @"

완료. 실행:

    run\pikapet.bat

런처는 기본으로 .\.venv 를 씁니다. 다른 곳을 쓰려면 PIKAPET_VENV를 지정하세요.
메뉴는 펫을 우클릭하면 나옵니다.
테스트: $VPy -m unittest discover -s run
"@
