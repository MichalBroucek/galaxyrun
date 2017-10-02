__author__ = 'brouk'

from src.meteorit import Meteorit

# TODO: this is only for testing level 2
# FIXME: THIS needs to be written for new level 2 !!!

# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = [
    [30, 300],
    [200, 300],

    [30, 700],
    [200, 800],
    [250, 820],

]


class MeteoritesLevel2:
    """
    Generate list of meteorites and update all of them
    """
    def __init__(self, center_x, center_y):
        self.meteorites = []
        for meteorite_pos in INITIAL_POS_OFFSETS:
            meteorite = Meteorit(source='pictures/meteor_smaller.png', pos=(center_x + meteorite_pos[0], center_y + meteorite_pos[1]))
            self.meteorites.append(meteorite)

    def update(self):
        """
        Update possitions of all meterorites
        :return:
        """
        for meteorite in self.meteorites:
            meteorite.update()
