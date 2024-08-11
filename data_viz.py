import streamlit as st
import pandas as pd
st.markdown("<h1 style = 'text-align: centre'> DATA VISUALIZATION</h1>",unsafe_allow_html=True )
file_name = []
files  = st.file_uploader("Upload files here",type='csv', accept_multiple_files= True)

if files:
    for file in files:
        file_name.append(file.name)
    print(file_name)