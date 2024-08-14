# Loan Prediction API

This project provides a RESTful API for predicting loan acceptance. The API is built using FastAPI and is containerized with Docker. It is deployed on AWS ECS.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **Docker**: To containerize the application for consistent and easy deployment.
- **AWS ECS**: To deploy and manage the Docker containers.

## Project Structure

- `main.py`: FastAPI application that serves the prediction model.
- `client.py`: Script to interact with the API and retrieve loan predictions.
- `Dockerfile`: Docker configuration file to build and run the FastAPI application.
- `requirements.txt`: List of Python dependencies.