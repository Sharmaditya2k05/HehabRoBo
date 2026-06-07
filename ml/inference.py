"""
ML inference module
Loads trained model and performs prediction
"""

import joblib
import os

MODEL_PATH = os.path.join("ml", "human_detector.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}. Run ml/train.py first."
    )

model = joblib.load(MODEL_PATH)

def predict(features):
    """
    Returns probability of human presence
    """
    return model.predict_proba([features])[0][1]
