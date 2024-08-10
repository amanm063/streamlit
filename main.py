import streamlit as st
import pandas as pd
table1 = pd.DataFrame({"column1": [1, 2, 3, 4, 5],"column2": [5,6,7,8,9]})
st.title("my name is aman")
st.subheader("and this is my website. WELCOME!")
st.header("and I am running this on streamlit")
#link in readme for both markdown and latex
st.markdown("**aman** *malik*")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json_dict = {"a":"1,234", "b": "3.24,23"}
st.json(json_dict)

code_block = """
def func(abc):
    print(abc)    
"""

st.code(code_block)

# we can do all these codes,json and latex and MK using write function

st.write("## HEADING 2 ")

# st.metric fx is used as a fx to show changes. 

st.metric(label="Portfolio", value= "200,000", delta="-20%")

# putting table in a container is not necessary but table is always static if we want to add sorting and all to the  table then we should use dataframe
with st.expander("My Table"):
    st.table(table1)
st.dataframe(table1)

# st.image for images, video and audio has same fx
st.image("https://i.imgur.com/6yGZQ6B.jpg")

# ctrl c to close the server

