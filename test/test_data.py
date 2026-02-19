from fastapi.testclient import TestClient


def test_create_data(client: TestClient):
    # создаём датчик
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Data Sensor",
            "ip": "7.7.7.7",
            "data_type": "temperature"
        }
    )

    sensor_id = create_sensor.json()["id"]

    response = client.post(
        f"/api/sensors/{sensor_id}/data",
        json={
            "temperature": 23.5,
            "humidity": 60
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["temperature"] == 23.5
    assert data["humidity"] == 60
    assert data["sensor_id"] == sensor_id


def test_get_sensor_data(client: TestClient):
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Data Sensor",
            "ip": "8.8.8.8",
            "data_type": "temperature"
        }
    )

    sensor_id = create_sensor.json()["id"]

    client.post(
        f"/api/sensors/{sensor_id}/data",
        json={
            "temperature": 20.0
        }
    )

    response = client.get(f"/api/sensors/{sensor_id}/data")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["temperature"] == 20.0


def test_update_data(client):
    sensor = client.post(
        "/api/sensors",
        json={
            "name": "TestSensor",
            "ip": "1.1.1.1",
            "data_type": "temperature"
        }
    )

    sensor_id = sensor.json()["id"]

    data = client.post(
        f"/api/sensors/{sensor_id}/data",
        json={
            "temperature": 20
        }
    )

    data_id = data.json()["id"]

    response = client.put(
        f"/api/sensors/{sensor_id}/data/{data_id}",
        json={
            "temperature": 30
        }
    )

    assert response.status_code == 200
    assert response.json()["temperature"] == 30


def test_delete_sensor_data(client: TestClient):
    create_sensor = client.post(
        "/api/sensors",
        json={
            "name": "Data Sensor",
            "ip": "9.9.9.9",
            "data_type": "temperature"
        }
    )

    sensor_id = create_sensor.json()["id"]

    create_data = client.post(
        f"/api/sensors/{sensor_id}/data",
        json={
            "temperature": 22.2
        }
    )

    data_id = create_data.json()["id"]

    response = client.delete(f"/api/sensors/{sensor_id}/data/{data_id}")
    assert response.status_code == 204

    response = client.get(f"/api/sensors/{sensor_id}/data")
    assert response.status_code == 200
    assert response.json() == []
