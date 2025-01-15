FROM python:3.8-slim

# Set build-time arguments for Django settings
ARG DEBUG=False
ARG ALLOWED_HOSTS
ARG SECRET_KEY
ARG DB_CREDENTIALS

# Make a working directory
WORKDIR /usr/src/app

# Copy only requirements first (for caching layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full project
COPY . .

# Expose the Django port (optional; mainly for documentation)
EXPOSE 8000

# Convert build args to environment variables in the final image
ENV DEBUG=${DEBUG}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV SECRET_KEY=${SECRET_KEY}
ENV DB_CREDENTIALS=${DB_CREDENTIALS}

# Collect static files so they're bundled in the final image
RUN python manage.py collectstatic --noinput

# For production, consider using gunicorn or uwsgi. For now, runserver is shown:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
