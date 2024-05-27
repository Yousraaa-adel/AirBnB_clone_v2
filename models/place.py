#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


metadata = Base.metadata
place_amenity = Table("place_amenity",metadata ,
    Column('place_id', String(60), ForeignKey("places.id"),primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey("amenities.id"),primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship("Amenity", secondary="place_amenity", back_populates="place_amenities", overlaps="place_amenities")
    
    if getenv("HBNB_TYPE_STORAGE") == 'db':
       reviews = relationship(
           "Review", cascade='all, delete, delete-orphan', backref="reviews"
       )

    else:
        @property
        def reviews(self):
            """ Getter for FileStorage Mode """
            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if reviews.place_id  == self.id:
                    review_list.append(review)
            return review_list
