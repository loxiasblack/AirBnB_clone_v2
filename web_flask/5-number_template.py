#!/usr/bin/python3
"""scripts that starts a Flask web applications"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """write the scripts below"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display the script below"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displat if texte"""
    name = text.replace("_", " ")
    return "C {}".format(name)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """display if text or is cool"""
    name = text.repalce("_", " ")
    return "Python {}".format(name)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display only if it's number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display an HTML"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
