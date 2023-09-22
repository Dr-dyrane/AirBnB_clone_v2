#!/usr/bin/python3
"""
Web Application with Flask

This script starts a Flask web application to display
a list of States and their associated Cities.

Web Application Routes:
- '/states': Displays a list of States.
- '/states/<id>': Displays the Cities associated with
a specific State or a "Not found!" message.

Usage:
    - Run this script to start the Flask web application.
    - Access the '/states' route in your web browser to see the list of States.
    - Access the '/states/<id>' route to see
    - Cities associated with a specific State.
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


@app.route('/states', strict_slashes=False)
def state():
    """
    Route that renders an HTML page displaying a list of States.

    Returns:
        str: Rendered HTML page with a list of States.
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
    Route that renders an HTML page displaying Cities associated with
    a specific State or "Not found!".

    Args:
        id (str): The ID of the State to display Cities for.

    Returns:
        str: Rendered HTML page with Cities - the State / "Not found!" message.
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
