from fastapi import APIRouter
from backend.schemas.exam import ExamAttempt
from backend.services.exam_service import process_exam_attempt

router = APIRouter()

@router.post("/submit-exam")
def submit_exam(attempt: ExamAttempt):
    result = process_exam_attempt(attempt)
    return {
        "message": "Exam submitted successfully",
        "data": result
    }
