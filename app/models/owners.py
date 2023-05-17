from datetime import datetime
from typing import ForwardRef, List, Union

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


class CompanyModel(BaseModelConfig):
    company_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=100)
    email: Union[EmailStr, None] = Field(default=None)
    phone: Union[str, None] = Field(default=None, min_length=1, max_length=15)
    website: Union[HttpUrl, None] = Field(default=None)
    address: str = Field(..., min_length=1, max_length=1000)
    links: List[str] = Field(default_factory=list)
    owned_share: float = Field(..., gte=0)
    parent: Union[ForwardRef("CompanyModel"), None] = Field(default=None)
    subsidiaries: List[ForwardRef("CompanyModel")] = Field(default_factory=list)


class EmploymentModel(BaseModelConfig):
    role: str = Field(..., min_length=1, max_length=100)
    salary: float = Field(..., gte=0)
    start_date: str = Field(..., min_length=1, max_length=100)
    end_date: Union[str, None] = Field(default=None, min_length=1, max_length=100)
    links: List[str] = Field(default_factory=list)


class CompanyOwnerModel(BaseModelConfig):
    total_share: int = Field(..., gt=0)
    owned_share: int = Field(..., gt=0)


class PropertyOwnerModel(BaseModelConfig):
    owned_share: float = Field(..., gt=0)
    from_date: datetime = Field(...)


class UnitOwnerModel(BaseModelConfig):
    owned_share: float = Field(..., gt=0)
    from_date: datetime = Field(...)
