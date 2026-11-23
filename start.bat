@echo off
title Free Fire Guild Glory Bot - Control Center & Terminal
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo [INFO] Setup check ho raha hai, kripya thoda intezar karein...
    "C:\Users\raikw\AppData\Local\Programs\Python\Python311\python.exe" -m venv venv
    ".\venv\Scripts\pip.exe" install -r requirements.txt
)

cls
echo ================================================================
echo   ⚡ FREE FIRE GUILD GLORY BOT - WEB CONTROL CENTER & TERMINAL
echo ================================================================
echo [*] Dashboard URL: http://127.0.0.1:25086
echo [*] Target Guild:  3056796518 (IND)
echo [*] Opening Dashboard in your browser...
echo.

start "" powershell -NoProfile -Command "Start-Sleep -Seconds 2; Start-Process 'http://127.0.0.1:25086'"

".\venv\Scripts\python.exe" -u dashboard_server.py

echo.
echo ================================================================
echo Bot Server band ho gaya hai. Window band karne ke liye koi key dabayein.
echo ================================================================
pause >nul
