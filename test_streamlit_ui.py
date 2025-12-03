"""
Test Streamlit UI components
Quick verification that all UI modules load correctly
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

print("Testing Streamlit UI Components...")
print("=" * 70)

# Test 1: Import components module
try:
    from src.ui.streamlit_components import (
        render_header,
        render_agent_card,
        render_agent1_form,
        render_progress_tracker,
        render_excel_viewer,
        render_system_status,
        render_status_cards
    )
    print("[OK] streamlit_components.py imports successfully")
except Exception as e:
    print(f"[FAIL] Failed to import streamlit_components: {e}")
    sys.exit(1)

# Test 2: Check app.py exists and is valid Python
try:
    app_path = Path(__file__).parent / "app.py"
    if not app_path.exists():
        print(f"❌ app.py not found at {app_path}")
        sys.exit(1)

    # Try to compile the app file
    with open(app_path, 'r', encoding='utf-8') as f:
        code = f.read()
        compile(code, str(app_path), 'exec')
    print("[OK] app.py exists and is valid Python")
except Exception as e:
    print(f"[FAIL] app.py validation failed: {e}")
    sys.exit(1)

# Test 3: Check Streamlit is installed
try:
    import streamlit
    print(f"[OK] Streamlit installed (version {streamlit.__version__})")
except ImportError:
    print("[FAIL] Streamlit not installed. Run: pip install streamlit")
    sys.exit(1)

# Test 4: Check required dependencies
try:
    import plotly
    print(f"[OK] Plotly installed (version {plotly.__version__})")
except ImportError:
    print("[FAIL] Plotly not installed. Run: pip install plotly")
    sys.exit(1)

try:
    import pandas
    print(f"[OK] Pandas installed (version {pandas.__version__})")
except ImportError:
    print("[FAIL] Pandas not installed. Run: pip install pandas")
    sys.exit(1)

print("\n" + "=" * 70)
print("SUCCESS: All Streamlit UI components validated successfully!")
print("=" * 70)
print("\nTo launch the web UI, run:")
print("   python main.py")
print("\n   Or directly:")
print("   streamlit run app.py")
