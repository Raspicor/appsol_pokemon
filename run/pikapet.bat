@echo off
rem 이 파일은 UTF-8이고 아래 메시지가 한글이므로, cmd의 코드 페이지를 먼저
rem 65001로 올린다. 그러지 않으면 한국어 Windows(949)에서 깨져 보인다.
chcp 65001 > nul
rem Windows에서 PikaPet 실행.
rem
rem   pikapet.bat            실행 (콘솔 창 없음)
rem   pikapet.bat --debug    시작 오류가 보이도록 콘솔을 남긴다
rem
rem macOS와 달리 여기서는 패치할 것이 없다. pet.pyc가 Windows 빌드이고
rem winlayer.pyc가 그 native 플랫폼 계층이므로 게임을 그대로 시작한다.
rem 이 디렉터리에서 pet.pyc를 돌리는 것이 run\을 sys.path에 올려 (안쪽의
rem `import winlayer`가 풀리도록) 하고, 게임이 에셋을 run\ 기준으로 찾게 만든다.
rem 에셋 junction이 필요한 이유가 이것이다.
setlocal
cd /d "%~dp0"

if "%PIKAPET_VENV%"=="" set "PIKAPET_VENV=%~dp0..\.venv"

set "PYW=%PIKAPET_VENV%\Scripts\pythonw.exe"
set "PY=%PIKAPET_VENV%\Scripts\python.exe"

if not exist "%PY%" (
  echo 오류: "%PIKAPET_VENV%" 에 virtualenv가 없습니다.
  echo install.ps1을 먼저 실행하거나, PIKAPET_VENV를 기존 venv로 지정하세요.
  exit /b 1
)

if /i "%~1"=="--debug" (
  "%PY%" -u pet.pyc %2 %3 %4 %5 %6 %7 %8 %9
  echo.
  echo [종료 코드 %ERRORLEVEL%]
  pause
  exit /b %ERRORLEVEL%
)

if exist "%PYW%" (
  start "" "%PYW%" pet.pyc %*
) else (
  start "" "%PY%" pet.pyc %*
)
