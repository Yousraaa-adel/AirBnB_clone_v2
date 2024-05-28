#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models

storage_engine = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ Representation of the State class. """

    if storage_engine == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship(
                "City", cascade='all, delete, delete-orphan', backref="state"
                )

    else:
        name = ""

        @property
        def cities(self):
            """ Getter for FileStorage Mode """
            result = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    result.append(city)
            return result
