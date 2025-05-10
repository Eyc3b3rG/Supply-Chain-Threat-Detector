import streamlit as st
import requests

st.title("Supply Chain Threat Detector")
st.write("Detect potential threats in your supply chain using an AI-powered LLM + RAG engine.")

query = st.text_input("Enter your supply chain query:")

if st.button("Submit Query"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        try:
            response = requests.post("http://localhost:8000/detect", json={"query": query}, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            st.success("Encrypted Answer:")
            st.code(data["answer_encrypted"])

            st.success("Sources Used:")
            st.json(data["sources"])

        except requests.exceptions.ConnectionError:
            st.error("🚫 Could not connect to the backend at http://localhost:8000.\n\nMake sure it's running.")

        except requests.exceptions.Timeout:
            st.error("⏳ The request timed out. Try again later.")

        except requests.exceptions.HTTPError as e:
            st.error(f"❌ Server error: {e.response.status_code} — {e.response.text}")

        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
