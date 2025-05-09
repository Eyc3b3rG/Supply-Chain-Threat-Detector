@echo off
echo ==========================================
echo Starting Supply Chain Threat Detector App
echo ==========================================

REM Activate your virtual environment if needed
REM call venv\Scripts\activate

REM Start backend server
start cmd /k python backend_api.py

REM Delay to give backend time to start
timeout /t 5 /nobreak > NUL

REM Start Streamlit frontend
start cmd /k streamlit run streamlit_app.py

exit