#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.place import Place
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            getter attribute cities that returns
            the list of City instances with state_id
            """
            list_cities = []
            dict_cities = models.storage.all(City)
            for key, city in dict_cities.items():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
