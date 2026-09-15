import streamlit as st
from auth import add_user, get_all_users
from db import init_db

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
