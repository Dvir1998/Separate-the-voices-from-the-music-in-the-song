import os
import streamlit as st

UPLOAD_DIR = "uploads"

def upload_file():
    st.header("העלאת קובץ שיר")

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    uploaded_file_path = None

    uploaded_file = st.file_uploader("בחר קובץ שיר", type=["mp3", "wav"], accept_multiple_files=False)
    
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        uploaded_file_path = file_path
        st.success(f"הקובץ {uploaded_file.name} הועלה בהצלחה.")

    return uploaded_file_path