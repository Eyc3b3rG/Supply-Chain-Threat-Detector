# Supply Chain Threat Detector (Updated)

This AI-powered application identifies and explains cybersecurity threats in supply chains. It features a local LLM with Retrieval-Augmented Generation (RAG) and simulated LoRA fine-tuning.

---

## 🧱 Architecture

```
Streamlit UI → FastAPI Backend → FAISS VectorStore → TinyLlama (LoRA or LlamaCpp)
                                 ↓
                       Encrypted Answer + Source Attribution
```

---

## 🔄 Auto PDF-to-TXT Pipeline

Before building the vector store, the app:
- Downloads latest cybersecurity PDFs from trusted sources (e.g., NIST, MITRE)
- Validates that PDFs have at least 5 pages and aren't encrypted
- Converts to `.txt` and replaces files in `/data` folder

---

## 🚀 Quickstart

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run backend:

```bash
uvicorn backend_api:app --reload
```

3. Launch UI:

```bash
streamlit run streamlit_app.py
```

---

## ✅ AI Engineering Challenge Compliance

- No public inference APIs used
- Offline LLM (TinyLlama) with optional adapter simulation
- Local vector search (FAISS)
- RAG + Graph RAG logic included
- Encrypted output using `cryptography.Fernet`
- Sources cited per answer

---

## 📁 Inputs

All documents auto-updated to:

- `./data/intel_supply_chain_protections.txt`
- `./data/microsoft_silk_typhoon_case.txt`
- `./data/mitre_system_of_trust.txt`
- `./data/nist_supply_chain_guidance.txt`
- `./data/supply_chain_risks.txt`