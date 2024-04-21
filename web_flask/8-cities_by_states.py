#!/usr/bin/python3
"""display states with city on it"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the cities by there states"""
    cities_non_sorted = list(storage.all(City).values())
    states_non_sorted = list(storage.all(State).values())
    states = sorted(states_non_sorted, key=lambda state: state.name)
    cities = sorted(cities_non_sorted, key=lambda city: city.name)
    return render_template("8-cities_by_states.html",
                           cities=cities, states=states)


@app.teardown_appcontext
def terdown_context(exception):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
