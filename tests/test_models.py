import importlib
from app import models 

def test_add_and_totals():
    models.weekly_store.clear()
    models.add_meal("Monday", "Salad", 150)
    models.add_meal("Monday", "Chicken", 300)   
    assert models.get_day_total("Monday") == 450