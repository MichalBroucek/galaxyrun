__author__ = 'brouk'

import unittest
import os
from src import level_persistance
from kivy.storage.jsonstore import JsonStore


class TestLevelPersistence(unittest.TestCase):
    # preparing to test ... run before each test method
    def setUp(self):
        """ Setting up for the test - setup default Level = 1"""
        persis = level_persistance.Persistence()
        persis.write_level(1)

    # ending the test ... run after each test method
    def tearDown(self):
        """Cleaning up after the test - setup default Level = 1"""
        persis = level_persistance.Persistence()
        persis.write_level(1)

    def test_read_level_default_valid(self):
        persis = level_persistance.Persistence()
        default_level = persis.read_level()
        self.assertEqual(default_level, 1, msg='Default level isn\'t 1 !')

    def test_read_level_valid(self):
        persis = level_persistance.Persistence()
        persis.write_level(2)
        level_two = persis.read_level()
        self.assertEqual(level_two, 2, msg='Expected read level isn\'t 2 !')

    def test_read_level_no_file(self):
        persis_file_del = level_persistance.Persistence()
        self.__delete_persistence_file(persis_file_del)
        persis = level_persistance.Persistence()
        self.assertEqual(persis.read_level(), 1, msg='Expected read level isn\'t 1. When persistent file is missing !')

    # Something wrong here ! - when corrupt file cannot instantiate new Json object ?

    # def test_read_level_corrupted_file(self):
    #     persis_file_corr = level_persistance.Persistence()
    #     file_name = persis_file_corr.JSON_FILE_NAME
    #     persis_file_corr = None
    #     self.__corrupt__persistence_file(file_name, "Error")
    #     persis = level_persistance.Persistence()
    #     self.assertEqual(persis.read_level(), 1, msg='Expected read level isn\'t 1. When persistent file is corrupted !')

    def test_write_level_valid(self):
        persis = level_persistance.Persistence()
        persis.write_level(3)

    def __delete_persistence_file(self, persistence_store):
        """
        Helper method to simulate that file was deleted
        :return:
        """
        assert isinstance(persistence_store, level_persistance.Persistence)
        try:
            os.remove(persistence_store.JSON_FILE_NAME)
        except OSError:
            self.assertTrue(False, msg="Persistence '{0}' file wasn't deleted!".format(persistence_store.JSON_FILE_NAME))
        except:
            print "UNKNOWN EXCEPTION WHEN DELETING PERSISTENCE FILE"

    def __corrupt__persistence_file(self, file_name, corrupt_value=""):
        """
        Helper method to simulate that persistence file was corrupted
        :return:
        """
        # write corrupted value into the persistence file
        with open(file_name, "w") as persistence_file:
            persistence_file.write(corrupt_value)
