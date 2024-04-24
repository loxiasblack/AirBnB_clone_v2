#!/usr/bin/python3
""""""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City


app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display the filters"""
    states_non_sorted = list(storage.all(State).values())
    cities_non_sorted = list(storage.all(City).values())
    amenities_non_sorted = list(storage.all(Amenity).values())
    states = sorted(states_non_sorted, key=lambda states: states.name)
    cities = sorted(cities_non_sorted, key=lambda cities: cities.name)
    amenities = sorted(amenities_non_sorted, key=lambda aminities: aminities.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

@app.teardown_appcontext
def teardown_appcontext(exceptions):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
