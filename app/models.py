# app/models.py

weekly_store = {}

def add_meal(day, name, calories):
    if day not in weekly_store:
        weekly_store[day] = []
    meal = {"day": day,"name": name, "calories": calories}
    weekly_store[day].append(meal)
    return meal

def get_day_total(day):
    if day not in weekly_store:
        return 0
    return sum(meal["calories"] for meal in weekly_store[day])

def get_week_total():
    return sum(get_day_total(day) for day in weekly_store)
