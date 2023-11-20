from fastapi.testclient import TestClient
from apps.login import app

client = TestClient(app)


def test_login_successful():
    response = client.post(
        "/api/login",
        json={"username": "john_doe", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful", "email": "john@example.com"}


def test_login_failed():
    response = client.post(
        "/api/login",
        json={"username": "nonexistent_user", "password": "wrong_password"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}
