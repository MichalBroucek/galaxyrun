#!/usr/bin/env python2
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'resizable', '0')

__author__ = 'brouk'

from kivy.app import App

from src.app_screen import AppScreen


# TODO:
# 0) Re-write unittests !!!
# DONE # 1) Add 'Game over' screen
# DONE # 2) Add '1st level done' - screen -
    # DONE # 2.1) Create nice new background for last 2 screens
    # DONE # 2.1) Add missing rocket efect for last screen (make it smaller ? or fly away ?)
    # DONE # 2.2) Add level successfully finnished screen
# DONE 3) Issue about screens - menu screen is not fullscreen on mobile HW device
# DONE # 5) Check persistence (for levels) - it it's working ?
# DONE # 6) Improve collision detection !!!
# 7) Make speed parametrized - the same speed for different displays !!!
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
    GameApp().run()
