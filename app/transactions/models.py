from enum import Enum
from decimal import Decimal
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class TransactionEnum(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Transaction(Base):
    __tablename__ = "transaction"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    description: Mapped[str] = mapped_column(String(72))
    category: Mapped[str] = mapped_column(String(30))
    transaction_type: Mapped[TransactionEnum]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"Transaction(id={self.id!r}, amount={self.amount!r}, description={self.description!r}, category={self.category!r}, transaction_type={self.transaction_type!r}, created_at={self.created_at!r})"
