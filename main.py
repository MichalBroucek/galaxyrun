#!/usr/bin/env python2
__author__ = 'brouk'

from kivy.app import App
from kivy.core.window import Window

from src.game import Game


# TODO:
# 0) Add more unittests !!!
# 0.7) Refactor - Create "game screens" ... intro, menu, game_running, game over ? and refactor src
#           New class for all for menus in separate src file and keep game.py for running game ?
#           Don't over-complicate this ! it's just POC !
# 1) Change 'Game over' screen
# 2) Add '1st level done' - screen -
# 5) Check persistence (for levels) - it it's working ?


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == "__main__":
    GameApp().run()
