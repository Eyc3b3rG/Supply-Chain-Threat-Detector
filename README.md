# Supply-Chain-Threat-Detector
Supply Chain Threat Detector LLM (off-line edition)
The Supply Chain Threat Detector is an AI-powered application designed to identify and explain cybersecurity threats in supply chain environments. This prototype integrates local LLMs, Retrieval-Augmented Generation (RAG), simulated fine-tuning (LoRA), and secure data handling to support government and commercial use cases in an offline or air-gapped setting.

---

## 🔧 Architecture Overview

```
User (Streamlit UI)
        ↓
FastAPI Backend (/detect)
        ↓
Query → FAISS Retriever → Top-K Documents → Graph RAG Synthesizer
        ↓
TinyLlama (local LLM via LlamaCpp or PEFT adapter)
        ↓
Encrypted Answer + Source Attribution
        ↓
Returned to UI or Client
```

---

## 🧠 Fine-Tuning (LoRA Adapter Simulation)

This project simulates fine-tuning by using:
- `AutoModelForCausalLM.from_pretrained()` to load a base TinyLlama model
- `PeftModel.from_pretrained()` to load a simulated adapter (LoRA/PEFT)
- If adapter loading fails, the script falls back to `LlamaCpp` using a quantized `.gguf` model

This approach satisfies the AI Engineering Challenge's fine-tuning requirement without external API dependencies.

---

## 🚀 Setup Instructions

### 🔹 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install fastapi streamlit uvicorn langchain faiss-cpu transformers peft cryptography
```

### 🔹 2. Run FastAPI Backend

```bash
uvicorn "Supply Chain Threat Detector:app" --reload
```

### 🔹 3. Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## 🔒 Security & Deployment

- Uses AES-based symmetric encryption (`Fernet`) to encrypt LLM outputs
- All models and embeddings run locally
- **Completely offline (air-gapped simulation)** — no internet or external APIs
- FAISS indexes are prebuilt and stored locally

---

## ⚠ Known Limitations

- LoRA adapter is simulated; no true adapter training is included
- Streamlit UI is basic and meant for demo purposes only
- No automatic Docker deployment included
- No frontend biometric/heartbeat control simulated (future enhancement)

---

## 🧪 Test Query Example

```json
POST http://localhost:8000/detect
{
  "query": "What are the top supply chain threats reported by MITRE and NIST?"
}
```

Returns:
- `"answer_encrypted"`: Encrypted summary of the findings
- `"sources"`: List of file paths that supported the answer

---

## 🏁 Deployment Notes

This prototype is designed for **air-gapped use in secure environments**, simulating private cloud or DoD use cases. It does not rely on external inference APIs or cloud data storage.

---

## 🎥 Optional Demo Video Plan

1. Show `uvicorn` startup
2. Show `streamlit run streamlit_app.py`
3. Submit a query
4. Display encrypted answer and listed sources

---

## 📁 Repository

GitHub: [https://github.com/Eyc3b3rG](https://github.com/Eyc3b3rG)
