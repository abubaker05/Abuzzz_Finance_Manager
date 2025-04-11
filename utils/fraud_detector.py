import pickle
import pandas as pd

def detect_fraud(df):
    encoder_path = "models/category_encoder.pkl"
    model_path = "models/fraud_model.pkl"

    # Load encoder and model
    with open(encoder_path, "rb") as f:
        encoder = pickle.load(f)
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    df_clean = df.copy()

    # Check for necessary columns
    if "amount" not in df_clean.columns or "type" not in df_clean.columns:
        raise ValueError("CSV must contain 'amount' and 'type' columns.")

    # Encode 'type' column
    df_clean["type_encoded"] = encoder.transform(df_clean["type"])

    # Predict using amount and encoded type
    df_clean["is_fraud"] = [1 if x == -1 else 0 for x in model.predict(df_clean[["amount", "type_encoded"]])]

    return df_clean
