from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.summaries.schemas import SpendingSummary, SummaryResponse
from app.transactions.models import Transaction
from datetime import date
from dateutil.relativedelta import relativedelta


def get_category_spending(db: Session, reference_date: date | None = None):

    if reference_date is None:
        reference_date = date.today()

    start_date = reference_date.replace(day=1)
    end_date = start_date + relativedelta(months=1, days=-1)

    stmt = (
        select(
            func.lower(Transaction.category).label("category"),
            Transaction.transaction_type,
            func.sum(Transaction.amount).label("amount"),
        )
        .where(
            Transaction.transaction_type == "expense",
            Transaction.created_at >= start_date,
            Transaction.created_at <= end_date,
        )
        .group_by(func.lower(Transaction.category), Transaction.transaction_type)
    )

    results = db.execute(stmt).all()
    summaries = [SummaryResponse.model_validate(row) for row in results]

    return SpendingSummary(
        start_date=start_date, end_date=end_date, summaries=summaries
    )
