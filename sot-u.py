#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


states = list(storage.all(State).values())
cities = list(storage.all(City).values())

for state in states:
    print(state.name)
print("--------")
for city in cities:
    print(city.name)
