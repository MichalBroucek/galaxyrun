__author__ = 'brouk'

from sprite import Sprite

# Note: Meteorite size is dynamic now and depends on screen size ! - abs. value needs to be parametrized

FRACTION_SCREEN_SIZE = 1.0 / 5.0  # 1/3 of the actual game screen

def print_coordinates(name, widget):
    print "{0}.x={1}".format(name, widget.x)
    print "{0}.right={1}".format(name, widget.right)
    print "{0}.y={1}".format(name, widget.y)
    print "{0}.top={1}".format(name, widget.top)


class Rock(Sprite):
    """
    Meteorite which can fly throw screen and collide with Rocket object
    """

    def __init__(self, source, offset_position):
        super(Rock, self).__init__(picture=source, allow_stretch=True, allow_keep_ratio=False)
        self.offset_x, self.offset_y = offset_position
        #self.speed = 10      # todo: change speed here according screen size ?
        self.speed = 2

    def update(self):
        self.center_y -= self.speed

    def collide_rock(self, wid):
        """
        Check if another widget collides with this meteorite.
        """
        if self.y < wid.top and self.top > wid.y:        # Y values are in collision
            if wid.right >= self.x and wid.x <= self.right:
                return True

        return False
