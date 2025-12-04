"""
Streamlit Header Components - Page header, styling, and agent cards

Author: Hadar Wayn
Date: December 2025
"""

import streamlit as st


def render_header():
    """Render the application header with logo and title"""
    st.set_page_config(
        page_title="L19 AI Grading System",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .agent-card {
            padding: 1.5rem;
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            margin: 1rem 0;
            transition: all 0.3s;
        }
        .agent-card:hover {
            border-color: #667eea;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
        }
        .status-badge {
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
        }
        .status-ready {
            background-color: #4caf50;
            color: white;
        }
        .status-pending {
            background-color: #ff9800;
            color: white;
        }
        .status-error {
            background-color: #f44336;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="main-header">
            <h1>🤖 L19 AI Agents Auto Homework Grading System</h1>
            <p style="font-size: 1.2rem; margin-top: 0.5rem;">
                Modern Web Interface • Automated Grading Pipeline • AI-Powered Feedback
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_agent_card(
    agent_number: int,
    agent_name: str,
    description: str,
    icon: str,
    button_label: str,
    on_click: callable
) -> bool:
    """Render an agent card with clickable button"""
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {icon} Agent {agent_number}: {agent_name}")
            st.markdown(f"<p style='color: #666;'>{description}</p>", unsafe_allow_html=True)
        with col2:
            return st.button(
                button_label,
                key=f"agent_{agent_number}_btn",
                use_container_width=True,
                type="primary"
            )
