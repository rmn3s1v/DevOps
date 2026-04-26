from fastapi import FastAPI
from app.routing import sensors, data
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

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

Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"]
).instrument(app).expose(app, include_in_schema=False)
