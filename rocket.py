__author__ = 'brouk'

from kivy.clock import Clock

from sprite import Sprite


# TODO: How to use subfolders on Android ?
# TODO: Buildozer needs special configuration ?
ROCKET_PNG = "pictures/rocket_01_40x69.png"
ROCKET_HIT_WHITE_PNG = "pictures/rocket_01_40x69_white_01.png"
ROCKET_HIT_RED_PNG = "pictures/rocket_01_40x69_red_01.png"

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
    def __init__(self, pos):
        super(Rocket, self).__init__(source=ROCKET_PNG, pos=pos)
        self.new_collision_detected = False            # Why it's needed
        self.collision_in_progress = False
        self.collision_complete = False

    def activate_explosion(self):
        if not self.collision_in_progress:
            self.new_collision_detected = False
            self.collision_in_progress = True
            self.__explode()
            print "################ EXPLODE #######################"

    def __explode(self):
        """
        Rocket hits meteorite and explodes
        :return:
        """
        self.__partial_explode()

    def __partial_explode(self):
        Clock.schedule_once(self.__set_explosion_1, 0)
        Clock.schedule_once(self.__set_explosion_2, 0.1)
        Clock.schedule_once(self.__set_explosion_3, 0.2)
        Clock.schedule_once(self.__set_explosion_4, 0.3)
        Clock.schedule_once(self.__set_explosion_5, 0.4)
        Clock.schedule_once(self.__set_explosion_6, 0.5)
        Clock.schedule_once(self.__set_explosion_7, 0.6)
        #Clock.schedule_once(self.__set_default_color, 1)

    def __set_default_color(self, dt):
        self.source = ROCKET_PNG
        self.size = (40, 69)
        self.collision_in_progress = False

    def __set_white_color(self, dt):
        self.source = ROCKET_HIT_WHITE_PNG
        self.size = (40, 69)

        self.source = ROCKET_PNG
        self.size = (40, 69)
        self.collision_in_progress = False

    def __set_red_color(self, dt):
        self.source = ROCKET_HIT_RED_PNG
        self.size = (40, 69)

    def __set_explosion_1(self, dt):
        self.source = EXPLOSION_1

    def __set_explosion_2(self, dt):
        self.source = EXPLOSION_2

    def __set_explosion_3(self, dt):
        self.source = EXPLOSION_3

    def __set_explosion_4(self, dt):
        self.source = EXPLOSION_4
        self.size = (60, 70)

    def __set_explosion_5(self, dt):
        self.source = EXPLOSION_5
        self.size = (60, 70)

    def __set_explosion_6(self, dt):
        self.source = EXPLOSION_6
        self.size = (60, 70)

    def __set_explosion_7(self, dt):
        self.source = EXPLOSION_7
        self.size = (60, 70)
        self.collision_complete = True
