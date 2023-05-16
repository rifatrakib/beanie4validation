from typing import List

from pydantic import parse_obj_as

from app.models.base import MapperSchema


def database_collection_mapper() -> MapperSchema:
    models = [
        {
            "database_name": "beanie",
            "model_path": [],
        }
    ]

    return parse_obj_as(type_=List[MapperSchema], obj=models)
