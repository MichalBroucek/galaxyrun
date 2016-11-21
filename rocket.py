__author__ = 'brouk'

from sprite import Sprite
from kivy.clock import Clock


ROCKET_PNG = "pictures/rocket_01_40x69.png"
ROCKET_HIT_WHITE_PNG = "pictures/rocket_01_40x69_white_01.png"
ROCKET_HIT_RED_PNG = "pictures/rocket_01_40x69_red_01.png"


class Rocket(Sprite):
    """
    Rocket
    """
    def __init__(self, pos):
        super(Rocket, self).__init__(source=ROCKET_PNG, pos=pos)
        self.num_lives = 3
        self.first_collision = False
        self.existing_collision = False

    def update(self):
        if self.first_collision:
            self.first_collision = False
            self.__explode()
            print "################ EXPLODE #######################"

    def __explode(self):
        """
        Rocket hits meteorite and explodes
        :return:
        """
        self.__partial_explode()
        self.num_lives -= 1
        print "++++++++ NUMBER OF LIVES: {0} ++++++++".format(self.num_lives)

    def __partial_explode(self):
        Clock.schedule_once(self.__set_white_color, 0)
        Clock.schedule_once(self.__set_red_color, 0.1)
        Clock.schedule_once(self.__set_white_color, 0.2)
        Clock.schedule_once(self.__set_red_color, 0.3)
        Clock.schedule_once(self.__set_white_color, 0.4)
        Clock.schedule_once(self.__set_red_color, 0.5)
        Clock.schedule_once(self.__set_default_color, 0.7)

    def __set_white_color(self, dt):
        self.source = ROCKET_HIT_WHITE_PNG

    def __set_default_color(self, dt):
        self.source = ROCKET_PNG

    def __set_red_color(self, dt):
        self.source = ROCKET_HIT_RED_PNG
