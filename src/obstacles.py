__author__ = 'brouk'

from obstacle import Obstacle


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


class Obstacles(object):
    """
    Base class for all obstacles for Meteorites, Rocks, ...
    """
    def __init__(self, picture_src, offset_positions=INITIAL_POS_OFFSETS):
        self.__obstacles = []
        for obstacle_pos in offset_positions:
            obstacle = Obstacle(picture_src=picture_src, offset_position=obstacle_pos)
            self.__obstacles.append(obstacle)

    def get_obstacle_list(self):
        return self.__obstacles

    def update(self):
        """
        Update positions of all obstacles
        :return:
        """
        for obstacle in self.__obstacles:
            obstacle.update()

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
