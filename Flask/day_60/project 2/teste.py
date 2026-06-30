#diff in requests and request
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=["POST"])
def weather():

    city = request.form["city"]     # Read from browser

    response = requests.get(
        f"https://api.weatherapi.com/?city={city}"
    )                               # Send to another server

    return response.text