#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states_non_sorted = list(storage.all(State).values())
    cities_non_sorted = list(storage.all(City).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    states = sorted(states_non_sorted, key=lambda states: states.name)
    cities = sorted(cities_non_sorted, key=lambda cities: cities.name)
    return render_template('100-hbnb.html', amenities=amenities,
                           states=states, cities=cities, places=places)

@app.teardown_appcontext
def teardown_context(exception):
    """remove the previous session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
