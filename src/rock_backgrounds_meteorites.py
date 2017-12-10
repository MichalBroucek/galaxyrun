__author__ = 'brouk'

from obstacles import Obstacles
from kivy.core.window import Window

FRACTION_SCREEN_SIZE = 1.0 / 1.5  # 1/3 of the actual game screen

# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = [
    # todo: meteorites just for test
    # Coordinates numbers are fraction of screen size - coordinates numbers: [a, b] means:
    # x_coordinate = screen_width * a
    # y_coordinate = screen_height * b

    # y_shift = 0.15
    # x_shift = 0.07

    [0.0, 1.6],

    [0.7, 2.5],

    # [0.6, 2.0],
    #
    # [0.0, 2.5]

]


class Rock_background_meteorites(Obstacles):
    """
    Generate list of Rocks backgrounds and side rock for decoration of level 2
    """

    def __init__(self, flight_speed=13):
        super(Rock_background_meteorites, self).__init__(picture_src='pictures/met_small.png', speed=flight_speed, offset_positions=INITIAL_POS_OFFSETS,
                                    allow_stretch=True, allow_keep_ratio=True)

    def add_all_to_widget(self, destination_widget):
        """
        Add all obstacles into widget defined as parameter
        :return:
        """
        for rock_obj in self.get_obstacle_list():
            rock_obj.size = (Window.size[0] * FRACTION_SCREEN_SIZE * 0.4, Window.size[1] * FRACTION_SCREEN_SIZE)
            rock_obj.pos = (Window.size[0] * rock_obj.offset_x, Window.size[1] * rock_obj.offset_y)
            destination_widget.add_widget(rock_obj)

    def collision_check(self, rocket_obj):
        """
        Empty method for checking collision with these background rocks
        :param rocket_obj:
        :return:
        """
        pass
