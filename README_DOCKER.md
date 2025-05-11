# 🚢 Dockerized Deployment – Supply Chain Threat Detector

This project uses Docker to containerize both the **FastAPI backend** and **Streamlit frontend**.

---

## 📁 Project Structure

```
.
├── backend_api.py
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── rebuild_docker.bat
└── README_DOCKER.md
```

---

## 🚀 Quick Start (Local Docker Build)

### 🔁 Rebuild from Scratch
Run the `.bat` script (for Windows users):

```bash
./rebuild_docker.bat
```

This will:
1. Stop existing containers
2. Rebuild images using `docker-compose`
3. Start both backend and frontend services

---

## 🧪 Manual Docker Commands

### Build & Run via Docker Compose

```bash
docker-compose down
docker-compose up --build
```

---

## 🌐 Accessing the App

- Frontend (Streamlit): [http://localhost:8501](http://localhost:8501)
- Backend (FastAPI): [http://localhost:8080/docs](http://localhost:8080/docs)

---

## ⚙️ Environment & Model Setup

### Models
To use local models like TinyLLaMA, ensure your `models/` folder is **excluded** from `.dockerignore` and structured like:

```
models/
└── tinylama-1.1b-chat-v1.0.Q4_K_M.gguf
```

---

## 📦 Notes

- `llama-cpp-python` and `faiss-cpu` are installed and pinned in `requirements.txt`.
- Dependencies are resolved using pip with `--no-cache-dir` to keep builds lean.
- Compatibility ensured for `langchain==0.1.17` and `langchain-community==0.0.36`.

---

## 🧼 .dockerignore Example

```
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
.env
models/
```

---

## 🛠 Troubleshooting

- ❗ If the backend fails to find a model path, verify `models/` exists inside the container (`docker exec -it container_name ls /app/models`)
- ✅ Ensure `llama-cpp-python` is installed and compatible with your system's CPU

