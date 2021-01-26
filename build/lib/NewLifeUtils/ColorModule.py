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
    RESET = "\x1B[0m"
    RELOAD = "\x1B[!p"
    CLEARSCREEN = "\x1Bc"

    BRIGHT = "\x1B[1m"
    NO_BRIGHT = "\x1B[2m"

    UNDERLINE = "\x1B[4m"
    NO_UNDERLINE = "\x1B[24m"

    REVERSE = "\x1B[7m"
    NO_REVERSE = "\x1B[27m"

    ALTERNATIVE_BUFF = "\x1B[?1049h"
    ORIGINAL_BUFF = "\x1B[?1049l"

    def title(title):
        return f"\x1B]2;{title}\x07"

    def rabdomrgb(self="Color"):
        if self not in ["Color", "gray"]:
            self = "Color"
        if self == "Color":
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

    def up(self=1):
        return f"\x1B[{self}A"

    def down(self=1):
        return f"\x1B[{self}B"

    def right(self=1):
        return f"\x1B[{self}C"

    def left(self=1):
        return f"\x1B[{self}D"

    def row(self=1):
        return f"\x1B[{self}G"

    def cursor_position(x, y):
        return f"\x1B[{x};{y}H"

    def scroll_down(self=1):
        return f"\x1B[{self}T"

    def scroll_up(self=1):
        return f"\x1B[{self}S"

    def push_right(self=1):
        return f"\x1B[{self}@"

    def erase_right(self=1):
        return f"\x1B[{self}P"

    def replace_right(self=1):
        return f"\x1B[{self}X"

    def push_down(self=1):
        return f"\x1B[{self}L"

    def erase_down(self=1):
        return f"\x1B{self}M"

    def next_tab(self):
        return f"\x1B{self}I"

    def prev_tab(self):
        return f"\x1B{self}Z"
