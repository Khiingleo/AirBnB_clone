#!/usr/bin/python3
"""Unitests for the models/base_model.py"""

import unittest
import os
import models
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """unittest for the BaseModel class"""

    @classmethod
    def setUp(cls):
        cls.base_model = BaseModel()

    @classmethod
    def tearDown(cls):
        del cls.base_model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_id_uniqueness(self):
        other_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_base_model.id)

    def test_string_representation(self):
        str_rep = str(self.base_model)
        self.assertIn("[BaseModel]", str_rep)
        self.assertIn("id", str_rep)
        self.assertIn("created_at", str_rep)
        self.assertIn("updated_at", str_rep)

    def test_save_updates_updated_at(self):
        orig_updated_at = self.base_model.updated_at
        with patch('models.storage') as mock_storage:
            self.base_model.save()
            self.assertNotEqual(orig_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_output(self):
        dt_created = self.base_model.created_at
        dt_updated = self.base_model.updated_at
        obj_dict = self.base_model.to_dict()
        expected_out = {
            'id': self.base_model.id,
            '__class__': 'BaseModel',
            'created_at': dt_created.isoformat(),
            'updated_at': dt_updated.isoformat()
        }
        self.assertDictEqual(obj_dict, expected_out)


if __name__ == '__main__':
    unittest.main()
