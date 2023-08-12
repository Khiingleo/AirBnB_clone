#!/usr/bin/python3
"""unittests for the models/state.py """

import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ test cases"""

    @classmethod
    def setUp(cls):
        cls.state = State()

    @classmethod
    def tearDown(cls):
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        stri = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), stri)

    def test_type(self):
        self.assertEqual(str, type(self.state.name))

    def test_str_representation(self):
        stri = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), stri)

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        created = self.state.created_at.isoformat()
        updated = self.state.updated_at.isoformat()
        self.assertEqual(state_dict['created_at'], created)
        self.assertEqual(state_dict['updated_at'], updated)
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_save(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

if __name__ == "__main__":
    unittest.main()
