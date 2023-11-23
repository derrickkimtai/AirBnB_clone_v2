#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.user import User
from models.city import City
from os import getenv

class DBStorage:
    """initilaze database """
    __engine = None
    __session = None

def __init__(self):
    '''database class'''
    user = getenv('HBNB_MYSQL_USER')
    pwd = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    db = getenv('HBNB_MYSQL_DB')
    self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db, pool_pre_ping=True))

    Base.metadata.create_all(self.__engine)

    if getenv('HBNB_ENV') == "test":
        Base.metadata.drop_all(self.__engine)    

def all(self, cls=None):
        """Returns a query contains objects"""
        dic_objects = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dic_objects[key] = obj
        else:
            for subcls in Base.__subclasses__():
                for obj in self.__session.query(subcls).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dic_objects[key] = obj
        return dic_objects

def new(self, obj):
        """add/make object to the current database session"""
        self.__session.add(obj)

def save(self):
        """commit all changes of  session and Flush"""
        self.__session.commit()

def delete(self, obj=None):
        """ delete obj by using session in curent """
        if obj is not None:
            self.__session.delete(obj)

def reload(self):
    Base.metadata.create_all(self.__engine)
    session_factory = sessionmaker(
    bind=self.__engine, expire_on_commit=False)
    Session = scoped_session(session_factory)
    self.__session = Session()

def close(self):
        """close the session"""
        self.__session.close()
