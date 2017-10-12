__author__ = 'brouk'

from kivy.clock import Clock

from sprite import Sprite

ROCKET_PNG = "pictures/rocket_01_40x69.png"
ROCKET_HIT_WHITE_PNG = "pictures/rocket_01_40x69_white_01.png"
ROCKET_HIT_RED_PNG = "pictures/rocket_01_40x69_red_01.png"

ROCKET_WIDTH = 40
ROCKET_HEIGHT = 69

EXPLOSION_1 = "pictures/explosion_process/explosion_1.png"
EXPLOSION_2 = "pictures/explosion_process/explosion_2.png"
EXPLOSION_3 = "pictures/explosion_process/explosion_3.png"
EXPLOSION_4 = "pictures/explosion_process/explosion_4.png"
EXPLOSION_5 = "pictures/explosion_process/explosion_5.png"
EXPLOSION_6 = "pictures/explosion_process/explosion_6.png"
EXPLOSION_7 = "pictures/explosion_process/explosion_7.png"


class Rocket(Sprite):
    """
    Rocket
    """
    def __init__(self, picture=ROCKET_PNG):
        super(Rocket, self).__init__(source=picture)
        self.allow_stretch = True
        self.new_collision_detected = False            # Why it's needed
        self.collision_in_progress = False
        self.collision_complete = False

    def activate_explosion(self):
        if not self.collision_in_progress:
            self.new_collision_detected = False
            self.collision_in_progress = True
            self.__explode()

    def __explode(self):
        Clock.schedule_once(self.__set_explosion_1, 0)
        Clock.schedule_once(self.__set_explosion_2, 0.1)
        Clock.schedule_once(self.__set_explosion_3, 0.2)
        Clock.schedule_once(self.__set_explosion_4, 0.3)
        Clock.schedule_once(self.__set_explosion_5, 0.4)
        Clock.schedule_once(self.__set_explosion_6, 0.5)
        Clock.schedule_once(self.__set_explosion_7, 0.6)

    def __set_default_color(self, dt):
        self.source = ROCKET_PNG
        self.size = (ROCKET_WIDTH, ROCKET_HEIGHT)
        self.collision_in_progress = False

    def __set_white_color(self, dt):
        self.source = ROCKET_HIT_WHITE_PNG
        self.size = (ROCKET_WIDTH, ROCKET_HEIGHT)

        self.source = ROCKET_PNG
        self.size = (ROCKET_WIDTH, ROCKET_HEIGHT)
        self.collision_in_progress = False

    def __set_red_color(self, dt):
        self.source = ROCKET_HIT_RED_PNG
        self.size = (ROCKET_WIDTH, ROCKET_HEIGHT)

    def __set_explosion_1(self, dt):
        self.source = EXPLOSION_1

    def __set_explosion_2(self, dt):
        self.source = EXPLOSION_2

    def __set_explosion_3(self, dt):
        self.source = EXPLOSION_3

    def __set_explosion_4(self, dt):
        self.source = EXPLOSION_4

    def __set_explosion_5(self, dt):
        self.source = EXPLOSION_5

    def __set_explosion_6(self, dt):
        self.source = EXPLOSION_6

    def __set_explosion_7(self, dt):
        self.source = EXPLOSION_7
        self.collision_complete = True
