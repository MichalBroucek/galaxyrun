__author__ = 'brouk'

from meteorit import Meteorit

# Initial [x_offset, y_offset] for individual meteorites
# TODO: debug possitions - some may be out of Game
INITIAL_POS_OFFSETS = [
    [50, 300],
    [200, 450],

    [0, 700],
    [-130, 800],
    [-330, 820],

    [-400, 1200],
    [220, 1000],

    [-300, 1400],
    [100, 1150],
    [-200, 1570],
    [50, 1350],
    [0, 1620],

    [220, 1900],
    [90, 2000],
    [-50, 2100],
    [-150, 2250],

    [-390, 2450],
    [-250, 2600],
    [-100, 2750],
    [200, 2850]
]


class Meteorites:
    """
    Generate list of meteorites and update all of them
    """
    def __init__(self, center_x, center_y):
        self.meteorites = []
        for meteorite_pos in INITIAL_POS_OFFSETS:
            meteorite = Meteorit(source='meteor_smaller.png', pos=(center_x + meteorite_pos[0], center_y + meteorite_pos[1]))
            self.meteorites.append(meteorite)

    def update(self):
        """
        Update possitions of all meterorites
        :return:
        """
        for meteorite in self.meteorites:
            meteorite.update()
