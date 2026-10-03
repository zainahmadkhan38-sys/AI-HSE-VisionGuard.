import os
import cv2
import streamlit as st
from ultralytics import YOLO

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI-HSE VisionGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .metric-card {
        background: white;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        text-align: center;
    }

    .metric-number {
        font-size: 2rem;
        font-weight: 700;
    }

    .metric-label {
        color: #6b7280;
        font-size: 0.9rem;
    }

    .alert-card {
        background: #fff7ed;
        border-left: 5px solid #f97316;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
    }

    .safe-card {
        background: #f0fdf4;
        border-left: 5px solid #22c55e;
        padding: 1rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD YOLO MODEL
# ============================================================

@st.cache_resource
def load_model():
    model_path = "yolo11n.pt"

    if not os.path.exists(model_path):
        return None

    return YOLO(model_path)


model = load_model()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🛡️ VisionGuard")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Security Dashboard",
        "Camera Monitoring",
        "Alert Center",
        "Event History",
        "HSE Summary"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI-powered Health, Safety & Environment monitoring system."
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🛡️ AI-HSE VisionGuard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered workplace safety monitoring dashboard</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECURITY DASHBOARD
# ============================================================

if page == "Security Dashboard":

    st.header("Security Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">04</div>
            <div class="metric-label">Active Cameras</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">12</div>
            <div class="metric-label">Today's Events</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">02</div>
            <div class="metric-label">Active Alerts</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">96%</div>
            <div class="metric-label">Safety Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("System Status")

    status1, status2, status3 = st.columns(3)

    with status1:
        st.success("🟢 AI Detection Online")

    with status2:
        st.success("🟢 Camera System Online")

    with status3:
        st.success("🟢 Monitoring Active")

    st.subheader("Recent Safety Activity")

    st.markdown("""
    <div class="alert-card">
        <strong>⚠️ Safety Event</strong><br>
        Person detected in monitored area.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="safe-card">
        <strong>✅ Normal Activity</strong><br>
        No critical safety violation detected.
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CAMERA MONITORING
# ============================================================

elif page == "Camera Monitoring":

    st.header("📹 Camera Monitoring")

    video_path = "data/cameras/cam01.mp4.mp4"

    if not os.path.exists(video_path):
        st.error(f"Video file not found: {video_path}")

        st.info(
            "Make sure the video is uploaded to "
            "data/cameras/ in your GitHub repository."
        )

    else:

        st.success("Camera 01 video found.")

        st.video(video_path)

        st.markdown("---")

        if model is None:
            st.warning(
                "YOLO model not found. Upload yolo11n.pt "
                "to the root of your GitHub repository."
            )

        else:

            st.subheader("AI Detection")

            start_detection = st.button(
                "▶️ Start AI Detection",
                type="primary"
            )

            if start_detection:

                cap = cv2.VideoCapture(video_path)

                if not cap.isOpened():

                    st.error("Unable to open the camera video.")

                else:

                    frame_placeholder = st.empty()
                    progress_placeholder = st.empty()

                    frame_count = 0

                    total_frames = int(
                        cap.get(cv2.CAP_PROP_FRAME_COUNT)
                    )

                    while cap.isOpened():

                        ret, frame = cap.read()

                        if not ret:
                            break

                        frame_count += 1

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

                        if total_frames > 0:

                            progress = min(
                                frame_count / total_frames,
                                1.0
                            )

                            progress_placeholder.progress(
                                progress
                            )

                    cap.release()

                    st.success(
                        "AI detection completed."
                    )


# ============================================================
# ALERT CENTER
# ============================================================

elif page == "Alert Center":

    st.header("🚨 Alert Center")

    st.subheader("Active Alerts")

    st.markdown("""
    <div class="alert-card">
        <strong>⚠️ Alert #001</strong><br>
        Potential safety violation detected.<br>
        <small>Camera: CAM-01</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-card">
        <strong>⚠️ Alert #002</strong><br>
        Person detected in restricted monitoring area.<br>
        <small>Camera: CAM-01</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Alert Controls")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✓ Acknowledge All Alerts"):
            st.success("All alerts acknowledged.")

    with col2:
        if st.button("🗑️ Clear Alert View"):
            st.info("Alert view cleared.")


# ============================================================
# EVENT HISTORY
# ============================================================

elif page == "Event History":

    st.header("📋 Event History")

    events = [
        ["10:15 AM", "CAM-01", "Person Detected", "Normal"],
        ["10:22 AM", "CAM-01", "Safety Event", "Warning"],
        ["10:41 AM", "CAM-02", "Person Detected", "Normal"],
        ["11:03 AM", "CAM-01", "Safety Event", "Warning"],
    ]

    st.table(
        {
            "Time": [x[0] for x in events],
            "Camera": [x[1] for x in events],
            "Event": [x[2] for x in events],
            "Status": [x[3] for x in events],
        }
    )


# ============================================================
# HSE SUMMARY
# ============================================================

elif page == "HSE Summary":

    st.header("📊 HSE Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Safety Events",
            "12"
        )

    with col2:
        st.metric(
            "Resolved Alerts",
            "10"
        )

    with col3:
        st.metric(
            "Safety Score",
            "96%"
        )

    st.markdown("---")

    st.subheader("Safety Overview")

    st.progress(0.96)

    st.success(
        "Current monitoring status: Operational"
    )

    st.info(
        "This dashboard provides an AI-assisted monitoring "
        "interface. Detection results should be reviewed "
        "by an authorized safety professional."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI-HSE VisionGuard • AI-assisted workplace safety monitoring"
)
