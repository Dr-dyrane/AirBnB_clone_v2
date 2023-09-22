#!/usr/bin/python3
"""This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and defines several routes:
- '/': Displays "Hello HBNB!" when accessed.
- '/hbnb': Displays "HBNB" when accessed.
- '/c/<text>': Displays "C " followed by the value of the text variable,
  with underscores (_) replaced by spaces.
- '/python/(<text>)': Displays "Python " followed by: value of - text variable,
  with (_) replaced by spaces. The default value of text is "is cool".
- '/number/<n>': Displays "n is a number" only if n is an integer.
- '/number_template/<n>': Displays an HTML page with an H1 tag containing
  "Number: n" inside the BODY tag, only if n is an integer.

Usage:
    Run this script directly to start the Flask web application.
"""

from flask import Flask, render_template

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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Display 'Python ' followed by the value of the text variable.

    Args:
        text (str): The text variable provided in the URL.

    Returns:
        str: A string containing "Python " followed by the processed text.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """Display 'n is a number' if n is an integer.

    Args:
        n (int): The number provided in the URL.

    Returns:
        str: A string containing "n is a number" if n is an integer,
        or a 404 error if n is not an integer.
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplate(n=None):
    """Display an HTML page with the number if n is an integer.

    Args:
        n (int): The number provided in the URL.

    Returns:
        str: An HTML page containing an H1 tag with "Number: n" - the BODY tag,
        or a 404 error if n is not an integer.
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
