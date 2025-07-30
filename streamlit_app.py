import streamlit as st
import pandas as pd

# Title
st.title("Health Equity Simulation Test")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    file_name = uploaded_file.name

    try:
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif file_name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format.")
            df = None

        if df is not None:
            st.success(f"Successfully loaded: {file_name}")
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")
