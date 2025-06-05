import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, roc_auc_score
from xgboost import XGBClassifier

# Load data
df = pd.read_csv("../data/claims.csv")
X = df[['claim_amount', 'claimant_age', 'incident_description']]
y = df['is_fraud']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['claim_amount', 'claimant_age']),
    ('txt', TfidfVectorizer(max_features=100), 'incident_description')
])

# Pipeline
pipeline = Pipeline([
    ('pre', preprocessor),
    ('clf', XGBClassifier(use_label_encoder=False, eval_metric='logloss'))
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))
print("AUC Score:", roc_auc_score(y_test, y_proba))

# Save
joblib.dump(pipeline, "../app/model_pipeline.pkl")
print("✅ Model saved to ../app/model_pipeline.pkl")
