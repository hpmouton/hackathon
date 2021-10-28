import streamlit as st
import pandas as pd
import datetime 
import altair as alt

st.write(""" # IndabaX Hackathon 2021 """)
st.write(""" ## Team Innate """)

df = pd.read_csv("./dataset.csv")
sorted_data = df.sort_values('DATE',ascending=True)
sorted_data[['DATE']] = sorted_data[['DATE']].applymap(str).applymap(lambda s: "{}/{}/{}".format(s[4:6],s[6:], s[0:4]))
st.title("Sample Data")
st.write(sorted_data.head(20))

#Dataframe for Installed_Preactive SDP_Status
status = "INSTALLED_PREACTIVE"
new_users_df = sorted_data[sorted_data['SDP_STATUS'].str.contains(status)]
st.title("New User Data")
st.write(new_users_df.head(20))
#Dataframe for Expired SDP_Status
status = "EXPIRED"
ex_users_df = sorted_data[sorted_data['SDP_STATUS'].str.contains(status)] 
st.title("Expired Data")
st.write(ex_users_df.head(20))

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

c = alt.Chart(new_users_df).mark_circle().encode(x='DATE', y='SDP_STATUS')

st.altair_chart(c, use_container_width=True)