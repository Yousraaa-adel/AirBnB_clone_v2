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


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    return render_template(
        "10-hbnb_filters.html",
        states=storage.all(State),
        amenities=storage.all(Amenity)
    )


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
