from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_response():
    response = client.get("/")
    assert response.json() == {"message": "Hello World"}


def test_home_message():
    response = client.get("/")
    assert response.json()["message"] == "Hello World"