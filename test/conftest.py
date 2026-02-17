import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import db

@pytest.fixture(scope="function")
def client():
    db.sensos.delete_many({})
    db.senso_data.delete_many({})

    with TestClient(app) as c:
        yield c

    db.sensors.delete_many({})
    db.sensor_data.delete_many({})
