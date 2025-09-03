import streamlit as st

#Page Navigation
pages=[
    st.Page(page:"app_pages/Demographics.py", title="Demographics")
    st.Page(page:"app_pages/Initial_Evaluation.py", title="Initial Evaluation")
]

#Adding pages to the sidebar
pg = st. navigation(paged, postition="sidebar", expanded=True)

#Running the app
pr.run()

st.set_page_config(page_title="Simulation Data", layout="wide")

# Content
st.markdown("<h2 style='color:#1F6B51; font-weight:bold;'>HEALTH EQUITY SIMULATION</h2>", unsafe_allow_html=True)
