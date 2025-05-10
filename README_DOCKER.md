# 🚢 Docker Deployment Guide for Supply Chain Threat Detector

This guide provides step-by-step instructions for building and running the Supply Chain Threat Detector locally using Docker on Windows (x86_64).

---

## 📥 Prerequisites

### 1. Install Docker Desktop for Windows (x86_64)

- Go to: [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)
- Download the version: **Docker Desktop for Windows – x86_64**
- Follow the installation wizard.
- Restart your system if prompted.

### 2. Enable WSL 2 or Hyper-V

Docker Desktop supports both WSL 2 and Hyper-V backends.

We recommend WSL 2 for most setups:

```powershell
wsl --install
```

Enable WSL integration in Docker Desktop > Settings > Resources > WSL Integration.

### 3. Verify Docker CLI is working

After installation, open a terminal or PowerShell and run:

```bash
docker --version
docker compose version
```

---

## 🚧 Build and Run with Docker

### Option 1: Docker Compose (Recommended)

```bash
cd docker_packaging
docker compose up --build
```

This command:
- Builds the backend and frontend containers
- Exposes Streamlit frontend on `http://localhost:8501`
- Exposes FastAPI backend on `http://localhost:8080`

### Option 2: Build Manually (Advanced)

```bash
# Build the image
docker build -t supply-chain-threat-detector .

# Run the container
docker run -p 8501:8501 supply-chain-threat-detector
```

---

## 🧹 Clean Up

```bash
docker compose down --volumes --remove-orphans
```

---

## 🧪 Test Your Setup

Open your browser and visit:

```
http://localhost:8501
```

Try submitting a query such as `supply chain risks`. If the app responds with an encrypted answer and sources, you're good to go!

---

## 📁 Project Structure Reference

- `Dockerfile` – Builds the container image for backend & frontend
- `docker-compose.yml` – Orchestrates both backend and frontend services
- `.dockerignore` – Prevents unwanted files from being copied
- `README_DOCKER.md` – This file

---

## 🛠️ Troubleshooting

- Make sure Docker Desktop is **running** before issuing Docker commands
- If `docker` is not recognized, log out and log back in or reboot
- Make sure WSL or Hyper-V is enabled

---

## 📦 Next Steps

✅ Once validated, push your Docker-ready project to GitHub.  
🏷️ Then, tag a new [release](https://github.com/Eyc3b3rG/Supply-Chain-Threat-Detector/releases) using the latest commit.
