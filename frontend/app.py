""" Sample UI page with text box for input and submit button to get response from backend query pipeline.py"""


import streamlit as st
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from rag_pipeline.query_pipeline import query_pipeline

st.set_page_config(page_title="Mithra Solutions Internal Copilot")


st.title("Mithra Solutions - Internal Code Copilot")

st.markdown("""
This tool helps you query internal codebases, SDKs, hardware APIs, error codes, and documentation.
""")

user_query = st.text_area("Enter your technical question:", height=150,
                          placeholder="e.g. How is HDMI handshake handled?")

submit_btn = st.button("Get Answer")

if submit_btn and user_query.strip() != "":
    with st.spinner("Processing..."):
        answer = query_pipeline(user_query)

    st.subheader("Answer:")
    st.write(answer)

elif submit_btn and user_query.strip() == "":
    st.warning("Please enter a valid question before submitting.")

st.markdown("---")
st.markdown("Mithra Solutions © 2024 - Internal AI Copilot Prototype")
