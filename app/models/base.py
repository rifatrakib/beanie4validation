from importlib import import_module
from typing import List

from pydantic import BaseModel, validator


class MapperSchema(BaseModel):
    name: str
    collections: List[str]

    @validator("collections")
    def validate_class_path(cls, value):
        for path in value:
            try:
                module_name, class_name = path.rsplit(".", 1)
                module = import_module(module_name)
                _ = getattr(module, class_name)
            except (ValueError, ImportError, AttributeError):
                raise ValueError(f"Invalid class path: {path}")
        return value
