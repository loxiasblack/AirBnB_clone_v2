#!/usr/bin/python3
"""scripts that starts a Flask web applications"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display the prompt below"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display the prompt below"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display if <text>"""
    name = text.replace("_", " ")
    return "C {}".format(name)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """display if <text> or diplay the default value"""
    name = text.replace("_", " ")
    return "Python {}".format(name)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display only if n is integer"""
    return "Number: {}".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display the template only if n is int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display the template only if n is int (even|odd)"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
