#!/usr/bin/env python2
__author__ = 'brouk'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

from background import Background
from rocket import Rocket
from meteorites import Meteorites


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.background = Background(source='background_02_800_450.png')
        self.size = self.background.size
        self.add_widget(self.background)

        self.rocket = Rocket(pos=(self.width / 2, 10))
        self.rocket.pos = (self.background.size[0] / 2, self.size_hint_y + 60)
        self.add_widget(self.rocket)

        self.meteorites = Meteorites(self.center_x, self.center_y)
        for meteorite in self.meteorites.meteorites:
            self.add_widget(meteorite)

        self.active_collision = False

        Clock.schedule_interval(self.update, 1.0/60.0)

    def update(self, *ignore):

        self.rocket.update()

        if self.rocket.explossion_in_progress:
            return

        self.background.update()
        self.meteorites.update()

        for meteorite in self.meteorites.meteorites:
            if meteorite.collide_meteorit(self.rocket):
                self.active_collision = True

        if self.active_collision:
            #print "\t\t| Collision |"
            if not self.rocket.existing_collision:
                self.rocket.first_collision = True
                self.rocket.existing_collision = True
        else:
            self.rocket.first_collision = False
            self.rocket.existing_collision = False

        self.active_collision = False

    def on_touch_move(self, touch):
        if touch.y < self.height / 5:
            self.rocket.center_x = touch.x


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == "__main__":
    GameApp().run()
