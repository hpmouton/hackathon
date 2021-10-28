import streamlit as st
import pandas as pd
import datetime 


st.write(""" # IndabaX Hackathon 2021 """)
st.write(""" ## Team Innate """)

df = pd.read_csv("./dataset.csv")
sorted_data = df.sort_values('DATE',ascending=True)
st.title("Sample Data")

st.write(sorted_data.head())