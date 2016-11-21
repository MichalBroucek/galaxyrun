__author__ = 'brouk'

from meteorit import Meteorit

# Initial [x_offset, y_offset] for individual meteorites
# TODO: debug possitions - some may be out of Game
INITIAL_POS_OFFSETS = [
    [50, 300],
    [200, 600],

    [-100, 800],
    [100, 900],

    [-200, 1200],
    [0, 1300],
    [150, 1350],

    [-200, 1600],
    [-50, 1800],
    [100, 1700],
]


class Meteorites:
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


