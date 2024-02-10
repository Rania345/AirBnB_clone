#!/usr/bin/python3
"""unittests for models/base_model.py"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def id_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def created_at_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def updated_at_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(expected_str, str(self.base_model))

    def save_method(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def to_dict_method(self):
        self.base_model.save()
        base_model_dict = self.base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            base_model_dict['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            base_model_dict['updated_at'],
            self.base_model.updated_at.isoformat()
        )

    def test_kwargs_with_class_key(self):
        data = {
            '__class__': 'Class',
            'id': '345',
            'created_at': '2024-02-10T20:12:55.789123',
            'updated_at': '2024-02-10T20:12:55.789123'
        }
        obj = BaseModel(**data)

        self.assertNotEqual(obj.__class__.__name__, 'Class')
        self.assertEqual(obj.id, '345')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
