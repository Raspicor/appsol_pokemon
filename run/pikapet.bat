@echo off
rem Launch PikaPet on Windows.
rem
rem   pikapet.bat            run it (no console window)
rem   pikapet.bat --debug    keep a console so startup errors are visible
rem
rem Unlike macOS there is nothing to patch here: pet.pyc is a Windows build and
rem winlayer.pyc is its native platform layer, so the game is started directly.
rem Running pet.pyc from this directory is what puts run\ on sys.path (so the
rem `import winlayer` inside it resolves) and makes the game resolve its assets
rem from run\, which is what the asset junctions are for.
setlocal
cd /d "%~dp0"

if "%PIKAPET_VENV%"=="" set "PIKAPET_VENV=%~dp0..\.venv"

set "PYW=%PIKAPET_VENV%\Scripts\pythonw.exe"
set "PY=%PIKAPET_VENV%\Scripts\python.exe"

if not exist "%PY%" (
  echo ERROR: no virtualenv at "%PIKAPET_VENV%".
  echo Run install.ps1 first, or set PIKAPET_VENV to an existing one.
  exit /b 1
)

if /i "%~1"=="--debug" (
  "%PY%" -u pet.pyc %2 %3 %4 %5 %6 %7 %8 %9
  echo.
  echo [exited with %ERRORLEVEL%]
  pause
  exit /b %ERRORLEVEL%
)

if exist "%PYW%" (
  start "" "%PYW%" pet.pyc %*
) else (
  start "" "%PY%" pet.pyc %*
)
