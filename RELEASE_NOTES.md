# 🚀 Release: v1.0.0-docker

**Release Date:** May 9, 2025  
**Status:** ✅ Stable | 📦 Ready for Public Use

---

## 🔍 Overview

This release introduces a fully Dockerized version of the **Supply Chain Threat Detector**, an AI-driven threat assessment platform leveraging local LLMs and RAG pipelines for secure, offline analysis of supply chain documentation.

Key features:
- Streamlit frontend with clean UX
- FastAPI backend serving LLM inferences
- Vector-based retrieval using `faiss-cpu`
- Works with local `.txt` inputs and `.gguf` model files
- Dockerized for seamless deployment and sharing

---

## 📦 How to Use

### Clone the repository
```bash
git clone https://github.com/Eyc3b3rG/Supply-Chain-Threat-Detector
cd Supply-Chain-Threat-Detector
```

### Start the application
```bash
docker-compose up --build
```

### Or pull and run from Docker Hub
```bash
docker pull eyc3b3rg/supply-chain-threat-detector:latest
docker run -p 8501:8501 -p 8080:8080 eyc3b3rg/supply-chain-threat-detector
```

---

## 🛠️ What’s Included

- ✅ `Dockerfile` for backend
- ✅ `docker-compose.yml` to run frontend + backend
- ✅ `.dockerignore` optimization
- ✅ `README_DOCKER.md` usage documentation
- ✅ `rebuild_docker.bat` script for Windows
- ✅ `requirements.txt` with version-pinned dependencies

---

## 🧪 Tested On

- Docker Desktop for Windows (v4.30+)
- Python 3.11 base image
- Compatible with TinyLLaMA and GGUF model formats

---

## 📎 Links

- 🔗 Docker Hub: [eyc3b3rg/supply-chain-threat-detector](https://hub.docker.com/r/eyc3b3rg/supply-chain-threat-detector)
- 🔗 GitHub Repo: [github.com/Eyc3b3rG/Supply-Chain-Threat-Detector](https://github.com/Eyc3b3rG/Supply-Chain-Threat-Detector)

---