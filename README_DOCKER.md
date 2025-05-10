# 🐳 Docker Deployment Guide: Supply Chain Threat Detector

This guide explains how to containerize and deploy the Supply Chain Threat Detector using Docker and Docker Compose.

---

## ✅ Prerequisites

- Docker Desktop installed: https://www.docker.com/products/docker-desktop/
- (Optional) Docker Compose (included with Docker Desktop)

---

## 📁 File Structure

```
.
├── Dockerfile
├── .dockerignore
├── docker-compose.yml
├── backend_api.py
├── streamlit_app.py
├── requirements.txt
└── data/
```

---

## 🧱 Option 1: Single Container (Backend + Frontend in One Image)

### 🔨 Build the Docker Image

```bash
docker build -t supply-chain-threat-detector .
```

### ▶️ Run the Container

```bash
docker run -p 8501:8501 -p 8080:8080 supply-chain-threat-detector
```

### 🌐 Access the App

- Streamlit UI: http://localhost:8501
- FastAPI Swagger Docs: http://localhost:8080/docs

---

## 🧩 Option 2: Docker Compose (Backend & Frontend as Separate Services)

### ▶️ Start with Compose

```bash
docker-compose up --build
```

This builds and runs:
- `backend` on port 8080
- `frontend` (Streamlit) on port 8501

### 🛑 Stop Containers

```bash
docker-compose down
```

---

## 🔐 Notes

- The app runs fully offline with no external API calls.
- If using `.env` for secrets, add it to `.dockerignore`.

---

## 🧼 Clean Up

```bash
docker system prune -a
```

---

## 📦 Ready for Submission

Ensure that your `.gguf` model and large files (if any) are either ignored or separately documented in your submission.

---