from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_user():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "the current user"}


def test_alexnet_model_name():
    model_name = "alexnet"
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 200
    assert response.json()["model_name"] == model_name
    assert response.json()["message"] == "Deep Learning FTW!"


def test_items_have_ids():
    response = client.get("/items")
    assert response.status_code == 200

    items: list[dict[str, str | int]] = response.json()

    assert len(items) == 3

    for item in items:
        assert "id" in item.keys(), "Item does not have an id"
        assert "item_name" in item.keys(), "Item does not have an item_name"


def test_get_item_by_id():
    item_id = 1
    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200

    response_item = response.json()

    assert response_item.get("id") == item_id


def test_different_items_have_different_names_and_ids():

    item_calls = [client.get(f"/items/{item_id}").json() for item_id in (0, 1, 2)]

    item_names = set(item.get("item_name") for item in item_calls)
    item_ids = set(item.get("id") for item in item_calls)

    assert len(item_calls) == len(item_names) == len(item_ids)
