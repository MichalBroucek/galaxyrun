__author__ = 'brouk'

from obstacle import Obstacle

# Note: Meteorite size is dynamic now and depends on screen size ! - abs. value needs to be parametrized

FRACTION_SCREEN_SIZE = 1.0 / 5.0  # 1/3 of the actual game screen

def print_coordinates(name, widget):
    print "{0}.x={1}".format(name, widget.x)
    print "{0}.right={1}".format(name, widget.right)
    print "{0}.y={1}".format(name, widget.y)
    print "{0}.top={1}".format(name, widget.top)


class Rock(Obstacle):
    """
    Rock which can fly throw screen and collide with Rocket object
    """

    def __init__(self, source, offset_position):
        super(Rock, self).__init__(picture_src=source, offset_position=offset_position, allow_stretch=True, allow_keep_ratio=False)
        self.speed = 2

    def update(self):
        """
        Update rock possition on the screen so it falls down throw screen
        """
        self.center_y -= self.speed

    def collide(self, wid):
        """
        Check if rock collide with another widget wid
        """
        print "not collide"
        if self.y < wid.top and self.top > wid.y:        # Y values are in collision
            if wid.right >= self.x and wid.x <= self.right:
                print "collide"
                return True

        return False
