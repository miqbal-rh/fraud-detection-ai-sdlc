# AI-Powered Fraud Detection – AI SDLC Demo

This project is part of our AI SDLC series and demonstrates how backend logic can be replaced by AI-powered intelligence using a fraud detection use case.

## 🔍 Project Summary

Rather than writing traditional business rules, we:
- **Curate and label a dataset** that reflects intended behavior (`train_model.py`, `Train_Model.ipynb`)
- **Select and train a machine learning model** to discover decision logic (TF-IDF + XGBoost)
- **Evaluate the model** using statistical metrics (precision, recall, AUC)
- **Expose predictions via REST API** (`main.py` using FastAPI)

Interpretability (e.g., SHAP) is discussed and can be added to explain predictions.

## 🛠️ Running the Example

Clone this repo:

```bash
git clone https://github.com/miqbal-rh/fraud-detection-ai-sdlc.git
cd fraud-detection-ai-sdlc
```

### 🧪 Option 1: Use the Python script
```bash
cd notebook
python train_model.py
```

### 📓 Option 2: Use the Jupyter notebook
```bash
cd notebook
jupyter notebook
# Open and run Train_Model.ipynb
```

Both options generate `model.joblib`.

### 🚀 Run the API
```bash
cd app
uvicorn main:app --reload
```

Test the prediction endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"claimant_age": 45, "claim_amount": 1200.50, "incident_description": "Theft reported after midnight"}'
```

## 📂 Directory Structure

```
├── app/
│   └── main.py         # FastAPI app exposing /predict endpoint
├── notebook/
│   ├── Train_Model.ipynb  # Jupyter notebook version of model training
│   └── train_model.py     # Python script for model training
└── model.joblib        # Trained pipeline (generated)
```

## 📌 Notes
- No business rules are hardcoded.
- The model generalizes behavior from data.
- SHAP-based interpretability is suggested for production scenarios.

This project embodies the shift from deterministic logic to data-driven intelligence in backend software engineering.
