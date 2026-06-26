from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from datetime import datetime
from app.transactions.models import TransactionEnum


class TransactionCreate(BaseModel):
    amount: Decimal
    description: str = Field(max_length=72)
    category: str = Field(max_length=32)
    transaction_type: TransactionEnum


class TransactionResponse(TransactionCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class TransactionUpdate(BaseModel):
    amount: Decimal | None = None
    description: str | None = Field(default=None, max_length=72)
    category: str | None = Field(default=None, max_length=32)
    transaction_type: TransactionEnum | None = None
