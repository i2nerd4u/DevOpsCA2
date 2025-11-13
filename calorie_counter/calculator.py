class CalorieCounter:
    """Class to track daily calorie intake."""
    def __init__(self):
        self.meals = []

    def add_food(self, food, calories):
        """Add a meal with calories"""
        self.meals.append({"food": food, "calories": calories})

    def total_calories(self):
        """Return total calories for the day."""
        return sum(meal["calories"] for meal in self.meals)
    
    def list_meals(self):
        """Return a list of all meals"""
        return self.meals

    def reset_day(self):
        """Reset total calories for a new day."""
        self.meals = []
