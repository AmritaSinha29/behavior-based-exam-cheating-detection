from backend.storage.memory_store import save_attempt
from backend.services.feature_extractor import extract_features
from backend.services.anomaly_detector import detect_anomaly
from backend.services.explainability import generate_explanation


def process_exam_attempt(attempt):
    features = extract_features(attempt)

    anomaly_result = detect_anomaly(features)

    explanations = generate_explanation(
        features,
        anomaly_result["anomaly_score"],
        anomaly_result["is_suspicious"]
    )

    response = {
        "student_id": features["student_id"],
        "features": features,
        "cheating_analysis": anomaly_result,
        "explanations": explanations
    }

    save_attempt(response)

    return response
