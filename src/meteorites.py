__author__ = 'brouk'

from src.meteorit import Meteorit


# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = [
    # todo: meteorites just for test
    # Coordinates numbers are fraction of screen size - coordinates numbers: [a, b] means:
    # x_coordinate = screen_width * a
    # y_coordinate = screen_height * b

    [0.7, 0.6],
    [0.2, 0.9],

    [-0.06, 1.3],
    [0.7, 1.5],

    [0.25, 1.6],
    [0.1, 1.8],
    [-0.05, 2.0],
    [0.4, 1.9],
    [0.8, 2.0],

    [0.75, 2.3],
    [0.6, 2.5],
    [0.0, 2.55],
    [0.45, 2.65],

    [0.25, 3.1],
    [0.1, 3.25],
    [0.41, 3.3],
    [0.56, 3.5],
    [0.71, 3.7],
    [0.86, 3.9],

    [3.0, 3.4],
    [-0.05, 4.0],
    [0.1, 4.25],

    [0.4, 4.85]

    # todo: ... add more ...
]


class Meteorites:
    """
    Generate list of meteorites and update all of them
    """
    def __init__(self):
        self.meteorites = []
        for meteorite_pos in INITIAL_POS_OFFSETS:
            meteorite = Meteorit(source='pictures/meteor_smaller.png', offset_position=meteorite_pos)
            self.meteorites.append(meteorite)

    def update(self):
        """
        Update possitions of all meterorites
        :return:
        """
        for meteorite in self.meteorites:
            meteorite.update()
