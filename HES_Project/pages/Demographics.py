import streamlit as st

st.set_page_config(page_title="Demographics", layout="wide")

# Header
st.markdown(
    f"""
    <div style='background-color:#1F6B51;padding:10px;display:flex;align-items:center;justify-content:flex-end;'>
        <div>
            <a href="/dashboard" style="color:white;margin-right:20px;">Dashboard</a>
            <a href="/reports" style="color:white;margin-right:20px;">Reports</a>
            <a href="/logout" style="color:white;margin-right:20px;">Log Out</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Content
st.markdown("<h2 style='color:#1F6B51; font-weight:bold;'>HEALTH EQUITY SIMULATION</h2>", unsafe_allow_html=True)