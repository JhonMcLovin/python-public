import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data # Caching to improve performance
def load_data():
    data = pd.read_csv(r"C:\Users\janis\Desktop\Nosleguma_Darbs\Streamlit\data\board_games.csv")
    return data

data = load_data()

unique_group_names = data['Board game type'].unique()

add_selectbox = st.sidebar.selectbox(
    "What type of board games would you like to see?",
    (unique_group_names)
)

# Filter the data based on the selected value
filtered_data = data[data['Board game type'] == add_selectbox]

# Create a Streamlit app
st.title(f"Board Games of Type: {add_selectbox}")
st.write(f"List of board games of type '{add_selectbox}':")
st.write(filtered_data)

# Concatenate unique 'Board game name' values based on the selected type
concatenated_names = filtered_data['Board game name'].unique().tolist()
concatenated_text = ', '.join(concatenated_names)

concatenated_man = filtered_data['Board game manufacturer'].unique().tolist()
concatenated_text2 = ', '.join(concatenated_man)

st.write(f"Concatenated 'Board game name' values for '{add_selectbox}':")
st.text(concatenated_text)

st.write(f"Concatenated 'Board game name' values for '{add_selectbox}':")
st.text(concatenated_text2)