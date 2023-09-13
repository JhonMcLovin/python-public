import streamlit as st
import pandas as pd


url = "https://raw.githubusercontent.com/JhonMcLovin/python-public/main/Covid2023.csv"
df = pd.read_csv(url)

df["location"] = pd.to_datetime(df["location"], errors='coerce').dt.date

st.title("COVID-19 Data Filtering App")
st.markdown("This app allows you to filter COVID-19 data from 2023.")

st.sidebar.header("Filter Options")

country = st.sidebar.selectbox("Select Country", df["location"].unique())

start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

filtered_df = df[(df["location"] == country) & (df["date"] > start_date) & (df["date"] < end_date)]


st.header("Filtered Data")
st.write(filtered_df)

if st.button("Download Filtered Data as CSV"):
    with st.spinner("Downloading..."):
        filtered_df.to_csv(f"{country}_covid_data.csv", index=False)
        st.success(f"{country}_covid_data.csv downloaded successfully!")

st.header("Original Data")
st.write(df)
