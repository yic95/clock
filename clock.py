#! /usr/bin/python3
# -*-coding: utf8-*-
'''
clock
main
'''
import time
from os import get_terminal_size
from os.path import sep as path_sep
from os.path import expandvars, isfile
from json import load


config_font_file = expandvars('$HOME') + '{sep}.config{sep}clock{sep}font.json'.format(sep=path_sep)
has_error = False

default_font = [
    [
        "  0##   ",
        " #   #  ",
        "#     # ",
        "#     # ",
        "#     # ",
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
        "2\'    # ",
        "      # ",
        "    ,#\' ",
        " ,##    ",
        "#\'      ",
        "####### "
    ],
    [
        " ,###,  ",
        "3\'    # ",
        "      # ",
        "  ###\'  ",
        "      # ",
        "#,    # ",
        " \'###\'  "
    ],
    [
        "  ,4#   ",
        " ,# #   ",
        ",#\' #   ",
        "#\'  #   ",
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
        ",#\'  \'6 ",
        "#\'      ",
        "# ####, ",
        "##    # ",
        "#     # ",
        "\'#####\' "
    ],
    [
        "7###### ",
        "     ,# ",
        "     #\' ",
        "    ,#\' ",
        "    #\'  ",
        "   ,#   ",
        "   #\'   "
    ],
    [
        " ,###,  ",
        "8\'   \'# ",
        "#,   ,# ",
        " >###<  ",
        "#\'   \'# ",
        "#,   ,# ",
        " \'###\'  ",
    ],
    [
        " #####  ",
        "#     # ",
        "#     # ",
        " ####,# ",
        "    ,#\' ",
        "   ,#\'  ",
        "   9\'   ",
    ],
    [
        "  ,#,   ",
        "  #:#   ",
        "        ",
        "        ",
        "        ",
        "  ###   ",
        "  \'#\'   ",
    ],
    7  # font height
]

if isfile(config_font_file):
    if bool(load(open(config_font_file, 'r'))) is True:
        if ( type(font[11]) != type(1) ) or ( type(font[0:11]) != type(list) ):
            font = default_font.copy()
            has_error = True
        else:
            font = load(open(config_font_file))
    else:
        has_error = True
else:
    font = default_font.copy()
    has_error = True

if has_error == True:
    print('\rERROR: Error font list.  Using default font.')


def string_to_banner(string: str, font: list=default_font)->str:
    '''\
    font[0] to font[9] are numbers. start with 0
    font[10] is :
    font[11] is font height
    '''
    return_text = ''
    for i in range(font[11]):
        for st in string:
            if st in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] :
                return_text += font[int(st)][i]
            else:
                return_text += font[10][i]
        if i != font[11]-1:  # detect if not last line
            return_text += '\n'
    return return_text


def create_screen(string: str, font: list=default_font)->str:
    # get terminal size
    terminal_width, terminal_height = get_terminal_size()

    banner = string_to_banner(string, font).split('\n')  # 分解
    for i in range(len(banner)):
        banner[i] = list(banner[i])

    #insert white spaces
    for i in range(len(banner)):
        banner[i].insert(0, ' '*int( (terminal_width-len(banner[i])) /2))
    #insert blank lines
    banner.insert(0, '\n'*(int( (terminal_height-len(banner)) /2 )) )
    banner.append('\n'*(int( (terminal_height-len(banner)) /2 )-1) )  # 減一是因為組合時會多加一個換行

    for i in range(len(banner)):
        banner[i] = ''.join(banner[i])
    return_string = '\n'.join(banner)  # 組合

    # add a line if the screen size shorter then terminal size
    if len(return_string.split('\n')) < terminal_height:
        return_string += '\n'

    # add date
    return_string += '\033[38;2;255;239;136m'+time.strftime('%Y-%m-%d')+'\033[0m'
    return return_string

while True:
    try:
        current_time = time.strftime('%H:%M:%S')
        print(create_screen(current_time), end='')
        time.sleep(0.1)
        print('\x1b[2K\x1b[1A'*(get_terminal_size()[1]), end='')
    except KeyboardInterrupt:
        break
print('\x1b[2K\x1b[1A'*(get_terminal_size()[1]), end='')
