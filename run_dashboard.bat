@echo off
title Disaster Monitoring System Launcher
echo ================================
echo   Starting Disaster Dashboard
echo ================================

REM Move to project directory
cd /d D:\FYP_Dashboard

REM Check Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Python is not available.
    echo Please install Python 3.11+ and try again.
    pause
    exit /b
)

echo ✅ Python found

REM Start watcher in new terminal
echo ▶ Starting Watcher...
start "Watcher" cmd /k python watcher.py

REM Give watcher time to initialize
timeout /t 3 >nul

REM Start Streamlit dashboard
echo ▶ Starting Dashboard...
start "Dashboard" cmd /k python -m streamlit run app.py

echo ================================
echo   System Started Successfully
echo ================================
echo.
echo 🔹 Watcher terminal must stay open
echo 🔹 Dashboard will open at:
echo    http://localhost:8501
echo.
pause


