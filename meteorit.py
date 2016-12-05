__author__ = 'brouk'

from sprite import Sprite


def print_coordinates(name, widget):
    print "{0}.x={1}".format(name, widget.x)
    print "{0}.right={1}".format(name, widget.right)
    print "{0}.y={1}".format(name, widget.y)
    print "{0}.top={1}".format(name, widget.top)


class Meteorit(Sprite):
    """
    Rocket
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
        bottom_bottom = self.y + 15
        bottom_top = self.y + 65
        bottom_x = self.x + 85
        bottom_right = self.right - 110

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
        middle_bottom = self.y + 66     # 1 px bigger than bottom_top
        middle_top = self.y + 153
        middle_x = self.x + 25
        middle_right = self.right - 30

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
        top_bottom = self.y + 154
        top_top = self.y + 183
        top_x = self.x + 55
        top_right = self.right - 50

        if top_bottom <= wid.top and wid.y <= top_top:
            if top_right >= wid.x and top_x <= wid.right:
                return True

        return False
