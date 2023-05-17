from beanie import Document, Link

from app.models.dwellings import BuildingModel, PropertyModel, UnitModel


class PropertyDocument(Document, PropertyModel):
    class Settings:
        name = "properties"
        indexes = ["property_id", "address", "price"]


class BuildingDocument(Document, BuildingModel):
    property_id: Link[PropertyModel]

    class Settings:
        name = "buildings"
        indexes = ["building_id", "property_id", "address", "price", "floors"]


class UnitDocument(Document, UnitModel):
    property_id: Link[PropertyModel]
    building_id: Link[BuildingModel]

    class Settings:
        name = "units"
        indexes = ["unit_id", "building_id", "property_id", "address", "bedrooms", "bathrooms", "price"]
