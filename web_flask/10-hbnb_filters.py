#!/usr/bin/python3
"""
Starts a Flask web application for displaying HBnB filters.

This script starts a Flask web application that displays HBnB filters
including States and Amenities.

Web Application Routes:
- '/hbnb_filters': Displays a webpage with HBnB filters.

Usage:
    - Run this script to start the Flask web application.
    - Access the '/hbnb_filters' route in your web browser to see the filters.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Route that renders an HTML page displaying HBnB filters.

    Returns:
        str: Rendered HTML page with HBnB filters (States and Amenities).
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
    Teardown method to remove the current SQLAlchemy Session.

    Args:
        exc: The exception, if any.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
