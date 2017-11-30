__author__ = 'brouk'

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window
from src.game import Game
import level_persistance
from kivy.core.audio import SoundLoader


def get_background(picture_path='pictures/background_bigger.png'):
    """
    Set and return full screen Image background
    :return:
    """
    bckg_image = Image(source=picture_path)
    bckg_image.allow_stretch = True
    bckg_image.size = Window.size
    return bckg_image


class AppScreen(FloatLayout):
    """
    Main screen window for whole app
    - includes all menus and main game as well
    - it's based on Layout to make game full screen
    """
    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)
        self.galaxy_run_l = None
        self.play_b = None
        self.exit_b = None
        self.levels_b = None
        self.levels_l = None
        self.level_1_b = None
        self.level_2_b = None
        self.level_3_b = None
        self.main_menu_b = None
        self.play_again_b = None
        self.menu_background = None
        self.game = None

        self.persis = level_persistance.Persistence()
        self.max_active_level = self.persis.read_level()

        self.sound = True
        self.music = SoundLoader.load('sound/2001_Space_Odyssey_big.mp3')
        self.music.volume = 0.05
        self.music.loop = True

        self.__activate_menu(None)

    def __activate_menu(self, event):
        """
        Initialize menu view and activate menu screen
        :return:
        """
        self.clear_widgets()

        self.__play_all_functional()

        if self.sound:
            self.music.play()

        self.bckg_image = get_background(picture_path='pictures/background_bigger.png')
        self.add_widget(self.bckg_image)

        # Galaxyrun Label
        self.galaxy_run_l = Label(text='[b]GALAXY RUN[/b]', markup=True)
        self.galaxy_run_l.font_size = 46
        self.galaxy_run_l.bold = True
        self.galaxy_run_l.color = [0.1, 0.1, 0.1, 0.5]
        self.galaxy_run_l.pos_hint = {'x': .0, 'y': .3}
        self.add_widget(self.galaxy_run_l)

        # New Game Button
        self.play_b = Button(text='New game', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .5})
        self.play_b.bind(on_press=self.activate_new_game)  # Add functionality to 'play button'
        self.add_widget(self.play_b)

        # Individual Levels Button
        self.levels_b = Button(text='Levels', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .3})
        self.levels_b.bind(on_press=self.activate_levels)  # Add functionality to 'Levels button'
        self.add_widget(self.levels_b)

        # Exit Button
        self.exit_b = Button(text='Exit', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .1})
        self.exit_b.bind(on_press=self.exit_game)  # Add functionality to 'Exit button'
        self.add_widget(self.exit_b)

    def activate_new_game(self, event):
        """
        Activate game screen on touch New Game button
        :return:
        """
        self.clear_widgets()
        self.game = Game(self)
        self.game.size = self.size
        self.add_widget(self.game)
        self.game.run_game(game_level=1, play_sound=True)

    def activate_level_2_game(self, event):
        """
        Activate Game for Level 2
        :param event:
        :return:
        """
        self.clear_widgets()
        self.game = Game(self)
        self.game.size = self.size
        self.add_widget(self.game)
        self.game.run_game(game_level=2, play_sound=True)

    def activate_levels(self, event):
        """
        Activate Levels game screen on touch Levels button
        :return:
        """
        self.clear_widgets()

        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        # Levels label
        self.levels_l = Label(text='[b]LEVELS[/b]', markup=True)
        self.levels_l.font_size = 46
        self.levels_l.bold = True
        self.levels_l.color = [0.1, 0.1, 0.1, 0.5]
        self.levels_l.pos_hint = {'x': .0, 'y': .3}
        self.add_widget(self.levels_l)

        # Level Buttons (levels 1, 2, 3 - active or not active)
        # todo: Icons for individual levels ... 1, 2, 3
        self.level_1_b = Button(text='1st Level', font_size=22, size_hint=(.15, .15), pos_hint={'x': .2, 'y': .5})
        self.level_1_b.bind(on_press=self.activate_new_game)
        self.add_widget(self.level_1_b)

        self.level_2_b = Button(text='2nd Level', font_size=22, size_hint=(.15, .15), pos_hint={'x': .4, 'y': .5})
        self.level_2_b.bind(on_press=self.activate_level_2_game)
        if self.max_active_level < 2:
            self.level_2_b.disabled = True
        self.add_widget(self.level_2_b)

        self.level_3_b = Button(text='3rd Level', font_size=22, size_hint=(.15, .15), pos_hint={'x': .6, 'y': .5})
        #self.level_2_b.bind(on_press=self.activate_new_game())
        if self.max_active_level < 3:
            self.level_3_b.disabled = True
        self.add_widget(self.level_3_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=22, size_hint=(.15, .15), pos_hint={'x': .4, 'y': .2})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def exit_game(self, event):
        """
        Exit Game
        :param event:
        :return:
        """
        App.get_running_app().stop()

    def get_game_over_menu_items(self):
        """
        Game over menu items - Play again X Main menu
        :return:
        """
        self.clear_widgets()

        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        self.game_over_l = Label(text='[b]GAME OVER[/b]', markup=True)
        self.game_over_l.font_size = 46
        self.game_over_l.bold = True
        self.game_over_l.color = [0.7, 0.7, 0.7, 0.2]
        self.game_over_l.pos_hint = {'x': .0, 'y': 0.1}
        self.add_widget(self.game_over_l)

        # Play again button
        self.play_again_b = Button(text='Play again', font_size=22, size_hint=(.15, .15), pos_hint={'x': .2, 'y': .3})
        self.play_again_b.bind(on_press=self.activate_new_game)
        self.add_widget(self.play_again_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=22, size_hint=(.15, .15), pos_hint={'x': .6, 'y': .3})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def level_finnish_screen(self, level=1):
        """
        Level successful screen
        :return:
        """
        self.clear_widgets()

        # Save new level into persistent layer and read it back into actual variable
        new_level = level + 1

        if new_level > self.max_active_level:
            self.persis.write_level(new_level)
            self.max_active_level = self.persis.read_level()
            print "--- NEW LEVEL SAVED ANd READ AGAIN: {0}".format(self.max_active_level)

        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        message_finnish = '[b]LEVEL  ' + str(level) + '  COMPLETED[/b]'
        self.level_completed_l = Label(text=message_finnish, markup=True)
        self.level_completed_l.font_size = 46
        self.level_completed_l.bold = True
        self.level_completed_l.color = [0.7, 0.7, 0.7, 0.2]
        self.level_completed_l.pos_hint = {'x': 0.0, 'y': 0.3}
        self.add_widget(self.level_completed_l)

        message_activated = "".join(['[b]Level ', str(new_level), ' activated[/b]'])
        self.level_activated_l = Label(text=message_activated, markup=True)
        self.level_activated_l.font_size = 46
        self.level_activated_l.bold = True
        self.level_activated_l.color = [0.7, 0.7, 0.7, 0.2]
        self.level_activated_l.pos_hint = {'x': 0.0, 'y': 0.0}
        self.add_widget(self.level_activated_l)

        # Play New level button
        button_label = "".join(['Play Level ', str(new_level)])
        self.new_level_b = Button(text=button_label, font_size=22, size_hint=(.20, .15), pos_hint={'x': .2, 'y': .2})
        # todo:  Add proper function here ...
        #self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.new_level_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=22, size_hint=(.15, .15), pos_hint={'x': .6, 'y': .2})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def __play_all_functional(self):
        functional_mp3 = SoundLoader.load('sound/function.mp3')
        functional_mp3.volume = 0.05
        if self.sound and functional_mp3:
            functional_mp3.play()
