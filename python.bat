@echo off
if "%~1"=="" (
    "%~dp0venv\Scripts\python.exe" "%~dp0run_all.py"
) else (
    "%~dp0venv\Scripts\python.exe" %*
)
