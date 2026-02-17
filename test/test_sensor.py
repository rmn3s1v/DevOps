from fastapi.testclient import TestClient

def test_create_sensor(client: TestClient):
    response = client.post(
        "/api/sensors",
        json={
            "name": "Test Sensor",
            "ip": "1.2.3.4",
            "data_type": "temperature"
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "Test Sensor"
    assert data["ip"] == "1.2.3.4"
    assert data["data_type"] == "temperature"
    assert "id" in data
    assert "created_at" in data

def test_get_all_sensort(client: TestClient):
    # создаём датчик
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Sensor 1",
            "ip": "2.2.2.2",
            "data_type": "humidity"
        }
    )

    response = client.get("/api/sensors")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1

def test_get_single_sensor(client: TestClient):
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Sensor 2",
            "ip": "3.3.3.3",
            "data_type": "pressure"
        }
    )

    sensor_id = create_sensor.json()["id"]

    response = client.get(f"/api/sensors/{sensor_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Sensor 2"


def test_update_sensor(client: TestClient):
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Old Name",
            "ip": "4.4.4.4",
            "data_type": "light"
        }
    )

    sensor_id = create_sensor.json()["id"]

    response = client.put(
        f"/api/sensors/{sensor_id}",
        json={
            "name": "New Name",
            "ip": "5.5.5.5"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "New Name"
    assert data["ip"] == "5.5.5.5"


def test_delete_sensor(client: TestClient):
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Delete Me",
            "ip": "6.6.6.6",
            "data_type": "temperature"
        }
    )

    sensor_id = create_sensor.json()["id"]

    response = client.delete(f"/api/sensors/{sensor_id}")
    assert response.status_code == 204

    # проверяем что удалился
    response = client.get(f"/api/sensors/{sensor_id}")
    assert response.status_code == 404
