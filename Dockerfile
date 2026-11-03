FROM python:3.10-slim
WORKDIR /app
RUN useradd -m appuser

# 1. Update keamanan bawaan OS Debian
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip dan package Python yang terdeteksi rentan oleh Trivy
RUN pip install --no-cache-dir --upgrade pip setuptools wheel msgpack urllib3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
