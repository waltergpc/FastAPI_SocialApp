from fastapi.testclient import TestClient
from app.main import app
from app import schemas


client = TestClient(app)


def test_root():
    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/", json={"email": "hello1234@gmail.com", "password": "password123"}
    )

    new_user = schemas.UserResponse(**res.json())
    assert res.status_code == 201
    assert new_user.email == "hello1234@gmail.com"
