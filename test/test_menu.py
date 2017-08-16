__author__ = 'brouk'

import unittest

from kivy.uix.button import Button
from src.background import Background
from kivy.uix.label import Label
from sprite import Sprite

from src import menu
from src import rocket
from src import meteorites


def button_press_action():
    """
    Test Button for testing ...
    :return:
    """
    print "Button pressed ..."


class TestMenu(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_main_menu_new_game_buttons(self):
        """
        Test Main menu - New Game Button
        """
        main_menu = menu.Menu()
        menu_background, galaxy_run_l, play_b, levels_b, exit_b = main_menu.get_main_menu_items()
        self.assertTrue(isinstance(menu_background, Background), msg='\'Background\' isn\'t instance of Background !')
        self.assertTrue(isinstance(galaxy_run_l, Label), msg='\'Game Label\' isn\'t instance of Label !')
        self.assertTrue(isinstance(play_b, Button), msg='\'New Game Button\' isn\'t instance of Button !')
        self.assertTrue(isinstance(levels_b, Button), msg='\'Levels Button\' isn\'t instance of Button !')
        self.assertTrue(isinstance(exit_b, Button), msg='\'Exit Button\' isn\'t instance of Button !')

    def test_run_game_menu_buttons(self):
        """
        Test Run Game menu items
        """
        main_menu = menu.Menu()
        game_background, my_rocket, my_slider, my_meteorites = main_menu.get_run_game_items(100, 30)
        self.assertTrue(isinstance(game_background, Background), msg='\'Game Background\' isn\'t instance of Background !')
        self.assertTrue(isinstance(my_rocket, rocket.Rocket), msg='\'Game Rocket\' doesn\'t exist in game run window !')
        self.assertTrue(isinstance(my_slider, Sprite), msg='\'Slider\' doesn\'t exist in game run window !')
        self.assertTrue(isinstance(my_meteorites, meteorites.Meteorites), msg='\'Meteorites\' don\'t exist in game run window !')

    def test_game_over_menu_buttons(self):
        """
        Test Game over menu items
        """
        main_menu = menu.Menu()
        game_over_l, play_again_b, main_menu_b = main_menu.get_game_over_menu_items()
        self.assertTrue(isinstance(game_over_l, Label), msg='\'Game Over Label\' doesn\'t exist in Game over window !')
        self.assertTrue(isinstance(play_again_b, Button), msg='\'Play Again Button\' doesn\'t exist in Game over window !')
        self.assertTrue(isinstance(main_menu_b, Button), msg='\'Main menu Button\' doesn\'t exist in Game over window !')

    def test_levels_menu_buttons(self):
        """
        Test levels menu items
        :return:
        """
        main_menu = menu.Menu()
        levels_background, levels_label, main_menu_b, levels_buttons = main_menu.get_levels_items(1)
        self.assertTrue(isinstance(levels_background, Background), msg='\'Background\' doesn\'t exist in Levels window !')
        self.assertTrue(isinstance(levels_label, Label), msg='\'Label\' doesn\'t exist in Levels window !')
        self.assertTrue(isinstance(main_menu_b, Button), msg='\'Main menu Button\' doesn\'t exist Levels window !')
        self.assertTrue(isinstance(levels_buttons[0], Button), msg='\'1st Level Button\' doesn\'t exist in Levels window !')
        self.assertTrue(isinstance(levels_buttons[1], Button), msg='\'2nd Level Button\' doesn\'t exist in Levels window !')
        self.assertTrue(isinstance(levels_buttons[2], Button), msg='\'3rd Level Button\' doesn\'t exist in Levels window !')
