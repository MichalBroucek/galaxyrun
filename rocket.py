__author__ = 'brouk'

from kivy.clock import Clock

from sprite import Sprite


# TODO: How to use subfolders on Android ?
# TODO: Buildozer needs special configuration ?
ROCKET_PNG = "pictures/rocket_01_40x69.png"
ROCKET_HIT_WHITE_PNG = "pictures/rocket_01_40x69_white_01.png"
ROCKET_HIT_RED_PNG = "pictures/rocket_01_40x69_red_01.png"

template = "pictures/explosion_process/explosion_%d.png"
explosions = [template % i for i in range(1, 8)]


class Rocket(Sprite):
    """
    Rocket
    """
    def __init__(self, pos):
        super(Rocket, self).__init__(source=ROCKET_PNG, pos=pos)
        self.first_collision = False
        self.existing_collision = False
        self.explosion_in_progress = False
        self.collision_complete = False
        self.explosion_step = 0

    def update(self):
        if self.first_collision:
            self.first_collision = False
            self.explosion_in_progress = True
            self.__explode()
            print "################ EXPLODE #######################"

        return not self.collision_complete

    def __explode(self):
        """
        Rocket hits meteorite and explodes
        :return:
        """
        Clock.schedule_interval(self.__explosion_callback, 0.1)

    def __explosion_callback(self, dt):
        self.source = explosions[self.explosion_step]
        self.explosion_step += 1
        self.collision_complete = (self.explosion_step == len(explosions))
        return not self.collision_complete

    def __set_default_color(self, dt):
        self.source = ROCKET_PNG
        self.size = (40, 69)
        self.explosion_in_progress = False

    def __set_white_color(self, dt):
        self.source = ROCKET_HIT_WHITE_PNG
        self.size = (40, 69)

        self.source = ROCKET_PNG
        self.size = (40, 69)
        self.explosion_in_progress = False

    def __set_red_color(self, dt):
        self.source = ROCKET_HIT_RED_PNG
        self.size = (40, 69)
