from fastapi import FastAPI
from backend.routers import exam, admin

app = FastAPI()

app.include_router(exam.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Backend is running"}
