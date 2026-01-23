def generate_explanation(features: dict, anomaly_score: float, is_suspicious: bool):
    reasons = []

    avg_time = features["avg_time_per_question"]
    variance = features["time_variance"]
    min_time = features["min_time"]

    if avg_time < 5:
        reasons.append("Extremely low average time per question")

    if variance > 100:
        reasons.append("Highly inconsistent answering pattern")

    if min_time < 3:
        reasons.append("Answered some questions unusually fast")

    if not reasons and is_suspicious:
        reasons.append("Overall behavior deviates from typical patterns")

    if not is_suspicious:
        reasons.append("Behavior within expected range")

    return reasons
