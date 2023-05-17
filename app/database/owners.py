from beanie import Document, Link

from app.database.dwellings import PropertyDocument, UnitDocument
from app.models.owners import (
    CompanyModel,
    CompanyOwnerModel,
    EmploymentModel,
    PersonModel,
    PropertyOwnerModel,
    UnitOwnerModel,
)


class PersonDocument(Document, PersonModel):
    class Settings:
        collection = "people"
        indexes = ["person_id", "first_name", "last_name", "address"]


class CompanyDocument(Document, CompanyModel):
    class Settings:
        collection = "companies"
        indexes = ["company_id", "name", "address"]


class EmploymentDocument(Document, EmploymentModel):
    person: Link[PersonDocument]
    company: Link[CompanyDocument]

    class Settings:
        collection = "employments"
        indexes = ["role"]


class CompanyOwnerDocument(Document, CompanyOwnerModel):
    person: Link[PersonDocument]
    company: Link[CompanyDocument]

    class Settings:
        collection = "company_owners"


class PropertyOwnerDocument(Document, PropertyOwnerModel):
    person: Link[PersonDocument]
    property: Link[PropertyDocument]

    class Settings:
        collection = "property_owners"


class UnitOwnerDocument(Document, UnitOwnerModel):
    person: Link[PersonDocument]
    property: Link[UnitDocument]

    class Settings:
        collection = "unit_owners"
