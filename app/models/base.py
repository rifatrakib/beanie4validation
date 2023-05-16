from datetime import datetime
from importlib import import_module
from typing import List

from pydantic import BaseModel, validator

from app.utilities.formatters import format_datetime_into_isoformat


class BaseDocument(BaseModel):
    class Config:
        orm_mode: bool = True
        use_enum_values: bool = True
        validate_assignment: bool = True
        allow_population_by_field_name: bool = True
        json_encoders: dict = {datetime: format_datetime_into_isoformat}


class MapperSchema(BaseModel):
    database_name: str
    model_paths: List[str]

    @validator("model_paths")
    def validate_model_paths(cls, value):
        for path in value:
            try:
                module_name, class_name = path.rsplit(".", 1)
                module = import_module(module_name)
                _ = getattr(module, class_name)
            except (ValueError, ImportError, AttributeError):
                raise ValueError(f"Invalid class path: {path}")
        return value
