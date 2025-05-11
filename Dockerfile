# Use a more complete base to support compilation
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by llama-cpp-python
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the backend API port
EXPOSE 8080

# Run the backend
CMD ["python", "backend_api.py"]

