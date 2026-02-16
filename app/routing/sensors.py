from fastapi import APIRouter, status

router = APIRouter(
    prefix="/sensors",
    tags=["Sensors"]
)
