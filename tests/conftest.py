import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import Base, get_db
from app.transactions.models import Transaction
from fastapi.testclient import TestClient
from app.main import app

engine = create_engine(settings.test_database_url)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
