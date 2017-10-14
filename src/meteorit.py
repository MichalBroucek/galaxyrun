__author__ = 'brouk'

from sprite import Sprite

# Note: Meteorite size is dynamic now and depends on screen size ! - abs. value needs to be parametrized

FRACTION_SCREEN_SIZE = 1.0 / 3.0  # 1/3 of the actual game screen


def print_coordinates(name, widget):
    print "{0}.x={1}".format(name, widget.x)
    print "{0}.right={1}".format(name, widget.right)
    print "{0}.y={1}".format(name, widget.y)
    print "{0}.top={1}".format(name, widget.top)


class Meteorit(Sprite):
    """
    Meteorite which can fly throw screen and collide with Rocket object
    """

    def __init__(self, source, offset_position):
        super(Meteorit, self).__init__(source=source, allow_stretch=True)
        self.offset_x, self.offset_y = offset_position
        # These are updated once Meteorites are added into screen (size of Meteorites is dynamic and so
        # collision coordinates)
        self.bottom_bottom, self.bottom_top, self.bottom_x, self.bottom_right = [0, 0, 0, 0]
        self.middle_bottom, self.middle_top, self.middle_x, self.middle_right = [0, 0, 0, 0]
        self.top_bottom, self.top_top, self.top_x, self.top_right = [0, 0, 0, 0]

    def update(self):
        #self.center_y -= 13
        self.center_y -= 5
        # TODO: check if meteorit is out of window and re-set Y coordinates if yes

    def collide_meteorit(self, wid):
        """
        Check if another widget collides with this meteorite.
        """
        # There are 3 different parts (on 'y' axis) with different 'x' and 'rights' where we detect collisions
        # 3 different rectangles for collision detection are used
        if self.__collide_with_bottom(wid):
            print "BOTTOM Collision ... Collision ... Collision ... Collision ..."
            return True
        # Detect collision than in middle part (middle rectangle)
        elif self.__collide_with_middle(wid):
            print "MIDDLE Collision ... Collision ... Collision ... Collision ..."
            return True
        # Detect collision in top part (top rectangle)
        if self.__collide_with_top(wid):
            print "TOP Collision ... Collision ... Collision ... Collision ..."
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
        # Has to be calculated here as it depends on meteorite position
        self.bottom_bottom, self.bottom_top, self.bottom_x, self.bottom_right = self.__get_bottom_borders()

        if self.bottom_bottom <= wid.top <= self.bottom_top:
            if wid.right >= self.bottom_x and wid.x <= self.bottom_right:
                return True

        return False

    def __collide_with_middle(self, wid):
        """
        Detect collision with middle part of meteorite
        :param wid: widget to collide with
        :return: True if collision happens
        """
        # Has to be calculated here as it depends on meteorite position
        self.middle_bottom, self.middle_top, self.middle_x, self.middle_right = self.__get_middle_borders()

        if self.middle_bottom <= wid.top <= self.middle_top:
            if self.middle_right >= wid.x and self.middle_x <= wid.right:
                return True

        return False

    def __collide_with_top(self, wid):
        """
        Detect collision with top part of meteorite
        :param wid:
        :return:
        """
        # Has to be calculated here as it depends on meteorite position
        self.top_bottom, self.top_top, self.top_x, self.top_right = self.__get_top_borders()

        if self.top_bottom <= wid.top and wid.y <= self.top_top:
            if self.top_right >= wid.x and self.top_x <= wid.right:
                return True

        return False

    def __get_bottom_borders(self):
        """
        Return borders for collision in bottom part
        There is overlap for crashing with meteorite
        :return:
        """
        COLLISION_BOTTOM_BOTTOM_OFFSET = 0.1    # (0.25) * size[1]
        COLLISION_BOTTOM_TOP_OFFSET = 0.35      # (0.65) * size[1]
        COLLISION_BOTTOM_LEFT_OFFSET = 0.4      # (0.4) * size[0]
        COLLISION_BOTTOM_RIGHT_OFFSET = 0.55     # (0.5) * size[0]

        bottom_bottom = self.y + (self.size[1] * COLLISION_BOTTOM_BOTTOM_OFFSET)
        bottom_top = self.y + (self.size[1] * COLLISION_BOTTOM_TOP_OFFSET)
        bottom_x = self.x + (self.size[0] * COLLISION_BOTTOM_LEFT_OFFSET)
        bottom_right = self.right - (self.size[0] * COLLISION_BOTTOM_RIGHT_OFFSET)

        return [bottom_bottom, bottom_top, bottom_x, bottom_right]

    def __get_middle_borders(self):
        """
        Return borders for collision in middle part
        There is overlap for crashing with meteorite
        :return:
        """
        COLLISION_MIDDLE_BOTTOM_OFFSET = 0.35
        COLLISION_MIDDLE_TOP_OFFSET = 0.75
        COLLISION_MIDDLE_LEFT_OFFSET = 0.33
        COLLISION_MIDDLE_RIGHT_OFFSET = 0.35

        middle_bottom = self.y + (self.size[1] * COLLISION_MIDDLE_BOTTOM_OFFSET)
        middle_top = self.y + (self.size[1] * COLLISION_MIDDLE_TOP_OFFSET)
        middle_x = self.x + (self.size[0] * COLLISION_MIDDLE_LEFT_OFFSET)
        middle_right = self.right - (self.size[0] * COLLISION_MIDDLE_RIGHT_OFFSET)

        return [middle_bottom, middle_top, middle_x, middle_right]

    def __get_top_borders(self):
        """
        Return borders for collision in top part
        There is overlap for crashing with meteorite
        :return:
        """
        COLLISION_TOP_BOTTOM_OFFSET = 0.75
        COLLISION_TOP_TOP_OFFSET = 0.9
        COLLISION_TOP_LEFT_OFFSET = 0.45
        COLLISION_TOP_RIGHT_OFFSET = 0.45

        top_bottom = self.y + (self.size[1] * COLLISION_TOP_BOTTOM_OFFSET)
        top_top = self.y + (self.size[1] * COLLISION_TOP_TOP_OFFSET)
        top_x = self.x + (self.size[0] * COLLISION_TOP_LEFT_OFFSET)
        top_right = self.right - (self.size[0] * COLLISION_TOP_RIGHT_OFFSET)

        return [top_bottom, top_top, top_x, top_right]
