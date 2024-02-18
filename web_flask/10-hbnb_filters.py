#!/usr/bin/python3
"""display the content of the 6-index.html"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states_non_sorted = list(storage.all(State).values())
    cities_non_sorted = list(storage.all(City).values())
    amenities_non_sorted = list(storage.all(Amenity).values())
    states = sorted(states_non_sorted, key=lambda state: state.name)
    cities = sorted(cities_non_sorted, key=lambda city: city.name)
    amenities = sorted(amenities_non_sorted, key=lambda amenity: amenity.name)
    return render_template("10-hbnb_filters.html", states=states, cities=cities, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
