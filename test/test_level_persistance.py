__author__ = 'brouk'

import unittest
from mock import Mock
from src import rocket
from src import level_persistance


class TestLevelPersistence(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test - setup default Level = 1"""
        persis = level_persistance.Persistence()
        persis.save_level(1)

    # ending the test
    def tearDown(self):
        """Cleaning up after the test - setup default Level = 1"""
        persis = level_persistance.Persistence()
        persis.save_level(1)

    def test_read_level_default_valid(self):
        persis = level_persistance.Persistence()
        default_level = persis.read_level()
        print "Default level : ", default_level
        self.assertEqual(default_level, 1, msg='Default level isn\'t 1 !')

    def test_read_level_valid(self):
        persis = level_persistance.Persistence()
        persis.save_level(2)
        level_two = persis.read_level()
        self.assertEqual(level_two, 2, msg='Expected read level isn\'t 2 !')

    def test_read_level_no_file(self):
        pass

    def test_read_level_wrong_file(self):
        pass

    def test_write_level_valid(self):
        persis = level_persistance.Persistence()
        persis.save_level(1)

