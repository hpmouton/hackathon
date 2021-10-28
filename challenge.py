import streamlit as st
import pandas as pd

st.write(""" # IndabaX Hackathon 2021 """)
st.write(""" ## Team Innate """)

df = pd.read_csv("./dataset.csv")
st.title("Sample Data")

st.write(df.head())