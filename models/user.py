#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_engine = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """ Representation of the User class. """

    if storage_engine == "db":
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            'Place', cascade='all, delete, delete-orphan', backref='user'
            )
        reviews = relationship(
            'Review', cascade='all, delete, delete-orphan', backref='user'
            )

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
