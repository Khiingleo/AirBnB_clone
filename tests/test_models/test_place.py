#!/usr/bin/python3
""" unittest for the models/place.py"""

import unittest
import os
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """test cases for the Place class"""

    @classmethod
    def setUp(cls):
        cls.place = Place()

    @classmethod
    def tearDown(cls):
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test_is_subclass(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])

    def test_type(self):
        self.assertEqual(str, type(self.place.city_id))
        self.assertEqual(str, type(self.place.user_id))
        self.assertEqual(str, type(self.place.name))
        self.assertEqual(str, type(self.place.description))
        self.assertEqual(int, type(self.place.number_rooms))
        self.assertEqual(int, type(self.place.number_bathrooms))
        self.assertEqual(int, type(self.place.max_guest))
        self.assertEqual(int, type(self.place.price_by_night))
        self.assertEqual(float, type(self.place.latitude))
        self.assertEqual(float, type(self.place.longitude))
        self.assertEqual(list, type(self.place.amenity_ids))

    def test_str_representation(self):
        stri = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), stri)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_save(self):
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

if __name__ == "__main__":
    unittest.main()
