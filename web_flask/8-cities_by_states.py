#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states_non_sorted = list(storage.all(State).values())
    citites_non_sorted = list(storage.all(City).values())
    states = sorted(states_non_sorted, key=lambda states: states.name)
    cities = sorted(citites_non_sorted, key=lambda cities: cities.name)
    return render_template('8-cities_by_states.html', states=states, cities=cities)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """close the session"""
    storage.close()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
