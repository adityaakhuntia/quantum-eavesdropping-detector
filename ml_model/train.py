import joblib
import os
from sklearn.ensemble import IsolationForest
from quantum_sim.bb84 import bb84_simulation

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

print("Generating NORMAL BB84 data...")

X = []

for _ in range(500):

    a_bits, a_bases, b_bases, b_bits = bb84_simulation(eavesdrop=False)

    # calculate QBER
    errors = sum(1 for i in range(len(a_bits)) if a_bits[i] != b_bits[i])
    qber = errors / len(a_bits)

    # simple entropy/randomness metric
    entropy = sum(a_bits) / len(a_bits)

    X.append([qber, entropy])

print("Training IsolationForest...")

model = IsolationForest(contamination=0.1)
model.fit(X)

joblib.dump(model, MODEL_PATH)

print("Model trained correctly and saved")