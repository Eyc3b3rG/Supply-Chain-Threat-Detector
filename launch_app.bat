
@echo off
echo ================================
echo Launching Supply Chain Threat Detector App
echo ================================

REM Navigate to the project directory
cd /d "%~dp0"

REM Start backend server on port 8080
start "Backend" cmd /k "uvicorn backend_api:app --reload --host 127.0.0.1 --port 8080"

REM Wait 5 seconds for backend to initialize
timeout /t 5 /nobreak >nul

REM Start Streamlit frontend
start "Frontend" cmd /k "streamlit run streamlit_app.py"
