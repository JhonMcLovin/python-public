import streamlit as st
import pandas as pd

# Load the data from the provided URL
url = "https://raw.githubusercontent.com/JhonMcLovin/python-public/main/Covid2023.csv"
df = pd.read_csv(url)
df["location"] = pd.to_datetime(df["location"], errors='coerce').dt.date
# Streamlit app title and description
st.title("COVID-19 Data Filtering App")
st.markdown("This app allows you to filter COVID-19 data from 2023.")

# Sidebar filters
st.sidebar.header("Filter Options")

# Filter by country
country = st.sidebar.selectbox("Select Country", df["location"].unique())

# Filter by date with "DD.MM.YYYY" format
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Apply filters
filtered_df = df[(df["location"] == country) & (df["date"] > start_date) & (df["date"] < end_date)]

# Display the filtered data
st.header("Filtered Data")
st.write(filtered_df)

# Download filtered data as CSV
if st.button("Download Filtered Data as CSV"):
    with st.spinner("Downloading..."):
        filtered_df.to_csv(f"{country}_covid_data.csv", index=False)
        st.success(f"{country}_covid_data.csv downloaded successfully!")

# Show the original data
st.header("Original Data")
st.write(df)
