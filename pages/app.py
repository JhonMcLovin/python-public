import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def load_data():
    data = pd.read_csv(r"https://raw.githubusercontent.com/JhonMcLovin/python-public/main/Covid2023.csv")
    data['date'] = pd.to_datetime(data['date'], format='%d.%m.%Y')
    data.sort_values(by='date', inplace=True)
    return data
    
data = load_data()

unique_locations = data['location'].unique()

st.title("COVID-19 Data Filtering App")

# add_selectbox = st.sidebar.selectbox(
#     "Filter Options",
#     unique_locations
#  )
# # Filter the data based on the selected value
# filtered_data = data[data['location'] == add_selectbox]

# Sidebar filters
st.sidebar.header("Filter Options")

# Filter by country
country = st.sidebar.selectbox("Select Country", df["location"].unique())

# Filter by date with "DD.MM.YYYY" format
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Apply filters
filtered_df = df[(df["location"] == country) & (df["date"] >= start_date) & (df["date"] <= end_date)]

#st.write(f"Data from '{add_selectbox}':")
st.write(f"Data from '{country}' for time period between '{start_date}' and '{end_date}' :")
st.write(filtered_data)



chart_data = filtered_data[['date', 'new_cases_smoothed', 'new_deaths_smoothed']]


st.line_chart(chart_data.set_index('date'))
