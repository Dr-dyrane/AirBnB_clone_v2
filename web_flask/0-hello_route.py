#!/usr/bin/python3
"""This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and defines one route:
- '/': Displays "Hello HBNB!" when accessed.

Usage:
    Run this script directly to start the Flask web application.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Display a greeting message.

    Returns:
        str: A string containing the greeting message "Hello HBNB!".
    """
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
