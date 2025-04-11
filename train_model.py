import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest
import pickle
import os

# Load dataset
df = pd.read_csv("data/transactions.csv")

# Encode 'type' for modeling
encoder = LabelEncoder()
df["type_encoded"] = encoder.fit_transform(df["type"])

# Train Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(df[["amount", "type_encoded"]])

# Save model and encoder
os.makedirs("models", exist_ok=True)

with open("models/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/category_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("✅ Model trained and saved successfully!")
