from typing import List

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import parse_file_as, parse_obj_as

from app.config.factory import settings
from app.database.dwellings import UnitDocument
from app.models.base import MapperSchema


def database_collection_mapper() -> MapperSchema:
    models = [
        {
            "database_name": "database_1",
            "model_paths": [
                "app.database.dwellings.PropertyDocument",
                "app.database.dwellings.BuildingDocument",
                "app.database.dwellings.UnitDocument",
                "app.database.owners.PersonDocument",
                "app.database.owners.CompanyDocument",
                "app.database.owners.EmploymentDocument",
                "app.database.owners.CompanyOwnerDocument",
                "app.database.owners.PropertyOwnerDocument",
                "app.database.owners.UnitOwnerDocument",
                "app.database.transactions.PropertyTransactionDocument",
                "app.database.transactions.UnitTransactionDocument",
            ],
        },
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


async def initialize():
    units = parse_file_as(path="app/resources/dwellings-data.json", type_=List[UnitDocument])
    for unit in units:
        await unit.building.property.save()
        await unit.building.save()
        await unit.save()


async def populate_collections():
    await pool_database_clients()
    await initialize()
