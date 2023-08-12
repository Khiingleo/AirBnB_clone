#!/usr/bin/python3
""" unittest for models/amenity"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ amenity unittest test cases"""

    @classmethod
    def setUp(cls):
        cls.amenity = Amenity()

    @classmethod
    def tearDown(cls):
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_isSubclass(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_unique_id(self):
        amenity1 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity1.id)

    def test_str_representation(self):
        stri = "[Amenity] ({}) {}".format(self.amenity.id,
                                          self.amenity.__dict__)
        self.assertEqual(str(self.amenity), stri)

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        created = self.amenity.created_at.isoformat()
        updated = self.amenity.updated_at.isoformat()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'], created)
        self.assertEqual(amenity_dict['updated_at'], updated)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == "__main__":
    unittest.main()
