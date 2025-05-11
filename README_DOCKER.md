# 🐳 Docker Setup for Supply Chain Threat Detector

This guide explains how to build, test, and deploy the Supply Chain Threat Detector application using Docker.

---

## 📦 Local Build and Run Instructions

### Build and Start Docker Containers

Run the following command from the project root to build and launch the containers:

```bash
docker-compose up --build
```

Or double-click the provided script:

```bash
rebuild_docker.bat
```

### Access the Application

- **Frontend (Streamlit)**: [http://localhost:8501](http://localhost:8501)
- **Backend (FastAPI)**: [http://localhost:8080/docs](http://localhost:8080/docs)

---

## 🔐 Environment and Model Setup

Ensure the following before running:

- A `.env` file in the root directory if sensitive variables are needed.
- Preload or mount your `./models` and `./data` folders with required `.gguf` and `.txt` files respectively.

---

## 🚀 Publishing Docker Image to Docker Hub

### Step 1: Tag the Local Image

```bash
docker tag supply-chain-threat-detector eyc3b3rg/supply-chain-threat-detector:latest
```

### Step 2: Push the Tagged Image

```bash
docker push eyc3b3rg/supply-chain-threat-detector:latest
```

Ensure you are authenticated using Docker CLI:

```bash
docker login -u eyc3b3rg
# Use your Docker Hub Personal Access Token (PAT) as the password
```

View the public image:  
👉 https://hub.docker.com/r/eyc3b3rg/supply-chain-threat-detector

---

## 📁 Additional Notes

- Use `.dockerignore` to exclude unnecessary files from the Docker build context.
- The backend image supports `llama-cpp-python` and `faiss-cpu`.
- Streamlit is hosted at port `8501`, FastAPI at port `8080`.

---

## 🛠 Maintenance

To clean up and rebuild from scratch:

```bash
docker-compose down
docker system prune -af
rebuild_docker.bat
```

---

*Last updated: Finalized Docker image for external review.*


