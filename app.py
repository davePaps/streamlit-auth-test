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
# login user

if st.button("Login user"):
    match = users_df[
        users_df["email"].str.strip().str.lower() == email.strip().lower()
    ]

    if not match.empty:
        name = match.iloc[0]["name"]
        st.success(f"Hello {name}")
    else:
        st.error("Get lost")

st.subheader("Users")

st.dataframe(users_df)
