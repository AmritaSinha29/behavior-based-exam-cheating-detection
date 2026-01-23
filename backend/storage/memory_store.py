exam_attempts = []


def save_attempt(attempt):
    exam_attempts.append(attempt)


def get_all_attempts():
    return exam_attempts


def get_suspicious_attempts():
    return [a for a in exam_attempts if a["cheating_analysis"]["is_suspicious"]]
