#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
import os
from sqlalchemy.orm import relationship
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenities.id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms =  Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship('Review', backref="place", cascade="all, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            reviews_instances = storage.all(Review)
            return [review for review in reviews_instances.values()
                    if review.place_id == self.id]
        
        @property
        def amenities(self):
            """"""
            return [amenity for amenity in self._current_place.amenities
                    if amenity.id in self._current_place.amenity_ids]
        
        @amenities.setter
        def amenities(self, amenity_instance):
            
            if isinstance(amenity_instance, Amenity):
                self._current_place.amenity_ids.append(amenity_instance.id)
