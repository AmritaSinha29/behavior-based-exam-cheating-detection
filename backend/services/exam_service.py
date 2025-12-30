from backend.storage.memory_store import save_attempt

def process_exam_attempt(attempt):
    save_attempt(attempt)
    return {
        "student_id": attempt.student_id,
        "total_questions": len(attempt.answers)
    }
