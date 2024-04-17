#!/usr/bin/python3
"""
Unit tests for the BaseModel.
"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Test class for the BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up any resources for the test cases."""
        pass

    def tearDown(self):
        """Clean up resources created during test cases."""
        try:
            os.remove('file.json')
        except OSError:
            pass

    def test_default(self):
        """Test check if an instance of \
                BaseModel created properly."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Test check if an instance of BaseModel\
                can be created with keyword arguments.
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Test check if TypeError is raised when\
                creating BaseModel instance with integer keys.
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test check if the 'save' method saves \
                the BaseModel instance properly."""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test check if the 'str' method returns\
                the expected string representation."""
        i = self.value()
        self.assertEqual(str(i), f"[{{self.name}}] ({i.id}) {{i.__dict__}}")

    def test_todict(self):
        """Test check if 'to_dict' method \
                returns a dictionary representation BaseModel instance."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test check if TypeError is raised\
                when creating BaseModel instance with None keys."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test check if KeyError is raised\
                when creating BaseModel instance with invalid keys."""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test check the data type of the 'id' attribute."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test check the data\
                type of the 'created_at' attribute."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test check the data type of the\
                'updated_at' attribute and their initial values."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
