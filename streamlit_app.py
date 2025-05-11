import streamlit as st
import requests

# Streamlit UI Configuration
st.set_page_config(page_title="Supply Chain Threat Detector", layout="wide")
st.title("🔗 AI-Powered Supply Chain Threat Detector")
st.markdown("Enter a cybersecurity query or concern related to supply chains:")

# Input form
query = st.text_input("Enter your supply chain security concern or question:", "")

if st.button("Analyze"):
    if not query:
        st.warning("Please enter a query before analyzing.")
    else:
        # Use the Docker service name instead of localhost for backend API
        backend_url = "http://backend:8080/detect"

        try:
            response = requests.post(backend_url, json={"query": query}, timeout=15)

            if response.status_code == 200:
                result = response.json()
                st.success("Threat Analysis Completed:")
                st.markdown(f"**Query:** {result.get('query')}")
                st.markdown(f"**Findings:** {result.get('result')}")
                st.markdown(f"**Encrypted Output:** `{result.get('encrypted_output')}`")
            else:
                st.error(f"Error from backend: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend API: {e}")


