#!/usr/bin/python3

"""
    This is a script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
