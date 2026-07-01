# Finance Tracker API

A production-grade REST API for personal finance management, built with Python and FastAPI. Supports full transaction lifecycle management with category-based spending summaries and a robust test suite.

> **Phase 2 in progress:** AI-powered transaction categorization and natural language financial insights using the Anthropic API.

---

## Tech Stack

| Layer      | Technology     |
| ---------- | -------------- |
| Framework  | FastAPI        |
| Language   | Python 3.12    |
| Database   | PostgreSQL     |
| ORM        | SQLAlchemy 2.0 |
| Migrations | Alembic        |
| Validation | Pydantic v2    |
| Testing    | pytest         |
| Server     | Uvicorn        |

---

## Features

- Full CRUD for financial transactions (create, read, update, delete)
- Partial updates via `PATCH` with Pydantic schema validation
- Category-based spending summaries with SQL aggregation
- Domain-driven architecture with a dedicated service layer
- Custom exception hierarchy decoupling business logic from HTTP
- Isolated test database with full pytest coverage across all endpoints
- Auto-generated interactive API docs via Swagger UI

---

## Architecture

```
app/
├── transactions/
│   ├── models.py        # SQLAlchemy ORM model
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── router.py        # FastAPI route definitions
│   ├── service.py       # Business logic layer
│   └── exceptions.py   # Custom exception hierarchy
├── summaries/
│   ├── schemas.py       # Summary response schema
│   ├── router.py        # Summary route definitions
│   └── service.py       # Aggregate query logic
├── config.py            # Pydantic Settings config
├── database.py          # SQLAlchemy engine and session management
└── main.py              # FastAPI app entry point
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL

### Installation

```bash
# Clone the repo
git clone git@github.com:JorgeLlanes/finance-tracker-api.git
cd finance-tracker-api

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```
APP_NAME=Finance Tracker API
DEBUG=True
DATABASE_URL=postgresql://your_user@localhost:5432/finance_tracker
TEST_DATABASE_URL=postgresql://your_user@localhost:5432/finance_tracker_test
```

### Database Setup

```bash
# Create the database
createdb finance_tracker

# Run migrations
alembic upgrade head
```

### Run the Server

```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

---

## API Endpoints

### Transactions

| Method   | Endpoint             | Description                    |
| -------- | -------------------- | ------------------------------ |
| `POST`   | `/transactions/`     | Create a transaction           |
| `GET`    | `/transactions/`     | Get all transactions           |
| `GET`    | `/transactions/{id}` | Get transaction by ID          |
| `PATCH`  | `/transactions/{id}` | Partially update a transaction |
| `DELETE` | `/transactions/{id}` | Delete a transaction           |

### Summaries

| Method | Endpoint      | Description                            |
| ------ | ------------- | -------------------------------------- |
| `GET`  | `/summaries/` | Get total spending grouped by category |

---

## Running Tests

```bash
# Create the test database
createdb finance_tracker_test

# Run the full test suite
pytest tests/ -v
```

Tests use an isolated PostgreSQL database that is created fresh and torn down after every test run, ensuring no data leakage between tests.

---

## Roadmap

- [x] Full CRUD for transactions
- [x] Category spending summaries
- [x] Custom exception architecture
- [x] Full pytest coverage
- [ ] AI-powered transaction categorization (Anthropic API)
- [ ] Natural language financial insights
- [ ] RAG-based query engine for conversational finance queries
- [ ] JWT authentication
- [ ] Deployment on Railway

---

## License

MIT
