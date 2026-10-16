# Local Kubernetes & Docker Microservice Pipeline

A production-grade Python Flask microservice containerized with Docker, deployed to a local Kubernetes (Minikube) cluster, and automated with CI/CD workflows. Designed for practicing cloud-native architecture completely free of cloud costs.

## Tech Stack
- **Application:** Python, Flask, Gunicorn
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **CI/CD:** GitHub Actions

## Quickstart
1. Build local Docker image inside Minikube:
   ```bash
   eval $(minikube docker-env)
   docker build -t flask-app:latest ./app
