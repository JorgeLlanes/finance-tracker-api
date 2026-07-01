from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.transactions.models import Transaction


def get_category_spending(db: Session):
    stmt = (
        select(
            func.lower(Transaction.category).label("category"),
            Transaction.transaction_type,
            func.sum(Transaction.amount).label("amount"),
        )
        .where(Transaction.transaction_type == "expense")
        .group_by(func.lower(Transaction.category), Transaction.transaction_type)
    )

    results = db.execute(stmt).all()

    return results
