
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "correlation_id" in data
    assert data["message"] == "Hello, world!"
    assert isinstance(data["correlation_id"], str)
    assert len(data["correlation_id"]) > 0
