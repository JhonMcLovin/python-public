import streamlit as st
import pandas as pd


url = "https://raw.githubusercontent.com/JhonMcLovin/python-public/main/Covid2023.csv"
df = pd.read_csv(url)


st.title("COVID-19 Data Filtering App")
st.markdown("This app allows you to filter COVID-19 data from 2023. Please wait while the data is loading...")

st.sidebar.header("Filter Options")

country = st.sidebar.selectbox("Select Country", df["location"].unique())

start_date = st.sidebar.date_input("Start Date", format="DD.MM.YYYY")
end_date = st.sidebar.date_input("End Date", format="DD.MM.YYYY")

filtered_df = df[(df["location"] == country)# & (df["date"] > start_date) & (df["date"] < end_date)]

st.header("Filtered Data")
st.write(df)

# Download filtered data as CSV
# if st.button("Download Filtered Data as CSV"):
#     with st.spinner("Downloading..."):
#         filtered_df.to_csv(f"{country}_covid_data.csv", index=False)
#         st.success(f"{country}_covid_data.csv downloaded successfully!")

# Show the original data
# st.header("Original Data")
# st.write(df)
