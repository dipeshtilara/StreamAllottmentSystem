import streamlit as st
import os

st.set_page_config(
    page_title="Stream Allotment Portal — Class XI 2025-26",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default chrome for a cleaner look
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

html_file = os.path.join(os.path.dirname(__file__), "stream_tool.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1100, scrolling=True)
