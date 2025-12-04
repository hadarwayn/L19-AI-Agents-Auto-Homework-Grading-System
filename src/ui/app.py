"""
L19 AI Agents Auto Homework Grading System - Streamlit Web UI
Modern, interactive web interface with clickable buttons and form fields

Author: Hadar Wayn
Date: December 2025
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.ui.streamlit_components import render_header
from src.ui.app_dashboard import render_dashboard
from src.ui.app_agent1_agent2 import render_agent1_page, render_agent2_page
from src.ui.app_agent3_agent4 import render_agent3_page, render_agent4_page
from src.ui.app_pipeline import render_run_all_page
from src.ui.app_utils import render_view_data_page, render_status_page, render_reset_page


def main():
    """Main Streamlit application"""
    render_header()
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'dashboard'
    if 'agent1_params' not in st.session_state:
        st.session_state.agent1_params = None
    with st.sidebar:
        st.markdown("## 🎯 Navigation")
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.current_page = 'dashboard'
            st.rerun()
        if st.button("📧 Agent 1: Email Extractor", use_container_width=True):
            st.session_state.current_page = 'agent1'
            st.rerun()
        if st.button("🔬 Agent 2: Repository Analyzer", use_container_width=True):
            st.session_state.current_page = 'agent2'
            st.rerun()
        if st.button("🤖 Agent 3: AI Feedback Generator", use_container_width=True):
            st.session_state.current_page = 'agent3'
            st.rerun()
        if st.button("✉️ Agent 4: Draft Creator", use_container_width=True):
            st.session_state.current_page = 'agent4'
            st.rerun()
        if st.button("🚀 Run All Agents", use_container_width=True, type="primary"):
            st.session_state.current_page = 'run_all'
            st.rerun()
        st.markdown("---")
        if st.button("📊 View Excel Files", use_container_width=True):
            st.session_state.current_page = 'view_data'
            st.rerun()
        if st.button("ℹ️ System Status", use_container_width=True):
            st.session_state.current_page = 'status'
            st.rerun()
        st.markdown("---")
        if st.button("🗑️ Reset System", use_container_width=True):
            st.session_state.current_page = 'reset'
            st.rerun()
    if st.session_state.current_page == 'dashboard':
        render_dashboard()
    elif st.session_state.current_page == 'agent1':
        render_agent1_page()
    elif st.session_state.current_page == 'agent2':
        render_agent2_page()
    elif st.session_state.current_page == 'agent3':
        render_agent3_page()
    elif st.session_state.current_page == 'agent4':
        render_agent4_page()
    elif st.session_state.current_page == 'run_all':
        render_run_all_page()
    elif st.session_state.current_page == 'view_data':
        render_view_data_page()
    elif st.session_state.current_page == 'status':
        render_status_page()
    elif st.session_state.current_page == 'reset':
        render_reset_page()


if __name__ == "__main__":
    main()
