import streamlit as st
from auth import add_user, get_all_users, create_otc
from db import init_db
from email_service import send_otc_email

# Ensure tables exist when app starts
init_db()

st.title("User Management")

# --- User Registration Form ---
with st.form("add_user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add User")

    if submitted:
        if name and email:
            success = add_user(name, email)
            if success:
                st.success(f"User '{name}' added successfully!")
            else:
                st.error("Email already exists.")
        else:
            st.warning("Please fill out both fields.")

# --- Display Registered Users ---
st.subheader("Current Users")
users = get_all_users()

if users:
    st.dataframe(users)  # Streamlit accepts lists of dicts directly!
else:
    st.info("No users registered yet.")

st.subheader("Request Login Code")

with st.form("request_otc_form"):
    login_email = st.text_input("Email address")
    request_otc = st.form_submit_button("Send Login Code")

    if request_otc:
        if login_email:
            otc = create_otc(login_email)

            if otc:
                 send_otc_email(login_email, otc)
                 st.success("Login code sent. Check your email.")
            else:
                st.error("No user found with that email address.")
        else:
            st.warning("Please enter your email address.")
