from fastapi import APIRouter, Depends
from app.summaries.schemas import SpendingSummary
from app.summaries import service
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()


@router.get("/", response_model=SpendingSummary)
def get_category_spending(db: Session = Depends(get_db)):
    return service.get_category_spending(db)
