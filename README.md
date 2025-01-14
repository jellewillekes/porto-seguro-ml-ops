## Porto Seguro MLOps Project

This repository shows an example of an MLOps pipeline built for the Porto Seguro Safe Driver Prediction dataset. The project demonstrates how to train and deploy a machine learning model using open-source tools and frameworks, including Docker, Kubernetes, and FastAPI. The project serves as an example (and reference) for scalable and production-ready machine learning system design.

### Overview

#### Porto Seguro Dataset
Predicting insurance risk scores is a critical task for reducing losses in the insurance industry. Using the Porto Seguro Safe Driver Prediction dataset, this project develops a machine learning model to predict the likelihood of claims, with an emphasis on high accuracy and operational scalability.

#### Key Features

- **Machine Learning Model**:
  - The model is built using XGBoost and optimized using Bayesian Optimization.
  - Performance is measured using the Gini coefficient, a common metric in risk prediction tasks.

- **Model Serving**:
  - A FastAPI-based REST API serves predictions and provides health checks.

- **Scalability**:
  - The application is containerized with Docker and deployed using Kubernetes.

### Project Structure
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

### Setup Instructions

#### Prerequisites
Install and set up the following programs:
- Python 3.10+
- Docker (Desktop)
- Kubernetes (Minikube for local testing)
- Git

#### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/porto-seguro-mlops.git
cd porto-seguro-mlops
```

#### Step 2: Train the Machine Learning Model
Train and save the machine learning model with metadata:
```bash
python scripts/train_model.py
```
This will generate:
- `models/xgboost_gini.pkl`: Serialized trained model.
- `models/model_metadata.json`: Metadata containing feature details.

#### Step 3: Build and Run the Docker Container Locally

**Build the Docker Image**:
```bash
docker build -t porto-seguro-api .
```

**Tag the Docker Image**:
```bash
docker tag porto-seguro-api jellewillekes/porto-seguro-api:latest
```
Replace `jellewillekes` with Docker Hub username where image is stored.

**Push the Docker Image**:
```bash
docker push jellewillekes/porto-seguro-api:latest
```

**Run the Docker Container Locally**:
```bash
docker run -p 8080:8080 porto-seguro-api
```

**Test the API**:
```bash
python scripts/run_predict.py
```

### Using the Deployed Endpoint

The `data/observation.csv` file contains input data with 91 features. To use the deployed endpoint:

1. Ensure the API is running and accessible. For Kubernetes deployment, retrieve the service URL:
   ```bash
   minikube service porto-seguro-service --url
   ```
   Replace `<SERVICE_URL>` below with the retrieved URL.

2. Send a request to the endpoint:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"features": [<list_of_91_features>]}' <SERVICE_URL>/predict
   ```
   Replace `<list_of_91_features>` with the actual feature values.

3. Alternatively, use the provided script to send requests:
   ```bash
   python scripts/run_predict.py
   ```
   This script reads the input data from `data/observation.csv`, formats it, and sends a request to the endpoint.

The response is a predicted likelihood of an insurance claim based on the provided features.
