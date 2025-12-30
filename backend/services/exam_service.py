from backend.storage.memory_store import save_attempt
from backend.services.feature_extractor import extract_features

def process_exam_attempt(attempt):
    features = extract_features(attempt)
    save_attempt(features)

    return {
        "message": "Exam processed",
        "features": features
    }
