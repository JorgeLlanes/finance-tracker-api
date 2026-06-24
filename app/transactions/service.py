from sqlalchemy.orm import Session
from sqlalchemy import select
from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate
from fastapi import HTTPException


def create_transaction(body: TransactionCreate, db: Session):
    new_transaction = Transaction(
        amount=body.amount,
        description=body.description,
        category=body.category,
        transaction_type=body.transaction_type,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def get_transactions(db: Session):
    stmt = select(Transaction)
    transactions = db.scalars(stmt).all()
    return transactions


def get_transaction_by_id(id: int, db: Session):
    stmt = select(Transaction).where(Transaction.id == id)
    result = db.execute(stmt)
    transaction = result.scalar_one_or_none()

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction


def delete_transaction(id: int, db: Session):
    stmt = select(Transaction).where(Transaction.id == id)
    result = db.execute(stmt)
    transaction = result.scalar_one_or_none()

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction successfully deleted"}
