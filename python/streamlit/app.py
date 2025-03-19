import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Apoorv")

## Display a simple text
st.write("This is a simple text")

## create a dataframe
df  = pd.DataFrame({
    '1st':[ 1,2,3,4],
    '2nd': [10,20,30,40]})

st.write("This is a Dataframe")
st.write(df)

## create a Line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)