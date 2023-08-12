#!/usr/bin/python
""" unittest for the models/engine/file_storage"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test cases for the file storage class"""
    @classmethod
    def setUp(cls):
        cls.file_storage = FileStorage()
        cls.file_storage.reload()

    @classmethod
    def tearDown(cls):
        for model in cls.file_storage._FileStorage__objects.values():
            model.save()
        del cls.file_storage
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        instances_dict = self.file_storage.all()
        self.assertIsNotNone(instances_dict)
        self.assertIsInstance(instances_dict, dict)
        self.assertIs(instances_dict, self.file_storage._FileStorage__objects)

    def test_new(self):
        bm = BaseModel()
        self.file_storage.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, self.file_storage._FileStorage__objects)

    def test_save_reload(self):
        bm = BaseModel()
        storage = FileStorage()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        storage.new(bm)
        storage.save()
        del storage
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn(key, all_objects)

    def test_reload_invalid_class(self):
        invalid_data = {"InvalidClass.123": {"__class__": "InvalidClass"}}
        with open(self.file_storage._FileStorage__file_path, 'w') as f:
            json.dump(invalid_data, f)
        with self.assertRaises(KeyError):
            self.file_storage.reload()

if __name__ == "__main__":
    unittest.main()
