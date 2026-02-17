import datetime
from typing import Literal
from uuid import UUID
from pydantic import BaseModel, Field, IPvAnyAddress


class SensorBase(BaseModel):
    name: str = Field(..., min_length=3)
    ip: IPvAnyAddress
    data_type: Literal["temperature", "humidity", "pressure", "light"]


class SensorCreate(BaseModel):
    name: str
    ip: IPvAnyAddress
    data_type: Literal["temperature", "humidity", "pressure", "light"]


class SensorUpdate(BaseModel):
    name: str | None = None
    ip: IPvAnyAddress | None = None
    data_type: Literal["temperature", "humidity", "pressure", "light"] | None = None


class SensorResponse(SensorBase):
    id: int
    created_at: datetime.datetime
