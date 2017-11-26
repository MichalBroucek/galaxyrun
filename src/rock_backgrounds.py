__author__ = 'brouk'

# import rock
from obstacles import Obstacles
from kivy.core.window import Window
from rocks_edges import INITIAL_POS_OFFSETS_RIGHT_EDGES, INITIAL_POS_OFFSETS_LEFT_EDGES
from rocks_edges import FRACTION_SCREEN_SIZE


# FRACTION_SCREEN_SIZE = 1.0 / 1.5  # 1/3 of the actual game screen
TEST_LEFT_LIST = [
    [0.81, 0.9],
    [0.74, 1.05],
    [0.67, 1.2]
]

TEST_RIGHT_LIST = [
    [0.14, 0.9],
    [0.21, 1.05],
    [0.28, 1.2]
]


def generate_list_of_background_rocks_coordinates():
    """
    Generates list of x,y coordinates for rocks background - these are on the sides so collision with Rocket is not
    possible.
    :return:
    """
    return generate_list_of_left_side_coordinates() + generate_list_of_right_side_coordinates()


def generate_list_of_right_side_coordinates():
    """
    Generate List of right side coordinates to fulfil LEFT side of the screen with rocks
    :return:
    """
    right_rocks_bck_coordinates = []
    offset_x = 0.07

    for coordinates in INITIAL_POS_OFFSETS_RIGHT_EDGES:
    #for coordinates in TEST_LEFT_LIST:
        # Generate coordinates for rocks till rest of the screen on the right side
        rock_x, rock_y = coordinates

        while rock_x < 1:
            # Keep adding rocks on the same Y level till end of Window screen = 1
            rock_x += offset_x
            right_rocks_bck_coordinates.append([rock_x, rock_y])

    return right_rocks_bck_coordinates

def generate_list_of_left_side_coordinates():
    """
    Generate List of right side coordinates to fulfil LEFT side of the screen with rocks
    :return:
    """
    left_rocks_bck_coordinates = []
    offset_x = 0.07

    for coordinates in INITIAL_POS_OFFSETS_LEFT_EDGES:
    #for coordinates in TEST_RIGHT_LIST:
        # Generate coordinates for rocks till rest of the screen on the right side
        rock_x, rock_y = coordinates

        while rock_x > 0:
            # Keep adding rocks on the same Y level till end of Window screen = 1
            rock_x -= offset_x
            left_rocks_bck_coordinates.append([rock_x, rock_y])

    return left_rocks_bck_coordinates


# Initial [x_offset, y_offset] for individual meteorites
INITIAL_POS_OFFSETS = generate_list_of_background_rocks_coordinates()


class Rock_background(Obstacles):
    """
    Generate list of Rocks backgrounds and side rock for decoration of level 2
    """

    def __init__(self):
        super(Rock_background, self).__init__(picture_src='pictures/square_3.png', speed=5,
                                              offset_positions=INITIAL_POS_OFFSETS,
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

    def collision_check(self, rocket_obj):
        """
        Empty method for checking collision with these background rocks
        :param rocket_obj:
        :return:
        """
        pass
