import streamlit as st
import pandas as pd
import datetime 
import plotly as px

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

def plot_raw_data():
    fig = px.Figure()
    fig.add_trace(px.Scatter(x=new_users_df['DATE'], y=new_users_df['SDP_STATUS'], name="New Users This Year"))
    fig.add_trace(px.Scatter(x=new_users_df['DATE'], y=new_users_df['SDP_STATUS'], name="New Users This Year"))

    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
plot_raw_data()

