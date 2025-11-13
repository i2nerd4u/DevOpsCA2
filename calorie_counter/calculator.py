class CalorieCounter:
    def __init__(self):
        self.entries = []

    def add_food(self, food_name, calories):
        if calories < 0:
            raise ValueError("Calories cannot be negative.")
        self.entries.append({"food": food_name, "calories": calories})

    def total_calories(self):
        return sum(item["calories"] for item in self.entries)

    def reset_day(self):
        self.entries = []
