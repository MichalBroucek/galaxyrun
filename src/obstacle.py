__author__ = 'brouk'

from sprite import Sprite

# Note: Meteorite size is dynamic now and depends on screen size ! - abs. value needs to be parametrized
FRACTION_SCREEN_SIZE = 1.0 / 5.0  # 1/5 of the actual game screen as default value for


class Obstacle(Sprite):
    """
    General obstacle as base class for other individual obstacle (Meteorite, Rock, ...
    """

    def __init__(self, picture_src, offset_position, allow_stretch=True, allow_keep_ratio=False):
        super(Obstacle, self).__init__(picture=picture_src, allow_stretch=allow_stretch, allow_keep_ratio=allow_keep_ratio)
        self.offset_x, self.offset_y = offset_position
        self.speed = 4      # Default speed for obstacle

    def update(self):
        """
        Update obstacle possition for falling down the screen
        """
        self.center_y -= self.speed

    def collide(self, wid):
        """
        Check if Obstacle collide with another widget 'wid'
        """
        if self.y < wid.top and self.top > wid.y:        # Y values are in collision
            if wid.right >= self.x and wid.x <= self.right:
                return True

        return False
