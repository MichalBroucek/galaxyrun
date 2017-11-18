__author__ = 'brouk'

# import rock
from obstacles import Obstacles
from kivy.core.window import Window

FRACTION_SCREEN_SIZE = 1.0 / 5.0  # 1/3 of the actual game screen

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


class Rocks(Obstacles):
    """
    Generate list of Rocks for level 2
    """

    def __init__(self):
        super(Rocks, self).__init__(picture_src='pictures/square_3.png', speed=2, offset_positions=INITIAL_POS_OFFSETS,
                                    allow_stretch=True, allow_keep_ratio=False)

    def add_all_to_widget(self, destination_widget):
        """
        Add all obstacles into widget defined as parameter
        :return:
        """
        for rock_obj in self.get_obstacle_list():
            rock_obj.size = (Window.size[0] * FRACTION_SCREEN_SIZE * 0.4, Window.size[1] * FRACTION_SCREEN_SIZE)
            rock_obj.pos = (Window.size[0] * rock_obj.offset_x, Window.size[1] * rock_obj.offset_y)
            destination_widget.add_widget(rock_obj)
