
# Porto Seguro MLOps Project

This repository shows an example of an MLOps pipeline built for the Porto Seguro Safe Driver Prediction dataset. The 
project demonstrates how to train and deploy a machine learning model using open-source tools and frameworks, including 
Docker, Kubernetes, and FastAPI. The project serves as an example (and refer back) for a scalable and prodcution-ready 
machine learning system design.

---

## Overview

### Porto Seguro Dataset
Predicting insurance risk scores is a critical task for reducing losses in the insurance industry. Using the Porto Seguro Safe Driver Prediction dataset, this project develops a machine learning model to predict the likelihood of claims, with an emphasis on high accuracy and operational scalability.

### Key Features
1. **Machine Learning Model**:
   - The model is built using XGBoost and optimized using Bayesian Optimization.
   - Performance is measured using the Gini coefficient, a common metric in risk prediction tasks.
2. **Model Serving**:
   - A FastAPI-based REST API serves predictions and provides health checks.
3. **Scalability**:
   - The application is containerized with Docker and deployed using Kubernetes.

---

## Project Structure
```
porto-seguro-mlops/
├── data/                
├── models/              
│   ├── xgboost_test_gini.pkl
│   ├── model_metadata.json
├── serving/                # FastAPI app for model serving
│   ├── predict.py          # Prediction and health-check endpoints
│   ├── requirements.txt   
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml    
│   ├── service.yaml        
├── scripts/                
│   ├── train_model.py      # Script to train the model
│   ├── create_observation.py  
│   ├── run_predict.py      # Script to test the FastAPI app
├── Dockerfile              
├── README.txt              
├── requirements.txt      
```
---

## Setup Instructions

### Prerequisites
Install and set up following programs:
- Python 3.10+
- Docker (Desktop)
- Kubernetes (Minikube for local testing)
- Git

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/porto-seguro-mlops.git
cd porto-seguro-mlops
```

---

### Step 2: Train the Machine Learning Model
Train and save the machine learning model with metadata:
```bash
python scripts/train_model.py
```
This will generate:
- `models/xgboost_test_gini.pkl`: Serialized trained model.
- `models/model_metadata.json`: Metadata containing feature details.

---

### Step 3: Build and Run the Docker Container Locally

#### Build the Docker Image
```bash
docker build -t porto-seguro-api .
```

#### Tag the Docker Image
```bash
docker tag porto-seguro-api jellewillekes/porto-seguro-api:latest
```
Replace `jellewillekes` with your actual Docker Hub username.

#### Push the Docker Image
```bash
docker push jellewillekes/porto-seguro-api:latest
```
Replace `jellewillekes` with your actual Docker Hub username.

#### Run the Docker Container Locally
```bash
docker run -p 8080:8080 porto-seguro-api
```

#### Test the API
```bash
python scripts/run_predict.py
```

---

### Step 4: Deploy to Kubernetes

#### Initialize Minikube
To deploy the application using Kubernetes, first ensure Minikube is installed and configured. Start Minikube and set the Docker environment:

```bash
minikube start
minikube docker-env
```

#### Deploy Kubernetes Resources
Apply the Kubernetes manifests to create and expose the deployment:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

- `deployment.yaml` specifies the application deployment, including replicas, resource limits, and liveness/readiness probes.
- `service.yaml` creates a LoadBalancer service to expose the application.

#### Verify Deployment
Ensure that the application is running by checking the status of pods:

```bash
kubectl get pods
```

#### Access the Deployed API
Retrieve the external IP or NodePort of the service, command to get URL to access the deployed API.

```bash
minikube service porto-seguro-service --url
```

#### Test the Deployed API
You can now send requests to the API, by using external IP or NodePortUse the external IP or NodePort:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"features": [<list_of_91_features>]}' <EXTERNAL_IP>
```

Replace `<list_of_91_features>` with the actual feature values and `<EXTERNAL_IP>` with the service URL.

Alternatively, use the `run_predict.py` script to send test requests:

```bash
python scripts/run_predict.py
```

The `data/observation.csv` file contains valid input data with 91 features.
The model is deployed on Kubernetes and accessible through a LoadBalancer service.
---
