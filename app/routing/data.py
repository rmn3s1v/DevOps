from typing import List
from fastapi import APIRouter, Query, status, HTTPException
from app.models.data_models import SensorDataResponse, SensorDataCreate
from app.crud.data_service import DataService
from app.crud.sensor_service import SensorService

router = APIRouter(tags=["Sensor Data"])

@router.post("/sensor/{sensor_id}/data", response_model=SensorDataResponse, status_code=status.HTTP_201_CREATED)
def create_data(sensor_id:int, data:SensorDataCreate):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found with add data")

    return DataService.create_data(sensor_id, data)

@router.get("/sensor/{sensor_id}/data", response_model=List[SensorDataResponse])
def get_sensor_data(sensor_id:int, limit: int=Query(100, le=1000)):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found with add data")

    return DataService.get_sensor_data(sensor_id, limit)

@router.get("/data", response_model=List[SensorDataResponse])
def get_sensor_data(limit: int=Query(100, le=1000)):
    return DataService.get_data_by_type(limit)

@router.delete("/sensor/{sensor_id}/data", status_code=status.HTTP_204_NO_CONTENT)
def delete_data(sensor_id:int):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found with add data")
    DataService.delete_sensor_data(sensor_id)
    return
