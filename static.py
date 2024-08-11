import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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

st.markdown('---')
st.write("Using sns for boxplot and finding the spends for different sex")

with st.container():
    fig,ax = plt.subplots()
    sns.set_theme(style="darkgrid")
    
    sns.boxplot(x="sex", y="total_bill", data=df, hue = "sex")
    st.pyplot(fig)

st.markdown('---')
st.write("Using plotly for boxplot and finding the spends for different sex")
with st.container():
    fig = px.box(df, x="sex", y="total_bill",color="smoker",color_discrete_sequence=["#3498db", "#e74c3c"])
    st.plotly_chart(fig)


st.markdown('---')
st.write("Using plotly and finding the spends for different sex but now  you choose which chart you want to display")
chart = ('box','violin','histogram')
chart_select = st.selectbox("Please choose one chart type",chart)
with st.container():
    if chart_select == 'box':
        fig = px.box(df, x="sex", y="total_bill",color="smoker",color_discrete_sequence=["#3498db", "#e74c3c"])
        st.plotly_chart(fig)
    elif chart_select == 'violin':
        fig = px.violin(df, x="sex", y="total_bill",color="smoker",color_discrete_sequence=["#3498db", "#e74c3c"])
        st.plotly_chart(fig)
    elif chart_select == 'histogram':
        fig = px.histogram(df, x="sex", y="total_bill",color="smoker",color_discrete_sequence=["#3498db", "#e74c3c"])
        st.plotly_chart(fig)
st.markdown('---')
# st.write("Using plotly and finding the spends for different sex but now  you choose which chart you want to display")
df_grouped = df.groupby(['day','sex'])['total_bill'].sum().reset_index()
st.write(df_grouped)
with st.container():
    fig = px.line(df_grouped, x="day", y="total_bill", color="sex", color_discrete_sequence=["#3498db", "#e74c3c"])
    st.plotly_chart(fig)


# st.markdown('---')
# st.write("Using plotly and finding the spends for different columns")

# feature = ["total_bill"]
# columns_selected = st.multiselect("Select columns to display", cat_columns)
# chart_type = st.selectbox("Select chart type", ["line", "bar"])

# if columns_selected:  # Check if columns_selected is not empty
#     df_grouped = df.groupby(columns_selected)[feature].sum().reset_index()

#     if chart_type == "line":
#         fig = px.line(df_grouped, x=columns_selected[0], y=feature[0], color_discrete_sequence=["#3498db", "#e74c3c"])
#     elif chart_type == "bar":
#         fig = px.bar(df_grouped, x=columns_selected[0], y=feature[0], color_discrete_sequence=["#3498db", "#e74c3c"])

#     st.plotly_chart(fig)
# else:
#     st.write("Please select at least one column to display.")