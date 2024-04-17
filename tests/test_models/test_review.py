#!/usr/bin/python3
"""
Unit tests for Review model.
"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Test class for Review model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test case to check data type of 'place_id' attribute in Review model.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test case to check data type of 'user_id' attribute in Review model.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test case to check data type of 'text' attribute in Review model.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
