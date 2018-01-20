#!/usr/bin/env python2
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'resizable', '0')

__author__ = 'brouk'

from kivy.app import App

from src.app_screen import AppScreen

# TODO:
# 32) PUSH it to Android market ... as Galaxyrun-Demo


class GameApp(App):
    def build(self):
        # game = Game()
        # return game
        appScreen = AppScreen()
        return appScreen

    def on_pause(self):
        """
        Pause App to be able to resume back to it after sending an email
        :return:
        """
        return True

    def on_resume(self):
        """
        Comming back to the same state of App after sending an email
        :return:
        """
        pass

if __name__ == "__main__":
    GameApp().run()
