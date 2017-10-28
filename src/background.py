__author__ = 'brouk'

from sprite import Sprite
from kivy.core.window import Window


class Background(Sprite):
    """
    Moving background
    """
    def __init__(self, picture, last_background_image=None):
        super(Background, self).__init__()

        self.image = Sprite(source=picture)
        self.image.allow_stretch = True
        self.image.size = Window.size
        self.add_widget(self.image)

        self.image_dupe = Sprite(source=picture, y=self.image.height)
        self.image_dupe.allow_stretch = True
        self.image_dupe.size = Window.size
        self.add_widget(self.image_dupe)

        self.last_background = False
        self.last_image = last_background_image
        # self.last_image_2 = last_backgrounds[1]

    def update(self):
        self.image.y -= 2
        self.image_dupe.y -= 2

        if self.last_background:
            # Update second half of the last screen (when 1st half is going out of visible area)
            if self.image_dupe.y <= 0:
                self.__set_image(picture=self.last_image_2)

        # Set screens position so it can run again from beginning
        if self.image.top <= 0:
            self.image.y = 0
            self.image_dupe.y = self.image.height

    def __set_image(self, picture):
        """
        Set new background screen
        :param picture:
        :return:
        """
        self.remove_widget(self.image)
        orig_image_y = self.image.y
        self.image = Sprite(source=picture, y=orig_image_y)
        self.image.allow_stretch = True
        self.image.size = Window.size
        self.add_widget(self.image)
        self.last_background = True

    def __set_image_dupe(self, picture):
        """
        Setup image dupe to new image (for last screen of level)
        :param piscture:
        :return:
        """
        self.remove_widget(self.image_dupe)
        orig_image_y = self.image_dupe.y
        self.image_dupe = Sprite(source=picture, y=orig_image_y)
        self.image_dupe.allow_stretch = True
        self.image_dupe.size = Window.size
        self.add_widget(self.image_dupe)

    def set_last_background(self):
        """
        Set 1st half of final background screen for current level
        - set only 1st half first to prevent jumps on the screen actual visible screen
        :return:
        """
        self.__set_image_dupe(self.last_image)
        self.last_background = True

    # def set_last_background_2nd_half(self):
    #     """
    #     Set 2nd half of final background screen for current level
    #     - set 2nd half first to prevent jumps on the screen actual visible screen
    #     :return:
    #     """
    #     self.__set_image(self.last_image_2)
