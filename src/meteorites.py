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

    [0.4, 4.85],
    [0.2, 4.95],
    [-0.1, 5.15],
    [0.05, 5.5],
    [0.25, 5.6],
    [0.77, 5.8],

    # random on right size
    [0.6, 4.95],
    [0.73, 5.25],
    [0.5, 5.2],
    [0.65, 5.55],

    [0.6, 6.2],
    [0.75, 6.45],
    [0.2, 6.3],

    [0.55, 6.9],
    [0.75, 7.0],
    [0.4, 7.05],
    [-0.05, 7.15],

    [-0.07, 7.7],
    [0.15, 7.65],
    [0.7, 7.69]

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

    def is_behind_last(self, current_y, last_meteorite):
        """
        Return true if actual 'y' coordinate is behind last meteorite
        - all meteorites past - it means end of level -
        :param current_y:
        :return:
        """
        offset_y = last_meteorite.size[1] * 3
        last_y = last_meteorite.y + last_meteorite.size[1] + offset_y
        print "ooo Actual y: {0}".format(current_y)
        print "ooo Last_y y: {0}".format(last_y)
        return current_y > last_y
