from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_user():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "the current user"}
