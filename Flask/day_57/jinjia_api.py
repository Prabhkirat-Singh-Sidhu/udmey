from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["Gender"]
    return render_template("guess.html", person_name = name, gender = gender)