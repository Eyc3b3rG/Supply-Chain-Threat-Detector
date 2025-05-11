# 🐳 Docker Deployment: Supply Chain Threat Detector

This repository contains a containerized AI-powered application that detects cybersecurity risks in supply chain data using LLMs and embeddings.

---

## 📁 Pre-Setup Instructions

### ✅ 1. Place Your LLM Model in the `models/` Folder
Ensure the `models/` folder exists and contains your `.gguf` LLM file:

```bash
mkdir -p models
mv tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf models/
```

> If you're using `.dockerignore`, make sure `models/` is **not excluded**.

---

### ✅ 2. Environment Variables (`.env`)
(Optional) Create a `.env` file if your app references environment-specific paths:

```env
MODEL_PATH=models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
VECTOR_STORE=vector_index.pkl
```

---

## 🚀 Step-by-Step Docker Instructions

### 🏗️ Build & Launch the Application

From the root of your project (where `docker-compose.yml` is located):

```bash
docker-compose up --build
```

This will:
- Build the **backend** (FastAPI) on `http://localhost:8080`
- Launch the **frontend** (Streamlit) on `http://localhost:8501`

---

### 🌐 Access the App in Your Browser

- Frontend (Streamlit): http://localhost:8501
- Backend (FastAPI): http://localhost:8080
- Swagger API Docs: http://localhost:8080/docs

---

### 🛑 To Stop the App

```bash
docker-compose down
```

---

## ⚡ One-Click Rebuild (Windows)

For convenience, Windows users can use the included `rebuild_docker.bat`:

```cmd
rebuild_docker.bat
```

This script:
- Stops existing containers
- Rebuilds Docker images with code and dependency changes
- Relaunches the services cleanly

> Double-click it from File Explorer or run from a Windows Command Prompt.

---

## 📝 Notes

- Always use `localhost` in the browser (not `0.0.0.0`)
- Make sure the backend URL in `streamlit_app.py` is set to: `http://backend:8080/detect` (not `localhost`)
