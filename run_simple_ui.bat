@echo off
setlocal
cd /d "%~dp0"

echo Starting Sim_Core simple runner UI...
echo.

where py >nul 2>nul
if %errorlevel%==0 (
    py tools\simple_runner_ui.py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python tools\simple_runner_ui.py
    ) else (
        echo [ERROR] Python executable was not found.
        echo Install Python 3 and run this file again.
        echo.
        pause
        exit /b 1
    )
)

set EXIT_CODE=%errorlevel%
if not "%EXIT_CODE%"=="0" (
    echo.
    echo [ERROR] UI failed to start. Exit code: %EXIT_CODE%
    echo Check the error message above.
    echo.
    pause
)

endlocal
