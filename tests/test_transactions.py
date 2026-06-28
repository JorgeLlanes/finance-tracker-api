def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_create_transaction(client):
    # Arrange — set up the data you need
    payload = {
        "amount": 14.99,
        "description": "testing subscription for apple music",
        "category": "subscription",
        "transaction_type": "expense",
    }

    # Act — perform the actual action being tested
    response = client.post("/transactions/", json=payload)

    # Assert — verify the outcome is correct
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