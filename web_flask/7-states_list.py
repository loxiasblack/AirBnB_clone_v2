#!/usr/bin/python3
"""list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    states = list(storage.all(State).values())
    sorted_list = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_list)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
