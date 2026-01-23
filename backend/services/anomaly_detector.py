from sklearn.ensemble import IsolationForest
import numpy as np

# -----------------------------
# Global model state
# -----------------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.15,
    random_state=42
)

trained = False
feature_history: list[list[float]] = []

# -----------------------------
# Detection function
# -----------------------------

def detect_anomaly(features: dict):

    global trained

    # Build numeric feature vector
    feature_vector = np.array([
        features["avg_time_per_question"],
        features["min_time"],
        features["max_time"],
        features["time_variance"]
    ], dtype=float)

    feature_history.append(feature_vector.tolist())

    print("HISTORY SIZE:", len(feature_history))
    print("VECTOR:", feature_vector.tolist())

    # Train once enough samples collected
    if len(feature_history) >= 5 and not trained:
        print("TRAINING MODEL...")
        model.fit(np.array(feature_history))
        trained = True

    # Not trained yet → neutral output
    if not trained:
        return {
            "is_suspicious": False,
            "anomaly_score": 0.0
        }

    # Predict
    prediction = model.predict([feature_vector])[0]
    score = model.decision_function([feature_vector])[0]

    # Convert numpy → python
    prediction_val = int(prediction)
    score_val = float(score)

    is_anomaly = (prediction_val == -1) or (score_val < -0.05)

    return {
        "is_suspicious": bool(is_anomaly),
        "anomaly_score": float(round(score_val, 4))
    }
