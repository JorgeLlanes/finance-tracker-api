from app.transactions import service
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.transactions.schemas import (
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate,
)
from app.transactions.exceptions import TransactionNotFoundError

router = APIRouter()


@router.post(
    "/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED
)
def create_transaction(body: TransactionCreate, db: Session = Depends(get_db)):
    return service.create_transaction(body, db)


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return service.get_transactions(db)


@router.get("/{id}", response_model=TransactionResponse)
def get_transaction_by_id(id: int, db: Session = Depends(get_db)):
    try:
        return service.get_transaction_by_id(id, db)
    except TransactionNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{id}", response_model=TransactionResponse)
def update_transaction(id: int, body: TransactionUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_transaction(id, body, db)
    except TransactionNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    try:
        return service.delete_transaction(id, db)
    except TransactionNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
