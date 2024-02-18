#!/usr/bin/python3
"""display the list of states or the cities on the state"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """display the list of states"""
    states_non_sorted = list(storage.all(State).values())
    states = sorted(states_non_sorted, key=lambda state: state.name)
    return render_template("9-states.html", states=states, list_all=True)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    """display the states with there cities"""
    state = storage.all(State).get("State." + id)
    if state:
        cities_non_sorted = [city for city in storage.all(City).values()
                             if city.state_id == state.id]
        cities = sorted(cities_non_sorted, key=lambda city: city.name)
        return render_template("9-states.html", states=state,
                               cities=cities, list_all=False)
    else:
        return render_template("9-states.html", not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
