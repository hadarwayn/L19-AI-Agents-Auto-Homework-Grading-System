"""
Agent 3 & 4 Pages - AI Feedback Generator and Draft Creator

Author: Hadar Wayn
Date: December 2025
"""

import streamlit as st
import time
from .streamlit_components import render_excel_viewer
from ..utils.paths import get_excel_file
from .agent_runner import _execute_agent3, _execute_agent4


def render_agent3_page():
    """Render Agent 3 execution page"""
    st.markdown("## 🤖 Agent 3: AI Feedback Generator")
    st.info("""
    **What this agent does:**
    - Reads Excel2.xlsx for grades
    - Selects persona based on grade range:
      - 90-100: Trump (Enthusiastic)
      - 70-90: Shahar Hason (Comedian)
      - 55-70: Bruce Lee (Philosopher)
      - 0-55: Dudi Amsalem (Direct)
    - Generates personalized AI feedback
    - Creates Excel3.xlsx with feedback
    """)
    excel2 = get_excel_file('Excel2.xlsx')
    if not excel2.exists():
        st.warning("⚠️ Excel2.xlsx not found. Please run Agent 2 first.")
        if st.button("▶️ Go to Agent 2", use_container_width=True):
            st.session_state.current_page = 'agent2'
            st.rerun()
        return
    if st.button("🚀 Run Agent 3", use_container_width=True, type="primary"):
        st.markdown("---")
        st.markdown("### 🔄 Execution")
        with st.spinner("Executing Agent 3..."):
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Reading Excel2.xlsx...")
            progress_bar.progress(10)
            time.sleep(0.5)
            status_text.text("Generating AI feedback...")
            progress_bar.progress(40)
            success = _execute_agent3()
            progress_bar.progress(100)
            if success:
                excel_path = get_excel_file('Excel3.xlsx')
                if excel_path.exists():
                    import openpyxl
                    wb = openpyxl.load_workbook(excel_path)
                    ws = wb.active
                    row_count = ws.max_row - 1
                    st.success(f"✅ Agent 3 completed! Generated **{row_count}** feedback messages")
                    render_excel_viewer(excel_path, "Excel3.xlsx - AI Feedback")
                    if row_count > 0:
                        st.info("💡 **Next Step:** Run Agent 4 to create Gmail drafts")
                        if st.button("▶️ Go to Agent 4", use_container_width=True):
                            st.session_state.current_page = 'agent4'
                            st.rerun()
            else:
                st.error("❌ Agent 3 failed. Check the logs for details.")


def render_agent4_page():
    """Render Agent 4 execution page"""
    st.markdown("## ✉️ Agent 4: Draft Creator")
    st.info("""
    **What this agent does:**
    - Reads Excel3.xlsx for feedback
    - Joins with Excel1.xlsx for email data
    - Creates Gmail draft replies
    - Uses student mapping for personalization
    - Drafts are NOT sent automatically
    """)
    excel3 = get_excel_file('Excel3.xlsx')
    if not excel3.exists():
        st.warning("⚠️ Excel3.xlsx not found. Please run Agent 3 first.")
        if st.button("▶️ Go to Agent 3", use_container_width=True):
            st.session_state.current_page = 'agent3'
            st.rerun()
        return
    if st.button("🚀 Run Agent 4", use_container_width=True, type="primary"):
        st.markdown("---")
        st.markdown("### 🔄 Execution")
        with st.spinner("Executing Agent 4..."):
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Reading Excel3.xlsx...")
            progress_bar.progress(20)
            time.sleep(0.5)
            status_text.text("Creating Gmail drafts...")
            progress_bar.progress(60)
            success = _execute_agent4({})
            progress_bar.progress(100)
            if success:
                st.success("✅ Agent 4 completed successfully! Gmail drafts created.")
                st.balloons()
                st.info("💡 **Done!** Check your Gmail Drafts folder to review and send.")
            else:
                st.error("❌ Agent 4 failed. Check the logs for details.")
