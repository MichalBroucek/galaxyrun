__author__ = 'brouk'

from kivy.uix.image import Image
from kivy.core.window import Window

class Sprite(Image):
    def __init__(self, picture, allow_stretch=False, allow_keep_ratio=False):
        super(Sprite, self).__init__(source=picture)
        if allow_keep_ratio:
            #todo: Maybe better solution ?
            self.keep_ratio = True
        else:
            self.keep_ratio = False

        if allow_stretch:
            self.allow_stretch = True
            self.size = Window.size

