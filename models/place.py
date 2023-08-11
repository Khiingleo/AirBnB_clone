#!/usr/bin/python3
"""defines a class Place that inherits from Base"""
from models.base_model import BaseModel


class Place(BaseModel):
    """inherits from BaseModel
    city_id (str)
    user_id (str)
    name (str)
    description (str)
    number_rooms (int)
    max_guest (int)
    price_by_night (int)
    latitude (float)
    longitude (float)
    amenity_ids (list of strings) (to be the amenity id)
    """
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
