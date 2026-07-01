from fastapi import FastAPI
from app.config import settings
from app.transactions.router import router as transactions_router
from app.summaries.router import router as summaries_router

app = FastAPI(title=settings.app_name)


@app.get("/health")
def root():
    return {"message": "Hello World"}


app.include_router(transactions_router, prefix="/transactions", tags=["transactions"])

app.include_router(summaries_router, prefix="/summaries", tags=["summaries"])
