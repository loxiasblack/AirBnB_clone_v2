#!/usr/bin/python3
""""""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """display the states"""
    states_non_sorted = list(storage.all(State).values())
    states = sorted(states_non_sorted, key=lambda state: state.name)
    return render_template("9-states.html", states=states)

@app.route('/states/<id>', strict_slashes=False)
def cities_by_state():
    """display the states with there cities"""
    
