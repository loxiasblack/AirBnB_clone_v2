#!/usr/bin/python3
"""The New database engine"""
from sqlalchemy import (create_engine)
import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """the file storage"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation"""
        db_user = os.getenv("HBNB_MYSQL_USER")
        db_password = os.getenv("HBNB_MYSQL_PWD")
        db_host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(db_user, db_password,
                                             db_host, db_name),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """retrive classes"""
        my_classes = (Amenity, City, Place, Review, State, User)
        objects = dict()

        if cls is None:
            for item in my_classes:
                query = self.__session.query(item)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """add object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit the changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        my_session = scoped_session(Session)
        self.__session = my_session()

    def close(self):
        """close the session"""
        self.__session.close()
