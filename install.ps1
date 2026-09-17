<#
.SYNOPSIS
    Set up PikaPet on Windows.

.DESCRIPTION
    Builds a Python 3.14 virtualenv, installs requirements.txt, repairs the
    run\assets links that git mangles on Windows, then runs tools\doctor.py.
    Safe to re-run.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File install.ps1
    powershell -ExecutionPolicy Bypass -File install.ps1 -Force
    powershell -ExecutionPolicy Bypass -File install.ps1 -Venv D:\envs\pikapet
#>
[CmdletBinding()]
param(
    [switch] $Force,
    [string] $Venv
)

$ErrorActionPreference = 'Stop'

# PowerShell 7.3+ turns anything a native command writes to stderr into a
# terminating error while ErrorActionPreference is Stop. pip and python both
# use stderr for ordinary notices, so opt out and check $LASTEXITCODE instead.
if (Test-Path variable:PSNativeCommandUseErrorActionPreference) {
    $PSNativeCommandUseErrorActionPreference = $false
}

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $Venv) { $Venv = Join-Path $Root '.venv' }

function Say  ($m) { Write-Host "`n==> $m" -ForegroundColor Cyan }
function Warn ($m) { Write-Host "    !! $m" -ForegroundColor Yellow }
function Die  ($m) { Write-Host "`nERROR: $m" -ForegroundColor Red; exit 1 }

if (-not $IsWindows -and $env:OS -ne 'Windows_NT') {
    Die 'install.ps1 is for Windows. On macOS use ./install.sh.'
}

# ---------------------------------------------------------------------------
# 1. Python 3.14
# ---------------------------------------------------------------------------
# pet.pyc is 3.14 bytecode -- a different version fails at import, so this is a
# hard requirement, not a preference. The python.org installer bundles tkinter,
# so unlike macOS there is nothing extra to install for the GUI.
Say 'Looking for Python 3.14'
$PyExe = $null
$PyArgs = @()

# `py -3.14` is the reliable route when several versions are installed.
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
Python 3.14 not found.

  pet.pyc is Python 3.14 bytecode and will not load on any other version.
  Install it from https://www.python.org/downloads/ (tick "Add python.exe to
  PATH" and keep the default "tcl/tk and IDLE" component), then re-run.
'@
}
$shown = if ($PyArgs) { "$PyExe $PyArgs" } else { $PyExe }
Write-Host "    $shown ($(& $PyExe @PyArgs -V))"

& $PyExe @PyArgs -c 'import tkinter' 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Die @'
This Python 3.14 has no tkinter.

  Re-run the python.org installer, choose "Modify", and enable the
  "tcl/tk and IDLE" option. The whole app is tkinter.
'@
}
Write-Host "    tkinter ok"

# ---------------------------------------------------------------------------
# 2. the virtualenv
# ---------------------------------------------------------------------------
if ($Force -and (Test-Path $Venv)) {
    Say "Removing existing venv at $Venv"
    Remove-Item -Recurse -Force $Venv
}
if (Test-Path $Venv) {
    Say "Reusing venv at $Venv"
} else {
    Say "Creating venv at $Venv"
    & $PyExe @PyArgs -m venv $Venv
    if ($LASTEXITCODE -ne 0) { Die 'venv creation failed' }
}

$VPy = Join-Path $Venv 'Scripts\python.exe'
if (-not (Test-Path $VPy)) { Die "venv looks broken: $VPy not found" }

Say 'Installing requirements'
& $VPy -m pip install --quiet --upgrade pip
& $VPy -m pip install --quiet -r (Join-Path $Root 'requirements.txt')
if ($LASTEXITCODE -ne 0) { Die 'pip install failed' }

# ---------------------------------------------------------------------------
# 3. asset links -- the one thing that always breaks on Windows
# ---------------------------------------------------------------------------
# run\assets, run\assets_v3, run\assets_v4 and run\badges_trainer are committed
# as git symlinks. With the default core.symlinks=false, git writes each one out
# as a small TEXT FILE containing "../assets", and the game -- which resolves
# assets relative to run\ -- then finds nothing and draws an empty pet.
#
# Junctions are used rather than symlinks on purpose: directory symlinks need
# admin rights or Developer Mode, junctions need neither.
Say 'Checking asset links'
foreach ($name in @('assets', 'assets_v3', 'assets_v4', 'badges_trainer')) {
    $link   = Join-Path $Root "run\$name"
    $target = Join-Path $Root $name

    if (-not (Test-Path $target)) {
        Warn "$name is missing from the repo root -- assets are incomplete"
        continue
    }
    $item = Get-Item $link -ErrorAction SilentlyContinue
    if ($item -and $item.PSIsContainer) {
        Write-Host "    run\$name ok"
        continue
    }
    if ($item) {
        # a text file left behind by git, or a broken link
        Remove-Item -Force -Recurse $link
    }
    New-Item -ItemType Junction -Path $link -Target $target | Out-Null
    Write-Host "    run\$name linked (junction -> $name)"
}

# ---------------------------------------------------------------------------
# 4. verify
# ---------------------------------------------------------------------------
Say 'Verifying'
& $VPy (Join-Path $Root 'tools\doctor.py')
if ($LASTEXITCODE -ne 0) { Die 'environment check failed (see above)' }

Write-Host @"

Done. Run it with:

    run\pikapet.bat

The launcher uses .\.venv by default; set PIKAPET_VENV to point somewhere else.
Right-click the pet for the menu.
Tests: $VPy -m unittest discover -s run
"@
