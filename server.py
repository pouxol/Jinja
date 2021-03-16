from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/guess/<name>")
def home(name):
    random_number = random.randint(1,10)
    this_year = datetime.now().year
    response = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = response["gender"]
    return render_template("index.html", num=random_number, year=this_year, name=name, gender=gender)


@app.route("/other_page/<numb>")
def other_page(numb):
    return "This is another Page!"


if __name__ == "__main__":
    app.run(debug=True)
