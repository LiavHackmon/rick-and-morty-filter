# Rick and Morty Characters Filter Service

## Overview

This project queries the [Rick and Morty API](https://rickandmortyapi.com/documentation/#rest) to retrieve all characters that meet the following criteria:

- Species: **Human**
- Status: **Alive**
- Origin: **Earth**

The filtered data includes the following fields:

- Name
- Location
- Image URL

The results are written to a CSV file and exposed through a REST API service.

---

## Features

1. **API Data Retrieval**  
   Queries the Rick and Morty API and filters characters based on species, status, and origin.

2. **CSV Export**  
   Exports the filtered data into a CSV file (`rick_and_morty_characters.csv`) with columns:  
   `Name, Location, Image`

3. **REST API**  
   Provides a Flask-based REST API with the following endpoints:
   - `GET /characters` — Returns the filtered character data as JSON.
   - `GET /healthcheck` — Returns a simple status response to verify the service health.

4. **Dockerized Application**  
   Includes a Dockerfile to build and run the application inside a container for easy deployment.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Docker (optional, for containerized deployment)
- Required Python packages (`requests`, `flask`, etc.)

---

### Running Locally (Without Docker)

1. Install dependencies:

```bash
pip install -r requirements.txt

Run the data retrieval script to generate the CSV file:
python rick_and_morty2.py

Start the Flask API server:
python app.py

Build the Docker image:
docker build -t rick-morty-app .

Run the container (mapping port 5000):
docker run --name rickmorty-container -d -p 5000:5000 rick-morty-app

---

## 🚀 Deploying to Kubernetes

### Prerequisites

- A running Kubernetes cluster (e.g., Minikube)
- `kubectl` CLI configured
- An Ingress Controller installed (e.g., NGINX Ingress)
- Docker image `liavhackmon/rick-morty-app:latest` pushed to Docker Hub

---

### Deployment Steps

1. **Start Minikube (if not already running):**

```bash
minikube start

minikube addons enable ingress

kubectl apply -f task2/yamls/Deployment.yaml
kubectl apply -f task2/yamls/Service.yaml
kubectl apply -f task2/yamls/Ingress.yaml


minikube tunnel

Access the application in your browser:

Home Page: http://localhost/rickmorty/

Characters Page: http://localhost/rickmorty/characters

Health Check: http://localhost/rickmorty/healthcheck

---

📦 Helm Chart Deployment (Bonus Task)
This task demonstrates how the Rick and Morty Flask-based web application was containerized and deployed to a Kubernetes cluster using Helm.
Created a Helm Chart
Initialized a Helm chart using helm create rickmorty, which generated a standardized folder structure including Chart.yaml, values.yaml, and a templates/ directory.

Configured values.yaml
Defined all necessary parameters in values.yaml for a flexible deployment:
Image repository and tag
Service type and ports
Ingress rules for external access via /rickmorty
Customized Kubernetes Templates
Updated deployment.yaml, service.yaml, and ingress.yaml to use Helm templating syntax (.Values) for full configurability.
Cleaned Unused Templates
Removed unnecessary template files such as hpa.yaml, tests/, and serviceaccount.yaml to keep the chart minimal and focused.
Validated the Chart
Ran helm lint . to ensure the chart structure and templates are valid.
Deployed with Helm
Deployed the application using:
helm install rickmorty .

Accessed the application via:
http://localhost/rickmorty
.
Easily removed the release using:
helm uninstall rickmorty
