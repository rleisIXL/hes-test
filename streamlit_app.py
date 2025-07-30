import streamlit as st

# Title
st.title("File Upload Example")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "pdf", "png", "jpg"])

# Check if a file has been uploaded
if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)
    
    # For text files
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text(content)

    # For CSV files
    elif uploaded_file.type == "text/csv":
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    # For images
    elif uploaded_file.type in ["image/png", "image/jpeg"]:
        from PIL import Image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # For PDF
    elif uploaded_file.type == "application/pdf":
        st.write("PDF file uploaded. Processing not implemented in this example.")
