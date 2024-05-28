#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place

storage_engine = getenv("HBNB_TYPE_STORAGE")

the_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

the_tables = {
    "states": State, "cities": City,
    "users": User, "places": Place,
    "reviews": Review, "amenities": Amenity
}

if storage_engine == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
