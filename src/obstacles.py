__author__ = 'brouk'

from obstacle import Obstacle

# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = [
    # todo: meteorites just for test
    # Coordinates numbers are fraction of screen size - coordinates numbers: [a, b] means:
    # x_coordinate = screen_width * a
    # y_coordinate = screen_height * b

    [0.7, 0.7],     # Example of obstacle coordinates
    [0.6, 0.8],     # Example of obstacle coordinates
    [0.5, 0.9]      # Example of obstacle coordinates
]


class Obstacles(object):
    """
    Base class for all obstacles for Meteorites, Rocks, ...
    """

    def __init__(self, picture_src, speed, offset_positions=INITIAL_POS_OFFSETS, allow_stretch=True,
                 allow_keep_ratio=True):
        self.__obstacles = []
        for obstacle_pos in offset_positions:
            obstacle = Obstacle(picture_src=picture_src, offset_position=obstacle_pos, obst_speed=speed,
                                allow_stretch=allow_stretch, allow_keep_ratio=allow_keep_ratio)
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

    def is_behind_last(self, current_y):
        """
        Return true if actual 'y' coordinate is behind last meteorite
        - all meteorites past - it means end of level -
        :param current_y:
        :return:
        """
        last_obstacle = self.__obstacles[-1]
        offset_y = last_obstacle.size[1] * 3
        last_y = last_obstacle.y + last_obstacle.size[1] + offset_y
        return current_y > last_y

    def collision_check(self, rocket_obj):
        """
        General check for collision of all obstacles (collision with square object) with rocket object
        :param rocket_obj:
        :return:
        """
        for obstacle in self.get_obstacle_list():
            if obstacle.y < rocket_obj.top and obstacle.top > rocket_obj.y:  # Y values are in collision
                if rocket_obj.right >= obstacle.x and rocket_obj.x <= obstacle.right:
                    return True

        return False
