from pydantic import BaseModel
from typing import List

class ExamAttempt(BaseModel):
    student_id: int
    answers: List[int]
    time_taken: List[float]
