import unittest

from mock import Mock

from src import rocket

__author__ = 'brouk'


class TestRocket(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        # os.chdir('..')                     # If run just this file from IDE
        pass

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_default_rocket(self):
        my_rocket = rocket.Rocket(pos=(60, 20))
        # self.assertIsNone(self.param.action, msg='action is "None" by default')
        # self.assertTrue(True, msg='(test 01) Verifying that assert works.')
        self.assertIsNotNone(my_rocket, msg='Rocket obj is None!')
        self.assertFalse(my_rocket.new_collision_detected,
                         msg='There is new collision when new Rocket is created !')
        self.assertFalse(my_rocket.collision_in_progress,
                         msg='There is collision in progress when Rocket is created!')
        self.assertFalse(my_rocket.collision_complete,
                         msg='There is collision completed when Rocket is created!')

    def test_activate_explosion_when_none_in_progress(self):
        my_rocket = rocket.Rocket(pos=(60, 20))
        my_rocket.collision_in_progress = False
        my_rocket.new_collision_detected = True
        my_rocket.collision_complete = False
        my_rocket._Rocket__explode = Mock(name='explode')
        my_rocket.activate_explosion()
        my_rocket._Rocket__explode.assert_called()
        self.assertFalse(my_rocket.new_collision_detected, msg='New collision state wasn\'t cleared!')
        self.assertTrue(my_rocket.collision_in_progress, msg='Collision process didn\'t start!')
        self.assertFalse(my_rocket.collision_complete, msg='Collision finished already!')

    def test_activate_explosion_when_one_in_progress(self):
        my_rocket = rocket.Rocket(pos=(60, 20))
        my_rocket.collision_in_progress = True
        my_rocket.new_collision_detected = True
        my_rocket.collision_complete = False
        my_rocket._Rocket__explode = Mock(name='explode')
        my_rocket.activate_explosion()
        my_rocket._Rocket__explode.assert_not_called()
        self.assertTrue(my_rocket.new_collision_detected, msg='New collision state was cleared!')
        self.assertTrue(my_rocket.collision_in_progress, msg='Collision process didn\'t start!')
        self.assertFalse(my_rocket.collision_complete, msg='Collision finished already!')


if __name__ == '__main__':
    unittest.main()
