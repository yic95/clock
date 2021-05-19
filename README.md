# Clock

A full screen clock written in python.

## Require

- True color support
- escape character support
- python3

## Features

- full screen
- not require curses
- custom refresh time

## useage

`Ctrl+c` : exit

## Customization

### Font

Font is a JSON file in `~/.config/clock/font.json` (default) like this:

```json
[
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
        "  ###'  ",
        "      # ",
        "#,    # ",
        " '###'  "
    ],
    [
        "  ,4#   ",
        " ,# #   ",
        ",#' #   ",
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
        "     ,# ",
        "     #' ",
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
    [ // space
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
    ],
    7 //font height
]
```

### theme
Theme is a json file in `~/.config/clock/theme.json` (default) like this:
```json
{
    //         ---fg--- --bg--
    "effect":"[38;5;255;48;5;0m"
}
```

### other settings
In `~/.config/clock/setting.json`:
```json
{
    "once":true,  // execue once
    "refresh_time":1,
    "date_left_bot_corner":true,
    "time_format":"%H:%M:%S",
    "date_format":"%Y-%m-%d",
    "font":"full/path/to/the/font",
    "theme":"full/path/to/the/theme"
}
```
