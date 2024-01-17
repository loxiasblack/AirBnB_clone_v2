#!/usr/bin/python3
"""test script to see if my client does what it should do"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBStorage:
    """New engine that store in a database"""
    __engine = None
    __session = None
    
    def __init__(self):
        """initializing"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        db = os.getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(user, password, host, db),
                                      pool_pre_ping=True)
        if host == "test":
            Base.metadata.drop_all()
            
    def all(self, cls=None):
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            
    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
