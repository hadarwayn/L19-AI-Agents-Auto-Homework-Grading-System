"""
L19 AI Agents Auto Homework Grading System
Main Entry Point

Launches modern Streamlit web UI for the grading system.
Run with: python main.py

Author: Hadar Wayn
Date: December 2025
"""

import sys
import subprocess
from pathlib import Path
import webbrowser
import time

from src.utils.paths import ensure_directories
from src.utils.logger import setup_logger

# Initialize logger
logger = setup_logger("main")


def main():
    """
    Main application entry point - Launches Streamlit web UI
    """
    try:
        # Ensure all required directories exist
        ensure_directories()

        print("=" * 70)
        print("🤖 L19 AI Agents Auto Homework Grading System")
        print("=" * 70)
        print("\n🚀 Launching modern web interface...")
        print("📍 URL: http://localhost:8501")
        print("\n💡 Tip: The app will open in your default browser automatically")
        print("   Press Ctrl+C to stop the server\n")

        logger.info("Launching Streamlit web UI")

        # Get app path
        app_path = Path(__file__).parent / "src" / "ui" / "app.py"

        if not app_path.exists():
            print(f"❌ Error: app.py not found at {app_path}")
            logger.error(f"app.py not found at {app_path}")
            return 1

        # Launch Streamlit
        try:
            # Open browser after a short delay
            def open_browser():
                time.sleep(2)
                webbrowser.open("http://localhost:8501")

            import threading
            threading.Thread(target=open_browser, daemon=True).start()

            # Run Streamlit
            subprocess.run([
                sys.executable,
                "-m",
                "streamlit",
                "run",
                str(app_path),
                "--server.port=8501",
                "--server.address=localhost",
                "--browser.serverAddress=localhost",
                "--browser.gatherUsageStats=false"
            ])

        except KeyboardInterrupt:
            print("\n\n⚠️  Server stopped by user")
            logger.info("Streamlit server stopped by user (Ctrl+C)")
            return 0

        return 0

    except Exception as e:
        print(f"\n❌ Error launching Streamlit: {e}")
        logger.exception("Error launching Streamlit web UI")
        print("\n💡 Try running manually: streamlit run src/ui/app.py")
        return 1


if __name__ == "__main__":
    sys.exit(main())
