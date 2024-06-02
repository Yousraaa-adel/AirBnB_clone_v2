#!/usr/bin/python3

"""
    This is a script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
"""

from flask import Flask, render_template
from models import *
from models import storage
from operator import attrgetter

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_cities():
    states = sorted(list(storage.all(State).values()), key=attrgetter("name"))
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

