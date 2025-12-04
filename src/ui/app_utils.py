"""
Utility Pages - View data, system status, and reset functionality

Author: Hadar Wayn
Date: December 2025
"""

import streamlit as st
import time
from .streamlit_components import render_excel_viewer, render_system_status, render_status_cards
from ..utils.paths import get_excel_file, get_excel_dir, clean_temp_repos


def render_view_data_page():
    """Render Excel files viewer page"""
    st.markdown("## 📊 View Excel Files")
    tab1, tab2, tab3 = st.tabs(["📧 Excel1: Emails", "🔬 Excel2: Analysis", "🤖 Excel3: Feedback"])
    with tab1:
        excel1 = get_excel_file('Excel1.xlsx')
        render_excel_viewer(excel1, "Excel1.xlsx - Email Extraction Data")
    with tab2:
        excel2 = get_excel_file('Excel2.xlsx')
        render_excel_viewer(excel2, "Excel2.xlsx - Repository Analysis")
    with tab3:
        excel3 = get_excel_file('Excel3.xlsx')
        render_excel_viewer(excel3, "Excel3.xlsx - AI Feedback")


def render_status_page():
    """Render system status page"""
    st.markdown("## ℹ️ System Status")
    status_data = render_system_status()
    render_status_cards(status_data)
    st.markdown("---")
    st.markdown("### 📁 File Details")
    for name, data in status_data['excel_files'].items():
        with st.expander(f"📄 {name}"):
            if data['exists']:
                st.write(f"✅ **Status:** Exists")
                st.write(f"📊 **Rows:** {data['rows']}")
                st.write(f"🕒 **Last Modified:** {data['modified'].strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                st.write(f"❌ **Status:** Not found")


def reset_system():
    """Reset the system by deleting Excel files and temp repos"""
    import shutil
    excel_files = ['Excel1.xlsx', 'Excel2.xlsx', 'Excel3.xlsx']
    excel_dir = get_excel_dir()
    for excel_file in excel_files:
        excel_path = excel_dir / excel_file
        if excel_path.exists():
            excel_path.unlink()
    clean_temp_repos()


def render_reset_page():
    """Render system reset page"""
    st.markdown("## 🗑️ Reset System")
    st.warning("""
    **⚠️ WARNING: This will delete:**
    - All Excel files (Excel1.xlsx, Excel2.xlsx, Excel3.xlsx)
    - All cloned repositories in temp/repos/
    - Logs remain intact

    This action cannot be undone!
    """)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        confirm = st.text_input("Type 'RESET' to confirm:", key="reset_confirm")
        if st.button("🗑️ Reset System", use_container_width=True, type="primary"):
            if confirm == "RESET":
                with st.spinner("Resetting system..."):
                    reset_system()
                    st.success("✅ System reset successfully!")
                    time.sleep(1)
                    st.session_state.current_page = 'dashboard'
                    st.rerun()
            else:
                st.error("❌ Please type 'RESET' to confirm")
