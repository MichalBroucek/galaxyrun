__author__ = 'brouk'

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import menu
from src.game import Game


def get_background(picture_path='pictures/background_bigger.jpg'):
    """
        Set and return full screen Image background
        :return:
        """
    bckg_image = Image(source=picture_path)
    bckg_image.allow_stretch = True
    return bckg_image


class AppScreen(FloatLayout):
    """
    Main screen window for whole app
    - includes all menus and main game as well
      - it's based on Layout to make game full screen
    """

    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)
        self.bckg_image = get_background()
        self.add_widget(self.bckg_image)

        self.play_b = None
        self.exit_b = None
        self.levels_b = None
        self.main_menu_b = None
        self.play_again_b = None
        self.menu_background = None
        self.galaxy_run_l = None

        self.game = Game()

        self.__activate_menu(None)

    def __deactivate_all_buttons(self):
        """
        Deactivate all buttons in the game - to prevent reaction on click on different screens
        - New button need to be added manually :-(  ... TODO: try to make it better
        """
        # if hasattr(self, 'play_b'):
        #     self.play_b.disabled = True
        # if hasattr(self, 'exit_b'):
        #     self.exit_b.disabled = True
        # if hasattr(self, 'levels_b'):
        #     self.levels_b.disabled = True
        # if hasattr(self, 'main_menu_b'):
        #     self.main_menu_b.disabled = True
        # if hasattr(self, 'play_again_b'):
        #     self.play_again_b.disabled = True

    def __activate_menu(self, event):
        """
        Initialize menu view and activate menu screen
        :return:
        """
        self.__deactivate_all_buttons()
        # self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b = self.menu.get_main_menu_items_2()

        # Galaxyrun Label
        # self.galaxy_run_l = Label(text='[b]GALAXY RUN[/b]', markup=True)
        # self.galaxy_run_l.font_size = 36
        # self.galaxy_run_l.x = screen_const.SCREEN_LENGTH / 2 - 30
        # self.galaxy_run_l.y = screen_const.SCREEN_HIGH - 150
        # self.galaxy_run_l.color = [0.7, 0.7, 0.7, 0.2]

        # New Game Button
        self.play_b = Button(text='New game', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .6})
        self.play_b.bind(on_press=self.activate_game)  # Add functionality to 'play button'
        self.add_widget(self.play_b)
        # self.play_b.x = screen_const.SCREEN_LENGTH / 2 - 30
        # self.play_b.y = self.galaxy_run_l.y - 75
        # self.play_b.size = (120, 60)

        # Individual Levels Button
        # self.levels_b = Button(text='Levels', font_size=22)
        # self.levels_b.x = screen_const.SCREEN_LENGTH / 2 - 30
        # self.levels_b.y = self.play_b.y - 85
        # self.levels_b.size = (120, 60)

        # Exit Button
        # self.exit_b = Button(text='Exit', font_size=22)
        # self.exit_b.x = screen_const.SCREEN_LENGTH / 2 - 30
        # self.exit_b.y = self.levels_b.y - 85
        # self.exit_b.size = (120, 60)

        # return [self.menu_background, self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b]
        # return [self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b]

        # self.add_widget(self.menu_background)
        # self.add_widget(self.galaxy_run_l)
        # self.play_b.bind(on_press=self.game.run_game)  # Add functionality to 'play button'
        # self.add_widget(self.play_b)
        # self.levels_b.bind(on_press=self.__activate_levels_screen)  # TODO: implement new levels menu!
        # self.add_widget(self.levels_b)
        # self.exit_b.bind(on_press=self.__exit_app)  # Move bind into menu.py
        # self.add_widget(self.exit_b)

    def activate_game(self, event):
        """
        Activate game screeen on touch New Game button
        :return:
        """
        self.game.size = self.size
        self.add_widget(self.game)
        self.game.run_game()
