__author__ = 'brouk'

from sprite import Sprite
from kivy.core.window import Window
from kivy.uix.image import Image


class Background(Sprite):
    """
    Moving background
    """
    def __init__(self, source):
        super(Background, self).__init__()

        self.image = Sprite(source=source)
        # todo: try to do it just with Image ... what purpouse is for Sprite here ?
        #self.image = Image(source='pictures/background_02_800_450.png')
        self.image.allow_stretch = True
        self.image.size = Window.size
        self.add_widget(self.image)

        self.image_dupe = Sprite(source=source, y=self.image.height)      # Orig.
        #self.image_dupe = Image(source='pictures/background_02_800_450.png', y=self.image.height)
        self.image_dupe.allow_stretch = True
        self.image_dupe.size = Window.size
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.y -= 2
        self.image_dupe.y -= 2

        if self.image.top <= 0:
            self.image.y = 0
            self.image_dupe.y = self.image.height
