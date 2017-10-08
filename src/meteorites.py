__author__ = 'brouk'

from src.meteorit import Meteorit

# TODO !!! Need to update collision mechanism as size of individual meteorites is dynamic according screen size now


# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = [
    # todo: meteorites just for test
    [0.1, 0.5],
    [0.2, 0.6],
    [0.3, 0.7],
    [0.4, 0.8],
    [0.5, 0.9],

    # [50, 300],
    # [200, 450],
    #
    # [0, 700],
    # [-130, 800],
    # [-330, 820],
    #
    # [-400, 1200],
    # [220, 1000],
    #
    # [-300, 1400],
    # [100, 1150],
    # [-200, 1570],
    # [50, 1350],
    # [0, 1620],
    #
    # [220, 1900],
    # [90, 2000],
    # [-50, 2100],
    # [-150, 2250],
    #
    # [-390, 2450],
    # [-250, 2600],
    # [-100, 2750],
    # [200, 2850]
]


class Meteorites:
    """
    Generate list of meteorites and update all of them
    """
    def __init__(self):
        self.meteorites = []
        for meteorite_pos in INITIAL_POS_OFFSETS:
            meteorite = Meteorit(source='pictures/meteor_smaller.png', offset_possition=meteorite_pos)
            self.meteorites.append(meteorite)

    def update(self):
        """
        Update possitions of all meterorites
        :return:
        """
        for meteorite in self.meteorites:
            meteorite.update()
