__author__ = 'brouk'

from sprite import Sprite
from kivy.core.window import Window


class Background(Sprite):
    """
    Moving background
    """
    def __init__(self, picture):
        super(Background, self).__init__()

        self.image = Sprite(source=picture)
        self.image.allow_stretch = True
        self.image.size = Window.size
        self.add_widget(self.image)

        self.image_dupe = Sprite(source=picture, y=self.image.height)      # Orig.
        self.image_dupe.allow_stretch = True
        self.image_dupe.size = Window.size
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.y -= 2
        self.image_dupe.y -= 2

        if self.image.top <= 0:
            self.image.y = 0
            self.image_dupe.y = self.image.height
