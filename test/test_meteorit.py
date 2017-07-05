__author__ = 'brouk'

import unittest
import meteorit


class TestMeteorit(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        self.meteorit = meteorit.Meteorit(source='pictures/meteor_smaller.png', pos=(30, 50))

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_update(self):
        # self.assertIsNone(self.param.action, msg='action is "None" by default')
        orig_y = self.meteorit.center_y
        self.meteorit.update()
        self.assertTrue(orig_y > self.meteorit.center_y, msg='Meteorit \'Y\' coordinate didn\'t change')
