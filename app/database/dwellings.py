from beanie import Document, Link

from app.models.dwellings import BuildingModel, PropertyModel, UnitModel


class PropertyDocument(Document, PropertyModel):
    class Settings:
        name = "properties"
        indexes = ["property_id", "address", "price"]


class BuildingDocument(Document, BuildingModel):
    property: Link[PropertyDocument]

    class Settings:
        name = "buildings"
        indexes = ["building_id", "address", "price", "floors"]


class UnitDocument(Document, UnitModel):
    building: Link[BuildingDocument]

    class Settings:
        name = "units"
        indexes = ["unit_id", "address", "bedrooms", "bathrooms", "price"]
