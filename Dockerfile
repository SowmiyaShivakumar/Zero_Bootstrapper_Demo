# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file if you have one (optional)
# COPY requirements.txt .

# Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# If you don't have requirements.txt, install directly:
RUN pip install --no-cache-dir fastapi uvicorn databases[mysql] sqlalchemy aiomysql

# Copy your app code
COPY main.py .

# Expose port 8000
EXPOSE 8000

# Command to run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn databases[mysql] sqlalchemy aiomysql

# Copy your app code
COPY main.py .

# Expose port 8000
EXPOSE 8000

# Command to run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
