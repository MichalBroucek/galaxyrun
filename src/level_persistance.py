__author__ = 'brouk'

import numbers
from kivy.storage.jsonstore import JsonStore
import app_screen

# Module to save and read complete modules - to be persistence between game run
# - Finished level is read when game starts and new level is saved into the file each time when new level is reach
# - configuration for speed is changed via configuration screen - and read at the beginning of the game
# - configuration for sound (ON/OFF) is changed via configuration screen - and read at the beginning of the game

LEVEL_STORE = 'galaxy_level'
SPEED_STORE = 'galaxy_speed'
SOUND_STORE = 'galaxy_sound'


class Persistence:
    """
    Class for read/write persistence for reached level, speed and sound configuration
    """

    def __init__(self):
        self.JSON_FILE_NAME = 'galaxyrun_config.json'
        try:
            self.store = JsonStore(self.JSON_FILE_NAME)
        except:
            print "Error cannot create/open persistence store!"

    def read_level(self):
        """
        Read current level from JSON file
        :return:
        """
        current_level = 1

        try:
            if self.store.exists(LEVEL_STORE):
                current_level_str = self.store.get(LEVEL_STORE)['level']
                current_level = int(current_level_str)
        except:
            print 'Exception when reading Galaxy run level from JSON file!'
            current_level = 1

        return current_level

    def write_level(self, current_level):
        """
        Store current level into JSON file
        :return:
        """
        try:
            if isinstance(current_level, numbers.Number):
                if 1 <= current_level <= 3:
                    current_level = str(current_level)
                    self.store.put(LEVEL_STORE, level=current_level)
        except:
            print "Error: cannot save game level!"

    def read_speed(self):
        """
        Read current speed game from JSON file
        :return:
        """
        current_speed = app_screen.SPEED_MEDIUM

        try:
            if self.store.exists(SPEED_STORE):
                current_speed_str = self.store.get(SPEED_STORE)['speed']
                current_speed = int(current_speed_str)
                # DEBUG
        except:
            print 'Exception when reading Galaxy run level from JSON file!'

        return current_speed

    def write_speed(self, current_speed):
        """
        Store current speed into JSON file
        :return:
        """
        try:
            if isinstance(current_speed, numbers.Number):
                if current_speed in [app_screen.SPEED_SLOW, app_screen.SPEED_MEDIUM, app_screen.SPEED_FAST]:
                    current_speed_str = str(current_speed)
                    self.store.put(SPEED_STORE, speed=current_speed_str)
        except:
            print "Error: cannot save game speed!"

    def read_sound(self):
        """
        Read current sound configuration (ON/OFF = True/False) from JSON file
        :return:
        """
        sound = False

        try:
            if self.store.exists(SOUND_STORE):
                current_sound_str = self.store.get(SOUND_STORE)['sound']
                if current_sound_str == 'ON':
                    sound = True
                elif current_sound_str == 'OFF':
                    sound = False
                else:
                    sound = False
        except:
            print 'Exception when reading Galaxy sound configuration from JSON file!'

        return sound

    def write_sound(self, current_sound_conf):
        """
        Store current sound configuration into JSON file
        :return:
        """
        print "SOUND as parameter: ", current_sound_conf
        try:
            if current_sound_conf:
                current_sound_str = 'ON'
            else:
                current_sound_str = 'OFF'
            self.store.put(SOUND_STORE, sound=current_sound_str)
        except:
            print "Error: cannot save game sound configuration!"
