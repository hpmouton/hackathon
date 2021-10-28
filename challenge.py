import streamlit as st
import pandas as pd

st.write(""" # IndabaX Hackathon 2021 """)

df = pd.read_csv("./dataset.csv")
st.title("Hello world!")
data = st.dataframe(df)

st.table(data,5)