import unittest
from mock import Mock
import os


import rocket

__author__ = 'brouk'


class TestRocket(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        # os.chdir('..')                     # If run just this file from IDE
        self.rocket = rocket.Rocket(pos=(60, 20))

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_default_rocket(self):
        # self.assertIsNone(self.param.action, msg='action is "None" by default')
        # self.assertTrue(True, msg='(test 01) Verifying that assert works.')
        self.assertIsNotNone(self.rocket, msg='Rocket obj is None!')
        self.assertFalse(self.rocket.new_collision_detected,
                         msg='There is new collision when new Rocket is created !')
        self.assertFalse(self.rocket.collision_in_progress,
                         msg='There is collision in progress when Rocket is created!')
        self.assertFalse(self.rocket.collision_complete,
                         msg='There is collision completed when Rocket is created!')

    def test_activate_explosion_when_none_in_progress(self):
        self.rocket.collision_in_progress = False
        self.rocket.new_collision_detected = True
        self.rocket.collision_complete = False
        self.rocket._Rocket__explode = Mock(name='explode')
        self.rocket.activate_explosion()
        self.rocket._Rocket__explode.assert_called()
        self.assertFalse(self.rocket.new_collision_detected, msg='New collision state wasn\'t cleared!')
        self.assertTrue(self.rocket.collision_in_progress, msg='Collision process didn\'t start!')
        self.assertFalse(self.rocket.collision_complete, msg='Collision finished already!')

    def test_activate_explosion_when_one_in_progress(self):
        self.rocket.collision_in_progress = True
        self.rocket.new_collision_detected = True
        self.rocket.collision_complete = False
        self.rocket._Rocket__explode = Mock(name='explode')
        self.rocket.activate_explosion()
        self.rocket._Rocket__explode.assert_not_called()
        self.assertTrue(self.rocket.new_collision_detected, msg='New collision state was cleared!')
        self.assertTrue(self.rocket.collision_in_progress, msg='Collision process didn\'t start!')
        self.assertFalse(self.rocket.collision_complete, msg='Collision finished already!')


if __name__ == '__main__':
    unittest.main()
