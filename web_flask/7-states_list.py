#!/usr/bin/python3
"""
Web Application with Flask

This script starts a Flask web application with various routes
for displaying States.

Web Application Routes:
- '/states_list': Displays a list of States.

Usage:
    - Run this script to start the Flask web application.
    - Access the '/states_list' route in your web browser to see
    - the list of States.
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """
    Route that renders an HTML page displaying a list of States.

    Returns:
        str: Rendered HTML page with a list of States.
    """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """
    Teardown method to remove the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
