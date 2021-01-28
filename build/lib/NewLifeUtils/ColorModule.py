from os import system
from random import randrange

system("")


class BGC:
    """
    BLACK - The background color in the black.
    RED - The background color in the red.
    GREEN - The background color in the green.
    YELLOW - The background color in the yellow.
    BLUE - The background color in the blue.
    PURPLE - The background color in the purple.
    CYAN - The background color in the cyan.
    BGRAY - The background color in the bright gray.
    GRAY - The background color in the gray.
    BRED - The background color in the bright red.
    LIME - The background color in the lime.
    BYELLOW - The background color in the bright yellow.
    BBLUE - The background color in the bright blue.
    MAGENTA - The background color in the magenta.
    BCYAN - The background color in the bright cyan.
    WHITE - The background color in the white.
    """

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
    """
    BLACK - The text color in the black.
    RED - The text color in the red.
    GREEN - The text color in the green.
    YELLOW - The text color in the yellow.
    BLUE - The text color in the blue.
    PURPLE - The text color in the purple.
    CYAN - The text color in the cyan.
    BGRAY - The text color in the bright gray.
    GRAY - The text color in the gray.
    BRED - The text color in the bright red.
    LIME - The text color in the lime.
    BYELLOW - The text color in the bright yellow.
    BBLUE - The text color in the bright blue.
    MAGENTA - The text color in the magenta.
    BCYAN - The text color in the bright cyan.
    WHITE - The text color in the white.
    """

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
    RESET - Removes all of the color codes
    RELOAD - Completely resets the console attributes
    CLEARSCREEN - Clears the console window
    BRIGHT - Replaces colors with brighter counterparts
    NO_BRIGHT - Disables BRIGHT
    UNDERLINE - Underline the text
    NO_UNDERLINE - Removes the underscore
    REVERSE - Changes the colors of the text and the console in places
    NO_REVERSE - Removes the substitution of flowers
    ALTERNATIVE_BUFF - Enables an alternative buffer
    ORIGINAL_BUFF - Returns the original buffer
    """

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

    def title(title: str):
        """
        :parameter title: The new window title
        :return: Text containing the code for changing the window title
        """
        return f"\x1B]2;{title}\x07"

    def rabdomrgb(color="Color"):
        """
        :parameter: color - [gray|color]
        :return: return code of custom random rgb (gray) color
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

    def randomd(n):
        """
        :param n: void variable
        :return: code of random color from color dictionary
        """
        n = randrange(0, 255)
        return f"\x1B[38;5;{n}m"

    def customrgb(r, g, b):
        """
        :param n: void variable
        :return: code of random color from rgb
        """
        return f"\x1B[38;2;{r};{g};{b}m"

    def customc(n):
        """
        :param n: void variable
        :return: code of your color from color dictionary
        """
        return f"\x1B[38;5;{n}m"

    def bcustomrgb(r, g, b):
        """
        :param n: void variable
        :return: code of your color from rgb (background)
        """
        return f"\x1B[48;2;{r};{g};{b}m"

    def bcustomc(n):
        """
        :param n: void variable
        :return: code of your color from color dictionary (background)
        """
        return f"\x1B[48;5;{n}m"


class MCC:
    """
    Attributes:
      CURSOR_DBLINK - to turn Off the blinking cursor
      CURSOR_EBLINK - Enable cursor flickering
      CURSOR_HIDE - Hide the cursor
      CURSOR_SHOW  -  Show the cursor
      ERASE_NXT_WINDOW - Clear the window from the cursor to the end of the window
      ERASE_PRV_WINDOW - Clear the window from the beginning of the window to the cursor
      ERASE_ALL_WINDOW - Clear the entire window
      ERASE_NXT_LINE - Clear to the end of the line
      ERASE_PRV_LINE - Clear from the end of the line
      ERASE_ALL_LINE  -  to Clear an entire line
      SET_TAB  -  Set the tab position in the current location
      DEL_TAB - Delete the tab position
      RES_TAB - Reset tabs
      SAVE_CURSOR - Save the cursor position
      LOAD_CURSOR - Return to the saved cursor position
    """

    CURSOR_DBLINK = "\x1B[?12h"
    CURSOR_EBLINK = "\x1B[?12l"
    CURSOR_HIDE = "\x1B[?25l"
    CURSOR_SHOW = "\x1B[?25h"

    ERASE_NXT_WINDOW = "\x1B[0J"
    ERASE_PRV_WINDOW = "\x1B[1J"
    ERASE_ALL_WINDOW = "\x1B[2J"
    ERASE_NXT_LINE = "\x1B[0K"
    ERASE_PRV_LINE = "\x1B[1K"
    ERASE_ALL_LINE = "\x1B[2K"
    SET_TAB = "\x1BH"
    DEL_TAB = "\x1B[0g"
    RES_TAB = "\x1B[3g"

    SAVE_CURSOR = "\x1B[s"
    LOAD_CURSOR = "\x1B[u"

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
