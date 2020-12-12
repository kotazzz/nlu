name = "NewLifeUtils"
version = "v5.0.1 dev"
description = """
In fact, there is active development, repeated rewriting of the code. All actions are published on github for orderly storage of changes and fixing all my actions. I don't encourage you to use my code. My goal is to learn how to write programs beautifully and learn how to use github. If you have any ideas, criticism, or suggestions , I'm happy to listen Now this is the 5th attempt to rewrite the code beautifully, each time I change the very structure of the code. In General, I didn't really study the language features, so my code will be disgusting to a professional programmer. Maybe someday I will achieve the effect that I need
"""

try:
    import os
    import datetime
    import re
    import traceback
    import time
    import random
except ModuleNotFoundError as e:
    print(f"Unable to import dependences: {e}")
    exit(-1)
except Exception as e:
    print(e)
    exit(-1)


class ColorModule(object):
    def __init__(self):
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


class StringUtilModule(object):
    def __init__(self):
        pass

    def remove_csi(self, text):
        return (
            re.sub(
                r"\\x1[bB]\[[\d;]*[a-zA-Z]{1}",
                "",
                text.encode("unicode_escape").decode(),
            )
            .encode()
            .decode("unicode_escape")
        )

    def screate(self, string, size=10, insert="r"):
        string = str(string)
        string = string.encode("unicode_escape").decode()
        matches = re.findall(r"\\x1[bB]\[[\d;]*[a-zA-Z]{1}", string, re.MULTILINE)
        resultCSILength = 0
        for match in matches:
            resultCSILength += len(match)
        spaces = " " * (size - (len(string.encode()) - resultCSILength))
        if insert == "r":
            return string.encode().decode("unicode_escape") + spaces
        if insert == "l":
            return spaces + str(string.encode().decode("unicode_escape"))

    def slice(self, text, chunkSize):
        return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]

    def parseArgs(self, readed):
        # [\'][a-zA-ZА-Яа-я\d\s[\]{}()\\\.\":;,-]*[\']|\b[a-zA-Z\d]+
        # [\"\'][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,-]*[\"\']|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,-]+
        # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,\'-]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-]+
        # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+
        # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@#_=%?\*\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+ (NOW)

        res = re.findall(
            r"[\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@#_=%?\*\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+",
            readed,
            re.MULTILINE,
        )
        res2 = []
        for item in res:
            res2.append(re.sub(r"\B'|\b'", "", item))
        res = [x for x in res2 if x != ""]
        if len(res) == 0:
            return {"command": "", "param": []}
        if len(res) == 1:
            return {"command": res[0], "param": []}
        else:
            return {"command": res[0], "param": res[1 : len(res)]}
        return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]


class LoggerModule(object):
    # Init logger
    def __init__(self, Color=None):
        if type(Color) == ColorModule:
            self.Color = Color
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

    def formatter(self, pattern, message, tag, tag_max, date, time, additional=None):
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
            f"{self.Color.ACC.BCUSTOMRGB(0, 43, 112)}{self.Color.ACC.CUSTOMRGB(235, 54, 30)}{message}",
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
        print(self.Color.MCC.PREVIOUSLINE + s)
        return read


class ExceptModule(object):
    def __init__(self, Logger=None, String=None):
        if type(Logger) == LoggerModule:
            self.Logger = Logger
        else:
            self.Logger = LoggerModule()
        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()

    def except_print(self, exception, exceptionType="err", tb=True):
        errorText = "\n-------------- {ExceptionTitle} --------------------\n"
        errorText += f"Type: {type(exception).__name__}\n\n"

        if exception.args == 0:
            errorText += f"Unknown error\n"
        else:
            errorText += f"About Error:\n\t{(chr(10)+chr(9)).join(exception.args)}\t\n"

        if tb:

            errorText += f"\n{traceback.format_exc()}"

        errorText += "\n-------------- {ExceptionTitle} --------------------\n"

        if exceptionType == "attention":
            self.Logger.log(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Attention!", 20)
                )
            )
        if exceptionType == "wrn":
            self.Logger.wrn(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Warning!", 20)
                )
            )
        elif exceptionType == "err":
            self.Logger.err(
                errorText.replace("{ExceptionTitle}", self.String.screate("Error!", 20))
            )
        elif exceptionType == "fatal":
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Fatal Error!", 20)
                )
            )
            exit(-1)
        else:
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate("Something wrong...", 20),
                )
            )


class TableBuildModule(object):
    def __init__(self, String=None, Color=None, default="double"):
        if type(Color) == ColorModule:
            self.Color = Color
        else:
            self.Color = ColorModule()

        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()

        self.tableManagerOneLine = "┌┬┐│─├┼┤└┴┘"
        self.tableManagerTwoLine = "╔╦╗║═╠╬╣╚╩╝"
        self.tableManagerDoubleH = "╓╥╖║─╟╫╢╙╨╜"
        self.tableManagerDoubleV = "╒╤╕│═╞╪╡╘╧╛"

        if default == "double":
            self.tableManagerCurrent = "╔╦╗║═╠╬╣╚╩╝"
        elif default == "single":
            self.tableManagerCurrent = "┌┬┐│─├┼┤└┴┘"
        elif default == "vertical":
            self.tableManagerCurrent = "╓╥╖║─╟╫╢╙╨╜"
        elif default == "horisontal":
            self.tableManagerCurrent = "╒╤╕│═╞╪╡╘╧╛"
        elif default == "simple":
            self.tableManagerCurrent = "+++|-++++++"
        else:
            self.tableManagerCurrent = self.tableManagerTwoLine

    def createTable(
        self,
        rowCount,
        sizes,
        data,
        title="TABLE",
        header=True,
        tableElement="",
        color="",
        align="l",
    ):
        if color == "":
            color = self.Color.FGC.CYAN
        color = self.Color.ACC.RESET + color
        if align == "r":
            align = "l"
        else:
            align = "r"
        # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
        # 0  1  2  3  4  5  6  7  8  9  10

        if tableElement == "":
            tableElement = self.tableManagerCurrent

        result = ""

        # Generate Header-line
        result += f"{color}{tableElement[0]}"

        for sizen in range(rowCount):
            result += f"{color}{tableElement[4]*sizes[sizen]}{color}{tableElement[1]}"
        result = result[:-1] + f"{color}{tableElement[2]}"

        # Generate Header
        if header:
            result += f"\n{color}{tableElement[3]}"
            for num in range(rowCount):
                result += f"{self.String.screate(data[num], sizes[num], align)}{color}{tableElement[3]}"
            result += f"\n{color}{tableElement[5]}"
            for headerPieceSize in sizes:
                result += (
                    f"{color}{tableElement[4]*headerPieceSize}{color}{tableElement[6]}"
                )
            result = result[:-1] + f"{color}{tableElement[7]}"
            data = data[rowCount:]

        # Generate DataSection
        for lineNum in range(0, len(data), rowCount):
            result += f"\n{color}{tableElement[3]}"
            for rowShift in range(0, rowCount):
                try:
                    result += f"{self.String.screate(data[lineNum+rowShift], sizes[rowShift], align)}{color}{tableElement[3]}"
                except:
                    result += f'{self.String.screate("", sizes[rowShift], align)}{color}{tableElement[3]}'
        result += f"\n{color}{tableElement[8]}"

        # Generate Footer-line
        for sizen in range(rowCount):
            result += f"{color}{tableElement[4]*sizes[sizen]}{color}{tableElement[9]}"
        result = result[:-1] + f"{color}{tableElement[10]}{self.Color.ACC.RESET}"

        return f'\n{self.String.screate(title, round(sum(sizes)/2), "l")}\n{result}\n'

    def createMultilineTable(
        self,
        rowCount,
        sizes,
        data,
        title="TABLE",
        tableElement="",
        color="",
        align="l",
    ):
        if color == "":
            color = self.Color.FGC.CYAN
        if align == "r":
            align = "l"
        else:
            align = "r"
        # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
        # 0  1  2  3  4  5  6  7  8  9  10
        # +  +  +  |  -  +  +  +  +  +  +
        # 0  1  2  3  4  5  6  7  8  9  10; , tableElement = '+++|-++++++'
        if tableElement == "":
            tableElement = self.tableManagerCurrent
        for i in range(len(data)):
            data[i] = self.stringManagerSlice(data[i], sizes[i % len(sizes)])
        result = ""
        for line in range(0, len(data), rowCount):
            maxtabsize = 0
            for row in range(0, rowCount):
                if len(data[line + row]) > maxtabsize:
                    maxtabsize = len(data[line + row])
            for row in range(0, rowCount):
                if len(data[line + row]) < maxtabsize:
                    while len(data[line + row]) < maxtabsize:
                        data[line + row].append("")

        # Generate Header-line
        result += f"{color}{tableElement[0]}"
        for headerPieceSize in sizes:
            result += (
                f"{color}{tableElement[4]*headerPieceSize}{color}{tableElement[1]}"
            )
        result = result[:-1] + f"{color}{tableElement[2]}\n"

        # Generate DataSection
        for line in range(0, len(data), rowCount):
            block = []
            for row in range(0, rowCount):
                for blockLineNum in range(len(data[line + row])):

                    try:
                        block[
                            blockLineNum
                        ] += f"{tableElement[3]}{self.String.screate(data[line+row][blockLineNum],sizes[row], align)}"
                    except:
                        block.append(
                            f"{tableElement[3]}{self.String.screate(data[line+row][blockLineNum],sizes[row], align)}"
                        )
            for blockLineNum in range(len(data[line + row])):
                block[blockLineNum] += tableElement[3]
            for line in block:
                result += f"{line}\n"

            result += f"{tableElement[5]}"
            for headerPieceSize in sizes:
                result += f"{tableElement[4]*headerPieceSize}{tableElement[6]}"
            result = result[:-1] + f"{tableElement[7]}\n"

        # Generate Footer-line
        result = result[: -1 * (4 + sum(sizes))] + tableElement[8]
        for headerPieceSize in sizes:
            result += f"{tableElement[4]*headerPieceSize}{tableElement[9]}"
        result = result[:-1] + f"{tableElement[10]}{self.Color.ACC.RESET}"

        return f'\n{self.String.screate(title+" IN DEV", round(sum(sizes)/2), "l")}\n{result}\n'


class CustomShellModule(object):
    class Command:
        command = "commandname"
        aliases = [command, "commandalias"]
        description = "My Super Duper Command"
        required = ["required parametr"]
        optional = ["optional parametr"]
        skipcheck = False

        def run(console):
            console.Logger.log(f'Command "{console.run["command"]}" executed now')

    class Task:
        def execute(console):
            console.Logger.log(f"This is a event task")

    class Function:
        name = "mygf"

        def execute(console):
            console.Logger.log(f"This is a global function")

    def __init__(
        self,
        Logger=None,
        Except=None,
        String=None,
        Color=None,
        name="root",
        about="default console",
    ):
        self.runState = "init"
        if type(Logger) == LoggerModule:
            self.Logger = Logger
        else:
            self.Logger = LoggerModule()
        if type(Except) == ExceptModule:
            self.Except = Except
        else:
            self.Except = ExceptModule()
        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()
        if type(Color) == ColorModule:
            self.Color = Color
        else:
            self.Color = ColorModule()

        self.cmdname = name
        self.cmdabout = about

        self.registeredInitTask = []
        self.registeredCommands = []
        self.registeredGlobalFunctions = {}
        self.registeredExitTask = []
        self.Logger.TagMaxLenght = len(self.cmdname) + 5
        self.Logger.logDefaultTag = f"[L] {self.cmdname.title()}"
        self.Logger.wrnDefaultTag = f"[W] {self.cmdname.title()}"
        self.Logger.errDefaultTag = f"[E] {self.cmdname.title()}"
        self.Logger.tipDefaultTag = f"[T] {self.cmdname.title()}"
        self.Logger.reaDefaultTag = f"[R] {self.cmdname.title()}"
        self.Logger.reaFormat = (
            "{white}[{time}] {blue}{tag}{empty}{reset}: {cyan}{read}{reset}"
        )

        self.runState = "setup"

    class __cls(Command):
        command = "cls"
        description = "clears display"
        aliases = [command, "clearscreen"]
        required = []
        optional = []

        def run(console):
            os.system("cls")

    class __help(Command):
        command = "help"
        description = "displays all commands in this module"
        aliases = [command]
        required = []
        optional = ["command"]

        def run(console):
            class CLR:
                MDL = console.Color.FGC.RED
                MDLDSK = console.Color.FGC.BRED
                CMD = console.Color.FGC.BLUE
                CMDDSK = console.Color.FGC.CYAN
                ALS = console.Color.FGC.PURPLE
                ALSTXT = console.Color.FGC.BPURPLE
                STTL = console.Color.FGC.GREEN
                SCMD = console.Color.ACC.UNDERLINE + console.Color.FGC.WHITE
                SREQ = console.Color.FGC.BGRAY
                SOPT = console.Color.FGC.GRAY
                R = console.Color.ACC.RESET

            helpPage = ""
            if console.paramCount == 0:
                helpPage += (
                    f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                )
                for command in console.registeredCommands:
                    syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                    if command["required"] != []:
                        syntax += (
                            f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                        )
                    if command["optional"] != []:
                        syntax += (
                            f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
                        )
                    helpPage += (
                        f'\t{CLR.CMD}{command["command"]}\n'
                        + f'\t\t{CLR.CMDDSK}Description {CLR.R}: {CLR.CMDDSK}{command["description"]}\n'
                        + f'\t\t{CLR.ALS}Aliases     {CLR.R}: {CLR.ALSTXT}{", ".join(command["aliases"])}\n'
                        + f"\t\t{CLR.STTL}Usage       {CLR.R}: {syntax}{CLR.R}\n"
                    )
                console.Logger.tip(helpPage, f"{console.cmdname} HELP")
            elif console.paramCount == 1:
                if console.parametrs[0] == "commands":
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                    for command in console.registeredCommands:
                        helpPage += f'\t{CLR.CMD}{command["command"]}\n'
                    console.Logger.tip(helpPage, f"{console.cmdname} HELP")
                else:
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                    finded = False
                    for command in console.registeredCommands:
                        if command["command"] == console.parametrs[0]:
                            syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                            if command["required"] != []:
                                syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                            if command["optional"] != []:
                                syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
                            helpPage += (
                                f'\t{CLR.CMD}{command["command"]}\n'
                                + f'\t\t{CLR.CMDDSK}Description: {command["description"]}\n'
                                + f'\t\t{CLR.ALS}Aliases: {CLR.ALSTXT}{", ".join(command["aliases"])}\n'
                                + f"\t\t{CLR.CMDDSK}Usage: {syntax}{CLR.R}\n"
                            )
                            console.Logger.tip(helpPage, f"{console.cmdname} HELP")
                            finded = True
                    if finded != True:
                        console.Logger.wrn(
                            f'Cannot find command "{console.parametrs[0]}"',
                            f"{console.cmdname} HELP",
                        )
            else:
                console.invalidUsage()

    class __hello(Command):
        command = "hello"
        description = "builtin command"
        aliases = [command, "hi"]
        required = []
        optional = ["name"]

        def run(console):
            if console.paramCount == 1:
                console.Logger.log(f"Hello, {console.parametrs[0]}")
            else:
                console.Logger.log(f"Hello, world!")

    class __exit(Command):
        command = "exit"
        aliases = [command, "quit"]
        description = "Exit from ConsoleShellManager"
        required = []
        optional = []
        skipcheck = False

        def run(console):
            console.runState = "quit"

    class __initDefaultTask(Task):
        def execute(console):
            console.Logger.log(f"Welcome to {console.cmdname}")

    class __exitDefaultTask(Task):
        def execute(console):
            console.Logger.log(
                f"Exit with code: {console.runState}, run command: {console.run}"
            )

    def registerInitTask(self, regClass):
        self.registeredInitTask.append(regClass.execute)

    def registerExitTask(self, regClass):
        self.registeredExitTask.append(regClass.execute)

    def registerGlobalFunctions(self, regClass):
        self.registerGlobalFunctions.append(
            {
                "name": regClass.name,
                "execute": regClass.execute,
            }
        )

    def registerCommand(self, regClass):
        self.registeredCommands.append(
            {
                "command": regClass.command,
                "aliases": regClass.aliases,
                "description": regClass.description,
                "required": regClass.required,
                "optional": regClass.optional,
                "skipcheck": regClass.skipcheck,
                "run": regClass.run,
            }
        )

    def invalidUsage(self, command):
        class CLR:
            SCMD = self.Color.ACC.UNDERLINE + self.Color.FGC.WHITE
            SREQ = self.Color.FGC.BGRAY
            SOPT = self.Color.FGC.GRAY
            R = self.Color.ACC.RESET

        syntax = ""
        syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
        if command["required"] != []:
            syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
        if command["optional"] != []:
            syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
        self.Logger.wrn(f"Invalid usage. Syntax: {syntax}")

    def main(self):
        self.runState = "run"

        # Basic registration

        self.registerCommand(self.__cls)
        self.registerCommand(self.__help)
        self.registerCommand(self.__hello)
        self.registerCommand(self.__exit)
        self.registerExitTask(self.__exitDefaultTask)
        self.registerInitTask(self.__initDefaultTask)

        for itask in self.registeredInitTask:
            itask(self)

        while self.runState == "run":
            try:
                _ = self.String.parseArgs(self.Logger.rea(f"{self.cmdname.title()} >"))
                self.command = _["command"]
                self.parametrs = _["param"]
                self.paramCount = len(self.parametrs)

                if self.command == "fuck":
                    nlu.tracebackManagerExceptionPrint(
                        Exception(
                            "Why you so evil?...",
                            ":_(",
                            "TIP: you can be beter",
                        ),
                        exceptionType="wrn",
                        tb=False,
                    )
                elif self.command != "":
                    for registered in self.registeredCommands:
                        if registered["command"] == self.command:
                            self.run = registered
                            if (
                                not (
                                    self.paramCount
                                    > (
                                        len(self.run["required"])
                                        + len(self.run["optional"])
                                    )
                                    or self.paramCount < len(self.run["required"])
                                )
                                or self.run["skipcheck"]
                            ):
                                registered["run"](self)
                            else:
                                self.invalidUsage(registered)
                            self.run = None
                            break
                    else:
                        self.Logger.wrn('Unknown Command, type "help"')

            except Exception as e:
                self.Except.except_print(e)

        for itask in self.registeredExitTask:
            itask(self)


class UtilsModule(object):
    def __init__(self, Logger=None):
        if type(Logger) == LoggerModule:
            self.Logger = Logger
        else:
            self.Logger = LoggerModule()

    def select_rand_list(self, source, use_zero=False):
        try:
            source[0]
        except IndexError:
            self.Logger.err(f"{source} is empty", "RS ERROR")
        except TypeError:
            self.Logger.err(f"{source} object is not subscriptable", "RS ERROR")
        else:
            if use_zero:
                self.Logger.log("Can use zero", "RS LOG")
                selector = random.randrange(1, len(source))
            else:
                self.Logger.log("Cant use zero", "RS LOG")
                selector = random.randrange(0, len(source))
            self.Logger.log(
                f"Select item #{selector} from {type(source).__name__}; result {source[selector]}",
                "RS LOG",
            )
            return source[selector]
        return None


class FileModule(object):
    def __init__(self):

        self.currentDirectory = os.getcwd() + "\\"
        self.workDirectory = self.currentDirectory + "NLUDIR\\"

    def get_path(self, path=""):
        if path == "":
            path = self.workDirectory
        elif path[0] == "+":
            if path[-1] not in ["/", "\\"]:
                path += "\\"
            path = self.workDirectory + path[1:]
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def open_file(self, name, mode="", path="", encoding="utf8"):
        path = self.get_path(path)

        try:
            open(path + name)
        except:
            open(path + name, "w")
        finally:
            if mode == "":
                f = open(path + name, encoding=encoding)
            else:
                f = open(path + name, mode, encoding=encoding)
        return f


class FilelogModule(object):
    def __init__(self, File=None, String=None, logname="log", rr=False):
        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()
        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()

        self.dateFormat = "%d-%m-%Y"
        self.timeFormat = "%H:%M:%S"
        startdate = datetime.datetime.now().strftime(self.dateFormat)
        starttime = datetime.datetime.now().strftime(self.timeFormat)
        if rr:
            file_snumber = 1
            while os.path.exists(
                f'{self.File.get_path("+log")}{logname}-{startdate}-{file_snumber}.log'
            ):
                file_snumber += 1
            self.logFileName = f"{logname}-{startdate}-{file_snumber}.log"
            self.logFile = self.File.open_file(self.logFileName, path="+log", mode="w")
        else:
            self.logFileName = f"{logname}-{startdate}.log"
            self.logFile = self.File.open_file(self.logFileName, path="+log", mode="a")
        self.logFile.write(f"------ NEW START AT {startdate} - {starttime} ------\n")

        self.errDefaultTag = "[!!!] Error"
        self.logDefaultTag = "[   ] Log"
        self.wrnDefaultTag = "[_!_] Warn"

        self.TagMaxLenght = 12

        self.errFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"
        self.logFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"
        self.wrnFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"

    def formatter(self, pattern, message, tag, path, additional=None):
        if additional is None:
            additional = {"void": ""}

        now = datetime.datetime.now()
        tag = self.String.screate(tag, self.TagMaxLenght)

        return pattern.format(
            **additional,
            date=now.strftime(self.dateFormat),
            time=now.strftime(self.timeFormat),
            tag=tag,
            path=path,
            tab="\t",
            message=message,
        )

    def log(self, message, path="main", tag=""):
        if tag == "":
            tag = self.logDefaultTag
        self.logFile.write(self.formatter(self.logFormat, message, tag, path))

    def wrn(self, message, path="main", tag=""):
        if tag == "":
            tag = self.wrnDefaultTag
        self.logFile.write(self.formatter(self.wrnFormat, message, tag, path))

    def err(self, message, path="main", tag=""):
        if tag == "":
            tag = self.errDefaultTag
        self.logFile.write(self.formatter(self.errFormat, message, tag, path))

    def cstm(self, pattern, text=""):
        self.logFile.write(self.formatter(pattern, message, tag, path))


class DatabaseManageModule(object):
    def __init__(self):
        pass


class RandomModule(object):
    def __init__(self):
        pass


class SortModule(object):
    def __partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

    def quick_sort(nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = __partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)


def testNlu():
    # try to init
    cm = ColorModule()
    print("ColorModule created")
    sm = StringUtilModule()
    print("StringUtilModule created")
    lm = LoggerModule(cm)
    print("LoggerModule created")
    em = ExceptModule(lm, sm)
    print("ExceptModule created")
    tbm = TableBuildModule(sm, cm)
    print("TableBuildModule created")
    csm = CustomShellModule(None, em, sm, cm)
    print("CustomShellModule created")
    um = UtilsModule()
    print("UtilsModule created")
    fm = FileModule()
    print("FileModule created")
    flm = FilelogModule()
    print("FilelogModule created")
    print("succeful!")
    # try to init
    # calculate elapsed
    elapsed = datetime.datetime.now()
    ColorModule()
    StringUtilModule()
    LoggerModule(cm)
    ExceptModule(lm, sm)
    TableBuildModule(sm, cm)
    CustomShellModule(None, em, sm, cm)
    UtilsModule(lm)
    FileModule()
    FilelogModule(fm)
    elapsed = datetime.datetime.now() - elapsed
    # calculate elapsed
    time.sleep(1 / 3)
    status = [
        f"Module",
        f"{cm.FGC.GREEN }ColorModule",
        f"{cm.FGC.GREEN }LoggerModule",
        f"{cm.FGC.GREEN }StringUtilModule",
        f"{cm.FGC.GREEN }ExceptModule",
        f"{cm.FGC.GREEN }CustomShellModule",
        f"{cm.FGC.GREEN }TableBuildModule",
        f"{cm.FGC.GREEN }UtilsModule",
        f"{cm.FGC.GREEN }FileModule",
        f"{cm.FGC.GREEN }FilelogModule",
        f"{cm.FGC.YELLOW}DatabaseManageModule",
        f"{cm.FGC.RED   }RandomModule",
    ]
    lm.tip(cm.ACC.CLEARSCREEN + tbm.createTable(1, [40], status, "Project Status"))
    lm.wrn(f"Elapsed time for init all modules: {elapsed}")

    def log(text, tag=""):
        flm.log(text, tag)
        lm.log(text, tag)

    log("HI!")
    log("HI!1")
    log("HI!2")
    log("HI!3")


if __name__ == "__main__":
    testNlu()

    pass