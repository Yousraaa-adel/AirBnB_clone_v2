#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv

storage_engine = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ Representation of the Amenity class. """

    if storage_engine == "db":

        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary="place_amenity", back_populates="amenities")

    else:
        name = ""
