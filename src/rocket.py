__author__ = 'brouk'

from kivy.clock import Clock
from sprite import Sprite
from kivy.core.audio import SoundLoader
import app_screen

ROCKET_PNG = "pictures/rocket_01_40x69.png"
# ROCKET_HIT_WHITE_PNG = "pictures/rocket_01_40x69_white_01.png"
# ROCKET_HIT_RED_PNG = "pictures/rocket_01_40x69_red_01.png"

template = "pictures/explosion_process/explosion_%d.png"
explosions = [template % i for i in range(1, 8)]


class Rocket(Sprite):
    """
    Rocket
    """
    def __init__(self, picture=ROCKET_PNG):
        super(Rocket, self).__init__(picture=picture, allow_stretch=True, allow_keep_ratio=False)
        self.new_collision_detected = False
        self.collision_in_progress = False
        self.collision_complete = False
        self.explosion_step = 0
        self.explosion_sound = SoundLoader.load('sound/explosion_02.wav')
        self.explosion_sound.volume = app_screen.MUSIC_VOLUME
        self.explosion_sound.seek(0.5)

    def activate_explosion(self, play_sound=False):
        if not self.collision_in_progress:
            self.new_collision_detected = False
            self.collision_in_progress = True
            self.__play_explosion_sound(play_sound)
            self.__explode()

    def __explode(self):
        Clock.schedule_interval(self.__explosion_callback, 0.1)

    def __explosion_callback(self, dt):
        self.source = explosions[self.explosion_step]
        self.explosion_step += 1
        self.collision_complete = (self.explosion_step == len(explosions))
        return not self.collision_complete

    def __play_explosion_sound(self, play_sound=False):
        """
        Play explosion sound if SOUND is ON
        :return:
        """
        if play_sound and self.explosion_sound:
            # print("Sound found at %s" % sound.source)
            # print("Sound is %.3f seconds" % sound.length)
            self.explosion_sound.play()
