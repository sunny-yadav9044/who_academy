# Base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install some packages using apt-get
RUN apt-get update && \
    apt-get install -y \
        nano \
        iputils-ping \
        curl

# Install dependencies
RUN pip install --upgrade pip
COPY ./authentication_service/requirements.txt /app/requirements.txt
RUN python3 -m pip install -r requirements.txt

# Copy source code
COPY ./authentication_service/ /app

# Expose port 8001
EXPOSE 8001

# Run tests
RUN python3 manage.py test

# Start the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
