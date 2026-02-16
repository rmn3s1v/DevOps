import datetime
from pydantic import BaseModel



class SensorDataBase(BaseModel):
    temperature: float | None = None
    humidity: int | None = None
    pressure: int | None = None
    light: int | None = None


class SensorDataCreate(SensorDataBase):
    pass


class SensorDataResponse(SensorDataBase):
    id: int
    sensor_id: int
    timestamp: datetime
