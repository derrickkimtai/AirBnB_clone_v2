#!/usr/bin/python3
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
import sys

class DBStorage:
    """Initialize database"""
    __engine = None
    __session = None

    def __init__(self):
        """Database class"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a query containing objects"""
        objects_dict = {}
        
        if cls:
            try:
                class_obj = getattr(sys.modules[__name__], cls)
                for obj in self.__session.query(class_obj).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects_dict[key] = obj
            except Exception as e:
                print(f"Error: {e}. Class {cls} not found or invalid.")
        else:
            for subclass in Base.__subclasses__():
                for obj in self.__session.query(subclass).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        """Add/make object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the session and flush"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj by using session in current"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
