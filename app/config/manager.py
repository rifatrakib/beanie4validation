from typing import List

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import parse_obj_as

from app.config.factory import settings
from app.models.base import MapperSchema


def database_collection_mapper() -> MapperSchema:
    models = [
        {
            "database_name": "database_1",
            "model_paths": [
                "app.models.properties.User",
            ],
        }
    ]

    return parse_obj_as(type_=List[MapperSchema], obj=models)


async def pool_database_clients() -> None:
    client = AsyncIOMotorClient(settings.MONGO_URI)
    models: List[MapperSchema] = database_collection_mapper()

    for model in models:
        await init_beanie(
            database=client[model.database_name],
            document_models=model.model_paths,
        )
