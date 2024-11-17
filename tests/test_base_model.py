#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel."""
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(
            model_dict['created_at'],
            model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'],
            model.updated_at.isoformat())

    def test_kwargs(self):
        """Test initialization with kwargs."""
        model = BaseModel()
        model.name = "My Model"
        model.number = 42
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertEqual(new_model.name, "My Model")
        self.assertEqual(new_model.number, 42)


if __name__ == '__main__':
    unittest.main()
