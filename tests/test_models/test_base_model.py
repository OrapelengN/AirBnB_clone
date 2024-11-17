#!/usr/bin/python3
"""Unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up resources before each test."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if an instance of BaseModel is correctly created."""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_string(self):
        """Test if id is a string."""
        self.assertIsInstance(self.model.id, str)

    def test_unique_id(self):
        """Test if ids are unique."""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_type(self):
        """Test the type of created_at attribute."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_save_method(self):
        """Test if save() method updates 'updated_at'."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
