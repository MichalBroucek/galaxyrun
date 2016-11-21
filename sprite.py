__author__ = 'brouk'

from kivy.uix.image import Image


class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size
