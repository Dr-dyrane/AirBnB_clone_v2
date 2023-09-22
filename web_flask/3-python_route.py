#!/usr/bin/python3
"""This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and defines four routes:
- '/': Displays "Hello HBNB!" when accessed.
- '/hbnb': Displays "HBNB" when accessed.
- '/c/<text>': Displays "C " followed by the value of the text variable, 
  with underscores (_) replaced by spaces.
- '/python/<text>': Displays "Python " followed by the value of the text variable,
  with underscores (_) replaced by spaces. The default value of text is "is cool".

Usage:
    Run this script directly to start the Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Display a greeting message.

    Returns:
        str: A string containing the greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a message.

    Returns:
        str: A string containing the message "HBNB".
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Display 'C ' followed by the value of the text variable.

    Args:
        text (str): The text variable provided in the URL.

    Returns:
        str: A string containing "C " followed by the processed text.
    """
    return "C {}".format(text.replace("_", " "))

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text):
    """Display 'Python ' followed by the value of the text variable.

    Args:
        text (str): The text variable provided in the URL.

    Returns:
        str: A string containing "Python " followed by the processed text.
    """
    return "Python {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
