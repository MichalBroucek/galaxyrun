#!/usr/bin/env python2
from kivy.config import Config

__author__ = 'brouk'

from kivy.app import App
from kivy.core.window import Window

from src.app_screen import AppScreen


# TODO:
# 0) Add more unittests !!!
# 1) Add 'Game over' screen
# 2) Add '1st level done' - screen -
# 5) Check persistence (for levels) - it it's working ?


class GameApp(App):
    def build(self):
        # game = Game()
        # return game
        appScreen = AppScreen()
        return appScreen

if __name__ == "__main__":
    Window.fullscreen = 'auto'
    Config.set('graphics', 'fullscreen', 'auto')
    print 'Window size: {0}'.format(Window.size)
    GameApp().run()
