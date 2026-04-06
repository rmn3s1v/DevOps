from typing import List
from fastapi import APIRouter, Query, status, HTTPException
from app.models.data_models import SensorDataResponse, SensorDataCreate, SensorDataUpdate
from app.crud.data_service import DataService
from app.crud.sensor_service import SensorService

router = APIRouter(tags=["Sensor Data"])

@router.post("/sensors/{sensor_id}/data", response_model=SensorDataResponse, status_code=status.HTTP_201_CREATED)
def create_data(sensor_id:int, data:SensorDataCreate):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found with add data")

    return DataService.create_data(sensor_id, data)

@router.get("/sensors/{sensor_id}/data", response_model=List[SensorDataResponse])
def get_sensor_data(sensor_id:int, limit: int=Query(100, le=1000)):
    sensor = SensorService.get_sensor(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found with add data")

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found with add data")
    DataService.delete_sensor_data(sensor_id, data_id)
    return
