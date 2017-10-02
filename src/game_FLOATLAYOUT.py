__author__ = 'brouk'

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

import menu
import screen_const
from kivy.core.window import Window
import level_persistance


# Game statuses
MAIN_MENU_STATE = "MAIN_MENU"
RUNNING_STATE = "RUNNING"
GAME_OVER_STATE = "GAME_OVER"

# TODO: needs to add Layout layer - as Layout will change size automatically (to fullscreen ...)
class Game(FloatLayout):
    """
    Default Widget size is 100,100  -> we need to change size here
    """
    def __init__(self):
        super(Game, self).__init__()
        self.menu = menu.Menu()

        #self.__activate_menu(None)

        self.start_game_init = False
        self.game_scene_init = False
        self.game_over_active = False
        self.levels_buttons = []
        persis = level_persistance.Persistence()
        self.level = persis.read_level()

    def __run_update(self):
        """
        Start main game loop updater
        """
        self.running_loop = Clock.schedule_interval(self.update, 1.0 / 60.0)

    def __stop_update(self):
        """
        Stop main game loop updater
        """
        self.running_loop.cancel()

    def update(self, *ignore):

        if self.level is 1:
            self.__update_level_1()

        if self.level is 2:
            self.__update_level_2()

    def __update_level_1(self):
        """
        Update screen and possition of object + detect all collisions for level 1
        :return:
        """
        if self.rocket.collision_complete:  # If collision complete -> stop updating and Game over
            self.__activate_game_over(None)

        if self.rocket.new_collision_detected:  # Activate collision process on new collision
            self.rocket.activate_explosion()
            print '... New collision detected NOW ...'

        if self.rocket.collision_in_progress:  # Doesn't update background and other game processes
            return

        if not self.rocket.collision_in_progress:  # Update of MAIN game screen - background & meteorites
            self.game_background.update()
            self.meteorites.update()

        for meteorite in self.meteorites.meteorites:  # Check for collision and setup rocket collision flag
            if meteorite.collide_meteorit(self.rocket):
                # todo: test for meteorite position
                print 'meteorite possition: {0}'.format(meteorite.pos)

                self.rocket.new_collision_detected = True

                # TODO: Add level 1 screen complete and save active level to 2

    def __update_level_2(self):
        """
        Update screen and possition of object + detect all collisions for level 2
        :return:
        """
        # if self.rocket.collision_complete:              # If collision complete -> stop updating and Game over
        #     self.__activate_game_over(None)
        #
        # if self.rocket.new_collision_detected:          # Activate collision process on new collision
        #     self.rocket.activate_explosion()
        #
        # if self.rocket.collision_in_progress:           # Doesn't update background and other game processes
        #     return

        if not self.rocket.collision_in_progress:  # Update of MAIN game screen - background & meteorites
            self.game_background.update()
            self.meteorites.update()

            # for meteorite in self.meteorites.meteorites:    # Check for collision and setup rocket collision flag
            #     if meteorite.collide_meteorit(self.rocket):
            #         self.rocket.new_collision_detected = True

    def on_touch_move(self, touch):
        """
        On touch in bottom part of the game move with rocket
        :param touch:
        :return:
        """
        if touch.y < self.slider.top:
            self.rocket.center_x = touch.x
            print 'on touch x = {0}'.format(touch.x)
            print 'rocket center x = {0}'.format(self.rocket.center_x)

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
        #self.menu_background, self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b = self.menu.get_main_menu_items()
        self.galaxy_run_l, self.play_b, self.levels_b, self.exit_b = self.menu.get_main_menu_items()

        # self.add_widget(self.menu_background)
        self.add_widget(self.galaxy_run_l)
        self.play_b.bind(on_press=self.run_game)  # Add functionality to 'play button'
        self.add_widget(self.play_b)
        self.levels_b.bind(on_press=self.__activate_levels_screen)  # TODO: implement new levels menu!
        self.add_widget(self.levels_b)
        self.exit_b.bind(on_press=self.__exit_app)  # Move bind into menu.py
        self.add_widget(self.exit_b)

    def run_game(self):
        """
        Initialize game window
        :return:
        """

        print 'Running the GAME Big time ...'

        self.__deactivate_all_buttons()

        if self.level is 1:
            self.game_background, self.rocket, self.slider, self.meteorites = self.menu.get_level_1_run_items(
                self.center_x, self.center_y)
        elif self.level is 2:
            self.game_background, self.rocket, self.slider, self.meteorites = self.menu.get_level_2_run_items(
                self.center_x, self.center_y)
        else:
            print "----> something ---> is ----> wrong !!!!"

        self.add_widget(self.game_background)

        #self.rocket.pos = (self.game_background.size[0] / 2, self.size_hint_y + 60)
        # todo: Potreba vyresit kolize s meteority !!!
        self.rocket.pos_hint = {'x': 0.0, 'y': -0.3}
        self.add_widget(self.rocket)

        self.slider.pos_hint = {'x': 0.0, 'y': -0.4}
        self.add_widget(self.slider)

        # for meteorite in self.meteorites.meteorites:
        #     self.add_widget(meteorite)

        self.__run_update()

    def __activate_game_over(self, event):
        """
        Initialize game over screen
        :return:
        """
        self.__deactivate_all_buttons()
        self.game_over_l, self.play_again_b, self.main_menu_b = self.menu.get_game_over_menu_items()
        self.add_widget(self.game_over_l)
        self.play_again_b.bind(on_press=self.run_game)
        self.add_widget(self.play_again_b)
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)
        self.__stop_update()

    def __activate_levels_screen(self, event):
        """
        Opens Levels screen for individuals levels
        :return:
        """
        self.__deactivate_all_buttons()
        self.levels_background, self.levels_label, self.main_menu_b, self.levels_buttons = self.menu.get_levels_items(
            self.level)
        self.add_widget(self.levels_background)
        self.add_widget(self.levels_label)
        self.levels_buttons[0].bind(on_press=self.run_game)
        self.add_widget(self.levels_buttons[0])
        self.add_widget(self.levels_buttons[1])
        self.add_widget(self.levels_buttons[2])
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def __activate_new_level(self, event):
        """
        Activate new level screeen
        :param event:
        :return:
        """
        print "New Level was activated ..."

    def __exit_app(self, event):
        """
        Close and exit App
        :param event:
        :return:
        """
        # new_level = 1
        # print 'Saving LEVEL: ', new_level
        # level_persistance.save_level(new_level)

        print "Bye bye ..."
        App.get_running_app().stop()
