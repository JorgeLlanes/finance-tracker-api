from fastapi import FastAPI
from app.config import settings
from app.transactions.router import router

app = FastAPI(title=settings.app_name)


@app.get("/health")
def root():
    return {"message": "Hello World"}


app.include_router(router, prefix="/transactions", tags=["transactions"])
