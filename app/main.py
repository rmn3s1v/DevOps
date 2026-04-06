from fastapi import FastAPI
from routing import sensors, data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensors.router, prefix="/api")
app.include_router(data.router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
