from beanie import Document, Link

from app.database.dwellings import PropertyDocument, UnitDocument
from app.database.owners import PersonDocument
from app.models.transactions import PropertyTransactionModel, UnitTransactionModel


class PropertyTransactionDocument(Document, PropertyTransactionModel):
    property: Link[PropertyDocument]
    buyer: Link[PersonDocument]
    seller: Link[PersonDocument]

    class Settings:
        collection = "property_transactions"


class UnitTransactionDocument(Document, UnitTransactionModel):
    unit: Link[UnitDocument]
    buyer: Link[PersonDocument]
    seller: Link[PersonDocument]

    class Settings:
        collection = "unit_transactions"
