__author__ = 'brouk'

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.app import App

import menu
import screen_const


# Game statuses
MAIN_MENU_STATE = "MAIN_MENU"
RUNNING_STATE = "RUNNING"
GAME_OVER_STATE = "GAME_OVER"


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.menu = menu.Menu()
        self.__activate_menu(None)
        self.start_game_init = False
        self.game_scene_init = False
        self.game_over_active = False

    def __run_update(self):
        """
        Start main game loop updater
        """
        self.running_loop = Clock.schedule_interval(self.update, 1.0/60.0)

    def __stop_update(self):
        """
        Stop main game loop updater
        """
        self.running_loop.cancel()

    def update(self, *ignore):

        if self.rocket.collision_complete:              # If collision complete -> stop updating and Game over
            self.__activate_game_over(None)

        if self.rocket.new_collision_detected:          # Activate collision process on new collision
            self.rocket.activate_explosion()

        if self.rocket.collision_in_progress:           # Doesn't update background and other game processes
            return

        if not self.rocket.collision_in_progress:       # Update of MAIN game screen - background & meteorites
            self.game_background.update()
            self.meteorites.update()

        for meteorite in self.meteorites.meteorites:    # Check for collision and setup rocket collision flag
            if meteorite.collide_meteorit(self.rocket):
                self.rocket.new_collision_detected = True

    def on_touch_move(self, touch):
        """
        On touch in bottom part of the game move with rocket
        :param touch:
        :return:
        """
        if touch.y < self.slider.top:
            self.rocket.center_x = touch.x

    def __deactivate_all_buttons(self):
        """
        Deactivate all buttons in the game - to prevent reaction on click on different screens
        - New button need to be added manually :-(  ... TODO: try to make it better
        """
        if hasattr(self, 'play_b'):
            self.play_b.disabled = True
        if hasattr(self, 'exit_b'):
            self.exit_b.disabled = True
        if hasattr(self, 'levels_b'):
            self.levels_b.disabled = True
        if hasattr(self, 'main_menu_b'):
            self.main_menu_b.disabled = True
        if hasattr(self, 'play_again_b'):
            self.play_again_b.disabled = True

    def __activate_menu(self, event):
        """
        Initialize menu view and activate menu screen
        :return:
        """
        self.__deactivate_all_buttons()
        self.menu_background, self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b = self.menu.get_main_menu_items()
        self.size = screen_const.SCREEN_SIZE        # Setup size of the main screen
        self.add_widget(self.menu_background)
        self.add_widget(self.galaxy_run_l)
        self.play_b.bind(on_press=self.__run_game)     # Add functionality to 'play button'
        self.add_widget(self.play_b)
        #self.levels_b.bind(on_press=self.__activate_game)  # TODO: implement new levels menu!
        self.add_widget(self.levels_b)
        self.exit_b.bind(on_press=self.__exit_app)          # Move bind into menu.py
        self.add_widget(self.exit_b)

    def __run_game(self, event):
        """
        Initialize game window
        :return:
        """
        self.__deactivate_all_buttons()
        self.game_background, self.rocket, self.slider, self.meteorites = self.menu.get_run_game_items(self.center_x, self.center_y)
        self.rocket.pos = (self.game_background.size[0] / 2, self.size_hint_y + 60)
        self.add_widget(self.game_background)
        self.add_widget(self.rocket)
        self.add_widget(self.slider)
        for meteorite in self.meteorites.meteorites:
            self.add_widget(meteorite)
        self.__run_update()

    def __activate_game_over(self, event):
        """
        Initialize game over screen
        :return:
        """
        self.__deactivate_all_buttons()
        self.game_over_l, self.play_again_b, self.main_menu_b = self.menu.get_game_over_menu_items()
        self.add_widget(self.game_over_l)
        self.play_again_b.bind(on_press=self.__run_game)
        self.add_widget(self.play_again_b)
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)
        self.__stop_update()

    def __exit_app(self, event):
        """
        Close and exit App
        :param event:
        :return:
        """
        print "Bye bye ..."
        App.get_running_app().stop()
