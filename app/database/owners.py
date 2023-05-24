from beanie import Document, Link

from app.database.dwellings import PropertyDocument, UnitDocument
from app.models.owners import PersonModel, PropertyOwnerModel, UnitOwnerModel


class PersonDocument(Document, PersonModel):
    class Settings:
        name = "people"
        indexes = ["person_id", "first_name", "last_name", "address"]


class PropertyOwnerDocument(Document, PropertyOwnerModel):
    person: Link[PersonDocument]
    property: Link[PropertyDocument]

    class Settings:
        name = "property_owners"


class UnitOwnerDocument(Document, UnitOwnerModel):
    person: Link[PersonDocument]
    unit: Link[UnitDocument]

    class Settings:
        name = "unit_owners"
