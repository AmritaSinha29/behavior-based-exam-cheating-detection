from backend.storage.memory_store import save_attempt
from backend.services.feature_extractor import extract_features
from backend.services.anomaly_detector import detect_anomaly

def process_exam_attempt(attempt):
    features = extract_features(attempt)
    anomaly_result = detect_anomaly(features)

    response = {
        "student_id": features["student_id"],
        "features": features,
        "cheating_analysis": anomaly_result
    }

    save_attempt(response)
    return response
