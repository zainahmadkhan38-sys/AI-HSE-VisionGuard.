import streamlit as st

st.set_page_config(
    page_title="AI-HSE VisionGuard",
    page_icon="🦺",
    layout="wide"
)

st.title("🦺 AI-HSE VisionGuard")

st.write("AI Workplace Safety Surveillance System")

st.success("VisionGuard is running!")

st.header("Security Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Cameras Online", 3)

with col2:
    st.metric("Active Alerts", 0)

with col3:
    st.metric("Confirmed Violations", 0)

with col4:
    st.metric("False Alarms", 0)
