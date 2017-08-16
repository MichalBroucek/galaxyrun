__author__ = 'brouk'

# Modul to create all menus for Game

from kivy.uix.label import Label
from kivy.uix.button import Button

from src.background import Background
from src import screen_const
from rocket import Rocket
from sprite import Sprite
from meteorites import Meteorites


class Menu:
    """
    Menu class for creating individual menus for game
    Individual methods returns list of buttons for individual menus
    """

    def __init__(self):
        self.play_b = None
        self.exit_b = None
        self.levels_b = None
        self.main_menu_b = None
        self.play_again_b = None
        self.menu_background = None
        self.galaxy_run_l = None

    def __deactivate_all_buttons(self):
        """
        Deactivate all buttons in the game - to prevent reaction on click on different screens
        - New button need to be added manually :-(  ... TODO: try to make it better
        """
        if self.play_b:
            self.play_b.disabled = True
        if self.exit_b:
            self.exit_b.disabled = True
        if self.levels_b:
            self.levels_b.disabled = True
        if self.main_menu_b:
            self.main_menu_b.disabled = True
        if self.play_again_b:
            self.play_again_b.disabled = True

    def get_main_menu_items(self):
        """
        Return Main menu items for main menu screen: New game, Levels, Exit and Background Widgets
        :return:
        """
        self.__deactivate_all_buttons()

        # Menu Background
        self.menu_background = Background(source='pictures/menu_background.png')

        # Galaxyrun Label
        self.galaxy_run_l = Label(text='[b]GALAXY RUN[/b]', markup=True)
        self.galaxy_run_l.font_size = 36
        self.galaxy_run_l.x = screen_const.SCREEN_LENGTH / 2 - 30
        self.galaxy_run_l.y = screen_const.SCREEN_HIGH - 150
        self.galaxy_run_l.color = [0.7, 0.7, 0.7, 0.2]

        # New Game Button
        self.play_b = Button(text='New game', font_size=22)
        self.play_b.x = screen_const.SCREEN_LENGTH / 2 - 30
        self.play_b.y = self.galaxy_run_l.y - 75
        self.play_b.size = (120, 60)

        # Individual Levels Button
        self.levels_b = Button(text='Levels', font_size=22)
        self.levels_b.x = screen_const.SCREEN_LENGTH / 2 - 30
        self.levels_b.y = self.play_b.y - 85
        self.levels_b.size = (120, 60)

        # Exit Button
        self.exit_b = Button(text='Exit', font_size=22)
        self.exit_b.x = screen_const.SCREEN_LENGTH / 2 - 30
        self.exit_b.y = self.levels_b.y - 85
        self.exit_b.size = (120, 60)

        return [self.menu_background, self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b]

    def get_run_game_items(self, center_x, center_y):
        """
        Return items for run engine
        :return:
        """

        game_background = Background(source='pictures/background_02_800_450.png')
        my_rocket = Rocket(pos=(screen_const.SCREEN_LENGTH / 2, 10))
        my_slider = Sprite(source='pictures/slider.png')
        my_meteorites = Meteorites(center_x, center_y)

        return [game_background, my_rocket, my_slider, my_meteorites]

    def get_game_over_menu_items(self):
        """
        Return Game over menu items
        :return:
        """
        game_over_l = Label(text='[b]GAME OVER[/b]', markup=True)
        game_over_l.font_size = 36
        game_over_l.x = screen_const.SCREEN_LENGTH / 2 - 30
        game_over_l.y = screen_const.SCREEN_HIGH / 2 - 10
        game_over_l.color = [0.7, 0.7, 0.7, 0.2]

        # Play again button
        play_again_b = Button(text='Play again', font_size=22)  # TODO: remove rocket, slider and meteorites
        play_again_b.x = game_over_l.x - 120
        play_again_b.y = game_over_l.y - 80
        play_again_b.size = (120, 60)

        # Main menu button
        main_menu_b = Button(text='Main menu', font_size=22)    # TODO: remove rocket, slider and meteorites
        main_menu_b.x = play_again_b.right + 100
        main_menu_b.y = play_again_b.y
        main_menu_b.size = (120, 60)

        return [game_over_l, play_again_b, main_menu_b]

    def get_levels_items(self, level):
        """
        Return items for Level menu (active and not active menus)
        :return:
        """
        # Menu Background
        menu_background = Background(source='pictures/menu_background.png')

        # Levels label
        levels_l = Label(text='[b]LEVELS[/b]', markup=True)
        levels_l.font_size = 36
        levels_l.x = screen_const.SCREEN_LENGTH / 2 - 30
        levels_l.y = screen_const.SCREEN_HIGH - 150
        levels_l.color = [0.7, 0.7, 0.7, 0.2]

        # Level Buttons (levels 1, 2, 3 - active or not active)
        # todo: Icons for individual levels ... 1, 2, 3
        level_1_b = Button(text='1st Level', font_size=22)    # TODO: remove rocket, slider and meteorites
        level_1_b.x = levels_l.x - 170
        level_1_b.y = levels_l.y - 80
        level_1_b.size = (120, 60)

        level_2_b = Button(text='2st Level', font_size=22)    # TODO: remove rocket, slider and meteorites
        level_2_b.x = level_1_b.right + 50
        level_2_b.y = levels_l.y - 80
        level_2_b.size = (120, 60)
        if level < 2:
            level_2_b.disabled = True

        level_3_b = Button(text='3rd Level', font_size=22)    # TODO: remove rocket, slider and meteorites
        level_3_b.x = level_2_b.right + 50
        level_3_b.y = levels_l.y - 80
        level_3_b.size = (120, 60)
        if level < 3:
            level_3_b.disabled = True

        # Main menu button
        main_menu_b = Button(text='Main menu', font_size=22)    # TODO: remove rocket, slider and meteorites
        main_menu_b.x = levels_l.x - 20
        main_menu_b.y = levels_l.y - 250
        main_menu_b.size = (120, 60)

        return [menu_background, levels_l, main_menu_b, [level_1_b, level_2_b, level_3_b]]
