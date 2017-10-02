#!/usr/bin/env python2
from kivy.config import Config

__author__ = 'brouk'

from kivy.app import App
from kivy.core.window import Window

from src.game import Game
from src.app_screen import AppScreen


# TODO:
# 0) Add more unittests !!!
# 0.7) Refactor - Create "game screens" ... intro, menu, game_running, game over ? and refactor src
#           New class for all for menus in separate src file and keep game.py for running game ?
#           Don't over-complicate this ! it's just POC !
# 1) Change 'Game over' screen
# 2) Add '1st level done' - screen -
# 5) Check persistence (for levels) - it it's working ?

#global_screen_size = None





class GameApp(App):
    def build(self):
        # game = Game()
        # return game
        appScreen = AppScreen()
        return appScreen

if __name__ == "__main__":
    #Window.size = (1024, 576)        # Size of the background picture
    Window.fullscreen = 'auto'
    Config.set('graphics', 'fullscreen', 'auto')
    print 'Window size: {0}'.format(Window.size)
    GameApp().run()
