#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

""" defines a BaseModel class which is the parent of all classes"""


class BaseModel():
    """The base class for the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """
        initialize the baseModel

        Args:
            *args: unused
            **kwargs: arguments for the constructor of a BaseModel
        """
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, time))
                    else:
                        setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid4()))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        returns the str output of the BaseaModel
        """
        return ("[{}] ({}) {}".
                format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all the keys/values of
        __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
