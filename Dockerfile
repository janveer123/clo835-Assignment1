FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 8080

# Run the app
CMD ["python3", "app.py"]