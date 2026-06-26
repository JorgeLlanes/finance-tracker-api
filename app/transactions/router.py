from app.transactions import service
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.transactions.schemas import (
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate,
)

router = APIRouter()


@router.post("/", response_model=TransactionResponse)
def create_transaction(body: TransactionCreate, db: Session = Depends(get_db)):
    return service.create_transaction(body, db)


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return service.get_transactions(db)


@router.get("/{id}", response_model=TransactionResponse)
def get_transaction_by_id(id: int, db: Session = Depends(get_db)):
    return service.get_transaction_by_id(id, db)


@router.patch("/{id}", response_model=TransactionResponse)
def update_transaction(id: int, body: TransactionUpdate, db: Session = Depends(get_db)):
    return service.update_transaction(id, body, db)


@router.delete("/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    return service.delete_transaction(id, db)
