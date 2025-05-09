# streamlit_app.py 

import streamlit as st
import requests 

st.title("Supply Chain Threat Detector")
st.write("Detect potential threats in your supply chain data using advanced AI models.")
st.write("Upload your data files and get insights on potential threats.")

query = st.text_input("Enter your supply chain query:")

if st.button("Submit Query"):
    response = requests.post("http://localhost:8000/detect", json={"query": query})
    if response.status_code == 200:
        data = response.json()
        st.write("Encrypted Answer: ")
        st.code(data["answer_encrypted"])
        st.write("Sources:")
        st.json(data["Sources"])
    else:
        st.error("Error: " + response.text)
