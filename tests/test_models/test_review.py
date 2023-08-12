#!/usr/bin/python3
""" unittest for models/review.py"""

import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test cases"""

    @classmethod
    def setUp(cls):
        cls.review = Review()

    @classmethod
    def tearDown(cls):
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertIsInstance(self.review, BaseModel)
    
    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, "")

    def test_type(self):
        self.assertEqual(str, type(self.review.place_id))
        self.assertEqual(str, type(self.review.user_id))
        self.assertEqual(str, type(self.review.text))

    def test_str_representation(self):
        stri = "[Review] ({}) {}".format(self.review.id,
                                         self.review.__dict__)
        self.assertEqual(str(self.review), stri)

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        created = self.review.created_at.isoformat()
        updated = self.review.updated_at.isoformat()
        self.assertEqual(review_dict['created_at'], created)
        self.assertEqual(review_dict['updated_at'], updated)
        self.assertEqual('to_dict' in dir(self.review), True)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

if __name__ == "__main__":
    unittest.main()
