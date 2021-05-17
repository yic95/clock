# Clock

A full screen clock written in python.

## Require

- True color support
- escape character support
- python3

## Features

- full screen
- not require curses

## useage

`Ctrl+c` : exit

## Customization

### Font

Font is a JSON file in `~/.config/clock/font.json` like this:

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
    7 //font height
]
```

### theme
Theme is a json file in `~/.config/clock/theme.json` like this:
```json
{
    //         ---fg--- --bg--
    "effect":"[38;5;255;48;5;0m"
}
```
### execute once
Add these lines in `~/.config/clock/setting.json`:
```json
{
    "once":true
}
```
