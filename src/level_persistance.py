__author__ = 'brouk'

import numbers
from kivy.storage.jsonstore import JsonStore

# Module to save and read complete modules - to be persistence between game run
# - Finished level is read when game starts and new level is saved into the file each time when new level is reach


class Persistence:
    """
    Class for read/write persistence level value
    read_level() - return current level from storage (JSON file)

    """

    def __init__(self):
        self.JSON_FILE_NAME = 'galaxyrun_level.json'
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
            if self.store.exists('galaxy_run'):
                current_level_str = self.store.get('galaxy_run')['level']
                current_level = int(current_level_str)
                #print 'Persistence Level read: ', current_level
        except:
            print 'Exception when reading Galaxy run level from JSON file!'

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
                    self.store.put('galaxy_run', level=current_level, org='brouk')
        except:
            print "Error: cannot save game level!"
