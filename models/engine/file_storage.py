#!/usr/bin/python3
"""Defines a file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to JSON file deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects as the obj with <obj class name>.id

        Args:
            obj
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file path (__file_path)"""
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSOn file (__file_path) exists, otherwise do nothing"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    cls = globals()[class_name]
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
