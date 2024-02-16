#!/usr/bin/python3
"""scripts that starts a Flask web applications"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display the prompt bellow"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display the prompt bellow"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """print with argument"""
    name = text.replace("_", " ")
    return "C {}".format(name)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """print with argument"""
    name = text.replace("_", " ")
    return "Python {}".format(name)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """print only if n is int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
