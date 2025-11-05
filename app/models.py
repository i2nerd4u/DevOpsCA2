# models.py
from collections import defaultdict

# Stores meals by day
weekly_store = defaultdict(list)

def add_meal(day, name, calories):
    """Add a meal to the weekly store."""
    weekly_store[day].append({"name": name, "calories": calories})

def get_week_total():
    """Calculate total calories for the week."""
    total = 0
    for meals in weekly_store.values():
        for meal in meals:
            total += meal["calories"]
    return total
