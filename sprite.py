__author__ = 'brouk'

from kivy.uix.image import Image
from kivy.core.window import Window

class Sprite(Image):
    def __init__(self, allow_stretch=False, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        #self.size = self.texture_size
        if allow_stretch:
            self.allow_stretch = True
            self.size = Window.size

