import streamlit as st

from database.database import login_user


def show():

    st.title("🔐 Login")

    st.write("Login to access your wardrobe.")

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    remember = st.checkbox(
        "Remember Me"
    )

    if st.button("Login", use_container_width=True):

        if email == "" or password == "":
            st.error("Please fill all fields.")
            return

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.user = user

            st.success("Login Successful!")

            st.balloons()

            st.rerun()

        else:

            st.error("Invalid Email or Password")

    st.divider()

    st.info(
        "Don't have an account? Go to Register."
    )
