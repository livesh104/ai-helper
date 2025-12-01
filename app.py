import streamlit as st
import google.generativeai as genai
import json

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="AI Exam Revision Tool",
    page_icon="📚",
    layout="wide"
)

# Global custom CSS
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: #e5e7eb;
}
.main {
    background: radial-gradient(circle at top, #1e293b 0, #020617 55%);
}
.block-container {
    padding-top: 1.5rem;
}
.big-title {
    font-size

