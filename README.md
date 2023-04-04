# Microservices API

This project consists of two microservices based on Python Django and DRF: one for user authentication and one for listing courses.

## User Authentication Microservice

The user authentication microservice provides token-based authentication for the API. It exposes the following endpoints:

- `/auth/token/generate`: POST request for generate token valid for 1 day.
- `/auth/token/validate`: POST request with the token in the Authorization header to invalidate the token.

## Course List Microservice

The course list microservice is protected by the user authentication microservice and exposes the following endpoint:

- `/courses`: GET request to retrieve a list of courses. This endpoint requires a valid token in the Authorization header. The endpoint accepts two optional query parameters:
  - `page`: Page number for pagination.
  - `page_size`: Number of courses per page.
  - `fields`: Comma-separated list of fields to be returned in the response.

This endpoint internally calls the open edX course list API to get the course details and return them to the user. The open edX course list API endpoint used is https://courses.edx.org/api/courses/v1/courses/?page=1&page_size=5.

## Third-party Libraries

This project uses `django-cors-headers` to allow CORS requests from the `localhost` domain.


## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Install Docker and Docker Compose.
3. Run `docker-compose up` to start the microservices.
4. Test the API endpoints using a tool like Postman or curl.
