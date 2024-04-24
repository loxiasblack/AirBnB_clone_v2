#!/usr/bin/python3
"""run the app"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """return the list of states"""
    states_non_sorted = list(storage.all(State).values())
    states = sorted(states_non_sorted, key=lambda states: states.name)
    return render_template('7-states_list.html', states=states, list_all=True)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    state = storage.all(State).get('State.' + id)
    if state:
        cities_non_sorted = list(storage.all(City).values())
        cities = sorted(cities_non_sorted, key=lambda cities: cities.name)
        return render_template('9-states.html', states=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
