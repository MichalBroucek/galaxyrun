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
# DONE 7) Make speed parametrized - the same speed for different displays !!!
# DONE 8) Make option to chose different speed ! slow, medium, fast ! - but all will be reasonable fast :-)
# DONE 9) Add 2nd level !
# CANCEL -  just 2 levels - 10) Add 3rd level !
# DONE 11) Add music and sound effects !
# DONE 12) Add configuration MENU
# DONE 13) Test user flow -> and un-bug it (game over for 2nd level -> play again 2nd level) !
# DONE 14) Make configuration persistent !
# DONE 15) Add more meteorites on background for level 2
# 15) Make more testing (different devices - optimize collisions - change music to free music ... )
# 16) Test speed values
# 16) Donate button (probably not possible ...) - free and pay version ? - 3rd level ? - longer levels ?
#       # OR at minimum add contact form ... :-)
# DONE 17) Use free music ! - almost done - just check it and commit ...
# DONE 17) Make LABEL and MENUs consistent


class GameApp(App):
    def build(self):
        # game = Game()
        # return game
        appScreen = AppScreen()
        return appScreen

if __name__ == "__main__":
    GameApp().run()
