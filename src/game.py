__author__ = 'brouk'

from kivy.uix.widget import Widget
from kivy.clock import Clock

from src.background import Background
from rocket import Rocket
from sprite import Sprite
from meteorites import Meteorites
from rocks_edges import Rocks_edges
from rock_backgrounds_meteorites import Rock_background_meteorites

from kivy.core.window import Window


class Game(Widget):
    def __init__(self, screen_ref):
        super(Game, self).__init__()
        self.game_screen = screen_ref
        self.running_level = 1          # todo: 1 as default ?
        # Make it separate for individual levels 1, 2, 3
        self.game_backgrounds = self.__get_background_for_game()
        self.rocket = Rocket(picture='pictures/rocket_01_40x69.png')
        self.slider = Sprite(picture='pictures/swiper.png', allow_stretch=True)
        self.obstacles = self.__get_obstacles_for_game()
        self.meteorites_background = self.__get_meteorites_background()
        self.last_screen = False
        self.sound = False

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
        """
        Update screens, rockets, meteorites, do checks for collision and everything else
        :return:
        """
        if self.last_screen:
            # If last screen then stop updating background and rocket flies away into another screen :)
            if self.game_backgrounds.image_dupe.y <= 5:
                self.rocket.y += 5

                if self.rocket.y >= self.game_backgrounds.image_dupe.top:
                    self.__activate_new_level()
                return

        if self.rocket.collision_complete:              # If collision complete -> stop updating and Game over
            self.__activate_game_over(None)

        if self.rocket.new_collision_detected:          # Activate collision process on new collision
            self.rocket.activate_explosion(self.sound)
            return

        if self.rocket.collision_in_progress:           # Doesn't update background and other game processes
            return

        if not self.rocket.collision_in_progress:       # Update of MAIN game screen - background & meteorites
            self.game_backgrounds.update()
            self.obstacles.update()
            if self.meteorites_background:
                self.meteorites_background.update()

        self.rocket.new_collision_detected = self.obstacles.collision_check(self.rocket)

        if not self.last_screen:
            if self.obstacles.is_behind_last(self.rocket.y):
                self.game_backgrounds.set_last_background()
                self.last_screen = True

    def on_touch_move(self, touch):
        """
        On touch in bottom part of the game move with rocket
        :param touch:
        :return:
        """
        if touch.y < self.slider.top:
            self.rocket.center_x = touch.x

    def run_game(self, game_level, play_sound=False, speed=13):
        """
        Initialize game window setup background, rocket, slider, obstacles and start game update loop
        :return:
        """
        self.clear_widgets()

        self.running_level = game_level     # Setup actual running level
        self.sound = play_sound

        # Setup Game background and obstacles for current level
        self.game_backgrounds = self.__get_background_for_game()
        self.add_widget(self.game_backgrounds.image)
        self.add_widget(self.game_backgrounds.image_dupe)

        self.obstacles = self.__get_obstacles_for_game(obstacles_speed=speed)
        self.meteorites_background = self.__get_meteorites_background(obstacles_speed=speed)

        self.add_widget(self.game_backgrounds)

        self.obstacles.add_all_to_widget(self)
        if self.meteorites_background:
            self.meteorites_background.add_all_to_widget(self)

        self.slider.size = (Window.size[0], Window.size[1] * 0.1)
        self.slider.pos = (0, 0)
        self.add_widget(self.slider)

        self.rocket.size = (Window.size[0] * 0.03, Window.size[1] * 0.1)
        self.rocket.pos = (self.center_x - self.rocket.size[0] / 2.0, self.y + 1.4 * self.slider.top)
        self.add_widget(self.rocket)

        self.__run_update()

    def __activate_game_over(self, event):
        """
        Stop game loop and activate game over screen
        :return:
        """
        self.__stop_update()
        self.game_screen.get_game_over_menu_items(self.running_level)

    def __activate_new_level(self):
        """
        Activate new level screeen
        :param event:
        :return:
        """
        self.__stop_update()
        self.game_screen.level_finnish_screen(self.running_level)

    def __get_background_for_game(self):
        """
        Set proper background for Game for specific game level
        :return:
        """
        if self.running_level == 1:
            return Background(background_picture='pictures/game_backgrounds/bckg_level_1.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')
        elif self.running_level == 2:
            return Background(background_picture='pictures/game_backgrounds/bckg_level_2b.png',
                                        #todo: Make new final screen for level 2
                                          last_background_image='pictures/final_screens/final_1_static.png')
        elif self.running_level == 3:
            #todo: make new background and final screen for level 3
            return Background(background_picture='pictures/game_backgrounds/bckg_level_1.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')
        else:
            return Background(background_picture='pictures/game_backgrounds/bckg_level_1.png',
                                          last_background_image='pictures/final_screens/final_1_static.png')

    def __get_obstacles_for_game(self, obstacles_speed=13):
        """
        Get lists of obstacles for individual levels
        1st level -> Meteorites
        :return:
        """
        if self.running_level == 1:
            return Meteorites(flight_speed=obstacles_speed)
        if self.running_level == 2:
            return Rocks_edges(flight_speed=obstacles_speed)
        elif self.running_level == 3:
            return None
        else:
            return None

    def __add_obstacles_for_game(self):
        """
        Add obstacles for current level
        :return:
        """
        if self.running_level == 1:
            self.obstacles.add_all_to_widget(self)
        elif self.running_level == 2:
            self.obstacles.add_all_to_widget(self)
        elif self.running_level == 3:
            self.obstacles = []
        else:
            pass

    def __get_meteorites_background(self, obstacles_speed=13):
        """
        Return meteorites which are flying on the background - no crash possible
        They are just for decoration
        :return:
        """
        if self.running_level == 1:
            return []
        if self.running_level == 2:
            return Rock_background_meteorites(flight_speed=obstacles_speed)
        elif self.running_level == 3:
            return []
        else:
            return None
