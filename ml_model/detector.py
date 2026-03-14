import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def detect_attack(features):
    model = joblib.load(MODEL_PATH)
    prediction = model.predict([features])[0]
    return prediction == -1