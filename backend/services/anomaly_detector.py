from sklearn.ensemble import IsolationForest
import numpy as np

# -----------------------------
# Global model + state
# -----------------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.4,   # aggressive for demo
    random_state=42
)

trained = False
feature_history = []

# -----------------------------
# Core detection logic
# -----------------------------

def detect_anomaly(features: dict):
    global trained

    # Convert features into numeric vector
    feature_vector = np.array([
        features["avg_time_per_question"],
        features["min_time"],
        features["max_time"],
        features["time_variance"]
    ], dtype=float)

    feature_history.append(feature_vector)

    print("HISTORY SIZE:", len(feature_history))
    print("VECTOR:", feature_vector.tolist())

    # Train model once enough data collected
    if len(feature_history) >= 5 and not trained:
        print("TRAINING MODEL...")
        model.fit(np.array(feature_history))
        trained = True

    # If trained, run prediction
    if trained:
        prediction = model.predict([feature_vector])[0]
        score = model.decision_function([feature_vector])[0]

        print("RAW PREDICTION:", prediction)
        print("RAW SCORE:", score)

        return {
            "is_suspicious": bool(prediction == -1),
            "anomaly_score": float(round(score, 4))
        }

    # Not enough data yet
    return {
        "is_suspicious": False,
        "anomaly_score": 0.0
    }
