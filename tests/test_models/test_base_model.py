#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid
from uuid import uuid4
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
            print("JSON file has been successfully removed.")
        except (FileExistsError, FileNotFoundError):
            print("JSON file doesn't exist/hasn't been created.")
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs_type(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_with_to_dict(self):
        """ Turning the instance into a dict then
            checking if these kwargs are there.
        """
        # current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        n = {'name': 'test'}
        new = self.value(**n)

        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, 'created_at'))
        self.assertTrue(hasattr(new, 'updated_at'))
        self.assertTrue(hasattr(new, 'name'))

    def test_kwargs_without_to_dict(self):
        """ Passing n as kwargs directly without turning
            into dict.
            new in ths case is not iterable so we
            used hasattr().
        """
        current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        n = {'name': 'test',
             'created_at': current_time,
             'updated_at': current_time}
        new = self.value(**n)

        # Check if the attributes are present directly on the 'new' object
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, 'created_at'))
        self.assertTrue(hasattr(new, 'updated_at'))
        self.assertTrue(hasattr(new, 'name'))

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    # def test_kwargs_with_no_created_at(self):
    #     """ """
    #     n = {'name': 'test'}
    #     with self.assertRaises(KeyError):
    #         new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_to_dict(self):
        """ """
        instance = BaseModel(name="Yassin", _sa_instance_state="hello")
        instance.to_dict()

        self.assertNotIn('_sa_instance_state', instance.__dict__)
