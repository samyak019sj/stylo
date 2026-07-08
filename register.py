import streamlit as st

from database.database import add_user


def show():

    st.title("📝 Create Account")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email Address"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button(
        "Register",
        use_container_width=True
    ):

        if (
            name == ""
            or email == ""
            or password == ""
        ):

            st.error("Please fill all fields.")
            return

        if password != confirm_password:

            st.error("Passwords do not match.")
            return

        success = add_user(
            name,
            email,
            password
        )

        if success:

            st.success(
                "Registration Successful!"
            )

            st.info(
                "Please login using your account."
            )

        else:

            st.error(
                "Email already exists."
            )

    st.divider()

    st.caption(
        "StyleSense AI © 2026"
    )
