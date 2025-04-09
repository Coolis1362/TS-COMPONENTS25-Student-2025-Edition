REM Change to the directory where the .bat file is located
cd /d "%~dp0"

REM Check if Python is installed
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed or not added to PATH.
    pause
    exit /b
)

REM Run the .exe

TS_UPDATES_for_TS_DOS.exe

pause