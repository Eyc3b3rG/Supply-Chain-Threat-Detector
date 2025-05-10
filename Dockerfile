
# Use official Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements.txt into the container
COPY ./requirements.txt ./requirements.txt

# Install system dependencies and Python libraries
RUN apt-get update && \
    apt-get install -y build-essential cmake libopenblas-dev git curl && \
    pip install --no-cache-dir -r requirements.txt

# Copy all source code into the container
COPY . .

# Run backend API on container start
CMD ["python", "backend_api.py"]
