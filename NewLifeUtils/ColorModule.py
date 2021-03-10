from os import system
from random import randrange

system("")


class BGC:
    """This class contains variables that output a special sequence. This sequence is not displayed on the screen,
    but affects the output of information. In this case, the code that changes the color of the text that is output after
    the sequence is output is output."""

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
    """This class contains variables that output a special sequence. This sequence is not displayed on the screen,
    but affects the output of information. In this case, a code is output that changes the background color behind the
    text that is output after the sequence is output"""

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
    """
    This class contains variables that output a special sequence. This sequence is not displayed on the screen,
    but affects the output of information. It contains different codes that may have different meanings and uses.
    """

    """Resets all text and background properties-underline, highlight, color, and so on"""
    RESET = "\x1B[0m"
    """Clears the screen as the cls (clear) command)"""
    RELOAD = "\x1B[!p"
    """Highlights the text with a more expressive color"""
    CLEARSCREEN = "\x1Bc"
    """Removes the effect of highlighting the text with a more expressive color"""
    BRIGHT = "\x1B[1m"
    """Removes the effect of highlighting the text with a more expressive color"""
    NO_BRIGHT = "\x1B[2m"
    """Removes the effect of highlighting the text with a more expressive color"""
    UNDERLINE = "\x1B[4m"
    """Underlines the text that comes after the output"""
    NO_UNDERLINE = "\x1B[24m"
    """Removes the underscore, if it was there before"""
    REVERSE = "\x1B[7m"
    """Swaps the background and text colors"""
    NO_REVERSE = "\x1B[27m"
    """Includes " alternative buffer\""""
    ALTERNATIVE_BUFF = "\x1B[?1049h"
    """Turns off the " alternative buffer\""""
    ORIGINAL_BUFF = "\x1B[?1049l"

    @staticmethod
    def title(title: str):
        """
        :parameter title: The new window title
        :return: Text containing the code for changing the window title
        """
        return f"\x1B]2;{title}\x07"

    @staticmethod
    def rabdomrgb(color="Color"):
        """
        :parameter: color - [gray|color]
        :return: Returns the random RGB color applied to the text
        """
        if color == "color":
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

    @staticmethod
    def randomd(n):
        """
        :param n: void variable
        :return: Returns a random RGB color applied to the text and taken from the dictionary
        """
        n = randrange(0, 255)
        return f"\x1B[38;5;{n}m"

    @staticmethod
    def customrgb(r, g, b):
        """
        :param n: void variable
        :return: applies the RGB color you have assigned to the text
        """
        return f"\x1B[38;2;{r};{g};{b}m"

    @staticmethod
    def customc(n):
        """
        :param n: void variable
        :return: applies the RGB color you assigned to the text using the dictionary.
        """
        return f"\x1B[38;5;{n}m"

    @staticmethod
    def bcustomrgb(r, g, b):
        """
        :param n: void variable
        :return: applies the RGB color you have assigned to the text (background)
        """
        return f"\x1B[48;2;{r};{g};{b}m"

    @staticmethod
    def bcustomc(n):
        """
        :param n: void variable
        :return: applies the RGB color you assigned to the text using the dictionary. (background)
        """
        return f"\x1B[48;5;{n}m"


class MCC:
    """This class contains variables that output a special sequence. This sequence is not displayed on the screen,
    but affects the output of the information. In this case, the code that changes the cursor position"""

    """Hide cursor blinking"""
    CURSOR_DBLINK = "\x1B[? 12h"
    """Turn on cursor blinking"""
    CURSOR_EBLINK = "\x1B[? 12l"
    """Hide crusor"""
    CURSOR_HIDE = "\x1B[? 25l"
    """Show the crusor"""
    CURSOR_SHOW = "\x1B[? 25h"

    """Erase everything after the cursor"""
    ERASE_NXT_WINDOW = "\x1B[0J"
    """Erase everything before the cursor"""
    ERASE_PRV_WINDOW = "\x1B[1J"
    """Erase everything"""
    ERASE_ALL_WINDOW = "\x1B[2J"
    """Erase everything after the cursor on the current line"""
    ERASE_NXT_LINE = "\x1B[0K"
    """Erase everything up to the cursor on the current line"""
    ERASE_PRV_LINE = "\x1B[1K"
    """Erase the entire line where the cursor is"""
    ERASE_ALL_LINE = "\x1B[2K"
    """Set tab stop"""
    SET_TAB = "\x1BH"
    """Delete tab stop"""
    DEL_TAB = "\x1B[0g"
    """Restore Tab Stop"""
    RES_TAB = "\x1B[3g"
    """Save cursor position"""
    SAVE_CURSOR = "\x1B[s"
    """Restore saved cursor position"""
    LOAD_CURSOR = "\x1B[u"

    @staticmethod
    def up(count=1):
        """
        Moves cursor up
        :param number of positions to shift
        """
        return f"\x1B[{count}A"

    @staticmethod
    def down(count=1):
        """
        Moves cursor down
        :param number of positions to shift
        """
        return f"\x1B[{count}B"

    @staticmethod
    def right(count=1):
        """
        Move cursor to the right
        :param number of positions to shift
        """
        return f"\x1B[{count}C"

    @staticmethod
    def left(count=1):
        """
        Shifts cursor left
        :param number of positions to shift
        """
        return f"\x1B[{count}D"

    @staticmethod
    def row(count=1):
        """
        Set the row where the cursor is
        :param row number
        """
        return f"\x1B[{count}G"

    @staticmethod
    def cursor_position(x, y):
        """
        Set the position where the cursor is
        :param row and column
        """
        return f"\x1B[{x}; {y} H"

    @staticmethod
    def scroll_down(count=1):
        return f"\x1B[{count}T"

    @staticmethod
    def scroll_up(count=1):
        return f"\x1B[{count}S"

    @staticmethod
    def push_right(count=1):
        return f"\x1B[{count}@"

    @staticmethod
    def erase_right(count=1):
        return f"\x1B[{count}P"

    @staticmethod
    def replace_right(count=1):
        return f"\x1B[{count}X"

    @staticmethod
    def push_down(count=1):
        return f"\x1B[{count}L"

    @staticmethod
    def erase_down(count=1):
        return f"\x1B {count}M"

    @staticmethod
    def next_tab(count):
        return f"\x1B {count}I"

    @staticmethod
    def prev_tab(count):
        return f"\x1B {count}Z"
