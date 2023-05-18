from datetime import datetime

from pydantic import Field

from app.models.base import BaseModelConfig

# class TransactionModel(BaseModelConfig):
#     date: datetime = Field(...)
#     amount: float = Field(..., gt=0)
#     type: str = Field(..., min_length=1, max_length=100)


class PropertyTransactionModel(BaseModelConfig):
    date: datetime = Field(...)
    amount: float = Field(..., gt=0)
    type: str = Field(..., min_length=1, max_length=100)


class UnitTransactionModel(BaseModelConfig):
    date: datetime = Field(...)
    amount: float = Field(..., gt=0)
    type: str = Field(..., min_length=1, max_length=100)
