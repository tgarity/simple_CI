# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application code to the container
COPY app.py .

# Install necessary dependencies
RUN pip install --no-cache-dir fastapi uvicorn