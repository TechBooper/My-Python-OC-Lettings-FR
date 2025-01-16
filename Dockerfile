# Use a lightweight Python image
FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y nginx libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /usr/src/app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Collect static files (can be adjusted if you use a storage backend like S3)
RUN python manage.py collectstatic --noinput

# Configure Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the Gunicorn port
EXPOSE 8000

# Start Gunicorn and Nginx with a process manager
CMD service nginx start && gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application

