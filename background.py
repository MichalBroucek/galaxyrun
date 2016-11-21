__author__ = 'brouk'

from sprite import Sprite


class Background(Sprite):
    """
    Moving background
    """
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source=source, y=self.height)
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.y -= 1
        self.image_dupe.y -= 1

        if self.image.top <= 0:
            self.image.y = 0
            self.image_dupe.y = self.height
