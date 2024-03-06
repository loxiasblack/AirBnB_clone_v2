#!/usr/bin/python3
"""scritps that show places"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display my page"""
    states_non_sorted = list(storage.all(State).values())
    states = sorted(states_non_sorted, key=lambda state: state.name)
    cities_non_sorted = list(storage.all(City).values())
    cities = sorted(cities_non_sorted, key=lambda city: city.name)
    amenities_non_sorted = list(storage.all(Amenity).values())
    amenities = sorted(amenities_non_sorted, key=lambda amenity: amenity.name)
    places_non_sorted = list(storage.all(Place).values())
    places = sorted(places_non_sorted, key=lambda place: place.name)
    return render_template("100-hbnb.html", states=states, cities=cities)
    
@app.teardown_appcontext
def teardown_db(exception):
    """remove the database"""
    storage.close()
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
