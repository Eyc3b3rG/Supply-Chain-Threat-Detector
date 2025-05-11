## 🐳 Running the Supply Chain Threat Detector with Docker

This application includes both a **backend** (FastAPI) and a **frontend** (Streamlit) service, orchestrated using Docker Compose.

---

### 📦 Step 1: Build and Start the Services

From the project root directory (where `docker-compose.yml` is located), run:

```bash
docker-compose up --build
```

This will:
- Build and run the FastAPI backend at `http://localhost:8080`
- Build and run the Streamlit frontend at `http://localhost:8501`

---

### 🌐 Access the Application

- **Frontend UI (Streamlit)**: [http://localhost:8501](http://localhost:8501)
- **Backend API (FastAPI)**: [http://localhost:8080](http://localhost:8080)

You should see confirmation messages like:
- `Uvicorn running on http://0.0.0.0:8080`
- `You can now view your Streamlit app in your browser.`

---

### 🛑 Stop the Services

To stop all containers, press `Ctrl+C` in the terminal or run:

```bash
docker-compose down
```

---

### 📝 Notes

- Ensure your `.env` and `models/` folder are correctly included or referenced.
- Avoid using `0.0.0.0` in the browser URL — use `localhost` instead.

---
