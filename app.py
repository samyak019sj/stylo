import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="StyleSense AI",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# LOAD CSS
# ==============================

def load_css():
    try:
        with open("assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

load_css()

# ==============================
# IMPORT PAGES
# ==============================

from pages import (
    home,
    upload,
    wardrobe,
    dashboard,
    recommendation,
    settings
)

from auth import (
    login,
    register
)

# ==============================
# SESSION STATE
# ==============================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("👔 StyleSense AI")

if st.session_state.logged_in:

    st.sidebar.success(
        f"Welcome {st.session_state.user[1]}"
    )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

# ==============================
# NAVIGATION
# ==============================

if st.session_state.logged_in:

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Upload",
            "Wardrobe",
            "Recommendation",
            "Dashboard",
            "Settings"
        ]
    )

else:

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Login",
            "Register"
        ]
    )

# ==============================
# ROUTING
# ==============================

if page == "Home":
    home.show()

elif page == "Login":
    login.show()

elif page == "Register":
    register.show()

elif page == "Upload":
    upload.show()

elif page == "Wardrobe":
    wardrobe.show()

elif page == "Recommendation":
    recommendation.show()

elif page == "Dashboard":
    dashboard.show()

elif page == "Settings":
    settings.show()
