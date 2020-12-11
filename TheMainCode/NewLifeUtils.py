# ColorModule
# LoggerModule
# StringUtilModule
# ExceptModule
# CustomShellModule
# UtilsModule
# FileModule
# FilelogModule
# TableBuildModule
# DatabaseManageModule
# RandomModule

name = "NewLifeUtils"
version = "v5.0.0 dev"
description = "Utils for you <3"

try:
    import os
    import datetime
except ModuleNotFoundError as e:
    print(f'Unable to import dependences: {e}')
    exit(-1)
except Exception as e:
    print(e) 
    exit(-1)

class ColorModule(object):
    def __init__(self):
        os.system('')
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

    class ACC:
        AFTERCLEAN = "\x1B[K"
        RESET = "\x1B[0m"
        UNDERLINE = "\x1B[4m"
        SWAP = "\x1B[7m"
        NOTNEGATIVE = "\x1B[27m"
        TOBRIGHT = "\x1B[1m"
        NOBRIGHT = "\x1B[2m"

        def CLEARSCREEN():
            NewLifeUtils.Libs.os.system("cls")
            return ""

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

        GOTO_FIRSTLINE = "\x1B[1G"
        GOTO_NEXTLINE = "\x1B[E"
        GOTO_PREVIOUSLINE = "\x1B[F"
        ERASELINE = "\x1B[2K"
        REWRITELINE = "\x1B[1G"

class LoggerModule(object):
    # Init logger
    def __init__(self, colorModule = None):
        if type(colorModule) == ColorModule:
            self.Color = colorModule
        else:
            self.Color = ColorModule()
            
        self.errFormat = "{white}[{time}] {red}{tag}{empty}: {red}{message}{reset}"
        self.logFormat = (
            "{white}[{time}] {green}{tag}{empty}{reset}: {green}{message}{reset}"
        )
        self.wrnFormat = (
            "{white}[{time}] {yellow}{tag}{empty}{reset}: {yellow}{message}{reset}"
        )
        self.reaFormat = "{white}[{time}] {blue}{tag}{empty}{reset}: {blue}{message} {cyan}[{read}]{reset}"
        self.tipFormat = (
            "{white}[{time}] {cyan}{tag}{empty}{reset}: {magenta}{message}{reset}"
        )

        self.errDefaultTag = "Error"
        self.logDefaultTag = "Log"
        self.wrnDefaultTag = "Warn"
        self.reaDefaultTag = "Input"
        self.tipDefaultTag = "Tips"
        self.loggerDateFormat = "%d-%m-%Y"
        self.loggerTimeFormat = "%H:%M:%S"
        self.loggerTagMaxLenght = 8

        self.loggerColorMap = {
            "black": self.Color.ACC.CUSTOMRGB(31, 31, 31),
            "gray": self.Color.ACC.CUSTOMRGB(219, 219, 219),
            "red": self.Color.ACC.CUSTOMRGB(245, 23, 23),
            "green": self.Color.ACC.CUSTOMRGB(13, 209, 39),
            "yellow": self.Color.ACC.CUSTOMRGB(235, 200, 23),
            "blue": self.Color.ACC.CUSTOMRGB(0, 98, 235),
            "magenta": self.Color.ACC.CUSTOMRGB(227, 23, 193),
            "cyan": self.Color.ACC.CUSTOMRGB(24, 212, 222),
            "white": self.Color.ACC.CUSTOMRGB(247, 247, 247),
            "reset": self.Color.ACC.RESET + self.Color.ACC.AFTERCLEAN,
        }
    def formatter(
        self, pattern, message, tag, tag_max, date, time, additional=None
    ):
        if additional is None:
            additional = {"void": ""}

        now = datetime.datetime.now()
        if len(tag) < tag_max:
            empty = " " * (tag_max - len(tag))
        else:
            empty = ""
        return f"{self.Color.ACC.RESET}{self.Color.MCC.REWRITELINE}" + pattern.format(
            **self.loggerColorMap,
            **additional,
            date=now.strftime(date),
            time=now.strftime(time),
            tag=tag,
            empty=empty,
            tab="\t",
            message=message,
        )

    def log(self, message, tag=""):
        if tag == "":
            tag = self.logDefaultTag
        print(
            self.formatter(
                self.logFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def wrn(self, message, tag=""):
        if tag == "":
            tag = self.wrnDefaultTag
        print(
            self.formatter(
                self.wrnFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def err(self, message, tag=""):
        if tag == "":
            tag = self.errDefaultTag
        print(
            self.formatter(
                self.errFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def tip(self, message, tag=""):
        if tag == "":
            tag = self.tipDefaultTag
        print(
            self.formatter(
                self.tipFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def rea(self, message, tag=""):
        if message[-1] not in [" ", ">", ":"]:
            message += ": "
        print(
            f"{self.Color_BCUSTOMRGB(0, 43, 112)}{self.Color_CUSTOMRGB(235, 54, 30)}{message}",
            end="",
        )
        read = input()

        if tag == "":
            tag = self.reaDefaultTag
        s = self.formatter(
            self.reaFormat,
            message,
            tag,
            self.loggerTagMaxLenght,
            self.loggerDateFormat,
            self.loggerTimeFormat,
            additional={"read": read},
        )
        print(self.Color_MCC.GOTO_PREVIOUSLINE + s)
        return read
    

        
        
if __name__ == "__main__":
    print('succeful start')
    c = ColorModule()
    l = LoggerModule(c)
    #e = ExceptModule(l)
    #e.except_print(Exception('oh no'),'wrn',False)
    l.log(f"This is a log")
    l.log(f"This is a log with custom tag", "MyTag1")
    l.tip(f"This is a tip")
    l.tip(f"This is a tip with custom tag", "MyTag2")
    l.wrn(f"This is a warn")
    l.wrn(f"This is a warn with custom tag", "MyTag3")
    l.err(f"This is a error")
    l.err(f"This is a error with custom tag", "MyTag4")
    print('succeful end')
    