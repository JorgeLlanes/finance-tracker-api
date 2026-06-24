from sqlalchemy.orm import Session
from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate

def create_transaction(body: TransactionCreate, db: Session):
    new_transaction = Transaction(
        amount = body.amount,
        description = body.description,
        category = body.category,
        transaction_type = body.transaction_type
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction



