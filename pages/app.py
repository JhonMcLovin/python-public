import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def load_data():
    data = pd.read_csv(r"https://raw.githubusercontent.com/JhonMcLovin/python-public/main/Covid2023.csv")
    return data
    
data = load_data()

unique_locations = data['location'].unique()

st.title("COVID-19 Data Filtering App")

add_selectbox = st.sidebar.selectbox(
    "Filter Options",
    unique_locations
)


# Filter the data based on the selected value
filtered_data = data[data['location'] == add_selectbox]



st.write(f"Data from '{add_selectbox}':")
st.write(filtered_data)



chart_data = filtered_data[['date', 'total_cases']]


st.line_chart(chart_data.set_index('date'))
