# this code shows how to add background images in web app

import streamlit as st

st.markdown("""
    <style>
        .stApp {
        background: url("https://images.unsplash.com/photo-1601850494422-3cf14624b0b3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        }
        [data-testid="stHeader"]{
            background-color: rgba(0,0,0,0);
            }
    </style>""", unsafe_allow_html=True)

st.title("Welcome to my Streamlit App")
