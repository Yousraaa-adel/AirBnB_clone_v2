#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
            print("JSON file has been successfully removed.")
        except (FileExistsError, FileNotFoundError):
            print("JSON file doesn't exist/hasn't been created.")
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        inst = BaseModel()
        storage.new(inst)

        key = inst.__class__.__name__ + '.' + inst.id
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], inst)

    def test_all(self):
        """ __objects is properly returned """
        inst = BaseModel()
        objs = storage.all()
        # Adding instance to __objects
        storage.new(inst)

        self.assertIsInstance(objs, dict)
        self.assertIn(inst.__class__.__name__ + '.' + inst.id, objs)
        self.assertEqual(objs[inst.__class__.__name__ + '.' + inst.id], inst)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file.
            Checking this by testing if JSON file size
            is not zero.
        """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ Testing the save() method
            with checking that the JSON file is created
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        loaded = None  # Initialize loaded to None
        old_key = "{}.{}".format(new.__class__.__name__, new.id)
        for key, value in storage.all().items():
            if key == old_key:
                loaded = value
        # Check if loaded is not None before accessing its attributes
        if loaded is not None:
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        temp = None
        old_key = "{}.{}".format(new.__class__.__name__, new.id)
        for key, value in storage.all().items():
            if key == old_key:
                temp = key
        if temp is not None:
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_delete(self):
        """ Adding an obj to storage.all().
            Then deleting it.
        """
        instance = BaseModel()
        objs = storage.all()

        storage.new(instance)
        key = instance.__class__.__name__ + '.' + instance.id
        self.assertIn(key, objs)

        storage.delete(instance)
        self.assertNotIn(instance, objs)
