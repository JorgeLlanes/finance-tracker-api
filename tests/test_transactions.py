from decimal import Decimal
from unittest.mock import patch

from app.ai.exceptions import AIServiceUnavailableError


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_create_transaction(client):
    payload = {
        "amount": 14.99,
        "description": "testing subscription for apple music",
        "category": "subscription",
        "transaction_type": "expense",
    }

    response = client.post("/transactions/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["description"] == "testing subscription for apple music"
    assert data["category"] == "subscription"


def test_get_transactions(client):
    payload_one = {
        "amount": 19.99,
        "description": "testing subscription for claude",
        "category": "subscription",
        "transaction_type": "expense",
    }
    payload_two = {
        "amount": 19.99,
        "description": "testing subscription for chatGPT",
        "category": "subscription",
        "transaction_type": "expense",
    }

    response_post_one = client.post("/transactions/", json=payload_one)
    response_post_two = client.post("/transactions/", json=payload_two)
    response_get = client.get("/transactions/")

    assert response_post_one.status_code == 201
    assert response_post_two.status_code == 201
    assert response_get.status_code == 200

    data = response_get.json()
    assert len(data) == 2
    descriptions = [item["description"] for item in data]
    assert "testing subscription for claude" in descriptions
    assert "testing subscription for chatGPT" in descriptions


def test_get_transaction_by_id(client):
    payload = {
        "amount": 29.99,
        "description": "testing subscription for gym membership",
        "category": "membership",
        "transaction_type": "expense",
    }

    response = client.post("/transactions/", json=payload)
    assert response.status_code == 201

    created_id = response.json()["id"]
    response_get = client.get(f"/transactions/{created_id}")

    assert response_get.status_code == 200
    data = response_get.json()
    assert data["description"] == "testing subscription for gym membership"
    assert data["category"] == "membership"


def test_get_transaction_by_id_not_found(client):
    nonexistent_id = 9999
    response = client.get(f"/transactions/{nonexistent_id}")

    assert response.status_code == 404
    assert (
        response.json()["detail"] == f"Transaction with id {nonexistent_id} not found"
    )


def test_update_transaction(client):
    payload = {
        "amount": 129.99,
        "description": "testing updating transaction - groceries",
        "category": "grocery",
        "transaction_type": "expense",
    }

    response = client.post("/transactions/", json=payload)
    assert response.status_code == 201

    created_id = response.json()["id"]
    response_update = client.patch(
        f"/transactions/{created_id}", json={"amount": 89.99}
    )
    assert response_update.status_code == 200

    data = response_update.json()
    assert Decimal(data["amount"]) == Decimal("89.99")
    assert data["description"] == "testing updating transaction - groceries"
    assert data["category"] == "grocery"


def test_update_transaction_not_found(client):
    nonexistent_id = 8888
    response = client.patch(
        f"/transactions/{nonexistent_id}", json={"category": "trip"}
    )

    assert response.status_code == 404
    assert (
        response.json()["detail"] == f"Transaction with id {nonexistent_id} not found"
    )


def test_delete_transaction(client):
    payload = {
        "amount": 59.99,
        "description": "att wifi subscription",
        "category": "subscription",
        "transaction_type": "expense",
    }

    response = client.post("/transactions/", json=payload)
    assert response.status_code == 201

    created_id = response.json()["id"]
    response_delete = client.delete(f"/transactions/{created_id}")

    assert response_delete.status_code == 200
    assert response_delete.json()["message"] == "Transaction successfully deleted"

    response_get = client.get(f"/transactions/{created_id}")
    assert response_get.status_code == 404
    assert (
        response_get.json()["detail"] == f"Transaction with id {created_id} not found"
    )


def test_delete_transaction_not_found(client):
    nonexistent_id = 7777
    response = client.delete(f"/transactions/{nonexistent_id}")

    assert response.status_code == 404
    assert (
        response.json()["detail"] == f"Transaction with id {nonexistent_id} not found"
    )


def test_categorize_transaction(client):
    with patch(
        "app.transactions.service.ai_client.categorize_transaction"
    ) as mock_categorize:
        mock_categorize.return_value = "subscription"

        response = client.post(
            "/transactions/categorize", json={"description": "Netflix"}
        )

        assert response.status_code == 200
        assert response.json()["category"] == "subscription"


def test_categorize_transaction_ai_failure(client):
    with patch(
        "app.transactions.service.ai_client.categorize_transaction"
    ) as mock_categorize:
        mock_categorize.side_effect = AIServiceUnavailableError()

        response = client.post(
            "/transactions/categorize", json={"description": "Netflix"}
        )

        assert response.status_code == 503
        assert response.json()["detail"] == "AI categorization service unavailable"
