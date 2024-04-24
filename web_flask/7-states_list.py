#!/usr/bin/python3
"""just a power of web framwirk"""

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """return an html with lists"""
    states = list(storage.all(State).values())
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def terdown_context(exception):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
