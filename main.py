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
# 6) Improve collision detection !!!
# 7) Make speed parametrized - the same speed for different displays !
# 8) Make option to chose different speed ! slow, medium, fast ! - but all will be reasonable fast :-)
# 9) Add 2nd level !
# 10) Add 3rd level !
# 11) Add music and sound effects !


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
