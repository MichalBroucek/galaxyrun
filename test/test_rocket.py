import unittest
#import unittest.mock
import os

# import sys
# sys.path.append('..')           # make parent directory visible for import
# from rocket import Rocket

import rocket

__author__ = 'brouk'


class TestRocket(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        #os.chdir('..')                     # If run just this file from IDE
        self.rocket = rocket.Rocket(pos=(60, 20))

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_default_rocket(self):
        #self.assertIsNone(self.param.action, msg='action is "None" by default')
        self.assertIsNotNone(self.rocket, msg='Rocket obj is None!')
        self.assertTrue(True, msg='(test 01) Verifying that assert works.')
        pass

if __name__ == '__main__':
    unittest.main()
