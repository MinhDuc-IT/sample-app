import pytest
from fastapi.testclient import TestClient

from app import app
from calculator import add, divide


client = TestClient(app)


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_web_client_is_served():
    response = client.get("/")

    assert response.status_code == 200
    assert "Agent-QC Calculator" in response.text


def test_add_api():
    response = client.get("/api/add", params={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_api():
    response = client.get("/api/divide", params={"a": 10, "b": 2})

    assert response.status_code == 200
    assert response.json() == {"result": 5.0}
