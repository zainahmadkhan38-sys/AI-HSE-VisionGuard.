import streamlit as st
import cv2
from ultralytics import YOLO

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI-HSE VisionGuard",
    page_icon="🦺",
    layout="wide"
)

# --------------------------------------------------
# LOAD YOLO MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")


model = load_model()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🦺 VisionGuard")
st.sidebar.write("HSE Security Control Room")

page = st.sidebar.radio(
    "Navigation",
    [
        "Security Dashboard",
        "Camera Monitoring",
        "Alert Center",
        "Event History",
        "HSE Summary"
    ]
)

st.sidebar.divider()
st.sidebar.success("System Online")

# --------------------------------------------------
# SECURITY DASHBOARD
# --------------------------------------------------

if page == "Security Dashboard":

    st.title("🛡️ Security Dashboard")

    st.caption("AI-HSE Workplace Safety Surveillance")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Cameras Online", "1")

    with col2:
        st.metric("Active Alerts", "0")

    with col3:
        st.metric("Confirmed Violations", "0")

    with col4:
        st.metric("False Alarms", "0")

    st.divider()

    st.subheader("System Status")

    st.success("🟢 Camera system is online.")

# --------------------------------------------------
# CAMERA MONITORING
# --------------------------------------------------

elif page == "Camera Monitoring":

    st.title("📹 Camera Monitoring")

    st.caption("AI person detection")

    st.divider()

    st.subheader("CAM-01")
    st.write("📍 Production Area")

    video_path = "data/cameras/cam01.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():

        st.error("Could not open camera video.")

    else:

        frame_placeholder = st.empty()

        stop_button = st.button("⏹️ Stop Detection")

        while cap.isOpened() and not stop_button:

            success, frame = cap.read()

            if not success:
                break

            # Run YOLO
            results = model(frame, verbose=False)

            # Draw detection boxes
            annotated_frame = results[0].plot()

            # Convert BGR to RGB
            annotated_frame = cv2.cvtColor(
                annotated_frame,
                cv2.COLOR_BGR2RGB
            )

            frame_placeholder.image(
                annotated_frame,
                channels="RGB",
                use_container_width=True
            )

        cap.release()

    st.success("🟢 Person detection enabled.")

# --------------------------------------------------
# ALERT CENTER
# --------------------------------------------------

elif page == "Alert Center":

    st.title("🚨 Alert Center")

    st.caption("Security verification of AI-detected HSE events")

    st.divider()

    st.info("No pending alerts.")

# --------------------------------------------------
# EVENT HISTORY
# --------------------------------------------------

elif page == "Event History":

    st.title("📋 Event History")

    st.caption("Previous HSE safety events")

    st.divider()

    st.info("No events recorded yet.")

# --------------------------------------------------
# HSE SUMMARY
# --------------------------------------------------

elif page == "HSE Summary":

    st.title("📊 HSE Summary")

    st.caption("Basic workplace safety statistics")

    st.divider()

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

    st.info("Violation chart will appear here once events are detected.")
