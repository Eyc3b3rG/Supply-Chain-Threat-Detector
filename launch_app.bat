@echo off
echo ============================================
echo Launching Supply Chain Threat Detector App
echo ============================================

:: Activate your Python environment if needed
:: call path\to\venv\Scripts\activate.bat

:: Step 1: Start the FastAPI backend
start cmd /k "python backend_api.py"

:: Give it a few seconds to start
timeout /t 5 >nul

:: Step 2: Launch the Streamlit frontend
start streamlit run streamlit_app.py
