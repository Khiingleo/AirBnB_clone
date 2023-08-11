#!/usr/bin/python3
"""Defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherits from basemodel
    place_id (str) - to be the place id
    user_id (str) - to be the user id
    """
    place_id = ""
    user_id = ""
    text = ""
