# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && \
    pip install --no-cache-dir --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8501 8080

# Start backend and frontend
CMD ["sh", "-c", "uvicorn backend_api:app --host 0.0.0.0 --port 8080 & streamlit run streamlit_app.py --server.port 8501"]