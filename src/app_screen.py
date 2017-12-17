__author__ = 'brouk'

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
import random
from src.game import Game
from sprite import Sprite
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


SPEED_SLOW = 7
SPEED_MEDIUM = 13
SPEED_FAST = 17

MUSIC_VOLUME = 0.05     # Headphones
#MUSIC_VOLUME = 0.5     # Android device


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

        # Configuration screen
        self.configuration_b = None
        self.configuration_l = None
        self.sound_on_b = None
        self.sound_off_b = None
        self.sound_checked = None
        self.speed_l = None
        self.speed_slow_b = None
        self.speed_medium_b = None
        self.speed_fast_b = None
        self.speed_checked = None

        self.game = None

        self.persis = level_persistance.Persistence()
        self.max_active_level = self.persis.read_level()

        #self.sound = False
        self.sound = self.persis.read_sound()
        self.speed = self.persis.read_speed()

        self.menu_music_list = self.__get_menu_music()

        self.click = SoundLoader.load('sound/click_1.wav')
        self.click.seek(0.4)
        self.click.volume = MUSIC_VOLUME

        self.click_configuration = SoundLoader.load('sound/click_2.wav')
        self.click_configuration.volume = MUSIC_VOLUME

        self.__activate_menu(None)

    def __activate_menu(self, event):
        """
        Initialize menu view and activate menu screen
        :return:
        """
        self.play_click_button()
        self.clear_widgets()
        #self.__play_all_functional()

        self.play_menu_music_list()

        self.bckg_image = get_background(picture_path='pictures/background_bigger.png')
        self.add_widget(self.bckg_image)

        # Galaxyrun Label
        self.galaxy_run_l = Label(text='[b]GALAXY RUN[/b]', markup=True)
        self.galaxy_run_l.font_size = 62
        self.galaxy_run_l.bold = True
        self.galaxy_run_l.color = [0.8, 0.8, 0.8, 0.5]
        self.galaxy_run_l.pos_hint = {'x': .0, 'y': .4}
        self.add_widget(self.galaxy_run_l)

        # New Game Button
        self.play_b = Button(text='New game', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .65})
        self.play_b.bind(on_press=self.activate_new_game)  # Add functionality to 'play button'
        self.add_widget(self.play_b)

        # Individual Levels Button
        self.levels_b = Button(text='Levels', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .47})
        self.levels_b.bind(on_press=self.activate_levels)  # Add functionality to 'Levels button'
        self.add_widget(self.levels_b)

        # Configuration Button
        self.configuration_b = Button(text='Configuration', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .28})
        self.configuration_b.bind(on_press=self.activate_configuratin_window)  # Add functionality to 'Levels button'
        self.add_widget(self.configuration_b)

        # Exit Button
        self.exit_b = Button(text='Exit', font_size=22, size_hint=(.2, .1), pos_hint={'x': .4, 'y': .1})
        self.exit_b.bind(on_press=self.exit_game)  # Add functionality to 'Exit button'
        self.add_widget(self.exit_b)

    def activate_new_game(self, event):
        """
        Activate game screen on touch New Game button
        :return:
        """
        self.play_click_button()
        self.stop_playing_menu_music_list()
        self.clear_widgets()
        self.game = Game(self)
        self.game.size = self.size
        self.add_widget(self.game)
        self.game.run_game(game_level=1, play_sound=self.sound, speed=self.speed)

    def activate_level_2_game(self, event):
        """
        Activate Game for Level 2
        :param event:
        :return:
        """
        self.play_click_button()
        self.stop_playing_menu_music_list()
        self.clear_widgets()
        self.game = Game(self)
        self.game.size = self.size
        self.add_widget(self.game)
        self.game.run_game(game_level=2, play_sound=self.sound, speed=self.speed)

    def activate_levels(self, event):
        """
        Activate Levels game screen on touch Levels button
        :return:
        """
        self.play_click_button()
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

    def activate_configuratin_window(self, event):
        """
        Activate configuration window
        configure: sound ON/Off, Speed: Slow, Medium, Fast
        :return:
        """
        self.play_click_button()
        self.clear_widgets()

        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        # Levels label
        self.configuration_l = Label(text='[b]CONFIGURATION[/b]', markup=True)
        self.configuration_l.font_size = 62
        self.configuration_l.bold = True
        self.configuration_l.color = [0.8, 0.8, 0.8, 0.5]
        self.configuration_l.pos_hint = {'x': .0, 'y': .3}
        self.add_widget(self.configuration_l)

        # Sound ON/OFF label
        self.sound_l = Label(text='[b]Sound[/b]', markup=True)
        self.sound_l.font_size = 47
        self.sound_l.bold = False
        self.sound_l.color = [0.8, 0.8, 0.8, 0.5]
        self.sound_l.pos_hint = {'x': -0.3, 'y': .15}
        self.add_widget(self.sound_l)

        # Sound ON button
        self.sound_on_b = Button(text='On', font_size=22, size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.45})
        self.sound_on_b.bind(on_press=self.__set_sound_on)
        self.add_widget(self.sound_on_b)

        # Sound OFF button
        self.sound_off_b = Button(text='Off', font_size=22, size_hint=(.1, .1), pos_hint={'x': 0.25, 'y': 0.45})
        self.sound_off_b.bind(on_press=self.__set_sound_off)
        self.add_widget(self.sound_off_b)

        # Sound checked icon
        self.sound_checked = Sprite(picture='pictures/checked.png', allow_stretch=True, allow_keep_ratio=True)
        if self.sound:
            self.sound_checked.pos_hint = {'x': 0.05, 'y': 0.33}
        else:
            self.sound_checked.pos_hint = {'x': 0.25, 'y': 0.33}
        self.sound_checked.size_hint = (0.09, 0.09)
        self.add_widget(self.sound_checked)

        # Speed SLOW/MEDIUM/FAST
        self.speed_l = Label(text='[b]Speed[/b]', markup=True)
        self.speed_l.font_size = 47
        self.speed_l.bold = False
        self.speed_l.color = [0.8, 0.8, 0.8, 0.5]
        self.speed_l.pos_hint = {'x': 0.2, 'y': .15}
        self.add_widget(self.speed_l)

        # Speed SLOW button
        self.speed_slow_b = Button(text='Slow', font_size=22, size_hint=(.1, .1), pos_hint={'x': 0.55, 'y': 0.45})
        self.speed_slow_b.bind(on_press=self.__set_speed_slow)
        self.add_widget(self.speed_slow_b)

        # Speed MEDIUM button
        self.speed_medium_b = Button(text='Medium', font_size=22, size_hint=(.1, .1), pos_hint={'x': 0.7, 'y': 0.45})
        self.speed_medium_b.bind(on_press=self.__set_speed_medium)
        self.add_widget(self.speed_medium_b)

        # Speed FAST button
        self.speed_fast_b = Button(text='Fast', font_size=22, size_hint=(.1, .1), pos_hint={'x': 0.85, 'y': 0.45})
        self.speed_fast_b.bind(on_press=self.__set_speed_fast)
        self.add_widget(self.speed_fast_b)

        # Speed checked icon
        self.speed_checked = Sprite(picture='pictures/checked.png', allow_stretch=True, allow_keep_ratio=True)
        if self.speed == SPEED_SLOW:
            self.speed_checked.pos_hint = {'x': 0.55, 'y': 0.33}
        elif self.speed == SPEED_MEDIUM:
            self.speed_checked.pos_hint = {'x': 0.7, 'y': 0.33}
        elif self.speed == SPEED_FAST:
            self.speed_checked.pos_hint = {'x': 0.85, 'y': 0.33}
        else:
            self.speed = SPEED_MEDIUM       # MEDIUM speed as default
        self.speed_checked.size_hint = (0.09, 0.09)
        self.add_widget(self.speed_checked)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=22, size_hint=(.15, .15), pos_hint={'x': .4, 'y': .1})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def exit_game(self, event):
        """
        Exit Game
        :param event:
        :return:
        """
        self.play_click_button()
        Clock.schedule_once(App.get_running_app().stop, 0.8)

    def get_game_over_menu_items(self, level=1):
        """
        Game over menu items - Play again X Main menu
        :return:
        """
        self.play_menu_music_list()
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
        activate_the_same_level_function = self.__get_level_function(level)
        self.play_again_b.bind(on_press=activate_the_same_level_function)
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
        self.play_menu_music_list()
        self.clear_widgets()

        # Save new level into persistent layer and read it back into actual variable
        new_level = level + 1

        if new_level > self.max_active_level:
            self.persis.write_level(new_level)
            self.max_active_level = self.persis.read_level()
            #print "--- NEW LEVEL SAVED ANd READ AGAIN: {0}".format(self.max_active_level)

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
        start_next_level_function = self.__get_level_function(new_level)
        self.new_level_b.bind(on_press=start_next_level_function)
        self.add_widget(self.new_level_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=22, size_hint=(.15, .15), pos_hint={'x': .6, 'y': .2})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def __play_all_functional(self):
        functional_mp3 = SoundLoader.load('sound/function.mp3')
        functional_mp3.volume = MUSIC_VOLUME       # PC headphones volume level
        if self.sound and functional_mp3:
            functional_mp3.play()

    def __set_sound_on(self, event):
        """
        Activate sound
        :param event:
        :return:
        """
        self.sound = True
        self.play_configuration_click_button()
        self.sound_checked.pos_hint = {'x': 0.05, 'y': 0.33}
        self.__play_all_functional()
        self.play_menu_music_list()
        self.persis.write_sound(self.sound)

    def __set_sound_off(self, event):
        """
        Deactivate sound
        :param event:
        :return:
        """
        self.play_configuration_click_button()
        self.sound = False
        self.sound_checked.pos_hint = {'x': 0.25, 'y': 0.33}
        self.stop_playing_menu_music_list()
        self.persis.write_sound(self.sound)

    def __set_speed_slow(self, event):
        """
        Set slow speed via configuration
        :param event:
        :return:
        """
        self.play_configuration_click_button()
        self.speed = SPEED_SLOW
        self.speed_checked.pos_hint = {'x': 0.55, 'y': 0.33}
        self.persis.write_speed(SPEED_SLOW)

    def __set_speed_medium(self, event):
        """
        Set medium speed via configuration
        :return:
        """
        self.play_configuration_click_button()
        self.speed = SPEED_MEDIUM
        self.speed_checked.pos_hint = {'x': 0.7, 'y': 0.33}
        self.persis.write_speed(SPEED_MEDIUM)

    def __set_speed_fast(self, event):
        """
        Set fast speed via configuration
        :param event:
        :return:
        """
        self.play_configuration_click_button()
        self.speed = SPEED_FAST
        self.speed_checked.pos_hint = {'x': 0.85, 'y': 0.33}
        self.persis.write_speed(SPEED_FAST)

    def __get_level_function(self, new_level):
        if new_level == 1:
            return self.activate_new_game
        elif new_level == 2:
            return self.activate_level_2_game
        else:
            return self.activate_new_game

    def play_click_button(self):
        if self.sound:
            self.click.play()

    def play_configuration_click_button(self):
        if self.sound:
            self.click_configuration.play()

    def __get_menu_music(self):
        music_1 = SoundLoader.load('sound/menu_1.mp3')
        music_1.volume = MUSIC_VOLUME
        music_1.loop = True
        music_2 = SoundLoader.load('sound/menu_2.mp3')
        music_2.volume = MUSIC_VOLUME
        music_2.loop = True
        music_3 = SoundLoader.load('sound/menu_3.mp3')
        music_3.volume = MUSIC_VOLUME
        music_3.loop = True
        return [music_1, music_2, music_3]

    def play_menu_music_list(self):
        menu_music = random.choice(self.menu_music_list)
        print menu_music
        menu_music.play()

    def stop_playing_menu_music_list(self):
        for music in self.menu_music_list:
            if music.state == 'play':
                music.stop()
