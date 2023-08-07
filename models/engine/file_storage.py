#!/usr/bin/python3
import json
from models.base_model import BaseModel

"""Defines a file storage class"""


class FileStorage:
    """ serializes instances to JSON file deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

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
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
