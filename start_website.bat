@echo off
title Free Fire Guild Glory Bot - Web Control Center & Terminal
cd /d "%~dp0"

echo ================================================================
echo   FREE FIRE GUILD GLORY BOT - CONTROL CENTER & LIVE TERMINAL
echo ================================================================
echo.

set "PY=.\venv\Scripts\python.exe"
if not exist "%PY%" (
    echo [!] Virtual environment not found. Checking system python...
    set "PY=python"
)

echo [*] Starting Web Control Center on http://127.0.0.1:25086 ...
echo [*] Opening website dashboard in your browser...
echo.

start "" powershell -NoProfile -Command "Start-Sleep -Seconds 2; Start-Process 'http://127.0.0.1:25086'"

"%PY%" -u dashboard_server.py

echo.
echo ================================================================
echo Web Server band ho gaya hai. Window band karne ke liye koi key dabayein.
echo ================================================================
pause >nul
