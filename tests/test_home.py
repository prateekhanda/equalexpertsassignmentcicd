def test_home_root(client):
    response = client.get("/api/v1/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["version"] == "1.0.0"


def test_home_alias(client):
    response = client.get("/api/v1/home")
    assert response.status_code == 200