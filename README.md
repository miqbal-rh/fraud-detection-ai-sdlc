
# Insurance Fraud Detection - AI SDLC Example

This repository demonstrates how an AI-powered backend service can be built, trained, and deployed to predict fraudulent insurance claims.

## 📦 Features
- ML pipeline with preprocessing and XGBoost training
- Model evaluation using AUC and classification report
- SHAP-based model interpretability
- REST API built with FastAPI
- Ready for containerized deployment via Docker

## 📁 Structure
```
fraud-detection-ai-sdlc/
├── data/
│   └── claims.csv
├── notebook/
│   └── train_model.ipynb
├── app/
│   ├── main.py
│   ├── model_pipeline.pkl
│   └── requirements.txt
├── Dockerfile
└── README.md
```

## 🚀 Quickstart

### 1. Train the Model
```bash
cd notebook
jupyter notebook train_model.ipynb
```

### 2. Serve the Model
```bash
cd app
uvicorn main:app --reload
```

### 3. Test the API
```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"claim_amount": 23000, "claimant_age": 30, "incident_description": "Car crash with minor injuries"}'
```

### 4. Docker Support
```bash
docker build -t fraud-detector .
docker run -p 8000:8000 fraud-detector
```
