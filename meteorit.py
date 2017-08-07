__author__ = 'brouk'

from sprite import Sprite

COLLISION_BOTTOM_BOTTOM_OFFSET = 15
COLLISION_BOTTOM_TOP_OFFSET = 65
COLLISION_BOTTOM_LEFT_OFFSET = 85
COLLISION_BOTTOM_RIGHT_OFFSET = 110

COLLISION_MIDDLE_BOTTOM_OFFSET = 66
COLLISION_MIDDLE_TOP_OFFSET = 153
COLLISION_MIDDLE_LEFT_OFFSET = 25
COLLISION_MIDDLE_RIGHT_OFFSET = 30

COLLISION_TOP_BOTTOM_OFFSET = 154
COLLISION_TOP_TOP_OFFSET = 183
COLLISION_TOP_LEFT_OFFSET = 55
COLLISION_TOP_RIGHT_OFFSET = 50


def print_coordinates(name, widget):
    print "{0}.x={1}".format(name, widget.x)
    print "{0}.right={1}".format(name, widget.right)
    print "{0}.y={1}".format(name, widget.y)
    print "{0}.top={1}".format(name, widget.top)


class Meteorit(Sprite):
    """
    Meteorite which can fly throw screen and collide with Rocket object
    """
    def __init__(self, source, pos):
        super(Meteorit, self).__init__(source=source, pos=pos)

    def update(self):
        self.center_y -= 7
        # TODO: check if meteorit is out of window and re-set Y coordinates if yes

    def collide_meteorit(self, wid):
        """
        Check if another widget collides with this meteorite.
        """
        # There are 3 different parts (on 'y' axis) with different 'x' and 'rights' where we detect collisions
        # 3 different rectangles for collision detection are used
        if self.__collide_with_bottom(wid):
            #print "BOTTOM Collision ... Collision ... Collision ... Collision ..."
            return True
        # Detect collision than in middle part (middle rectangle)
        elif self.__collide_with_middle(wid):
            #print "MIDDLE Collision ... Collision ... Collision ... Collision ..."
            return True
        # Detect collision in top part (top rectangle)
        if self.__collide_with_top(wid):
            #print "TOP Collision ... Collision ... Collision ... Collision ..."
            return True

        return False

    def __get_x_percent(self, value):
        percent_value = value * self.x
        return percent_value

    def __get_y_percent(self, value):
        percent_value = value * self.y
        return percent_value

    def __collide_with_bottom(self, wid):
        """
        Detect collision with bottom part of meteorite
        :param wid: widget to collide with
        :return: True if collision happens
        """
        bottom_bottom = self.y + COLLISION_BOTTOM_BOTTOM_OFFSET
        bottom_top = self.y + COLLISION_BOTTOM_TOP_OFFSET
        bottom_x = self.x + COLLISION_BOTTOM_LEFT_OFFSET
        bottom_right = self.right - COLLISION_BOTTOM_RIGHT_OFFSET

        if bottom_bottom <= wid.top <= bottom_top:
            if bottom_right >= wid.x and bottom_x <= wid.right:
                return True

        return False

    def __collide_with_middle(self, wid):
        """
        Detect collision with middle part of meteorite
        :param wid: widget to collide with
        :return: True if collision happens
        """
        middle_bottom = self.y + COLLISION_MIDDLE_BOTTOM_OFFSET     # 1 px bigger than bottom_top
        middle_top = self.y + COLLISION_MIDDLE_TOP_OFFSET
        middle_x = self.x + COLLISION_MIDDLE_LEFT_OFFSET
        middle_right = self.right - COLLISION_MIDDLE_RIGHT_OFFSET

        if middle_bottom <= wid.top <= middle_top:
            if middle_right >= wid.x and middle_x <= wid.right:
                return True

        return False

    def __collide_with_top(self, wid):
        """
        Detect collision with top part of meteorite
        :param wid:
        :return:
        """
        top_bottom = self.y + COLLISION_TOP_BOTTOM_OFFSET
        top_top = self.y + COLLISION_TOP_TOP_OFFSET
        top_x = self.x + COLLISION_TOP_LEFT_OFFSET
        top_right = self.right - COLLISION_TOP_RIGHT_OFFSET

        if top_bottom <= wid.top and wid.y <= top_top:
            if top_right >= wid.x and top_x <= wid.right:
                return True

        return False
