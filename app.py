import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI-HSE VisionGuard",
    page_icon="🦺",
    layout="wide"
)

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

    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Cameras Online",
            "3"
        )

    with col2:
        st.metric(
            "Active Alerts",
            "0"
        )

    with col3:
        st.metric(
            "Confirmed Violations",
            "0"
        )

    with col4:
        st.metric(
            "False Alarms",
            "0"
        )

    st.divider()

    st.subheader("System Status")

    st.success("🟢 All camera systems are online.")

    st.info(
        "No active HSE safety alerts require Security verification."
    )

# --------------------------------------------------
# CAMERA MONITORING
# --------------------------------------------------

elif page == "Camera Monitoring":

    st.title("📹 Camera Monitoring")

    st.caption("Multiple workplace camera feeds")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("CAM-01")
        st.write("📍 Production Area")
        st.info("Camera feed will appear here.")
        st.success("🟢 Monitoring")

    with col2:

        st.subheader("CAM-02")
        st.write("📍 Workshop")
        st.info("Camera feed will appear here.")
        st.success("🟢 Monitoring")

    st.divider()

    st.subheader("CAM-03")
    st.write("📍 Conveyor Area")
    st.info("Camera feed will appear here.")
    st.success("🟢 Monitoring")

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


