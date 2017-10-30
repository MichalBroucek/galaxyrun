__author__ = 'brouk'

from kivy.clock import Clock
from sprite import Sprite

ROCKET_PNG = "pictures/rocket_01_40x69.png"
ROCKET_HIT_WHITE_PNG = "pictures/rocket_01_40x69_white_01.png"
ROCKET_HIT_RED_PNG = "pictures/rocket_01_40x69_red_01.png"

template = "pictures/explosion_process/explosion_%d.png"
explosions = [template % i for i in range(1, 8)]


class Rocket(Sprite):
    """
    Rocket
    """
    def __init__(self, picture=ROCKET_PNG):
        super(Rocket, self).__init__(source=picture)
        self.allow_stretch = True
        self.new_collision_detected = False
        self.collision_in_progress = False
        self.collision_complete = False
        self.explosion_step = 0

    def activate_explosion(self):
        if not self.collision_in_progress:
            self.new_collision_detected = False
            self.collision_in_progress = True
            self.__explode()

    def __explode(self):
        Clock.schedule_interval(self.__explosion_callback, 0.1)

    def __explosion_callback(self, dt):
        self.source = explosions[self.explosion_step]
        self.explosion_step += 1
        self.collision_complete = (self.explosion_step == len(explosions))
        return not self.collision_complete
