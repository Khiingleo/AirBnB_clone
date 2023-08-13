#!/usr/bin/python3
"""Define a module City that inherits from  Base"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherits from the class BaseModel"""
    state_id = ""
    name = ""
