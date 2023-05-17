from datetime import datetime
from typing import List, Union

from pydantic import Field

from app.models.base import BaseModelConfig


class PropertyModel(BaseModelConfig):
    property_id: int = Field(..., gt=0)
    description: str = Field(..., min_length=1, max_length=1000)
    address: str = Field(..., min_length=1, max_length=1000)
    price: float = Field(..., gt=0)
    type: str = Field(..., min_length=1, max_length=100)
    area: float = Field(..., gt=0)
    bedrooms: int = Field(..., gt=0)
    bathrooms: int = Field(..., gt=0)
    common_parking: bool = Field(...)
    parking: Union[int, None] = Field(..., gt=0)
    status: str = Field(..., min_length=1, max_length=100)


class BuildingModel(BaseModelConfig):
    building_id: int = Field(..., gt=0)
    description: str = Field(..., min_length=1, max_length=1000)
    address: str = Field(..., min_length=1, max_length=1000)
    price: float = Field(..., gt=0)
    type: str = Field(..., min_length=1, max_length=100)
    area: float = Field(..., gt=0)
    floors: int = Field(..., gt=0)
    underground: Union[int, None] = Field(..., gt=0)
    parking: int = Field(..., gt=0)
    status: str = Field(..., min_length=1, max_length=100)
    established_at: datetime = Field(...)


class UnitModel(BaseModelConfig):
    unit_id: int = Field(..., gt=0)
    description: str = Field(..., min_length=1, max_length=1000)
    address: str = Field(..., min_length=1, max_length=1000)
    price: float = Field(..., gt=0)
    type: str = Field(..., min_length=1, max_length=100)
    area: float = Field(..., gt=0)
    bedrooms: int = Field(..., gt=0)
    bathrooms: int = Field(..., gt=0)
    amenities: List[str] = Field(default_factory=list)
