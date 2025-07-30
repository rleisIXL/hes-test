import streamlit as st
import pandas as pd

# Title
st.title("Health Equity Simulation Test")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the file (as a DataFrame if it's CSV)
    df = pd.read_csv(uploaded_file)

    # Display the data
    st.write("Preview of uploaded data:")
    st.dataframe(df)
