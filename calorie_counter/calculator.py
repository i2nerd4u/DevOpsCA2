"""This module contains the CalorieCounter class for tracking daily calories."""
class CalorieCounter:
    """Handles calorie counting for the day."""

    def __init__(self):
        self.total = 0
        self.food_log = []

    def add_food(self, food: str, calories: int):
        """Add calories for a food item."""
        self.food_log.append((food, calories))
        self.total += calories

    def total_calories(self):
        """Return total calories for the day."""
        return self.total

    def reset_day(self):
        """Reset total calories for a new day."""
        self.total = 0
