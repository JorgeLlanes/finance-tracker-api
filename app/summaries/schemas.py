from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from app.transactions.models import TransactionEnum


class SummaryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    category: str
    amount: Decimal
    transaction_type: TransactionEnum
