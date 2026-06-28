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
