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
    """ Displays a text """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays a text """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """ Displays a text """
    return "C " + text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text):
    """ Displays a text """
    return "Python " + text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def isnum(n):
    """ Displays a number """
    try:
        if n.isdigit():
            return f"{n} is a number"
    except ValueError:
        return "404 Not Found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
