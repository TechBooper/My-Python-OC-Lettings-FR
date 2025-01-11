# 1) Choose a base image
FROM python:3.8-slim

# 2) Set a working directory within the container
WORKDIR /usr/src/app

# 3) Copy and install dependencies
#    Copy only requirements first so Docker can cache pip installs if nothing changed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy the entire project into the container
COPY . .

# 5) Expose the port Django will run on
EXPOSE 8000

# 6) Command to run the development server (for testing only)
#    For production, consider using gunicorn or uwsgi + reverse proxy (e.g., Nginx).
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
