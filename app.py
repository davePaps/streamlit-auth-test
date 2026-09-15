import streamlit as st
from data import users_df
from auth import add_user

st.title("OTC Login Test")

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Add user"):
    users_df, added = add_user(users_df, name, email)

    if added:
        st.success("User added")
    else:
        st.error("That email already exists")

st.subheader("Users")

st.dataframe(users_df)
