import streamlit as st
import pandas as pd
import datetime 
from plotly import graph_objs as px

st.write(""" # IndabaX Hackathon 2021 """)
st.write(""" ## Team Innate """)

df = pd.read_csv("./dataset.csv")
sorted_data = df.sort_values('DATE',ascending=True)
st.title("Sample Data")
st.write(sorted_data.head(20))
#Dataframe for Installed_Preactive SDP_Status
status = "INSTALLED_PREACTIVE"
new_users_df = df[df['SDP_STATUS'].str.contains(status)] 
st.title("New User Data")
st.write(new_users_df.head(20))
#Dataframe for Expired SDP_Status
status = "EXPIRED"
ex_users_df = df[df['SDP_STATUS'].str.contains(status)] 
st.title("Expired Data")
st.write(ex_users_df.head(20))

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

numOfNewUsers = len(new_users_df)
numOfExpiredUsers = len(ex_users_df)

chart_data = pd.DataFrame(new_users_df)
st.line_chart(chart_data)
