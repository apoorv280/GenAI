import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your Name.")




if name:
    st.write(f"Hello, {name}")

age  = st.slider("Select Your AGE:", 0,100,25)
st.write(f"You are {age} years old")

options = ['Python','JAVA','R']
choice = st.selectbox("Choose Your Language to work:", options)
st.write(f"You Selected {choice}")

data = {
    "Name": ['A','P','AP','PG'],
    "Age": [24,23,32,30],
    "City": ['Pune','Toronto','Delhi','Ireland']
}

df = pd.DataFrame(data)
df.to_csv('Sample.csv')
st.write(df)

uploaded_file = st.file_uploader("choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
