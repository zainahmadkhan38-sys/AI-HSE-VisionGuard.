```python
import streamlit as st
from ultralytics import YOLO
import cv2
import os
import time

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI-HSE VisionGuard",
    page_icon="🦺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

    .main {
        background-color: #f5f7fa;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .dashboard-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .dashboard-subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .status-card {
        padding: 18px;
        border-radius: 12px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .metric-label {
        color: #6b7280;
        font-size: 0.85rem;
        margin-bottom: 5px;
    }

    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
    }

    .online {
        color: #16a34a;
        font-weight: 600;
    }

    .warning {
        color: #d97706;
        font-weight: 600;
    }

    .danger {
        color: #dc2626;
        font-weight: 600;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        background: white;
        border: 1px solid #e5e7eb;
        margin-top: 15px;
    }

    .camera-header {
        padding: 12px 16px;
        background: #111827;
        color: white;
        border-radius: 10px 10px 0 0;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.8rem;
        margin-top: 40px;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")


try:
    model = load_model()
    model_status = True
except Exception as e:
    model = None
    model_status = False
    model_error = str(e)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.markdown("# 🦺 VisionGuard")
st.sidebar.caption("AI-HSE Security Control Room")

st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Security Dashboard",
        "Camera Monitoring",
        "Alert Center",
        "Event History",
        "HSE Summary"
    ]
)

st.sidebar.divider()

if model_status:
    st.sidebar.success("🟢 AI SYSTEM ONLINE")
else:
    st.sidebar.error("🔴 AI SYSTEM ERROR")

st.sidebar.caption("VisionGuard v1.0")
st.sidebar.caption("AI-powered workplace safety monitoring")

# ---------------------------------------------------------
# SECURITY DASHBOARD
# ---------------------------------------------------------

if page == "Security Dashboard":

    st.markdown(
        '<div class="dashboard-title">🛡️ Security Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'AI-powered workplace health and safety surveillance'
        '</div>',
        unsafe_allow_html=True
    )

    # METRICS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="status-card">
            <div class="metric-label">CAMERAS ONLINE</div>
            <div class="metric-value">1</div>
            <div class="online">● Operational</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="status-card">
            <div class="metric-label">ACTIVE ALERTS</div>
            <div class="metric-value">0</div>
            <div class="online">● No active alerts</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="status-card">
            <div class="metric-label">CONFIRMED VIOLATIONS</div>
            <div class="metric-value">0</div>
            <div class="online">● Clear</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="status-card">
            <div class="metric-label">FALSE ALARMS</div>
            <div class="metric-value">0</div>
            <div class="online">● None recorded</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # SYSTEM STATUS
    st.subheader("System Status")

    status_col1, status_col2 = st.columns(2)

    with status_col1:

        if model_status:
            st.success("🟢 AI detection engine is operational.")
        else:
            st.error("🔴 AI model could not be loaded.")

        st.markdown("""
        <div class="info-box">
            <b>Detection Engine</b><br>
            YOLO object detection<br><br>
            <b>Monitoring Mode</b><br>
            Workplace surveillance
        </div>
        """, unsafe_allow_html=True)

    with status_col2:

        st.markdown("""
        <div class="info-box">
            <b>Camera Network</b><br><br>
            🟢 CAM-01 — Production Area<br>
            🟢 Connection available<br>
            🟢 Video source configured
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# CAMERA MONITORING
# ---------------------------------------------------------

elif page == "Camera Monitoring":

    st.markdown(
        '<div class="dashboard-title">📹 Camera Monitoring</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Real-time AI object detection from workplace camera footage'
        '</div>',
        unsafe_allow_html=True
    )

    video_path = "data/cameras/cam01.mp4.mp4"

    st.markdown(
        '<div class="camera-header">📹 CAM-01 — Production Area</div>',
        unsafe_allow_html=True
    )

    if not os.path.exists(video_path):

        st.error(
            f"Video file not found: `{video_path}`"
        )

        st.info(
            "Make sure the video exists at data/cameras/cam01.mp4.mp4"
        )

    elif model is None:

        st.error("AI model could not be loaded.")

    else:

        st.write("")

        start_detection = st.button(
            "▶️ Start AI Detection",
            type="primary"
        )

        if start_detection:

            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():

                st.error("Could not open the camera video.")

            else:

                frame_placeholder = st.empty()

                progress = st.progress(0)

                total_frames = int(
                    cap.get(cv2.CAP_PROP_FRAME_COUNT)
                )

                frame_count = 0

                while cap.isOpened():

                    success, frame = cap.read()

                    if not success:
                        break

                    results = model(
                        frame,
                        verbose=False
                    )

                    annotated_frame = results[0].plot()

                    annotated_frame = cv2.cvtColor(
                        annotated_frame,
                        cv2.COLOR_BGR2RGB
                    )

                    frame_placeholder.image(
                        annotated_frame,
                        channels="RGB",
                        use_container_width=True
                    )

                    frame_count += 1

                    if total_frames > 0:

                        progress_value = min(
                            frame_count / total_frames,
                            1.0
                        )

                        progress.progress(
                            progress_value
                        )

                    time.sleep(0.01)

                cap.release()

                progress.empty()

                st.success(
                    "🟢 Video processing completed."
                )

        else:

            st.info(
                "Click **Start AI Detection** to begin monitoring."
            )

# ---------------------------------------------------------
# ALERT CENTER
# ---------------------------------------------------------

elif page == "Alert Center":

    st.markdown(
        '<div class="dashboard-title">🚨 Alert Center</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Review and verify AI-detected HSE events'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Active Alerts", "0")

    with col2:
        st.metric("Pending Review", "0")

    with col3:
        st.metric("Critical Alerts", "0")

    st.divider()

    st.success(
        "🟢 No pending safety alerts."
    )

    st.info(
        "AI-generated alerts will appear here when safety events are detected."
    )

# ---------------------------------------------------------
# EVENT HISTORY
# ---------------------------------------------------------

elif page == "Event History":

    st.markdown(
        '<div class="dashboard-title">📋 Event History</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Historical workplace safety events'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        "No safety events have been recorded yet."
    )

    st.divider()

    st.subheader("Event Log")

    st.dataframe(
        {
            "Event": [],
            "Camera": [],
            "Status": [],
            "Time": []
        },
        use_container_width=True
    )

# ---------------------------------------------------------
# HSE SUMMARY
# ---------------------------------------------------------

elif page == "HSE Summary":

    st.markdown(
        '<div class="dashboard-title">📊 HSE Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Workplace health and safety performance overview'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Alerts", "0")

    with col2:
        st.metric("Confirmed", "0")

    with col3:
        st.metric("False Alarms", "0")

    with col4:
        st.metric("PPE Violations", "0")

    with col5:
        st.metric("Unsafe Acts", "0")

    st.divider()

    st.subheader("Violations by Type")

    st.info(
        "Violation statistics will appear here once events are detected."
    )

    st.divider()

    st.subheader("Current Safety Status")

    st.success(
        "🟢 No confirmed HSE violations recorded."
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        AI-HSE VisionGuard • Workplace Safety Intelligence Platform
    </div>
    """,
    unsafe_allow_html=True
)
```

**Important:** this code specifically uses:

```python
video_path = "data/cameras/cam01.mp4.mp4"
```

so it matches the filename you currently have in GitHub.

After replacing `app.py`, **commit the changes and reboot Streamlit**. Also make sure `yolo11n.pt` is in the repository root.
