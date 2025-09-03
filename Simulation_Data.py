import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Simulation Data", "Demographics", "Initital Evaluation"],
    )

if selected == "Simulation Data":
    st.title("Simulation Data")
if selected == "Demographics":
    st.title("Demographics")
if selected == "Initital Evaluation":
    st.title("Initial Eval")


# Content
st.markdown("<h2 style='color:#1F6B51; font-weight:bold;'>HEALTH EQUITY SIMULATION</h2>", unsafe_allow_html=True)
