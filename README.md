# Fraud Detection AI SDLC – Backend Intelligence Example

This repository demonstrates how to design and develop an AI-powered backend service by replacing traditional rule-based logic with data-driven intelligence. It complements [AI SDLC – Part 3](https://github.com/miqbal-rh/fraud-detection-ai-sdlc), a broader series exploring how software engineering changes when AI becomes the primary engine of backend behavior.

## 🌟 Overview

In traditional systems:
- Developers write **rules**
- Behavior is governed by **if-else logic**
- Ambiguity is treated as a **problem**

In AI-powered systems:
- Developers **curate examples**
- Models **learn behavior** from data
- Ambiguity becomes a **source of learning**

This project offers a minimal yet complete AI backend system that:
- Simulates fraud-labeled insurance claim data
- Trains a predictive model using structured and unstructured fields
- Exposes the model through a FastAPI service

## 🚀 Try It Locally

### 1. Clone the repo

```bash
git clone https://github.com/miqbal-rh/fraud-detection-ai-sdlc.git
cd fraud-detection-ai-sdlc
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train_model.py
```

This will:
- Generate synthetic claim data
- Train an XGBoost pipeline
- Serialize it as `model.joblib`

### 4. Run the API

```bash
cd app
uvicorn main:app --reload
```

### 5. Make a prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"claimant_age": 45, "claim_amount": 1200.50, "incident_description": "Theft reported after midnight"}'
```

## 🧠 What's Inside

### Data Curation (instead of static requirements)
- `train_model.py` simulates and labels historical claim data.

### Model Training (instead of rule encoding)
- Combines numerical features and text vectorization (TF-IDF)
- Uses `XGBoostClassifier` in a pipeline

### Statistical Evaluation (instead of local testing)
- Prints AUC and precision/recall scores during training

### Optional Interpretability
- Tools like [SHAP](https://github.com/slundberg/shap) can be added to explain predictions (not included in this repo)

### RESTful Intelligence (instead of hardcoded decision branches)
- `app/main.py` exposes a single `/predict` endpoint

## 📂 Directory Structure

```
fraud-detection-ai-sdlc/
│
├── app/
│   └── main.py               # FastAPI server
│
├── notebook/venv/            # Local virtual environment (excluded via .gitignore)
│
├── train_model.py            # End-to-end training logic
├── model.joblib              # Trained model artifact
├── requirements.txt
└── README.md
```

## 📌 Notes

- Do **not** commit `venv/`, `__pycache__/`, or `.ipynb_checkpoints/`
- `.gitignore` should include:
  ```
  venv/
  __pycache__/
  *.pyc
  .ipynb_checkpoints/
  ```

## 🔄 From Engineering to Orchestration

This project isn't just about fraud detection. It illustrates a deeper shift:

| Traditional Software | AI-Based Development          |
|----------------------|-------------------------------|
| Write rules          | Curate labeled data           |
| Predict deterministically | Learn from patterns        |
| Test interactively   | Validate statistically         |
| Debug logic          | Interpret model behavior       |
| Write conditionals   | Expose model via REST API      |

As a developer, you're not scripting every possibility. You're orchestrating learning—and overseeing models as they evolve.
