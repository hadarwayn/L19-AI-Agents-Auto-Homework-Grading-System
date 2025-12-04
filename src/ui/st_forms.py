"""
Streamlit Form Components - Input forms and progress trackers

Author: Hadar Wayn
Date: December 2025
"""

import streamlit as st
from typing import Optional, Dict, Any


def render_agent1_form() -> Optional[Dict[str, Any]]:
    """Render Agent 1 parameter form with input fields"""
    st.markdown("### 📧 Email Search Parameters")
    with st.form("agent1_form"):
        col1, col2 = st.columns(2)
        with col1:
            email_subject = st.text_input(
                "Email Subject",
                placeholder="e.g., GradingL19 or Homework",
                help="Search term for email subject (case-insensitive substring match)"
            )
            sender_email = st.text_input(
                "Sender Email (Optional)",
                placeholder="student@example.com",
                help="Filter by sender email address (leave empty for all senders)"
            )
        with col2:
            max_emails = st.slider(
                "Maximum Emails",
                min_value=1,
                max_value=100,
                value=20,
                help="Maximum number of emails to process (1-100)"
            )
            st.markdown(f"""
            <div style='padding: 1rem; background-color: #f0f2f6; border-radius: 8px; margin-top: 1rem;'>
                <strong>📊 Search Preview:</strong><br>
                • Subject: <code>{email_subject if email_subject else '(all)'}</code><br>
                • Sender: <code>{sender_email if sender_email else '(all)'}</code><br>
                • Max: <code>{max_emails}</code> emails
            </div>
            """, unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍 Search & Extract Emails", use_container_width=True)
        if submitted:
            query_parts = []
            if email_subject:
                words = email_subject.split()
                if len(words) <= 3:
                    query_parts.append(f'subject:{email_subject}')
                else:
                    key_words = ' '.join(words[:3])
                    query_parts.append(f'subject:{key_words}')
            if sender_email:
                query_parts.append(f'from:{sender_email}')
            query = ' '.join(query_parts) if query_parts else ''
            return {
                'email_subject': email_subject if email_subject else None,
                'sender_email': sender_email if sender_email else None,
                'max_emails': max_emails,
                'query': query
            }
    return None


def render_progress_tracker(agent_name: str, status: str = "running"):
    """Render a progress tracker for agent execution"""
    if status == "running":
        st.info(f"⏳ {agent_name} is running...")
        progress_bar = st.progress(0)
        return progress_bar
    elif status == "success":
        st.success(f"✅ {agent_name} completed successfully!")
    elif status == "error":
        st.error(f"❌ {agent_name} failed!")
