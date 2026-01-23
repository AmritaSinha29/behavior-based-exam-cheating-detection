from fastapi import APIRouter
from backend.storage.memory_store import get_all_attempts, get_suspicious_attempts

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/attempts")
def all_attempts():
    return get_all_attempts()


@router.get("/suspicious")
def suspicious_attempts():
    return get_suspicious_attempts()
