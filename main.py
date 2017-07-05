#!/usr/bin/env python2
__author__ = 'brouk'

from kivy.app import App
from kivy.core.window import Window

from game import Game

# TODO:
# 0) Add unittests !!!
# 0.5) Refactor - create src folder and clean code and design for further maintenance !
# 1) Add 'Game over'
# 2) Add '1st level done'
# 3) Add game menu
# 4) Add saving progress ? - just open new levels


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == "__main__":
    GameApp().run()
