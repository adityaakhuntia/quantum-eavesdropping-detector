from sklearn.ensemble import IsolationForest

def get_model():
    return IsolationForest(
        n_estimators=150,
        contamination=0.15,
        random_state=42
    )
