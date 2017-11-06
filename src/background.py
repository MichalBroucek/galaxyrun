__author__ = 'brouk'

from sprite import Sprite
from kivy.core.window import Window
from kivy.uix.widget import Widget


class Background(Widget):
    """
    Moving background
    """
    def __init__(self, background_picture, last_background_image=None):
        super(Background, self).__init__()
        self.image = Sprite(picture=background_picture, allow_stretch=True)
        self.image_dupe = Sprite(picture=background_picture, allow_stretch=True)
        self.image_dupe.y = Window.height
        self.last_background = False
        self.last_image_str = last_background_image

    def update(self):
        self.image.y -= 2
        self.image_dupe.y -= 2

        # Set screens position so it can run again from beginning
        if self.image.top <= 0:
            self.image.y = 0
            self.image_dupe.y = Window.height

    def set_last_background(self):
        """
        Set final background screen for current level
        :return:
        """
        self.remove_widget(self.image_dupe)
        self.image_dupe = Sprite(picture=self.last_image_str, allow_stretch=True)
        self.add_widget(self.image_dupe)
        self.last_background = True
