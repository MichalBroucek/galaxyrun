__author__ = 'brouk'

from obstacles import Obstacles
from kivy.core.window import Window

FRACTION_SCREEN_SIZE = 1.0 / 3.0  # 1/3 of the actual game screen

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

]


class Meteorites(Obstacles):
    """
    Generate list of Rocks for level 2
    """
    def __init__(self):
        super(Meteorites, self).__init__(picture_src='pictures/meteor_smaller.png', speed=17,
                                         offset_positions=INITIAL_POS_OFFSETS, allow_stretch=True,
                                         allow_keep_ratio=True)

    def add_all_to_widget(self, destination_widget):
        """
        Add all obstacles into widget defined as parameter
        :return:
        """
        for meteorite_obj in self.get_obstacle_list():
            meteorite_obj.size = (Window.size[0] * FRACTION_SCREEN_SIZE, Window.size[1] * FRACTION_SCREEN_SIZE)
            meteorite_obj.pos = (Window.size[0] * meteorite_obj.offset_x, Window.size[1] * meteorite_obj.offset_y)
            destination_widget.add_widget(meteorite_obj)

    def collision_check(self, rocket_obj):
        """
        Check for collision between all Meteorites and rocket
        :param rocket_obj:
        :return:
        """
        for meteorite in self.get_obstacle_list():
            # There are 3 different parts (on 'y' axis) with different 'x' and 'rights' where we detect collisions
            # 3 different rectangles for collision detection are used
            if self.__collide_with_bottom(meteorite, rocket_obj):
                return True
            # Detect collision than in middle part (middle rectangle)
            elif self.__collide_with_middle(meteorite, rocket_obj):
                return True
            # Detect collision in top part (top rectangle)
            if self.__collide_with_top(meteorite, rocket_obj):
                return True

        return False

    def __collide_with_bottom(self, meteorite, rocket):
        """
        Detect collision with bottom part of meteorite
        :param rocket: widget to collide with
        :return: True if collision happens
        """
        # Has to be calculated here as it depends on meteorite position
        bottom_bottom, bottom_top, bottom_x, bottom_right = self.__get_bottom_borders(meteorite)

        if bottom_bottom <= rocket.top <= bottom_top:
            if rocket.right >= bottom_x and rocket.x <= bottom_right:
                return True

        return False

    def __collide_with_middle(self, meteorite, rocket):
        """
        Detect collision with middle part of meteorite
        :param rocket: widget to collide with
        :return: True if collision happens
        """
        # Has to be calculated here as it depends on meteorite position
        middle_bottom, middle_top, middle_x, middle_right = self.__get_middle_borders(meteorite)

        if middle_bottom <= rocket.top <= middle_top:
            if middle_right >= rocket.x and middle_x <= rocket.right:
                return True

        return False

    def __collide_with_top(self, meteorite, rocket):
        """
        Detect collision with top part of meteorite
        :param rocket:
        :return:
        """
        # Has to be calculated here as it depends on meteorite position
        top_bottom, top_top, top_x, top_right = self.__get_top_borders(meteorite)

        if top_bottom <= rocket.top and rocket.y <= top_top:
            if top_right >= rocket.x and top_x <= rocket.right:
                return True

        return False

    def __get_bottom_borders(self, meteorite):
        """
        Return borders for collision in bottom part
        There is overlap for crashing with meteorite
        :return:
        """
        COLLISION_BOTTOM_BOTTOM_OFFSET = 0.1  # (0.25) * size[1]
        COLLISION_BOTTOM_TOP_OFFSET = 0.35  # (0.65) * size[1]
        COLLISION_BOTTOM_LEFT_OFFSET = 0.4  # (0.4) * size[0]
        COLLISION_BOTTOM_RIGHT_OFFSET = 0.55  # (0.5) * size[0]

        bottom_bottom = meteorite.y + (meteorite.size[1] * COLLISION_BOTTOM_BOTTOM_OFFSET)
        bottom_top = meteorite.y + (meteorite.size[1] * COLLISION_BOTTOM_TOP_OFFSET)
        bottom_x = meteorite.x + (meteorite.size[0] * COLLISION_BOTTOM_LEFT_OFFSET)
        bottom_right = meteorite.right - (meteorite.size[0] * COLLISION_BOTTOM_RIGHT_OFFSET)

        return [bottom_bottom, bottom_top, bottom_x, bottom_right]

    def __get_middle_borders(self, meteorite):
        """
        Return borders for collision in middle part
        There is overlap for crashing with meteorite
        :return:
        """
        COLLISION_MIDDLE_BOTTOM_OFFSET = 0.35
        COLLISION_MIDDLE_TOP_OFFSET = 0.75
        COLLISION_MIDDLE_LEFT_OFFSET = 0.33
        COLLISION_MIDDLE_RIGHT_OFFSET = 0.35

        middle_bottom = meteorite.y + (meteorite.size[1] * COLLISION_MIDDLE_BOTTOM_OFFSET)
        middle_top = meteorite.y + (meteorite.size[1] * COLLISION_MIDDLE_TOP_OFFSET)
        middle_x = meteorite.x + (meteorite.size[0] * COLLISION_MIDDLE_LEFT_OFFSET)
        middle_right = meteorite.right - (meteorite.size[0] * COLLISION_MIDDLE_RIGHT_OFFSET)

        return [middle_bottom, middle_top, middle_x, middle_right]

    def __get_top_borders(self, meteorite):
        """
        Return borders for collision in top part
        There is overlap for crashing with meteorite
        :return:
        """
        COLLISION_TOP_BOTTOM_OFFSET = 0.75
        COLLISION_TOP_TOP_OFFSET = 0.9
        COLLISION_TOP_LEFT_OFFSET = 0.45
        COLLISION_TOP_RIGHT_OFFSET = 0.45

        top_bottom = meteorite.y + (meteorite.size[1] * COLLISION_TOP_BOTTOM_OFFSET)
        top_top = meteorite.y + (meteorite.size[1] * COLLISION_TOP_TOP_OFFSET)
        top_x = meteorite.x + (meteorite.size[0] * COLLISION_TOP_LEFT_OFFSET)
        top_right = meteorite.right - (meteorite.size[0] * COLLISION_TOP_RIGHT_OFFSET)

        return [top_bottom, top_top, top_x, top_right]
