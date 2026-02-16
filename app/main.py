from fastapi import FastAPI
from app.routing import sensors, data

app = FastAPI()

app.include_router(sensors.router, prefix="/api")
app.include_router(data.router, prefix="/api")
