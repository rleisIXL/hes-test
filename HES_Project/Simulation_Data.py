import streamlit as st

st.set_page_config(page_title="Simulation Data", layout="wide")

st.markdown(
    """
    <style>
        /* Sidebar background color */
        section[data-testid="stSidebar"] {
            background-color: #f0f0f5;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.title("Sidebar")
st.sidebar.write("This is a customized sidebar.")

# Content
st.markdown("<h2 style='color:#1F6B51; font-weight:bold;'>HEALTH EQUITY SIMULATION</h2>", unsafe_allow_html=True)
