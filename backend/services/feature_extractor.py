import statistics

def extract_features(attempt):
    times = attempt.time_taken

    features = {
        "student_id": attempt.student_id,
        "total_questions": len(times),
        "avg_time_per_question": sum(times) / len(times),
        "min_time": min(times),
        "max_time": max(times),
        "time_variance": statistics.pvariance(times)
    }

    return features
