#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                             cascade="all, delete-orphan")
    
    @property
    def cities(self):
        from models import storage
        city_instances = storage.all(City)
        return [city for city in city_instances.values() 
                if city.state_id == self.id]
