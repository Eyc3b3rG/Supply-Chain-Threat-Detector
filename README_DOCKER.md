# 🚢 Docker Deployment Guide for Supply Chain Threat Detector

This guide provides instructions for building and running the Supply Chain Threat Detector app using Docker.

## 🧰 Prerequisites

Make sure Docker is installed and running on your system:

- 🪟 **Windows**:
  - Download Docker Desktop from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
  - Ensure Docker CLI commands like `docker` and `docker compose` are recognized in your terminal
  - Restart your computer after installation if needed

- 🍎 **macOS**: Use Docker Desktop or Homebrew
- 🐧 **Linux**: Follow your distro’s Docker install instructions

To verify Docker is installed:

```bash
docker --version
docker compose version
```

## 📦 Build the Docker Image

From the project root directory (where the `Dockerfile` is located), run:

```bash
docker compose build
```

## ▶️ Run the Containers

Start the backend and frontend services using:

```bash
docker compose up
```

To run in detached mode:

```bash
docker compose up -d
```

## 🔍 Access the App

Once the containers are running, access the app via your browser at:

```text
http://localhost:8501
```

## 🧪 Stopping and Cleaning Up

To stop the services:

```bash
docker compose down
```

To remove volumes and orphan containers:

```bash
docker compose down --volumes --remove-orphans
```

## 📁 Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── backend_api/
├── streamlit_app.py
└── README_DOCKER.md
```

---
© 2025 Eyc3b3rG | For demonstration purposes only.
