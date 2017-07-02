__author__ = 'brouk'

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.app import App

from background import Background
from rocket import Rocket
from meteorites import Meteorites
from sprite import Sprite

# Game statuses
MAIN_MENU_STATE = "MAIN_MENU"
RUNNING_STATE = "RUNNING"
GAME_OVER_STATE = "GAME_OVER"


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
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
        # Main ACTION LOOP ... TODO: Make it simple !!!

        if self.rocket.collision_complete:              # If collision complete -> stop updating and Game over
            self.__activate_game_over(None)

        if self.rocket.new_collision_detected:          # Activate collision process on new collision
            self.rocket.activate_explossion()

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

    def __activate_menu(self, event):
        """
        Initialize menu view and activate menu screen
        :return:
        """
        self.menu_background = Background(source='pictures/menu_background.png')
        self.size = self.menu_background.size
        self.add_widget(self.menu_background)

        x_coordinates = self.right / 2 - 30
        y_coordinates = self.top - 150
        self.galaxy_run_l = Label(text='[b]GALAXY RUN[/b]', markup=True)
        self.galaxy_run_l.font_size = 36
        self.galaxy_run_l.x = x_coordinates
        self.galaxy_run_l.y = y_coordinates
        self.galaxy_run_l.color = [0.7, 0.7, 0.7, 0.2]
        self.add_widget(self.galaxy_run_l)

        # Two buttons - menu x play again
        self.play_b = Button(text='Play', font_size=22)
        self.play_b.x = self.right / 2 - 30
        self.play_b.y = self.galaxy_run_l.y - 80
        self.play_b.size = (120, 60)
        self.play_b.bind(on_press=self.__activate_game)
        self.add_widget(self.play_b)
        self.exit_b = Button(text='Exit', font_size=22)
        self.exit_b.x = self.right / 2 - 30
        self.exit_b.y = self.play_b.y - 100
        self.exit_b.size = (120, 60)
        self.exit_b.bind(on_press=self.__exit_app)
        self.add_widget(self.exit_b)

    def __activate_game(self, event):
        """
        Initialize game window
        :return:
        """
        self.game_background = Background(source='pictures/background_02_800_450.png')
        self.rocket = Rocket(pos=(self.width / 2, 10))
        self.rocket.pos = (self.game_background.size[0] / 2, self.size_hint_y + 60)
        self.slider = Sprite(source='pictures/slider.png')
        self.meteorites = Meteorites(self.center_x, self.center_y)

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
        print "-----------------"
        print "--- GAME OVER ---"
        print "-----------------"
        self.game_over_l = Label(text='[b]GAME OVER[/b]', markup=True)
        self.game_over_l.font_size = 36
        self.game_over_l.x = self.right / 2 - 30
        self.game_over_l.y = self.top / 2 - 10
        self.game_over_l.color = [0.7, 0.7, 0.7, 0.2]
        self.add_widget(self.game_over_l)
        # Two buttons - menu x play again
        self.play_again_b = Button(text='Play again', font_size=22)  # TODO: remove rocket, slider and meteorites
        self.play_again_b.x = self.game_over_l.x - 120
        self.play_again_b.y = self.game_over_l.y - 80
        self.play_again_b.size = (120, 60)
        self.play_again_b.bind(on_press=self.__activate_game)
        self.add_widget(self.play_again_b)
        self.main_menu_b = Button(text='Main menu', font_size=22)    # TODO: remove rocket, slider and meteorites
        self.main_menu_b.x = self.play_again_b.right + 100
        self.main_menu_b.y = self.play_again_b.y
        self.main_menu_b.size = (120, 60)
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
