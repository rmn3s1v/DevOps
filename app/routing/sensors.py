from typing import List
from fastapi import APIRouter, status, HTTPException
from app.models.sensor_models import SensorCreate, SensorResponse, SensorUpdate
from app.crud.sensor_service import SensorService

router = APIRouter(
    prefix="/sensors",
    tags=["Sensors"]
)

@router.post("", response_model=SensorResponse, status_code=status.HTTP_201_CREATED)
def create_sensor(sensor: SensorCreate):
    return SensorService.create_sensor(sensor)

@router.get("", response_model=List[SensorResponse])
def get_sensors():
    return SensorService.get_all_sensors()

@router.get("/{sensor_id}", response_model=SensorResponse)
def get_sensor_id(sensor_id:int):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")

    return sensor

@router.put("/{sensor_id}", response_model=SensorResponse)
def update_sensor(sensor_id:int, sensor: SensorUpdate):
    existing = SensorService.get_sensor(sensor_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")

    return SensorService.update_sensor(sensor_id, sensor)

@router.delete("/sensor_id", status_code=status.HTTP_204_NO_CONTENT)
def delete_sensor(sensor_id:int):
    existing = SensorService.get_sensor(sensor_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")

    SensorService.delete_sensor(sensor_id)
    return
