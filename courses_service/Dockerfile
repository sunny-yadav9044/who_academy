# Base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./courses_service/requirements.txt /app/requirements.txt
RUN python3 -m pip install -r requirements.txt

# Copy source code
COPY ./courses_service/ /app

# Expose port 8000
EXPOSE 8000

# Run the test cases
CMD ["python3", "manage.py", "test"]

# Start the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
