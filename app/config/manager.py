import json
from typing import List

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import parse_file_as, parse_obj_as

from app.config.factory import settings
from app.database.dwellings import PropertyDocument, UnitDocument
from app.database.owners import PersonDocument, PropertyOwnerDocument, UnitOwnerDocument
from app.database.transactions import PropertyTransactionDocument, UnitTransactionDocument
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

    persons = parse_file_as(path="app/resources/persons-data.json", type_=List[PersonDocument])
    for person in persons:
        await person.save()

    with open("app/resources/property-ownership-data.json", "r") as f:
        property_ownerships = json.load(f)

    for property_ownership in property_ownerships:
        person = await PersonDocument.find_one({"person_id": property_ownership["person_id"]})
        property = await PropertyDocument.find_one({"property_id": property_ownership["property_id"]})
        record = PropertyOwnerDocument(
            person=person,
            property=property,
            owned_share=property_ownership["owned_share"],
            from_date=property_ownership["from_date"],
        )
        await record.save()

    with open("app/resources/unit-ownership-data.json", "r") as f:
        unit_ownerships = json.load(f)

    for unit_ownership in unit_ownerships:
        person = await PersonDocument.find_one({"person_id": unit_ownership["person_id"]})
        unit = await UnitDocument.find_one({"unit_id": unit_ownership["unit_id"]})
        record = UnitOwnerDocument(
            person=person,
            unit=unit,
            owned_share=unit_ownership["owned_share"],
            from_date=unit_ownership["from_date"],
        )
        await record.save()

    with open("app/resources/property-transaction-data.json", "r") as f:
        property_transactions = json.load(f)

    for property_transaction in property_transactions:
        buyer = await PersonDocument.find_one({"person_id": property_transaction["buyer_id"]})
        seller = await PersonDocument.find_one({"person_id": property_transaction["seller_id"]})
        property = await PropertyDocument.find_one({"property_id": property_transaction["property_id"]})
        record = PropertyTransactionDocument(
            buyer=buyer,
            seller=seller,
            property=property,
            amount=property_transaction["amount"],
            date=property_transaction["date"],
            type=property_transaction["type"],
        )
        await record.save()

    with open("app/resources/unit-transaction-data.json", "r") as f:
        unit_transactions = json.load(f)

    for unit_transaction in unit_transactions:
        buyer = await PersonDocument.find_one({"person_id": unit_transaction["buyer_id"]})
        seller = await PersonDocument.find_one({"person_id": unit_transaction["seller_id"]})
        unit = await UnitDocument.find_one({"unit_id": unit_transaction["unit_id"]})
        record = UnitTransactionDocument(
            buyer=buyer,
            seller=seller,
            unit=unit,
            amount=unit_transaction["amount"],
            date=unit_transaction["date"],
            type=unit_transaction["type"],
        )
        await record.save()


async def populate_collections():
    await pool_database_clients()
    await initialize()
