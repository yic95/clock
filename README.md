# Clock

A full screen clock written in python.

## Require

- True color support
- Escape character support
- Python3

## Features

- full screen
- not require curses
- custom refresh time

## Useage

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

### Theme

Color format is escape code, see [this](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors) for more information.
Theme is a json file in `~/.config/clock/theme.json` (default) like this:

```json
{
    //         ---fg--- --bg--
    "effect":"[38;5;255;48;5;0m"
}
```

### Other settings

In `~/.config/clock/setting.json`:

```json
{
    "once":true,  // execute once
    "refresh_time":1,
    "date_left_bot_corner":true,
    "time_format":"%H:%M:%S", // only support numbers, : and space
    "date_format":"%Y-%m-%d",
    "font":"full/path/to/the/font",
    "theme":"full/path/to/the/theme"
}
```
