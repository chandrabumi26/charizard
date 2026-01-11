FROM python:3.12-slim

# Set working directory di container
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app ./app
COPY vendor ./vendor

# Default command (buat test dulu)
CMD ["python", "app/extract.py"]
