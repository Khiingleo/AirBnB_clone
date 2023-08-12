#!/usr/bin/python3
"""unittest for models/user.py"""

import os
import models
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """test cases for the user class"""

    @classmethod
    def setUp(cls):
        cls.user = User()

    @classmethod
    def tearDown(cls):
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_type(self):
        self.assertEqual(str, type(self.user.email))
        self.assertEqual(str, type(self.user.password))
        self.assertEqual(str, type(self.user.first_name))
        self.assertEqual(str, type(self.user.last_name))

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        stri = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), stri)

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        created = self.user.created_at.isoformat()
        updated = self.user.updated_at.isoformat()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'], created)
        self.assertEqual(user_dict['updated_at'], updated)
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

if __name__ == "__main__":
    unittest.main()
