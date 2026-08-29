from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import date
from app.transactions.models import TransactionEnum


class SummaryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    category: str
    amount: Decimal
    transaction_type: TransactionEnum


class SpendingSummary(BaseModel):

    start_date: date
    end_date: date
    summaries: list[SummaryResponse]
