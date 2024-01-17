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
        """"""
        db_user = os.getenv("HBNB_MYSQL_USER")
        db_password = os.getenv("HBNB_MYSQL_PWD")
        db_host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")

        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(db_user, db_password, db_host, db_name),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)
    
    def all(self, cls=None):
        """"""
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]
        dictionary = {}
        for class_obj in classes:
            query_result = self.__session.query(class_obj).all()
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dictionary[key] = obj
        return dictionary
            
        
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
