from typing import Annotated, List
from fastapi import APIRouter, Query, status, HTTPException
from app.models.data_models import SensorDataResponse, SensorDataCreate, SensorDataUpdate
from app.crud.data_service import DataService
from app.crud.sensor_service import SensorService
from app.metrics import (
    sensor_data_created_total,
    sensor_data_create_errors_total,
    sensor_data_value,
    sensor_temperature_value,
    sensor_humidity_value,
    sensor_pressure_value,
    sensor_light_value,
)

detail="Sensor not found with add data"

router = APIRouter(tags=["Sensor Data"])

@router.post("/sensors/{sensor_id}/data", response_model=SensorDataResponse, status_code=status.HTTP_201_CREATED)
def create_data(sensor_id: int, data: SensorDataCreate):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        sensor_data_create_errors_total.labels(
            reason="sensor_not_found"
        ).inc()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

    try:
        created_data = DataService.create_data(sensor_id, data)

        if data.temperature is not None:
            sensor_data_created_total.labels(data_type="temperature").inc()
            sensor_data_value.labels(data_type="temperature").set(data.temperature)
            sensor_temperature_value.set(data.temperature)

        if data.humidity is not None:
            sensor_data_created_total.labels(data_type="humidity").inc()
            sensor_data_value.labels(data_type="humidity").set(data.humidity)
            sensor_humidity_value.set(data.humidity)

        if data.pressure is not None:
            sensor_data_created_total.labels(data_type="pressure").inc()
            sensor_data_value.labels(data_type="pressure").set(data.pressure)
            sensor_pressure_value.set(data.pressure)

        if data.light is not None:
            sensor_data_created_total.labels(data_type="light").inc()
            sensor_data_value.labels(data_type="light").set(data.light)
            sensor_light_value.set(data.light)

        return created_data

    except Exception:
        sensor_data_create_errors_total.labels(
            reason="create_sensor_data_failed"
        ).inc()
        raise

@router.get("/sensors/{sensor_id}/data", response_model=List[SensorDataResponse])
def get_sensor_data(sensor_id:int, limit: Annotated[int, Query(le=1000)] = 100):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    return DataService.get_sensor_data(sensor_id, limit)

@router.put("/sensors/{sensor_id}/data/{data_id}", response_model=SensorDataResponse)
def update_data(sensor_id: int, data_id: int, data: SensorDataUpdate):
    existing = DataService.update_data(sensor_id, data_id, data)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found"
        )
    return existing

@router.delete("/sensors/{sensor_id}/data/{data_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_data(sensor_id:int, data_id: int):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    DataService.delete_sensor_data(sensor_id, data_id)
