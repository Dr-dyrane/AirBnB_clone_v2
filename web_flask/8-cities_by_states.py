#!/usr/bin/python3
"""
Web Application with Flask

This script starts a Flask web application to display
a list of States and their associated Cities.

Web Application Routes:
- '/cities_by_states': Displays a list of States with their associated Cities.

Usage:
    - Run this script to start the Flask web application.
    - Access the '/cities_by_states' route in your web browser
    - to see the list of States and Cities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """
    Teardown method to remove the current SQLAlchemy Session.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Route that renders an HTML page displaying
    a list of States with their associated Cities.

    Returns:
        str: Rendered HTML page with States and Cities.
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
