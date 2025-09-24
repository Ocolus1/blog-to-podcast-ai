#!/usr/bin/env python3
"""
Blog2Podcast Streamlit App Launcher

This script launches the Streamlit web interface for the Blog2Podcast converter.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import openai
        import requests
        from blog_to_podcast.crew import BlogToPodcast
        print("✅ All dependencies are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("💡 Please install dependencies first:")
        print("   pip install -e .")
        return False

def check_environment():
    """Check if required environment variables are set."""
    required_vars = ['OPENAI_API_KEY', 'FIRECRAWL_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"⚠️  Missing environment variables: {', '.join(missing_vars)}")
        print("💡 Please set them in your .env file:")
        for var in missing_vars:
            print(f"   {var}=your_api_key_here")
        return False
    
    print("✅ Environment variables are configured.")
    return True

def launch_app():
    """Launch the Streamlit app."""
    app_path = Path(__file__).parent / "app.py"
    
    print("🚀 Launching Blog2Podcast Streamlit App...")
    print(f"📁 App location: {app_path}")
    print("🌐 The app will open in your default browser")
    print("⏹️  Press Ctrl+C to stop the app")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--server.address", "localhost",
            "--server.port", "8501"
        ], check=True)
    except KeyboardInterrupt:
        print("\n⏹️  App stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching app: {e}")
        print("💡 Try running manually: streamlit run app.py")

def main():
    """Main function to run the app launcher."""
    print("🎙️ Blog2Podcast AI Converter - Streamlit App Launcher")
    print("=" * 55)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment
    if not check_environment():
        print("\n🔧 You can still run the app, but conversions may fail without proper API keys.")
        response = input("Continue anyway? (y/N): ").lower().strip()
        if response != 'y':
            sys.exit(1)
    
    # Launch the app
    print("\n" + "=" * 55)
    launch_app()

if __name__ == "__main__":
    main()
