#!/usr/bin/python3
"""Test cases for the city"""

from models.city import City
import os
import unittest
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """test cases for the city class"""

    @classmethod
    def setUp(cls):
        cls.city = City()

    @classmethod
    def tearDown(cls):
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_types(self):
        self.assertEqual(str, type(self.city.name))
        self.assertEqual(str, type(self.city.state_id))

    def test_check_fr_func(self):
        self.assertIsNotNone(City.__doc__)

    def test_str_representation(self):
        stri = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), stri)

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        created = self.city.created_at.isoformat()
        updated = self.city.updated_at.isoformat()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'], created)
        self.assertEqual(city_dict['updated_at'], updated)
        self.assertEqual('to_dict' in dir(self.city), True)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

if __name__ == "__main__":
    unittest.main()
