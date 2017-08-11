#!/usr/bin/env python2
__author__ = 'brouk'

from kivy.app import App
from kivy.core.window import Window

from src.game import Game


# TODO:
# 0) Add more unittests !!!
# DONE 0.5) Refactor - create src folder and clean code and design for further maintenance !
# 0.7) Refactor - Create "game states" ... intro, menu, game_running, game over ? and refactor src
#           New class for all for menus in separate src file and keep game.py for running game ?
#           Don't over-complicate this ! it's just POC !
# 1) Add 'Game over' screen
# 2) Add '1st level done' - screen -
# DONE 3) Add game menu
# 5) Add all levels screen (with opened and closed levels) - need to write it into file (persistence) ?!


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == "__main__":
    GameApp().run()
