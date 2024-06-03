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


@app.route("/states", strict_slashes=False)
def states():
    return render_template(
        "7-states_list.html",
        states=storage.all(State)
    )


@app.route("/states/<id>", strict_slashes=False)
def cities(id=None):
    return render_template(
        "9-states.html",
        states=storage.all(State).get(
            "State.{}".format(id)
        )
    )


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
