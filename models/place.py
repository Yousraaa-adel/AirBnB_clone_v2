#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Table
import models
from os import getenv


storage_engine = getenv("HBNB_TYPE_STORAGE")

if storage_engine == "db":
    metadata = Base.metadata

    place_amenity = Table("place_amenity", metadata,
        Column(
            'place_id', String(60), ForeignKey(
                "places.id", onupdate='CASCADE', ondelete='CASCADE'
                ),
            primary_key=True
            ),
        Column(
            'amenity_id', String(60), ForeignKey(
                "amenities.id", onupdate='CASCADE', ondelete='CASCADE'
                ),
            primary_key=True
            )
    )


class Place(BaseModel, Base):
    """ Representation of the Place class. """
    if storage_engine == "db":
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", back_populates="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, back_populates="place_amenities",
            viewonly=False
            )

    else:

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """ Getter for ammenities. """
            result = []
            for review in models.storage.all(models.Review).values():
                if review.place_id  == self.id:
                    result.append(review)
            return result

        @amenities.setter
        def amenities(self, obj):
            """ Setter for ammenities. """
            from models.amenity import Amenity
            classes = {
            "Amenity": Amenity
        }
            temp_class = classes['Amenity']
            if (isinstance(obj, temp_class)):
                self.amenity_ids.append(obj.id)
