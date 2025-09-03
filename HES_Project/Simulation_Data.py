import streamlit as st

def page_link():
    st.page_link("app_pages/Demographics.py", label="Demographics Page")
    st.page_link("app_pages/Initial_Evaluation.py", label="Eval Page")

st.set_page_config(page_title="Simulation Data", layout="wide")

# Content
st.markdown("<h2 style='color:#1F6B51; font-weight:bold;'>HEALTH EQUITY SIMULATION</h2>", unsafe_allow_html=True)
