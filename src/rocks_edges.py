__author__ = 'brouk'

# import rock
from obstacles import Obstacles
from kivy.core.window import Window

FRACTION_SCREEN_SIZE = 1.0 / 5.0  # 1/3 of the actual game screen

# Initial [x_offset, y_offset] for individual rock edges on the LEFT side
# Coordinates numbers are fraction of screen size - coordinates numbers: [a, b] means:
    # x_coordinate = screen_width * a
    # y_coordinate = screen_height * b
    # y_shift = 0.15
    # x_shift = 0.07
INITIAL_POS_OFFSETS_LEFT_EDGES = [
    [0.0, 0.6],
    [0.07, 0.75],
    [0.14, 0.9],
    [0.21, 1.05],
    [0.28, 1.2],

    [0.28, 1.35],
    [0.28, 1.5],
    [0.28, 1.65],

    [0.35, 1.8],
    [0.35, 1.95],
    [0.28, 2.1],

    [0.21, 2.25],
    [0.14, 2.4],
    [0.07, 2.55],
    [0.0, 2.7],
    [0.0, 2.85],

    [0.07, 3.0],
    [0.14, 3.15],
    [0.21, 3.3],
    [0.28, 3.45],
    [0.35, 3.6],
    [0.42, 3.75],
    [0.49, 3.85],
    [0.56, 4],

    [0.49, 4.15],
    [0.42, 4.3],

    # LEFT BUT same Y level
    [0.35, 4.3],
    [0.28, 4.3],
    [0.21, 4.3],
    [0.14, 4.3],
    [0.07, 4.3],
    [0.0, 4.3],

    [0.0, 4.45],
    [0.0, 4.6],
    [0.0, 4.75],
    [0.0, 4.9],
    [0.07, 5.05],
    [0.07, 5.2],
    [0.07, 5.35],
    [0.14, 5.5],
    [0.21, 5.65],
    [0.21, 5.8],

    [0.28, 5.8],
    [0.35, 5.8],
    [0.42, 5.8],
    [0.49, 5.8],

    [0.49, 5.95],
    [0.49, 6.1],
    [0.49, 6.25],
    [0.49, 6.4]
]

# Initial [x_offset, y_offset] for individual rock edge on the RIGHT side
# Coordinates numbers are fraction of screen size - coordinates numbers: [a, b] means:
    # x_coordinate = screen_width * a
    # y_coordinate = screen_height * b
    # y_shift = 0.15
    # x_shift = 0.07
INITIAL_POS_OFFSETS_RIGHT_EDGES = [
    [0.95, 0.6],
    [0.88, 0.75],
    [0.81, 0.9],
    [0.74, 1.05],
    [0.67, 1.2],

    [0.67, 1.35],
    [0.67, 1.5],
    [0.67, 1.65],

    [0.6, 1.8],
    [0.6, 1.95],
    [0.67, 2.1],

    [0.6, 2.25],
    [0.53, 2.4],
    [0.46, 2.55],
    [0.39, 2.7],
    [0.39, 2.85],

    [0.46, 3.0],
    [0.53, 3.15],
    [0.6, 3.3],
    [0.67, 3.45],
    [0.74, 3.6],
    [0.81, 3.75],
    [0.88, 3.85],
    [0.95, 4],

    [0.88, 4.15],
    [0.88, 4.3],
    [0.88, 4.45],
    [0.88, 4.6],
    [0.81, 4.75],

    # The same Y level !
    [0.74, 4.9],
    [0.67, 4.9],
    [0.6, 4.9],
    [0.53, 4.9],
    [0.46, 4.9],
    [0.39, 4.9],
    [0.32, 4.9],

    [0.32, 5.05],
    [0.32, 5.2],
    [0.39, 5.35],

    [0.46, 5.35],
    [0.53, 5.35],
    [0.6, 5.35],
    [0.67, 5.35],
    [0.74, 5.35],

    [0.74, 5.5],
    [0.74, 5.65],
    [0.74, 5.8],
    [0.74, 5.95],
    [0.74, 6.1],
    [0.74, 6.25],
    [0.74, 6.4],
]

INITIAL_POS_OFFSETS = INITIAL_POS_OFFSETS_LEFT_EDGES + INITIAL_POS_OFFSETS_RIGHT_EDGES


class Rocks_edges(Obstacles):
    """
    Generate list of Rocks for level 2
    """

    def __init__(self):
        super(Rocks_edges, self).__init__(picture_src='pictures/square_3.png', speed=5, offset_positions=INITIAL_POS_OFFSETS,
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
