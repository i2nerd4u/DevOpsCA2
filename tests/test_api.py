import pytest
from app.app import create_app
from app import models

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_meal(client):
    models.weekly_store.clear()
    response = client.post("/api/add", json={
        "day": "Monday",
        "name": "Salad",
        "calories": 150
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["day"] == "Monday"
    assert data["name"] == "Salad"
    assert data["calories"] == 150

def test_get_day_total(client):
    models.weekly_store.clear()
    models.add_meal("Monday", "Salad", 150)
    response = client.get("/total/Monday")
    assert response.status_code == 200
    data = response.get_json()
    assert data["day"] == "Monday"
    assert data["total_calories"] == 150

def test_get_week_total(client):
    models.weekly_store.clear()
    models.add_meal("Monday", "Salad", 150)
    models.add_meal("Tuesday", "Chicken", 300)
    response = client.get("/total/week")
    assert response.status_code == 200
    data = response.get_json()
    assert data["week_total_calories"] == 450
