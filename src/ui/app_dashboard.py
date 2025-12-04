"""
Dashboard Page - Main dashboard with agent cards and quick actions

Author: Hadar Wayn
Date: December 2025
"""

import streamlit as st
from .streamlit_components import render_system_status, render_status_cards


def render_dashboard():
    """Render the main dashboard with agent cards"""
    st.markdown("## 🏠 Dashboard")
    status_data = render_system_status()
    render_status_cards(status_data)
    st.markdown("---")
    st.markdown("## 🤖 Agents")
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown("""
            <div class="agent-card">
                <h3>📧 Agent 1: Email Extractor</h3>
                <p>Extract homework submissions from Gmail with flexible search parameters</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("▶️ Run Agent 1", key="dash_agent1", use_container_width=True):
                st.session_state.current_page = 'agent1'
                st.rerun()
        with st.container():
            st.markdown("""
            <div class="agent-card">
                <h3>🤖 Agent 3: AI Feedback</h3>
                <p>Generate personalized feedback using 4 celebrity personas</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("▶️ Run Agent 3", key="dash_agent3", use_container_width=True):
                st.session_state.current_page = 'agent3'
                st.rerun()
    with col2:
        with st.container():
            st.markdown("""
            <div class="agent-card">
                <h3>🔬 Agent 2: Repository Analyzer</h3>
                <p>Clone and analyze GitHub repositories with multi-threading</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("▶️ Run Agent 2", key="dash_agent2", use_container_width=True):
                st.session_state.current_page = 'agent2'
                st.rerun()
        with st.container():
            st.markdown("""
            <div class="agent-card">
                <h3>✉️ Agent 4: Draft Creator</h3>
                <p>Create Gmail draft replies with AI-generated feedback</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("▶️ Run Agent 4", key="dash_agent4", use_container_width=True):
                st.session_state.current_page = 'agent4'
                st.rerun()
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚀 Run All Agents", key="dash_run_all", use_container_width=True, type="primary"):
            st.session_state.current_page = 'run_all'
            st.rerun()
    with col2:
        if st.button("📊 View Excel Files", key="dash_view", use_container_width=True):
            st.session_state.current_page = 'view_data'
            st.rerun()
    with col3:
        if st.button("🗑️ Reset System", key="dash_reset", use_container_width=True):
            st.session_state.current_page = 'reset'
            st.rerun()
