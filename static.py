import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Matplot lib static plots")
df = pd.read_csv("tips.csv")
# df.set_index(df.columns[0])

# st.dataframe(df.head())
# to remove index I am making the 1st column as index
st.dataframe(df.head().set_index(df.columns[0]))

st.markdown("---")

data_types = df.dtypes
cat_columns =  tuple(data_types[data_types == "object"].index) 



with st.container():
    feature = st.selectbox("select the column you want to display",  cat_columns)
    counts = df[feature].value_counts()
    with st.expander(label="click here to see the charts"):
    # Plot the results as a bar graph
        
        st.subheader("Bar Graph")
        sns.set_style('whitegrid')
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(counts.index, counts.values, color=['skyblue', 'pink'])
        ax.set_xlabel(feature)
        ax.set_ylabel("Count")
        ax.set_title("counts as a graph")
        ax.tick_params(axis='x', rotation=45)
        for i, (label, value) in enumerate(zip(counts.index, counts.values)):
            ax.text(i, value + 3, f"{value}", ha='center', va='bottom')
        # st.write("")  # add some whitespace
        # fig.tight_layout()
        st.pyplot(fig, clear_figure=False)
        # st.write("")  # add some whitespace
    
# Plot the results as a pie chart
        st.subheader("Pie Chart")
        sns.set_style('whitegrid')
        fig, ax = plt.subplots(figsize=(7, 6))
        ax.pie(counts.values, labels=counts.index, colors=['skyblue', 'pink'], autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax.set_title("counts shown as pie chart")
        # st.write("")  # add some whitespace
        # fig.tight_layout()
        st.pyplot(fig, clear_figure=False)
        # st.write("")  # add some whitespace