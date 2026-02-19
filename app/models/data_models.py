import datetime
from typing import Optional
from pydantic import BaseModel



class SensorDataBase(BaseModel):
    temperature: float | None = None
    humidity: int | None = None
    pressure: int | None = None
    light: int | None = None


class SensorDataCreate(SensorDataBase):
    pass


class SensorDataUpdate(BaseModel):
    temperature: Optional[float] = None
    humidity: Optional[int] = None
    pressure: Optional[int] = None
    light: Optional[int] = None


class SensorDataResponse(SensorDataBase):
    id: int
    sensor_id: int
    timestamp: datetime.datetime
