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
    states_non_sorted = list(storage.all(State).values())
    cities_non_sorted = list(storage.all(City).values())
    states = sorted(states_non_sorted, key=lambda state: state.name)
    cities = sorted(cities_non_sorted, key=lambda city: city.name)
    return render_template("9-states.html", states=states, cities=cities)

@app.teardown_appcontext
def teardown_db(exception):
    """remove the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    

