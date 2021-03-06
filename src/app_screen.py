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
from kivy.utils import platform
from plyer import email

# TODO: check if this is necessary for Android build !!!
try:
    import os
    javapath = "/home/brouk/Android/Sdk/platforms/android-24/*"
    os.environ['CLASSPATH'] = javapath
    print 'CLASSPATH: ', os.environ['CLASSPATH']
except:
    print "!!! ERROR when setting Java CLASS_PATH !!!"

from jnius import autoclass


def get_background(picture_path='pictures/background_bigger.png'):
    """
    Set and return full screen Image background
    :return:
    """
    bckg_image = Image(source=picture_path)
    bckg_image.allow_stretch = True
    bckg_image.size = Window.size
    return bckg_image


SPEED_SLOW = 14
SPEED_MEDIUM = 20
SPEED_FAST = 26

# MUSIC_VOLUME = 0.05     # Headphones
MUSIC_VOLUME = 0.5        # Android device

FONT_SIZE_BUTTON = 28                   # OK - small screen
FONT_SIZE_HEADLINES = 61                # OK - small screen

SIZE_HINT_BUTTON_NORMAL = (.24, .1)     # OK - small screen
SIZE_HINT_BUTTON_LEVELS = (.20, .15)    # OK - small screen
SIZE_HINT_BUTTON_BIG = (.20, .15)       # OK - small screen
SIZE_HINT_BUTTON_SMALL = (.17, .1)      # OK - small screen
SIZE_HINT_BUTTON_CONF = (.13, .1)       # OK - small screen


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

        self.send_msg_b = None
        self.help_b = None
        self.text_msg_contain = None

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
        self.galaxy_run_l = Label(text='[b]GALAXY RUN demo[/b]', markup=True)
        self.galaxy_run_l.font_size = FONT_SIZE_HEADLINES
        self.galaxy_run_l.bold = True
        self.galaxy_run_l.color = [0.8, 0.8, 0.8, 0.5]
        self.galaxy_run_l.pos_hint = {'x': .0, 'y': .4}
        self.add_widget(self.galaxy_run_l)

        # New Game Button
        self.play_b = Button(text='New game', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_NORMAL,
                             pos_hint={'x': .4, 'y': .65})
        self.play_b.bind(on_press=self.activate_new_game)  # Add functionality to 'play button'
        self.add_widget(self.play_b)

        # Individual Levels Button
        self.levels_b = Button(text='Levels', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_NORMAL,
                               pos_hint={'x': .4, 'y': .47})
        self.levels_b.bind(on_press=self.activate_levels)  # Add functionality to 'Levels button'
        self.add_widget(self.levels_b)

        # Configuration Button
        self.configuration_b = Button(text='Configuration', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_NORMAL,
                                      pos_hint={'x': .4, 'y': .28})
        self.configuration_b.bind(on_press=self.activate_configuratin_window)  # Add functionality to 'Levels button'
        self.add_widget(self.configuration_b)

        # Send message button
        self.send_msg_b = Button(text='Send Msg', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_SMALL,
                                 pos_hint={'x': .8, 'y': .28})
        self.send_msg_b.bind(on_press=self.activate_send_msg)
        self.add_widget(self.send_msg_b)

        # Help button
        self.help_b = Button(text='Help', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_SMALL,
                             pos_hint={'x': .1, 'y': .28})
        self.help_b.bind(on_press=self.activate_help)
        self.add_widget(self.help_b)

        # Exit Button
        self.exit_b = Button(text='Exit', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_NORMAL,
                             pos_hint={'x': .4, 'y': .1})
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
        speed_for_level_2 = self.speed - 7
        self.game.run_game(game_level=2, play_sound=self.sound, speed=speed_for_level_2)

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
        self.levels_l.font_size = FONT_SIZE_HEADLINES
        self.levels_l.bold = True
        self.levels_l.color = [0.8, 0.8, 0.8, 0.5]
        self.levels_l.pos_hint = {'x': .0, 'y': .3}
        self.add_widget(self.levels_l)

        # Level Buttons (levels 1, 2, 3 - active or not active)
        # todo: Icons for individual levels ... 1, 2, 3
        self.level_1_b = Button(text='1st Level', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                pos_hint={'x': .2, 'y': .5})
        self.level_1_b.bind(on_press=self.activate_new_game)
        self.add_widget(self.level_1_b)

        self.level_2_b = Button(text='2nd Level', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                pos_hint={'x': .6, 'y': .5})
        self.level_2_b.bind(on_press=self.activate_level_2_game)
        if self.max_active_level < 2:
            self.level_2_b.disabled = True
        self.add_widget(self.level_2_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                  pos_hint={'x': .4, 'y': .2})
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
        self.configuration_l.font_size = FONT_SIZE_HEADLINES
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
        self.sound_on_b = Button(text='On', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_CONF,
                                 pos_hint={'x': 0.05, 'y': 0.45})
        self.sound_on_b.bind(on_press=self.__set_sound_on)
        self.add_widget(self.sound_on_b)

        # Sound OFF button
        self.sound_off_b = Button(text='Off', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_CONF,
                                  pos_hint={'x': 0.25, 'y': 0.45})
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
        self.speed_slow_b = Button(text='Slow', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_CONF,
                                   pos_hint={'x': 0.5, 'y': 0.45})
        self.speed_slow_b.bind(on_press=self.__set_speed_slow)
        self.add_widget(self.speed_slow_b)

        # Speed MEDIUM button
        self.speed_medium_b = Button(text='Medium', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_CONF,
                                     pos_hint={'x': 0.67, 'y': 0.45})
        self.speed_medium_b.bind(on_press=self.__set_speed_medium)
        self.add_widget(self.speed_medium_b)

        # Speed FAST button
        self.speed_fast_b = Button(text='Fast', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_CONF,
                                   pos_hint={'x': 0.84, 'y': 0.45})
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
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                  pos_hint={'x': .4, 'y': .1})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def activate_help(self, event):
        """
        Activate Help for game
        :return:
        """
        self.clear_widgets()

        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        # Levels label
        help_l = Label(text='[b]HELP[/b]', markup=True)
        help_l.font_size = FONT_SIZE_HEADLINES
        help_l.bold = True
        help_l.color = [0.8, 0.8, 0.8, 0.5]
        help_l.pos_hint = {'x': .0, 'y': .35}
        self.add_widget(help_l)

        # Help text
        text = \
        """
        [b]play game[/b]     - Goal of the game is to flight through galaxy without collision
                                 with another object
                               - Just touch the 'slider' in the bottom of the screen and move
                                 to the right or to the left side

        [b]speed[/b]          - In configuration screen you can choose among SLOW,
                                MEDIUM or FAST speed

        [b]sound[/b]          - In configuration screen you can switch sound ON or OFF
        """
        help_text = Label(text=text, markup=True)
        help_text.font_size = 22
        help_text.color = [0.97, 0.97, 0.97, 0.9]
        help_text.pos_hint = {'x': 0.0, 'y': 0.0}
        self.add_widget(help_text)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_NORMAL,
                                  pos_hint={'x': .4, 'y': .1})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def __is_data_connection(self):
        """
        Check Android DATA connection here - using pyjnius
        :return:
        """
        is_connected = False

        if platform == 'android':
            try:
                # Note: this is working ONLY on Android phone !
                Context = autoclass('android.content.Context')                                  # Context is a normal java class in the Android API
                PythonActivity = autoclass('org.renpy.android.PythonActivity')                  # PythonActivity is provided by the Kivy bootstrap app in python-for-android
                activity = PythonActivity.mActivity                                             # The PythonActivity stores a reference to the currently running activity
                connectivity_service = activity.getSystemService(Context.CONNECTIVITY_SERVICE)  # Get Connectivity service
                active_network_info = connectivity_service.getActiveNetworkInfo()               # Get active Network info

                if active_network_info:
                    # print "OOOOOOOOO active_network_info.toString(): {} OOOOOOOOO".format(active_network_info.toString())
                    # print "OOOOOOOOO active_network_info.getTypeName(): {} OOOOOOOOO".format(active_network_info.getTypeName())
                    # print "OOOOOOOOO active_network_info.isConnected(): {} OOOOOOOOO".format(active_network_info.isConnected())
                    is_connected = active_network_info.isConnected()
                else:
                    print "No Active network !"
                    is_connected = False
            except:
                print "ERROR_IS_CONNECTED from Android API ..."
                is_connected = False
        else:
            print "No Android platform -> Cannot detect data connection"

        return is_connected

    def activate_send_msg(self, event):
        """
        Activate screen for sending email message
        :return:
        """
        if not self.__is_data_connection():
            self.__activate_no_connection_screen()
        else:
            self.__send_email_via_ext_app()

    def __update_textinput_content(self, instance, value):
        """
        Just for testing purpposes
        :return:
        """
        self.text_msg_contain = value

    def __send_email_via_ext_app(self):
        """
        Send Email message screen - Connection is available
        :return:
        """
        try:
            email.send(recipient='michalbroucek@gmail.com', subject='Galaxyrun demo feedback', text='Your message from App here: ')
            self.__activate_menu(None)
        except:
            print '!!! Cannot send an EMAIL - unknow reason !!!'
            self.__activate_no_connection_screen()

    def __activate_no_connection_screen(self):
        """
        Warning screen about - No connection Available
        :return:
        """
        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        # No connection label text
        no_connection_l = Label(text='[b]No Internet connection available ![/b]', markup=True)
        no_connection_l.font_size = FONT_SIZE_HEADLINES
        no_connection_l.bold = True
        no_connection_l.color = [0.8, 0.8, 0.8, 0.5]
        no_connection_l.pos_hint = {'x': .0, 'y': .3}
        self.add_widget(no_connection_l)

        # No connection label description
        no_connection_l = Label(text='Please check or activate your data connection.')
        no_connection_l.font_size = 47
        no_connection_l.bold = True
        no_connection_l.color = [0.8, 0.8, 0.8, 0.5]
        no_connection_l.pos_hint = {'x': .0, 'y': .0}
        self.add_widget(no_connection_l)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                  pos_hint={'x': .4, 'y': .2})
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
        self.game_over_l.font_size = FONT_SIZE_HEADLINES
        self.game_over_l.bold = True
        self.game_over_l.color = [0.8, 0.8, 0.8, 0.5]
        self.game_over_l.pos_hint = {'x': .0, 'y': 0.1}
        self.add_widget(self.game_over_l)

        # Play again button
        self.play_again_b = Button(text='Play again', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                   pos_hint={'x': .2, 'y': .3})
        activate_the_same_level_function = self.__get_level_function(level)
        self.play_again_b.bind(on_press=activate_the_same_level_function)
        self.add_widget(self.play_again_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_LEVELS,
                                  pos_hint={'x': .6, 'y': .3})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def level_finish_screen(self, level=1):
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

        # Menu Background
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        message_finnish = '[b]LEVEL  ' + str(level) + '  COMPLETED[/b]'
        self.level_completed_l = Label(text=message_finnish, markup=True)
        self.level_completed_l.font_size = FONT_SIZE_HEADLINES
        self.level_completed_l.bold = True
        self.level_completed_l.color = [0.8, 0.8, 0.8, 0.5]
        self.level_completed_l.pos_hint = {'x': 0.0, 'y': 0.3}
        self.add_widget(self.level_completed_l)

        message_activated = "".join(['[b]Level ', str(new_level), ' activated[/b]'])
        self.level_activated_l = Label(text=message_activated, markup=True)
        self.level_activated_l.font_size = 47
        self.level_activated_l.bold = True
        self.level_activated_l.color = [0.8, 0.8, 0.8, 0.5]
        self.level_activated_l.pos_hint = {'x': 0.0, 'y': 0.0}
        self.add_widget(self.level_activated_l)

        # Play New level button
        button_label = "".join(['Play Level ', str(new_level)])
        self.new_level_b = Button(text=button_label, font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_BIG,
                                  pos_hint={'x': .2, 'y': .2})
        start_next_level_function = self.__get_level_function(new_level)
        self.new_level_b.bind(on_press=start_next_level_function)
        self.add_widget(self.new_level_b)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_BIG,
                                  pos_hint={'x': .6, 'y': .2})
        self.main_menu_b.bind(on_press=self.__activate_menu)
        self.add_widget(self.main_menu_b)

    def last_level_finish_screen(self):
        """
        Last level screen was completed - CONGRATULATION (no more levels available)
        :return:
        """
        self.play_menu_music_list()
        self.clear_widgets()

        # Menu Background
        # TODO: make new background + some item (rocket + meteorites)
        self.bckg_image = get_background(picture_path='pictures/menu_background.png')
        self.add_widget(self.bckg_image)

        message_finnish = '[b]LAST LEVEL IS COMPLETED[/b]'
        self.level_completed_l = Label(text=message_finnish, markup=True)
        self.level_completed_l.font_size = FONT_SIZE_HEADLINES
        self.level_completed_l.bold = True
        self.level_completed_l.color = [0.8, 0.8, 0.8, 0.5]
        self.level_completed_l.pos_hint = {'x': 0.0, 'y': 0.3}
        self.add_widget(self.level_completed_l)

        message_activated = "".join(['[b]                 Congratulation\n\nyou finished last level in DEMO mode[/b]'])
        self.level_activated_l = Label(text=message_activated, markup=True)
        self.level_activated_l.font_size = 45
        self.level_activated_l.bold = True
        self.level_activated_l.color = [0.8, 0.8, 0.8, 0.5]
        self.level_activated_l.pos_hint = {'x': 0.0, 'y': 0.0}
        self.add_widget(self.level_activated_l)

        # Main menu button
        self.main_menu_b = Button(text='Main menu', font_size=FONT_SIZE_BUTTON, size_hint=SIZE_HINT_BUTTON_BIG,
                                  pos_hint={'x': .4, 'y': .1})
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
        if self.sound:
            menu_music = random.choice(self.menu_music_list)
            menu_music.play()

    def stop_playing_menu_music_list(self):
        for music in self.menu_music_list:
            if music.state == 'play':
                music.stop()
