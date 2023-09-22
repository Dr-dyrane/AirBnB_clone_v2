#!/usr/bin/python3
"""
Flask Web Application

This script starts a Flask web application with various routes
for different purposes.

Routes:
- '/': Returns a greeting message.
- '/hbnb': Returns "HBNB".
- '/c/<text>': Displays "C" followed by the value of the text variable.
- '/python' and '/python/<text>': Displays "Python" followed by:
    value - the text variable.
- '/number/<int:n>': Displays "<n> is a number" if n is an integer.
- '/number_template/<int:n>': Displays an HTML page with
    the number if n is an integer.
- '/number_odd_or_even/<int:n>': Displays an HTML page with information
    about whether n is even or odd.

Usage:
    Run this script to start the Flask web application.
    Access the defined routes in your web browser.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Route that returns a greeting.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that returns "HBNB".

    Returns:
        str: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """
    Route that displays "C" followed by the value of the text variable.

    Args:
        text (str): The text to be displayed.
        
    Returns:
        str: "C" followed by the modified text.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """
    Route that displays "Python" followed by the value of the text variable.

    Args:
        text (str, optional): The text to be displayed. Defaults to "is cool".

    Returns:
        str: "Python" followed by the modified text.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """
    Route that displays "<n> is a number" if n is an integer.

    Args:
        n (int): The number to be checked.

    Returns:
        str: "<n> is a number" if n is an integer.
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """
    Route that displays an HTML page with the number if n is an integer.

    Args:
        n (int, optional): The number to be displayed in the HTML page.
        Defaults to None.

    Returns:
        str: HTML page with the number if n is an integer.
    """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """
    Route that displays an HTML page with information
    about whether n is even or odd.

    Args:
        n (int, optional): The number to be checked. Defaults to None.

    Returns:
        str: HTML page with information about whether n is even or odd.
    """
    if isinstance(n, int):
        if n % 2:
            eo = "odd"
        else:
            eo = "even"
        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run()
