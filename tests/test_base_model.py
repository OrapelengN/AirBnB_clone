#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def test_init_from_dict(self):
        """ Test initialization from a dictionary. """
        model = BaseModel()
        model.name = "TestModel"
        model.number = 42
        model_dict = model.to_dict()

        # Create a new instance using the dictionary
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.number, model.number)
        self.assertNotEqual(new_model, model)

    def test_to_dict_output(self):
        """Test the output of to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_save(self):
        """Test the save method updates 'updated_at'."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
