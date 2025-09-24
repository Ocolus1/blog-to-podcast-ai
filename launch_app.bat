@echo off
echo 🎙️ Blog2Podcast AI Converter - Starting Web App...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.10+ and try again
    pause
    exit /b 1
)

REM Check if the project is installed
python -c "import blog_to_podcast" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -e .
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Launch the app
echo 🚀 Launching Streamlit app...
echo 🌐 Your browser will open automatically
echo ⏹️  Close this window or press Ctrl+C to stop the app
echo.

python run_app.py

pause
