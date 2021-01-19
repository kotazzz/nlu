from enum import Enum
from os import system
from random import randrange

system("")


class BGC:
    BLACK = "\x1B[40m"
    RED = "\x1B[41m"
    GREEN = "\x1B[42m"
    YELLOW = "\x1B[43m"
    BLUE = "\x1B[44m"
    PURPLE = "\x1B[45m"
    CYAN = "\x1B[46m"
    BGRAY = "\x1B[47m"
    GRAY = "\x1B[100m"
    BRED = "\x1B[101m"
    LIME = "\x1B[102m"
    BYELLOW = "\x1B[103m"
    BBLUE = "\x1B[104m"
    MAGENTA = "\x1B[105m"
    BCYAN = "\x1B[106m"
    WHITE = "\x1B[107m"


class FGC:
    BLACK = "\x1B[30m"
    RED = "\x1B[31m"
    GREEN = "\x1B[32m"
    YELLOW = "\x1B[33m"
    BLUE = "\x1B[34m"
    PURPLE = "\x1B[35m"
    CYAN = "\x1B[36m"
    BGRAY = "\x1B[37m"
    GRAY = "\x1B[90m"
    BRED = "\x1B[91m"
    LIME = "\x1B[92m"
    BYELLOW = "\x1B[93m"
    BBLUE = "\x1B[94m"
    MAGENTA = "\x1B[95m"
    BCYAN = "\x1B[96m"
    WHITE = "\x1B[97m"


class ACC:
    reset = "\x1B[0m"
    reload = "\x1B[!p"
    clearscreen = "\x1Bc"

    bright = "\x1B[1m"
    no_bright = "\x1B[2m"

    underline = "\x1B[4m"
    no_underline = "\x1B[24m"

    reverse = "\x1B[7m"
    no_reverse = "\x1B[27m"

    alternative_buff = "\x1B[?1049h"
    original_buff = "\x1B[?1049l"

    def title(title):
        return f"\x1B]2;{title}\x07"

    def rabdomrgb(mode="Color"):
        if mode not in ["Color", "gray"]:
            mode = "Color"
        if mode == "Color":
            r, g, b = (
                randrange(0, 255),
                randrange(0, 255),
                randrange(0, 255),
            )
        else:
            r = randrange(0, 255)
            g = r
            b = r
        return f"\x1B[38;2;{r};{g};{b}m"

    def randomd(n):
        n = randrange(0, 255)
        return f"\x1B[38;5;{n}m"

    def customrgb(r, g, b):
        return f"\x1B[38;2;{r};{g};{b}m"

    def customc(n):
        return f"\x1B[38;5;{n}m"

    def bcustomrgb(r, g, b):
        return f"\x1B[48;2;{r};{g};{b}m"

    def bcustomc(n):
        return f"\x1B[48;5;{n}m"


class MCC:
    cursor_dblink = "\x1B[?12h"
    cursor_eblink = "\x1B[?12l"
    cursor_hide = "\x1B[?25l"
    cursor_show = "\x1B[?25h"

    erase_nxt_window = "\x1B[0J"
    erase_prv_window = "\x1B[1J"
    erase_all_window = "\x1B[2J"
    erase_nxt_line = "\x1B[0K"
    erase_prv_line = "\x1B[1K"
    erase_all_line = "\x1B[2K"
    set_tab = "\x1BH"
    del_tab = "\x1B[0g"
    res_tab = "\x1B[3g"

    save_cursor = "\x1B[s"
    load_cursor = "\x1B[u"

    def up(count=1):
        return f"\x1B[{count}A"

    def down(count=1):
        return f"\x1B[{count}B"

    def right(count=1):
        return f"\x1B[{count}C"

    def left(count=1):
        return f"\x1B[{count}D"

    def row(count=1):
        return f"\x1B[{count}G"

    def cursor_position(x, y):
        return f"\x1B[{x};{y}H"




    def scroll_down(count=1):
        return f"\x1B[{count}T"

    def scroll_up(count=1):
        return f"\x1B[{count}S"

    def push_right(count=1):
        return f"\x1B[{count}@"

    def erase_right(count=1):
        return f"\x1B[{count}P"

    def replace_right(count=1):
        return f"\x1B[{count}X"

    def push_down(count=1):
        return f"\x1B[{count}L"

    def erase_down(count=1):
        return f"\x1B{count}M"

    def next_tab(count):
        return f"\x1B{count}I"

    def prev_tab(count):
        return f"\x1B{count}Z"


