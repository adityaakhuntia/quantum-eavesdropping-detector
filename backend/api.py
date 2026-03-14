from fastapi import FastAPI
from quantum_sim.bb84 import bb84_simulation
from ml_model.detector import detect_attack

app = FastAPI()

@app.get("/analyze")
def analyze(eavesdrop: bool = False):

    a_bits, a_bases, b_bases, b_bits = bb84_simulation(eavesdrop)

    # calculate QBER
    errors = sum(1 for i in range(len(a_bits)) if a_bits[i] != b_bits[i])
    qber = errors / len(a_bits)

    # simple entropy metric
    entropy = sum(a_bits) / len(a_bits)

    features = [qber, entropy]

    result = detect_attack(features)

    return {
        "attack_detected": bool(result),
        "qber": qber
    }