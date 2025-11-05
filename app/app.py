from flask import Flask, render_template, request
from models import add_meal, weekly_store, get_week_total
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        calories = int(request.form.get("calories", 0))
        day = datetime.now().strftime("%A")
        add_meal(day, name, calories)

    week_total = get_week_total()
    return render_template("index.html", week_total=week_total, store=weekly_store)

if __name__ == "__main__":
    app.run(debug=True)
