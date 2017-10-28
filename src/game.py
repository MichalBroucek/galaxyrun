__author__ = 'brouk'

from kivy.uix.widget import Widget
from kivy.clock import Clock

from src.background import Background
from rocket import Rocket
from sprite import Sprite
from meteorites import Meteorites
import meteorit

from kivy.core.window import Window


class Game(Widget):
    def __init__(self, screen_ref):
        super(Game, self).__init__()
        self.game_screen = screen_ref
        self.level = screen_ref.level
        # Make it separate for individual levels 1, 2, 3
        self.game_background = self.__get_background_for_game()
        self.rocket = Rocket(picture='pictures/rocket_01_40x69.png')
        self.slider = Sprite(source='pictures/swiper.png')
        self.obstacles = self.__get_obstacles_for_game()
        self.last_screen = False

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
        if self.level == 1:
            self.__update_first_level()

    def on_touch_move(self, touch):
        """
        On touch in bottom part of the game move with rocket
        :param touch:
        :return:
        """
        if touch.y < self.slider.top:
            self.rocket.center_x = touch.x

    def run_game(self):
        """
        Initialize game window
        :return:
        """
        self.clear_widgets()

        self.add_widget(self.game_background)

        self.slider.pos = (0, 0)
        self.slider.size = (Window.size[0], Window.size[1] * 0.1)
        self.add_widget(self.slider)

        self.rocket.size = (Window.size[0] * 0.1, Window.size[1] * 0.1)
        self.rocket.pos = (self.center_x - self.rocket.size[0] / 2.0, self.y + 1.4 * self.slider.top)
        self.add_widget(self.rocket)

        for meteorite_obj in self.obstacles.meteorites:
            meteorite_obj.size = (Window.size[0] * meteorit.FRACTION_SCREEN_SIZE, Window.size[1] * meteorit.FRACTION_SCREEN_SIZE)
            meteorite_obj.pos = (Window.size[0] * meteorite_obj.offset_x, Window.size[1] * meteorite_obj.offset_y)
            self.add_widget(meteorite_obj)
        self.__run_update()

    def __activate_game_over(self, event):
        """
        Stop game loop and activate game over screen
        :return:
        """
        self.__stop_update()
        self.game_screen.get_game_over_menu_items()

    def __activate_new_level(self):
        """
        Activate new level screeen
        :param event:
        :return:
        """
        self.__stop_update()
        self.game_screen.level_finnish_screen(self.level)

    def __get_background_for_game(self):
        """
        Get proper background for Game for current level
        :return:
        """
        if self.level == 1:
            return Background(picture='pictures/background_02_800_450.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')
        elif self.level == 2:
            return Background(picture='pictures/background_02_800_450.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')
        elif self.level == 3:
            return Background(picture='pictures/background_02_800_450.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')
        else:
            return Background(picture='pictures/background_02_800_450.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')

    def __get_obstacles_for_game(self):
        """
        Get lists of obstacles for individual levels
        1st level -> Meteorites
        :return:
        """
        if self.level == 1:
            return Meteorites()
        if self.level == 2:
            return None
        elif self.level == 3:
            return None
        else:
            return None

    def __update_first_level(self):
        """
        Update screens, rockets, meteorites, do checks for collision and all for 1st level
        :return:
        """
        if self.last_screen:
            # If last screen then stop updating background and rocket flies away into another screen :)
            if self.game_background.image_dupe.y <= 5:
                self.rocket.y += 5

                if self.rocket.y >= self.game_background.image_dupe.top:
                    self.__activate_new_level()
                return

        if self.rocket.collision_complete:              # If collision complete -> stop updating and Game over
            self.__activate_game_over(None)

        if self.rocket.new_collision_detected:          # Activate collision process on new collision
            self.rocket.activate_explosion()
            return

        if self.rocket.collision_in_progress:           # Doesn't update background and other game processes
            return

        if not self.rocket.collision_in_progress:       # Update of MAIN game screen - background & meteorites
            self.game_background.update()
            self.obstacles.update()

        for meteorite in self.obstacles.meteorites:    # Check for collision and setup rocket collision flag
            if meteorite.collide_meteorit(self.rocket):
                self.rocket.new_collision_detected = True

        if not self.last_screen:
            if self.obstacles.is_behind_last(self.rocket.y, self.obstacles.meteorites[-1]):
                self.game_background.set_last_background()
                self.last_screen = True
