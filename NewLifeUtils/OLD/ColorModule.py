from NewLifeUtils import os

info = """
Dependence: ---
Dependents: ---
About: ---
"""
os.system("")


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
    BGREEN = "\x1B[102m"
    BYELLOW = "\x1B[103m"
    BBLUE = "\x1B[104m"
    BPURPLE = "\x1B[105m"
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
    BGREEN = "\x1B[92m"
    BYELLOW = "\x1B[93m"
    BBLUE = "\x1B[94m"
    BPURPLE = "\x1B[95m"
    BCYAN = "\x1B[96m"
    WHITE = "\x1B[97m"


class CLU:
    def arr_to_rgb(arr):
        return f"\x1B[38;2;{arr[0]};{arr[1]};{arr[2]}m"


class ACC:
    AFTERCLEAN = "\x1B[K"
    OLDRESET = "\x1B[0m"
    RESET = "\x1B[0m" + "\x1B[x" + "\x1B[K"
    UNDERLINE = "\x1B[4m"
    SWAP = "\x1B[7m"
    NOTNEGATIVE = "\x1B[27m"
    TOBRIGHT = "\x1B[1m"
    NOBRIGHT = "\x1B[2m"
    CLEARSCREEN = "\x1Bc"

    def RANDOMRGB(mode="Color"):
        if mode not in ["Color", "gray"]:
            mode = "Color"
        if mode == "Color":
            r, g, b = (
                NewLifeUtils.Libs.random.randrange(0, 255),
                NewLifeUtils.Libs.random.randrange(0, 255),
                NewLifeUtils.Libs.random.randrange(0, 255),
            )
        else:
            r = NewLifeUtils.Libs.random.randrange(0, 255)
            g = r
            b = r
        return f"\x1B[38;2;{r};{g};{b}m"

    def RANDOMD():
        n = NewLifeUtils.Libs.random.randrange(0, 255)
        return f"\x1B[38;5;{n}m"

    def CUSTOMRGB(r, g, b):
        return f"\x1B[38;2;{r};{g};{b}m"

    def CUSTOMC(n):
        return f"\x1B[38;5;{n}m"

    def BCUSTOMRGB(r, g, b):
        return f"\x1B[48;2;{r};{g};{b}m"

    def BCUSTOMC(n):
        return f"\x1B[48;5;{n}m"


class MCC:
    def UP(count):
        return f"\x1B[{count}A"

    def DOWN(count):
        return f"\x1B[{count}B"

    def RIGHT(count):
        return f"\x1B[{count}V"

    def LEFT(count):
        return f"\x1B[{count}D"

    def CURSORPOSITION(x, y):
        return f"\x1B[{x};{y}H"

    FIRSTLINE = "\x1B[1G"
    NEXTLINE = "\x1B[E"
    PREVIOUSLINE = "\x1B[F"
    ERASELINE = "\x1B[2K"
    REWRITELINE = "\x1B[1G"
