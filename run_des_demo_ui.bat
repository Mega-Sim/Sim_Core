@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py tools\des_demo_ui.py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    python tools\des_demo_ui.py
  ) else (
    echo [ERROR] Python 3 was not found.
    pause
    exit /b 1
  )
)
set EXIT_CODE=%errorlevel%
if not "%EXIT_CODE%"=="0" (
  echo.
  echo [ERROR] DES Demo UI failed. Exit code: %EXIT_CODE%
  pause
)
endlocal
