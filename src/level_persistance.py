__author__ = 'brouk'

from kivy.storage.jsonstore import JsonStore


# Module to save and read complete modules - to be persistence between game run
# - Finished level is read when game starts and new level is saved into the file each time when new level is reach

class Persistence:
    """
    Class for read/write persistence level value
    """

    def __init__(self):
        self.JSON_FILE_NAME = 'galaxyrun_level.json'
        self.store = JsonStore(self.JSON_FILE_NAME)

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
                # print 'Level: ', current_level
        except:
            print 'Exception when reading Galaxy run level from JSON file!'

        return current_level

    def save_level(self, current_level):
        """
        Store current level into JSON file
        :return:
        """
        current_level = str(current_level)
        self.store.put('galaxy_run', level=current_level, org='brouk')
