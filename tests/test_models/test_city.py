#!/usr/bin/python3
"""
Unit tests for City model.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Test class for City model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test case to check data type of \
                the 'state_id' attribute in City model.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test case to check the data type of \
                the 'name' attribute in City model.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
