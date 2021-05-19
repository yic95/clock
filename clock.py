#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
clock
main
'''
import time
from os import get_terminal_size
from os.path import sep as path_sep
from os.path import expandvars, isfile
from json import load

class Font:
    """\
    class Font:
        methods:
            load_custom_font: Load custom font. Use default font if this method is not called.
            get_font: Return self.font.
        vars:
            config_font_file: The path to the font file.
            has_error: True if the custom font has error.
            default_font: Default font.
            font: font.
    """
    def __init__(self, path:str=''):
        """\
        path_to_font: The path to the font file. Default is '~/.config/clock/font.json'
        """
        self.config_path = path
        self.has_error = False
        self.font = list()
        self.default_font = [
            [
                "  0##   ",
                " #   #  ",
                "#   / # ",
                "#  /  # ",
                "# /   # ",
                " #   #  ",
                "  ###   "
            ],
            [
                "  ##    ",
                " 1 #    ",
                "   #    ",
                "   #    ",
                "   #    ",
                "   #    ",
                ".#####. "
            ],
            [
                " ,####  ",
                "2'    # ",
                "      # ",
                "    ,#' ",
                " ,##    ",
                "#'      ",
                "####### "
            ],
            [
                " ,###,  ",
                "3'    # ",
                "      # ",
                "   ##'  ",
                "      # ",
                "#,    # ",
                " '###'  "
            ],
            [
                "  ,#    ",
                " ,4     ",
                ",#'     ",
                "#'  #   ",
                "####### ",
                "    #   ",
                "    #   "
            ],
            [
                "5###### ",
                "#       ",
                "#  __   ",
                "##'^^'# ",
                "      # ",
                ",    ,# ",
                " '==='  "
            ],
            [
                " ,####, ",
                ",#'  '6 ",
                "#'      ",
                "# ####, ",
                "##    # ",
                "#     # ",
                "'#####' "
            ],
            [
                "7###### ",
                "#    ,# ",
                "#    #' ",
                "    ,#' ",
                "    #'  ",
                "   ,#   ",
                "   #'   "
            ],
            [
                " ,###,  ",
                "8'   '# ",
                "#,   ,# ",
                " >###<  ",
                "#'   '# ",
                "#,   ,# ",
                " '###'  ",
            ],
            [
                " #####  ",
                "#     # ",
                "#     # ",
                " ####,# ",
                "    ,#' ",
                "   ,#'  ",
                "   9'   ",
            ],
            [
                "  ,#,   ",
                "  #:#   ",
                "        ",
                "        ",
                "        ",
                "  ###   ",
                "  '#'   ",
            ],
            [
                "        ",
                "        ",
                "        ",
                "        ",
                "        ",
                "        ",
                "        ",
            ],
            7  # font height
        ]
        self.font = self.default_font
    def load(self):
        '''\
        load custom font, save it to self.font and return True if font is valid
        if font is not valid, return False
        '''
        has_error = False
        if isfile(self.config_path):
            font = load(open(self.config_path))
            has_error = False
            if bool(font) is True:
                if type(font[-1]) == type(1):
                    self.font = font.copy()
                else:
                    self.font = self.default_font
                    has_error = True
            else:
                has_error = True
                self.font = self.default_font
        else:
            self.font = self.default_font

        if has_error is True:
            self.has_error = True
            print('\a\rERROR: Error font list.  Using default font.')
    def get_font(self):
        """return self.font"""
        return self.font


class Theme:
    """\
    theme to change fg, bg
    """
    def __init__(self, path: str=''):
        self.config_path = path
        self.default_theme = {
                'effect':'[38;5;255;48;5;0m'}
        self.theme = self.default_theme.copy()
    def load(self):
        """Load the theme, use default theme if custom theme isn't fcound"""
        if isfile(self.config_path):
            self.theme = load(open(self.config_path))
            # add default settings.
            for k, v in self.default_theme.items():
                self.theme.setdefault(k, v)



class Settings:
    """\
    class Settings:
        methods:
            |read_config: return config.
        vars:
            |config_file_path : ~/.config/clock/settings.json
    """
    def __init__(self):
        self.config_files_dir = expandvars('$HOME')+\
                '{sep}.config{sep}clock'.format(sep=path_sep)
        self.config_file_path = self.config_files_dir + '{sep}setting.json'.format(sep=path_sep)

        self.default_setting = {
            'font' : self.config_files_dir + '{sep}font.json'.format(sep=path_sep),
            'theme' : self.config_files_dir + '{sep}theme.json'.format(sep=path_sep),
            'once': False,
            'date_left_bot_corner': True,
            'refresh_time': 1,
            'time_format': '%H:%M:%S',
            'date_format': '%Y-%m-%d',
        }
        self.settings = self.default_setting.copy()
    def load(self)-> dict:
        """read settings(dict) from file config_file_path"""
        if isfile(self.config_file_path):
            self.settings = load(open(self.config_file_path))
            # add default settings.
            for k, v in self.default_setting.items():
                self.settings.setdefault(k, v)
    def get_settings(self):
        """get the settings dict"""
        return self.settings

class App:
    """\
    main app.
    require classes: Font
    """
    def __init__(self):
        self.settings = Settings()
        self.settings.load()
        self.font = Font(self.settings.settings['font'])
        self.font.load()
        self.theme = Theme(self.settings.settings['theme'])
        self.theme.load()

    def string_to_banner(self)->str:
        '''\
        return a ascii art text.
        font from self.font, text from self.time_string.
        '''
        return_text = ''
        font = self.font.font
        string = time.strftime(self.settings.settings['time_format'])
        for i in range(font[-1]):
            for st in string:
                if st in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] :
                    return_text += font[int(st)][i]
                elif st == ':':
                    return_text += font[10][i]
                elif st == ' ':
                    return_text += font[11][i]
            if i != font[-1]-1:  # detect if not last line
                return_text += '\n'
        return return_text


    def get_screen(self)->str:
        """\
        return a full-screen text.
        """
        # get terminal size
        terminal_width, terminal_height = get_terminal_size()

        # 分解
        banner = self.string_to_banner().split('\n')
        for i in range(len(banner)):
            banner[i] = list(banner[i])

        if self.settings.settings['date_left_bot_corner'] is False:
            banner.insert(0, list('\n'))
            banner.insert(0, list(time.strftime(self.settings.settings['date_format'])))

        font_height = len(banner)

        # insert blank lines before text
        for _ in range(int((terminal_height-font_height)/2)):
            banner.insert(0, list('\n'))

        # insert white spaces
        for i in range(len(banner)):
            terminal_width_space = ' '*int( (terminal_width-len(banner[i])) /2)
            if banner[i] == list('\n'):
                banner[i].insert(0, ' '*(terminal_width))
            else:
                banner[i].insert(0, terminal_width_space)
                banner[i].append(terminal_width_space)
                banner[i].append('\n')

        # insert blank lines after text
        for _ in range(int((terminal_height-font_height)/2)-1):
            banner.append(list(' '* terminal_width + '\n'))
        # banner[0].insert(0, '\033'+self.theme.theme['effect'])
        # banner[-1].append('\033[0m')

        # 組合
        for i in range(len(banner)):
            banner[i] = ''.join(banner[i])
        return_string = ''.join(banner)


        # add a line if the screen size shorter then terminal size
        if len(return_string.split('\n')) < terminal_height:
            return_string += '\n'

        # add date
        if self.settings.settings['date_left_bot_corner'] is True:
            return_string += ' ' + time.strftime(self.settings.settings['date_format'])+'\033[0m'

        # \r to return cursor to the begin of the line
        return self.apply_theme(return_string)
    def apply_theme(self, screen_text):
        """apply theme to screen"""
        return '\033' + self.theme.theme['effect'] + screen_text + '\033[0m'
    def run(self):
        """run the app and until KeyboardInterrupt occue"""
        refresh_time = int(self.settings.settings['refresh_time'])
        if self.settings.settings['once'] == False:
            while True:
                try:
                    print(self.get_screen(), end='\r')
                    time.sleep(refresh_time)
                    print('\x1b[2K\x1b[1A'*(get_terminal_size()[1]), end='')  # clear the screen
                except KeyboardInterrupt:
                    break
            print('\x1b[2K\x1b[1A'*(get_terminal_size()[1]), end='') #  clear the screen
        else:
            self.time_string = time.strftime('%H:%M:%S')
            print(self.get_screen(), end='')


if __name__ == '__main__':
    app = App()
    app.run()
