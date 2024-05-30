from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# List of daily cooking tips
cooking_tips = [
    "Use a sharp knife to save time and avoid accidents.",
    "Prep all your ingredients before you start cooking.",
    "Keep your herbs fresh by storing them properly.",
    "Learn to use and respect the power of fresh spices.",
    "Invest in good quality pots and pans."
]

@app.route('/daily_tip')
def daily_tip():
    # Simple daily tip logic: rotate tips based on the day of the year
    from datetime import datetime
    day_of_year = datetime.now().timetuple().tm_yday
    tip = cooking_tips[day_of_year % len(cooking_tips)]
    return jsonify({"tip": tip})

@app.route('/random_tip')
def random_tip():
    # Return a random tip from the list
    tip = random.choice(cooking_tips)
    return jsonify({"tip": tip})

if __name__ == '__main__':
    app.run(port=2000, debug=True)


