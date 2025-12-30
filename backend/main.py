from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ExamAttempt(BaseModel):
    student_id: int
    answers: List[int]
    time_taken: List[float]

@app.get("/")
def root():
    return {"message": "Backend is running successfully"}

@app.get("/status")
def status():
    return {"status": "Server is healthy"}

@app.post("/submit-exam")
def submit_exam(attempt: ExamAttempt):
    return {
        "message": "Exam submitted successfully",
        "student_id": attempt.student_id,
        "total_questions": len(attempt.answers)
    }
