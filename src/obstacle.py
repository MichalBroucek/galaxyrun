__author__ = 'brouk'

from sprite import Sprite


class Obstacle(Sprite):
    """
    General obstacle as base class for other individual obstacle (Meteorite, Rock, ...
    """

    def __init__(self, picture_src, obst_speed, offset_position, allow_stretch=True, allow_keep_ratio=False):
        super(Obstacle, self).__init__(picture=picture_src, allow_stretch=allow_stretch,
                                       allow_keep_ratio=allow_keep_ratio)
        self.offset_x, self.offset_y = offset_position
        self.speed = obst_speed

    def update(self):
        """
        Update obstacle position for falling down the screen
        """
        self.center_y -= self.speed

    def collide(self, wid):
        """
        Check if Obstacle collide with another widget 'wid'
        """
        if self.y < wid.top and self.top > wid.y:  # Y values are in collision
            if wid.right >= self.x and wid.x <= self.right:
                return True

        return False
