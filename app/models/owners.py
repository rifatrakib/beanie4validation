from datetime import datetime
from typing import List, Union

from pydantic import EmailStr, Field, HttpUrl

from app.models.base import BaseModelConfig


class PersonModel(BaseModelConfig):
    person_id: int = Field(..., gt=0)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: Union[EmailStr, None] = Field(default=None)
    phone: Union[str, None] = Field(default=None, min_length=1, max_length=15)
    website: Union[HttpUrl, None] = Field(default=None)
    address: str = Field(..., min_length=1, max_length=1000)
    links: List[str] = Field(default_factory=list)


class PropertyOwnerModel(BaseModelConfig):
    owned_share: float = Field(..., gt=0)
    from_date: datetime = Field(...)


class UnitOwnerModel(BaseModelConfig):
    owned_share: float = Field(..., gt=0)
    from_date: datetime = Field(...)
