#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    
    # id = Column(String(60), primary_key=True, nullable=False)
    # created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    # updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            print("Initializing with default values")
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            print("Initializing with provided values")
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    iso = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, iso))
                else:
                    setattr(self, key, value)

            if not hasattr(self, "created_at"):
                self.created_at = datetime.now()
            if not hasattr(self, "updated_at"):
                self.updated_at = datetime.now()

        self.id = str(uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        from models import storage
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        print("Dictionary before removing _sa_instance_state:", dictionary)
        dictionary.pop('_sa_instance_state', None)
        print("Dictionary after removing _sa_instance_state:", dictionary)


        return dictionary

    def delete(self):
        """ Deletes the current instance from the storage. """
        from models import storage
        # This method should be called on an instance.
        print(storage)
