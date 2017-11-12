__author__ = 'brouk'

from src.rock import Rock


# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = [
    # todo: meteorites just for test
    # Coordinates numbers are fraction of screen size - coordinates numbers: [a, b] means:
    # x_coordinate = screen_width * a
    # y_coordinate = screen_height * b

    # [0.8, 0.6],
    # [0.7, 0.7],
    # [0.6, 0.8],
    [0.5, 0.9]

    # [0.7, 0.6],
    # [0.2, 0.9],
    #
    # [-0.06, 1.3],
    # [0.7, 1.5],
    #
    # [0.25, 1.6],
    # [0.1, 1.8],
    # [-0.05, 2.0],
    # [0.4, 1.9],
    # [0.8, 2.0]

]


class Rocks:
    """
    Generate list of Rocks for level 2
    """
    def __init__(self):
        self.rocks = []
        for rocks_pos in INITIAL_POS_OFFSETS:

            rock = Rock(source='pictures/square_3.png', offset_position=rocks_pos)

            self.rocks.append(rock)

    def update(self):
        """
        Update positions of all meteorites
        :return:
        """
        for rock in self.rocks:
            rock.update()

    def is_behind_last(self, current_y, last_meteorite):
        # """
        # Return true if actual 'y' coordinate is behind last meteorite
        # - all meteorites past - it means end of level -
        # :param current_y:
        # :return:
        # """
        # offset_y = last_meteorite.size[1] * 3
        # last_y = last_meteorite.y + last_meteorite.size[1] + offset_y
        # return current_y > last_y
        pass
