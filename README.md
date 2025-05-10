
# 🛡️ Supply Chain Threat Detector

This app uses local LLMs and vector embeddings to identify potential cybersecurity threats in supply chain documents.

---

## 🚀 How to Run the App

### ✅ Prerequisites

- Python 3.11+
- Install requirements:

```bash
pip install -r requirements.txt
```

---

## 🔄 Launch the App (Windows)

1. **Double-click** `launch_app.bat`:
   - Auto-fetches 5 supply chain cybersecurity PDFs
   - Converts them to `.txt` (5–10 pages each)
   - Replaces existing text files
   - Validates file structure
   - Builds vector store
   - Starts FastAPI backend on `http://localhost:8000`

2. **In a second terminal**, run:

```bash
streamlit run streamlit_app.py
```

3. Navigate to `http://localhost:8501` in your browser.

---

## 🧠 LLM + Embedding Details

- **LLM:** TinyLlama `.gguf` model via LlamaCpp
- **Embeddings:** Local BAAI `bge-small-en-v1.5` using Hugging Face **locally** via LangChain (✅ rules compliant)

---

## 🔐 Windows Firewall Exception

If Python is blocked, open PowerShell (as Admin) and run:

```powershell
New-NetFirewallRule -DisplayName "Allow Python for FastAPI" -Direction Inbound -Action Allow -Program "$($env:LOCALAPPDATA)\Programs\Python\Python311\python.exe" -Profile Domain,Private,Public -Protocol TCP -LocalPort 8000
```

Or go to:
```
Control Panel > Windows Defender Firewall > Allow an app or feature
```

✅ Ensure **Python** is checked for Domain, Private, and Public.

---

## 📁 Directory Structure

```
Supply_Chain_Threat_Detector/
├── data/                        # 5 auto-fetched and validated .txt files
├── models/                     # TinyLlama .gguf models
├── backend_api.py              # FastAPI backend
├── streamlit_app.py            # Streamlit UI
├── launch_app.bat              # Launcher script (Windows)
├── validate_data.py            # Ensures proper .txt file quality
├── requirements.txt
└── README.md
```

---

## 📜 License

MIT
