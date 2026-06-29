# FastAPI CI/CD Project 🚀

## Overview

A FastAPI application demonstrating modern DevOps practices including:

- FastAPI REST API
- Docker containerization
- GitHub Actions CI pipeline
- Automated testing with Pytest
- Railway cloud deployment
- Health monitoring endpoint

## Tech Stack

- Python 3.10
- FastAPI
- Docker
- GitHub Actions
- Railway
- Pytest

## Live Demo

https://fastapi-cicd-project-production.up.railway.app

## API Documentation

https://fastapi-cicd-project-production.up.railway.app/docs

## Health Check

https://fastapi-cicd-project-production.up.railway.app/health

## Run Locally

```bash
git clone https://github.com/student-ishikakamble/fastapi-cicd-project.git
cd fastapi-cicd-project

pip install -r requirements.txt
uvicorn main:app --reload
```

## Run Tests

```bash
pytest -v
```

## Docker

```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

## CI Pipeline

GitHub Actions automatically:

- Installs dependencies
- Runs automated tests
- Validates application integrity

## Project Structure

```text
fastapi-cicd-project/
│
├── .github/workflows/
├── Dockerfile
├── main.py
├── requirements.txt
├── test_main.py
└── README.md
```