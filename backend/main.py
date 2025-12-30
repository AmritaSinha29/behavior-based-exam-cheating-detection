from fastapi import FastAPI
from backend.routers import exam

app = FastAPI()

app.include_router(exam.router)

@app.get("/")
def root():
    return {"message": "Backend is running"}
