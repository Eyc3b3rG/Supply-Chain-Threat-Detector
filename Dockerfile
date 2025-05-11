# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y build-essential cmake libopenblas-dev git curl && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Expose port (optional, useful for FastAPI)
EXPOSE 8080

# Run backend API
CMD ["python", "backend_api.py"]
