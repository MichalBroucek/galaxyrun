__author__ = 'brouk'

import unittest

from src import meteorit
from src import rocket


class TestMeteorit(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        self.meteorit = meteorit.Meteorit(source='pictures/meteor_smaller.png', pos=(100, 100))

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_update_y(self):
        """
        Test update functionality of meteorit object
        """
        orig_y = self.meteorit.center_y
        self.meteorit.update()
        self.assertTrue(orig_y > self.meteorit.center_y, msg='Meteorit \'Y\' coordinate didn\'t change !')
        self.assertEqual(orig_y - 7, self.meteorit.center_y, msg='Update didn\'t move center_y about -7 !')

    def test_colide_meteorit_bottom(self):
        """
        Test collision with bottom part of meteorite
        """
        rocket_x_collision_threshold = self.meteorit.x - rocket.ROCKET_WIDTH + meteorit.COLLISION_BOTTOM_LEFT_OFFSET
        rocket_y_collision_threshold = self.meteorit.y - rocket.ROCKET_HEIGHT + meteorit.COLLISION_BOTTOM_BOTTOM_OFFSET

        test_rocket = rocket.Rocket(pos=(rocket_x_collision_threshold + 1, rocket_y_collision_threshold + 1))
        self.assertTrue(self.meteorit.collide_meteorit(test_rocket), msg='Collision with bottom meteorit wasn\'t detected !')

    def test_colide_meteorit_midle(self):
        """
        Test collision with middle part of meteorite
        """
        rocket_x_collision_threshold = self.meteorit.x - rocket.ROCKET_WIDTH + meteorit.COLLISION_MIDDLE_LEFT_OFFSET
        rocket_y_collision_threshold = self.meteorit.y - rocket.ROCKET_HEIGHT + meteorit.COLLISION_MIDDLE_BOTTOM_OFFSET

        test_rocket = rocket.Rocket(pos=(rocket_x_collision_threshold + 1, rocket_y_collision_threshold + 1))
        self.assertTrue(self.meteorit.collide_meteorit(test_rocket), msg='Collision with midle meteorit wasn\'t detected !')

    def test_colide_meteorit_top(self):
        """
        Test collision with top part of meteorite
        """
        rocket_x_collision_threshold = self.meteorit.x - rocket.ROCKET_WIDTH + meteorit.COLLISION_TOP_LEFT_OFFSET
        rocket_y_collision_threshold = self.meteorit.y - rocket.ROCKET_HEIGHT + meteorit.COLLISION_TOP_BOTTOM_OFFSET

        test_rocket = rocket.Rocket(pos=(rocket_x_collision_threshold + 1, rocket_y_collision_threshold + 1))
        self.assertTrue(self.meteorit.collide_meteorit(test_rocket), msg='Collision with top meteorit wasn\'t detected !')
