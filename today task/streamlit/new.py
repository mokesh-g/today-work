import streamlit as st

st.title("Hello streamlit")
name = st.text_input("Enter your name:")

if st.button("submit"):
    st.success(f"Welcome {name} 🎉")