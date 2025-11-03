from flask import Flask, request, jsonify
from app.models import add_meal, get_day_total as models_get_day_total, get_week_total as models_get_week_total

def create_app():
    app = Flask(__name__)

    @app.route('/api/add', methods=['POST'])
    def add():
        data = request.json
        day = data.get('day')
        name = data.get('name')
        calories = data.get('calories', 0)
        if not day or not name:
            return jsonify({"error": "Day and name are required"}), 400 
        meal = add_meal(day, name, calories)
        return jsonify(meal), 201

    @app.route('/total/<day>', methods=['GET'])
    def day_total(day):
        total = models_get_day_total(day)
        return jsonify({"day": day, "total_calories": total}), 200

    @app.route('/total/week', methods=['GET'])
    def week_total():
        total = models_get_week_total()
        return jsonify({"week_total_calories": total}), 200

    return app
