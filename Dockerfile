FROM python:3.11-slim

# Set working directory
WORKDIR /app

# 1. Copy the requirements file first
COPY requirements.txt .

# 2. INSTALL the library inside the image
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy your application code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
