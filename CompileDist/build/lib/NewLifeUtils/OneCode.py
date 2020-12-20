# -*- coding: utf-8 -*-
# New Life Utils
__version__ = "5.0.1"
name = "NewLifeUtils"
description = """
In fact, there is active development, repeated rewriting of the code. All actions are published on github for orderly storage of changes and fixing all my actions. I don't encourage you to use my code. My goal is to learn how to write programs beautifully and learn how to use github. If you have any ideas, criticism, or suggestions , I'm happy to listen Now this is the 5th attempt to rewrite the code beautifully, each time I change the very structure of the code. In General, I didn't really study the language features, so my code will be disgusting to a professional programmer. Maybe someday I will achieve the effect that I need
"""
lang = "en"

try:
    import os
    import datetime
    import re
    import traceback
    import time
    import random
    import sqlite3
    import json
    import inspect

    from pathlib import Path
    from itertools import islice
except ModuleNotFoundError as e:
    print(f"Unable to import dependences: {e}")
    exit(-1)
except Exception as e:
    print(e)
    exit(-1)

# Language Setting Up
if lang.lower() not in ["en", "ru"]:
    lang = "en"
if lang.lower() == "en":
    currentLangStorage = {
        "LoggerModule": {
            "err_default_tag": "Error",
            "log_default_tag": "Log",
            "rea_default_tag": "Read",
            "tip_default_tag": "Tip",
            "wrn_default_tag": "Warn",
        },
        "ExceptModule": {
            "about": "About Error:",
            "attention": "Attention!",
            "fatal": "Fatal Error!",
            "unknown": "Unknown Error",
            "warning": "Warning!",
            "wrong": "Something wrong...",
        },
        "CustomShellModule": {
            "def_cls_al1": "clearscreen",
            "def_cls_cmd": "cls",
            "def_cls_dsk": "clears display",
            "def_cmdabout": "default console",
            "def_cmdname": "root",
            "def_exit_al1": "quit",
            "def_exit_cmd": "exit",
            "def_exit_dsk": "Exit from ConsoleShellManager",
            "def_hello_al1": "hi",
            "def_hello_cmd": "hello",
            "def_hello_dsk": "builtin command",
            "def_hello_op1": "name",
            "def_help_cmd": "help",
            "def_help_dsk": "displays all commands in this module",
            "def_help_op1": "command|'commands'",
            "exit1": "Exit with code:",
            "exit2": "run command",
            "same_name_err1": "Console commands with the same names were registered.",
            "same_name_err2": "Commands",
            "same_name_err3": "TIP: check register section and delete or change one of the commands",
            "some_err1": "Why you so evil?...",
            "some_err2": ":_(",
            "some_err3": "TIP: you can be beter",
            "unknown": "Unknown Command, type 'help'",
            "welcome": "Welcome to ",
        },
    }


def getlang(modulename, key):
    if modulename not in currentLangStorage.keys():
        return " <Underfined Module> "
    else:
        try:
            return currentLangStorage[modulename][key]
        except:
            return " <Underfined Key> "


class Global:
    lastFilelogModuleInit = ""


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

    def screate(self, string, size=10, insert="r", filler_symbol=" "):
        calcstreeng = self.remove_csi(string)

        spaces = str(filler_symbol) * (size - len(calcstreeng))
        if insert == "r":
            return string + spaces
        if insert == "l":
            return spaces + string

    def sslice(self, text, chunkSize):
        text = str(text)
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
    def __init__(
        self, File=None, Color=None, String=None, FileLogger=None, enableFileLog=True
    ):
        if type(FileLogger) == FilelogModule():
            self.FileLogger = FileLogger
        else:
            self.FileLogger = FilelogModule()

        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()

        if type(Color) == ColorModule:
            self.Color = Color
        else:
            self.Color = ColorModule()

        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()

        self.enableFileLog = enableFileLog

        f = self.File.open_file("colors.json", mode="r+", path="+logger_data")
        try:
            self.color_map = json.loads(f.read())
        except Exception as e:
            print(e)
            defaultcolormap = '{"Indianred":[205,92,92],"lightcoral":[240,128,128],"salmon":[250,128,114],"darksalmon":[233,150,122],"lightsalmon":[255,160,122],"crimson":[220,20,60],"red":[255,0,0],"firebrick":[178,34,34],"darkred":[139,0,0],"pink":[255,192,203],"lightpink":[255,182,193],"hotpink":[255,105,180],"deeppink":[255,20,147],"mediumvioletred":[199,21,133],"palevioletred":[219,112,147],"coral":[255,127,80],"tomato":[255,99,71],"orangered":[255,69,0],"darkorange":[255,140,0],"orange":[255,165,0],"gold":[255,215,0],"yellow":[255,255,0],"lightyellow":[255,255,224],"lemonchiffon":[255,250,205],"lightgoldenrodyellow":[250,250,210],"papayawhip":[255,239,213],"moccasin":[255,228,181],"peachpuff":[255,218,185],"palegoldenrod":[238,232,170],"khaki":[240,230,140],"darkkhaki":[189,183,107],"lavender":[230,230,250],"thistle":[216,191,216],"plum":[221,160,221],"violet":[238,130,238],"orchid":[218,112,214],"fuchsia":[255,0,255],"magenta":[255,0,255],"mediumorchid":[186,85,211],"mediumpurple":[147,112,219],"blueviolet":[138,43,226],"darkviolet":[148,0,211],"darkorchid":[153,50,204],"darkmagenta":[139,0,139],"purple":[128,0,128],"indigo":[75,0,130],"slateblue":[106,90,205],"darkslateblue":[72,61,139],"cornsilk":[255,248,220],"blanchedalmond":[255,235,205],"bisque":[255,228,196],"navajowhite":[255,222,173],"wheat":[245,222,179],"burlywood":[222,184,135],"tan":[210,180,140],"rosybrown":[188,143,143],"sandybrown":[244,164,96],"goldenrod":[218,165,32],"darkgoldenrod":[184,134,11],"peru":[205,133,63],"chocolate":[210,105,30],"saddlebrown":[139,69,19],"sienna":[160,82,45],"brown":[165,42,42],"maroon":[128,0,0],"black":[0,0,0],"gray":[128,128,128],"silver":[192,192,192],"white":[255,255,255],"olive":[128,128,0],"lime":[0,255,0],"green":[0,128,0],"aqua":[0,255,255],"teal":[0,128,128],"blue":[0,0,255],"navy":[0,0,128],"greenyellow":[173,255,47],"chartreuse":[127,255,0],"lawngreen":[124,252,0],"limegreen":[50,205,50],"palegreen":[152,251,152],"lightgreen":[144,238,144],"mediumspringgreen":[0,250,154],"springgreen":[0,255,127],"mediumseagreen":[60,179,113],"seagreen":[46,139,87],"forestgreen":[34,139,34],"darkgreen":[0,100,0],"yellowgreen":[154,205,50],"olivedrab":[107,142,35],"darkolivegreen":[85,107,47],"mediumaquamarine":[102,205,170],"darkseagreen":[143,188,143],"lightseagreen":[32,178,170],"darkcyan":[0,139,139],"cyan":[0,255,255],"lightcyan":[224,255,255],"paleturquoise":[175,238,238],"aquamarine":[127,255,212],"turquoise":[64,224,208],"mediumturquoise":[72,209,204],"darkturquoise":[0,206,209],"cadetblue":[95,158,160],"steelblue":[70,130,180],"lightsteelblue":[176,196,222],"powderblue":[176,224,230],"lightblue":[173,216,230],"skyblue":[135,206,235],"lightskyblue":[135,206,250],"deepskyblue":[0,191,255],"dodgerblue":[30,144,255],"cornflowerblue":[100,149,237],"mediumslateblue":[123,104,238],"royalblue":[65,105,225],"mediumblue":[0,0,205],"darkblue":[0,0,139],"midnightblue":[25,25,112],"snow":[255,250,250],"honeydew":[240,255,240],"mintcream":[245,255,250],"azure":[240,255,255],"aliceblue":[240,248,255],"ghostwhite":[248,248,255],"whitesmoke":[245,245,245],"seashell":[255,245,238],"beige":[245,245,220],"oldlace":[253,245,230],"floralwhite":[255,250,240],"ivory":[255,255,240],"antiquewhite":[250,235,215],"linen":[250,240,230],"lavenderblush":[255,240,245],"mistyrose":[255,228,225],"gainsboro":[220,220,220],"lightgrey":[211,211,211],"darkgrey":[169,169,169],"grey":[128,128,128],"dimgrey":[105,105,105],"lightslategrey":[119,136,153],"slategrey":[112,128,144],"darkslategrey":[47,79,79]}'
            f.write(defaultcolormap)
            self.color_map = json.loads(defaultcolormap)
        f.close()
        origcolors = self.color_map
        colors = []
        for key in self.color_map:
            self.color_map[key] = self.Color.ACC.CUSTOMRGB(*tuple(self.color_map[key]))
            colors.append(f"{self.color_map[key]}{key}{self.color_map[key]}")
        self.color_map["reset"] = self.Color.ACC.RESET

        t = TableBuildModule()
        self.color_data = {}
        self.color_data["table"] = t.createTable(5, [], colors[:-1], header=False)
        self.color_data["colors"] = origcolors

        self.log_pattern = "{greenyellow}[{time}] {lightgreen}{tag}{snow} : {mediumspringgreen}{message}"
        self.wrn_pattern = "{darkorange}[{time}] {orange}{tag}{snow} : {gold}{message}"
        self.err_pattern = "{crimson}[{time}] {red}{tag}{snow} : {firebrick}{message}"
        self.tip_pattern = (
            "{fuchsia}[{time}] {magenta}{tag}{snow} : {mediumorchid}{message}"
        )
        self.rea_pattern = "{cyan}[{time}] {lightcyan}{tag}{snow} : {paleturquoise}{message} > {mediumslateblue}[{readed}]"

        self.log_default_tag = getlang("LoggerModule", "log_default_tag")
        self.wrn_default_tag = getlang("LoggerModule", "wrn_default_tag")
        self.err_default_tag = getlang("LoggerModule", "err_default_tag")
        self.tip_default_tag = getlang("LoggerModule", "tip_default_tag")
        self.rea_default_tag = getlang("LoggerModule", "rea_default_tag")

        #  READ

        self.date_format = "%d-%m-%Y"
        self.time_format = "%H:%M:%S"

        self.tag_length = 10

    def tag_check(self, tag, default):
        if tag == "":
            return self.String.screate(default, self.tag_length)
        else:
            return self.String.screate(tag, self.tag_length)

    def to_format(self, pattern, args):
        now = datetime.datetime.now()

        return (
            pattern.format(
                **args,
                **self.color_map,
                date=now.strftime(self.date_format),
                time=now.strftime(self.time_format),
            )
            + self.color_map["reset"]
        )

    def out(self, text):
        if self.enableFileLog:
            self.FileLogger.drec(self.String.remove_csi(text))
        print(text)

    log = lambda self, message, tag="": self.out(
        self.to_format(
            self.log_pattern,
            {"message": message, "tag": self.tag_check(tag, self.log_default_tag)},
        )
    )
    wrn = lambda self, message, tag="": self.out(
        self.to_format(
            self.wrn_pattern,
            {"message": message, "tag": self.tag_check(tag, self.wrn_default_tag)},
        )
    )
    err = lambda self, message, tag="": self.out(
        self.to_format(
            self.err_pattern,
            {"message": message, "tag": self.tag_check(tag, self.err_default_tag)},
        )
    )
    tip = lambda self, message, tag="": self.out(
        self.to_format(
            self.tip_pattern,
            {"message": message, "tag": self.tag_check(tag, self.tip_default_tag)},
        )
    )
    cstm = lambda self, pattern, text, args: self.out(self.to_format(pattern, **args))

    rea = lambda self, message, tag="": self.read(message, tag)

    def read(self, message, tag=""):
        if message[-1] not in [" ", ">", ":"]:
            message += ": "
        print(
            f"{self.Color.ACC.BCUSTOMRGB(0, 43, 112)}{self.Color.ACC.CUSTOMRGB(235, 54, 30)}{message}",
            end="",
        )
        readed = input()

        self.out(
            self.Color.MCC.PREVIOUSLINE
            + self.Color.ACC.RESET
            + self.to_format(
                self.rea_pattern,
                {
                    "message": message,
                    "tag": self.tag_check(tag, self.rea_default_tag),
                    "readed": readed,
                },
            )
        )
        return readed


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
            errorText += f'{getlang("ExceptModule","unknown")}\n'
        else:
            errorText += f'{getlang("ExceptModule","about")}:\n\t{(chr(10)+chr(9)).join(exception.args)}\t\n'

        if tb:

            errorText += f"\n{traceback.format_exc()}"

        errorText += "\n-------------- {ExceptionTitle} --------------------\n"

        if exceptionType == "attention":
            self.Logger.log(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate(getlang("ExceptModule", "attention"), 20),
                )
            )
        if exceptionType == "wrn":
            self.Logger.wrn(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate(getlang("ExceptModule", "warning"), 20),
                )
            )
        elif exceptionType == "err":
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate(getlang("ExceptModule", "error"), 20),
                )
            )
        elif exceptionType == "fatal":
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate(getlang("ExceptModule", "fatal"), 20),
                )
            )
            exit(-1)
        else:
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate(getlang("ExceptModule", "wrong"), 20),
                )
            )
    def get_etypes(self):
        return ['attention','wrn','err','fatal']

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

    def find_max(self, row_count, data):
        line_len = []
        for i in range(row_count):
            line_len.append(0)
        for linenum in range(0, len(data), row_count):
            for row in range(row_count):
                if len(self.String.remove_csi(data[linenum + row])) > line_len[row]:
                    line_len[row] = len(self.String.remove_csi(data[linenum + row]))
        return line_len

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
        if sizes == []:
            sizes = self.find_max(rowCount, data)
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
        if sizes == []:
            sizes = self.find_max(rowCount, data)
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
            data[i] = self.String.sslice(data[i], sizes[i % len(sizes)])
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
        result = result[: -1 * (2 + rowCount + sum(sizes))] + tableElement[8]
        for headerPieceSize in sizes:
            result += f"{tableElement[4]*headerPieceSize}{tableElement[9]}"
        result = result[:-1] + f"{tableElement[10]}{self.Color.ACC.RESET}"

        return f'\n{self.String.screate(title+" IN DEV", round(sum(sizes)/2), "l")}\n{result}\n'

    def get_column(self, data, row_count, num):
        num = num % row_count
        table = []
        for line in range(0, len(data), row_count):
            linearr = []
            for row in range(0, row_count):
                linearr.append(data[line + row])
            table.append(linearr)
        results = []
        for line in table:
            results.append(line[num - 1])
        return results

    def get_multi_column(self, data, row_count, ids):
        columns = []
        for num in ids:
            columns.append(self.get_column(data, row_count, num))
        sizes = len(columns[0])
        restabledata = []
        for num in range(sizes):
            for column in columns:
                restabledata.append(column[num])
        return restabledata

    def join_column(self, columns):
        m = 0
        for elem in columns:
            if len(elem) > m:
                m = len(elem)
        for elem in columns:
            while len(elem) < m:
                elem.append("")
        table = []
        for line in range(len(columns[0])):
            for row in range(len(columns)):
                table.append(columns[row][line])
        return table

    def get_record(self, row_count, data, record_id):
        return data[row_count * record_id : row_count * record_id + row_count]

    def get_record_count(self, row_count, data):
        return len(data) / row_count


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
        name=getlang("CustomShellModule", "def_cmdname"),
        about=getlang("CustomShellModule", "def_cmdabout"),
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

    class cls_(Command):
        command = getlang("CustomShellModule", "def_cls_cmd")
        description = getlang("CustomShellModule", "def_cls_dsk")
        aliases = [command, getlang("CustomShellModule", "def_cls_al1")]
        required = []
        optional = []

        def run(console):
            os.system("cls")

    class help_(Command):
        command = getlang("CustomShellModule", "def_help_cmd")
        description = getlang("CustomShellModule", "def_help_dsk")
        aliases = [command]
        required = []
        optional = [getlang("CustomShellModule", "def_help_op1")]

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

    class hello_(Command):
        command = getlang("CustomShellModule", "def_hello_cmd")
        description = getlang("CustomShellModule", "def_hello_dsk")
        aliases = [command, getlang("CustomShellModule", "def_hello_al1")]
        required = []
        optional = [getlang("CustomShellModule", "def_hello_op1")]

        def run(console):
            if console.paramCount == 1:
                console.Logger.log(f"Hello, {console.parametrs[0]}")
            else:
                console.Logger.log(f"Hello, world!")

    class exit_(Command):
        command = getlang("CustomShellModule", "def_exit_cmd")
        aliases = [command, getlang("CustomShellModule", "def_exit_al1")]
        description = getlang("CustomShellModule", "def_exit_dsk")
        required = []
        optional = []
        skipcheck = False

        def run(console):
            console.runState = "quit"

    class initDefaultTask_(Task):
        def execute(console):
            console.Logger.log(
                f'{getlang("CustomShellModule", "welcome")} {console.cmdname}'
            )

    class exitDefaultTask_(Task):
        def execute(console):
            console.Logger.log(
                f'{getlang("CustomShellModule", "exit1")}: {console.runState}, {getlang("CustomShellModule", "exit2")}: {console.run}'
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

        self.registerCommand(self.cls_)
        self.registerCommand(self.help_)
        self.registerCommand(self.hello_)
        self.registerCommand(self.exit_)
        self.registerExitTask(self.exitDefaultTask_)
        self.registerInitTask(self.initDefaultTask_)
        cmdnames = []
        for command in self.registeredCommands:
            cmdnames.append(command["command"])

        if len(cmdnames) != len(set(cmdnames)):
            self.Except.except_print(
                Exception(
                    "Console commands with the same names were registered. here is a list of registered console commands (their names)",
                    f"Commands: {', '.join(cmdnames)}",
                    "TIP: check register section and delete or change one of the commands",
                ),
                exceptionType="fatal",
                tb=False,
            )
        for itask in self.registeredInitTask:
            itask(self)

        while self.runState == "run":
            try:
                readed = self.String.parseArgs(
                    self.Logger.rea(f"{self.cmdname.title()} >")
                )
                self.command = readed["command"]
                self.parametrs = readed["param"]
                self.paramCount = len(self.parametrs)

                if self.command == "fuck":
                    self.Except.except_print(
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
                        if self.command in registered["aliases"]:
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
    def __init__(self, File=None):
        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()

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

    def getfromfname(self, a):
        res = ""
        i = 0
        for e in inspect.stack():
            try:
                res += e.code_context[0]
            except Exception as e:
                res += " <Unknown> "
        return res.rstrip("\n").rsplit("\n", 1)[-1]

    def __partition(self, nums, low, high):
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

    def quick_sort(self, nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = __partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

    def bprint(self, text, maxlinelength=9, font="default"):
        filenamess = self.File.get_directory_content("+fonts")
        files = []
        for filename in filenamess:
            files.append(self.File.get_path("+fonts") + filename)
        fonts = []
        for file in files:
            current = open(file, encoding="utf-8")
            fontsrc = json.loads(current.read())
            fonts.append(fontsrc["name"])
            if fontsrc["name"] == font:
                sym = fontsrc
                break
        else:
            print(f'font "{font}" cant found. Avaliable: {", ".join(fonts)}. Using default')
            sym = {"name":"default","letters":{"0":[" ██████╗   ","██╔═████╗  ","██║██╔██║  ","████╔╝██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"1":[" ██╗       ","███║       ","╚██║       "," ██║       "," ██║       "," ╚═╝       ","           "],"2":["██████╗    ","╚════██╗   "," █████╔╝   ","██╔═══╝    ","███████╗   ","╚══════╝   ","           "],"3":["██████╗    ","╚════██╗   "," █████╔╝   "," ╚═══██╗   ","██████╔╝   ","╚═════╝    ","           "],"4":["██╗  ██╗   ","██║  ██║   ","███████║   ","╚════██║   ","     ██║   ","     ╚═╝   ","           "],"5":["███████╗   ","██╔════╝   ","███████╗   ","╚════██║   ","███████║   ","╚══════╝   ","           "],"6":[" ██████╗   ","██╔════╝   ","███████╗   ","██╔═══██╗  ","╚██████╔╝  "," ╚═════╝   ","           "],"7":["███████╗   ","╚════██║   ","    ██╔╝   ","   ██╔╝    ","   ██║     ","   ╚═╝     ","           "],"8":[" █████╗    ","██╔══██╗   ","╚█████╔╝   ","██╔══██╗   ","╚█████╔╝   "," ╚════╝    ","           "],"9":[" █████╗    ","██╔══██╗   ","╚██████║   "," ╚═══██║   "," █████╔╝   "," ╚════╝    ","           "],"!":["██╗        ","██║        ","██║        ","╚═╝        ","██╗        ","╚═╝        ","           "],"\"":["           ","           ","           ","           ","           ","           ","           "],"#":[" ██╗ ██╗   ","████████╗  ","╚██╔═██╔╝  ","████████╗  ","╚██╔═██╔╝  "," ╚═╝ ╚═╝   ","           "],"$":["▄▄███▄▄·   ","██╔════╝   ","███████╗   ","╚════██║   ","███████║   ","╚═▀▀▀══╝   ","           "],"%":["██╗ ██╗    ","╚═╝██╔╝    ","  ██╔╝     "," ██╔╝      ","██╔╝██╗    ","╚═╝ ╚═╝    ","           "],"&":["   ██╗     ","   ██║     ","████████╗  ","██╔═██╔═╝  ","██████║    ","╚═════╝    ","           "],"'":["           ","           ","           ","           ","           ","           ","           "],"(":[" ██╗       ","██╔╝       ","██║        ","██║        ","╚██╗       "," ╚═╝       ","           "],")":["██╗        ","╚██╗       "," ██║       "," ██║       ","██╔╝       ","╚═╝        ","           "],"*":["           ","▄ ██╗▄     "," ████╗     ","▀╚██╔▀     ","  ╚═╝      ","           ","           "],"+":["           ","           ","           ","           ","           ","           ","           "],",":["           ","           ","           ","           ","▄█╗        ","╚═╝        ","           "],"-":["           ","           ","█████╗     ","╚════╝     ","           ","           ","           "],".":["           ","           ","           ","           ","██╗        ","╚═╝        ","           "],"/":["    ██╗    ","   ██╔╝    ","  ██╔╝     "," ██╔╝      ","██╔╝       ","╚═╝        ","           "],":":["           ","██╗        ","╚═╝        ","██╗        ","╚═╝        ","           ","           "],";":["           ","██╗        ","╚═╝        ","▄█╗        ","▀═╝        ","           ","           "],"<":["  ██╗      "," ██╔╝      ","██╔╝       ","╚██╗       "," ╚██╗      ","  ╚═╝      ","           "],"=":["           ","           ","           ","           ","           ","           ","           "],">":["██╗        ","╚██╗       "," ╚██╗      "," ██╔╝      ","██╔╝       ","╚═╝        ","           "],"?":["██████╗    ","╚════██╗   ","  ▄███╔╝   ","  ▀▀══╝    ","  ██╗      ","  ╚═╝      ","           "],"@":[" ██████╗   ","██╔═══██╗  ","██║██╗██║  ","██║██║██║  ","╚█║████╔╝  "," ╚╝╚═══╝   ","           "],"A":[" █████╗    ","██╔══██╗   ","███████║   ","██╔══██║   ","██║  ██║   ","╚═╝  ╚═╝   ","           "],"B":["██████╗    ","██╔══██╗   ","██████╔╝   ","██╔══██╗   ","██████╔╝   ","╚═════╝    ","           "],"C":[" ██████╗   ","██╔════╝   ","██║        ","██║        ","╚██████╗   "," ╚═════╝   ","           "],"D":["██████╗    ","██╔══██╗   ","██║  ██║   ","██║  ██║   ","██████╔╝   ","╚═════╝    ","           "],"E":["███████╗   ","██╔════╝   ","█████╗     ","██╔══╝     ","███████╗   ","╚══════╝   ","           "],"F":["███████╗   ","██╔════╝   ","█████╗     ","██╔══╝     ","██║        ","╚═╝        ","           "],"G":[" ██████╗   ","██╔════╝   ","██║  ███╗  ","██║   ██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"H":["██╗  ██╗   ","██║  ██║   ","███████║   ","██╔══██║   ","██║  ██║   ","╚═╝  ╚═╝   ","           "],"I":["██╗        ","██║        ","██║        ","██║        ","██║        ","╚═╝        ","           "],"J":["     ██╗   ","     ██║   ","     ██║   ","██   ██║   ","╚█████╔╝   "," ╚════╝    ","           "],"K":["██╗  ██╗   ","██║ ██╔╝   ","█████╔╝    ","██╔═██╗    ","██║  ██╗   ","╚═╝  ╚═╝   ","           "],"L":["██╗        ","██║        ","██║        ","██║        ","███████╗   ","╚══════╝   ","           "],"M":["███╗   ███╗","████╗ ████║","██╔████╔██║","██║╚██╔╝██║","██║ ╚═╝ ██║","╚═╝     ╚═╝","           "],"N":["███╗   ██╗ ","████╗  ██║ ","██╔██╗ ██║ ","██║╚██╗██║ ","██║ ╚████║ ","╚═╝  ╚═══╝ ","           "],"O":[" ██████╗   ","██╔═══██╗  ","██║   ██║  ","██║   ██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"P":["██████╗    ","██╔══██╗   ","██████╔╝   ","██╔═══╝    ","██║        ","╚═╝        ","           "],"Q":[" ██████╗   ","██╔═══██╗  ","██║   ██║  ","██║▄▄ ██║  ","╚██████╔╝  "," ╚══▀▀═╝   ","           "],"R":["██████╗    ","██╔══██╗   ","██████╔╝   ","██╔══██╗   ","██║  ██║   ","╚═╝  ╚═╝   ","           "],"S":["███████╗   ","██╔════╝   ","███████╗   ","╚════██║   ","███████║   ","╚══════╝   ","           "],"T":["████████╗  ","╚══██╔══╝  ","   ██║     ","   ██║     ","   ██║     ","   ╚═╝     ","           "],"U":["██╗   ██╗  ","██║   ██║  ","██║   ██║  ","██║   ██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"V":["██╗   ██╗  ","██║   ██║  ","██║   ██║  ","╚██╗ ██╔╝  "," ╚████╔╝   ","  ╚═══╝    ","           "],"W":["██╗    ██╗ ","██║    ██║ ","██║ █╗ ██║ ","██║███╗██║ ","╚███╔███╔╝ "," ╚══╝╚══╝  ","           "],"X":["██╗  ██╗   ","╚██╗██╔╝   "," ╚███╔╝    "," ██╔██╗    ","██╔╝ ██╗   ","╚═╝  ╚═╝   ","           "],"Y":["██╗   ██╗  ","╚██╗ ██╔╝  "," ╚████╔╝   ","  ╚██╔╝    ","   ██║     ","   ╚═╝     ","           "],"Z":["███████╗   ","╚══███╔╝   ","  ███╔╝    "," ███╔╝     ","███████╗   ","╚══════╝   ","           "],"[":["███╗       ","██╔╝       ","██║        ","██║        ","███╗       ","╚══╝       ","           "],"\\":["           ","           ","           ","           ","           ","           ","           "],"]":["███╗       ","╚██║       "," ██║       "," ██║       ","███║       ","╚══╝       ","           "],"^":[" ███╗      ","██╔██╗     ","╚═╝╚═╝     ","           ","           ","           ","           "],"_":["           ","           ","           ","           ","███████╗   ","╚══════╝   ","           "],"`":["           ","           ","           ","           ","           ","           ","           "],"a":[" █████╗    ","██╔══██╗   ","███████║   ","██╔══██║   ","██║  ██║   ","╚═╝  ╚═╝   ","           "],"b":["██████╗    ","██╔══██╗   ","██████╔╝   ","██╔══██╗   ","██████╔╝   ","╚═════╝    ","           "],"c":[" ██████╗   ","██╔════╝   ","██║        ","██║        ","╚██████╗   "," ╚═════╝   ","           "],"d":["██████╗    ","██╔══██╗   ","██║  ██║   ","██║  ██║   ","██████╔╝   ","╚═════╝    ","           "],"e":["███████╗   ","██╔════╝   ","█████╗     ","██╔══╝     ","███████╗   ","╚══════╝   ","           "],"f":["███████╗   ","██╔════╝   ","█████╗     ","██╔══╝     ","██║        ","╚═╝        ","           "],"g":[" ██████╗   ","██╔════╝   ","██║  ███╗  ","██║   ██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"h":["██╗  ██╗   ","██║  ██║   ","███████║   ","██╔══██║   ","██║  ██║   ","╚═╝  ╚═╝   ","           "],"i":["██╗        ","██║        ","██║        ","██║        ","██║        ","╚═╝        ","           "],"j":["     ██╗   ","     ██║   ","     ██║   ","██   ██║   ","╚█████╔╝   "," ╚════╝    ","           "],"k":["██╗  ██╗   ","██║ ██╔╝   ","█████╔╝    ","██╔═██╗    ","██║  ██╗   ","╚═╝  ╚═╝   ","           "],"l":["██╗        ","██║        ","██║        ","██║        ","███████╗   ","╚══════╝   ","           "],"m":["███╗   ███╗","████╗ ████║","██╔████╔██║","██║╚██╔╝██║","██║ ╚═╝ ██║","╚═╝     ╚═╝","           "],"n":["███╗   ██╗ ","████╗  ██║ ","██╔██╗ ██║ ","██║╚██╗██║ ","██║ ╚████║ ","╚═╝  ╚═══╝ ","           "],"o":[" ██████╗   ","██╔═══██╗  ","██║   ██║  ","██║   ██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"p":["██████╗    ","██╔══██╗   ","██████╔╝   ","██╔═══╝    ","██║        ","╚═╝        ","           "],"q":[" ██████╗   ","██╔═══██╗  ","██║   ██║  ","██║▄▄ ██║  ","╚██████╔╝  "," ╚══▀▀═╝   ","           "],"r":["██████╗    ","██╔══██╗   ","██████╔╝   ","██╔══██╗   ","██║  ██║   ","╚═╝  ╚═╝   ","           "],"s":["███████╗   ","██╔════╝   ","███████╗   ","╚════██║   ","███████║   ","╚══════╝   ","           "],"t":["████████╗  ","╚══██╔══╝  ","   ██║     ","   ██║     ","   ██║     ","   ╚═╝     ","           "],"u":["██╗   ██╗  ","██║   ██║  ","██║   ██║  ","██║   ██║  ","╚██████╔╝  "," ╚═════╝   ","           "],"v":["██╗   ██╗  ","██║   ██║  ","██║   ██║  ","╚██╗ ██╔╝  "," ╚████╔╝   ","  ╚═══╝    ","           "],"w":["██╗    ██╗ ","██║    ██║ ","██║ █╗ ██║ ","██║███╗██║ ","╚███╔███╔╝ "," ╚══╝╚══╝  ","           "],"x":["██╗  ██╗   ","╚██╗██╔╝   "," ╚███╔╝    "," ██╔██╗    ","██╔╝ ██╗   ","╚═╝  ╚═╝   ","           "],"y":["██╗   ██╗  ","╚██╗ ██╔╝  "," ╚████╔╝   ","  ╚██╔╝    ","   ██║     ","   ╚═╝     ","           "],"z":["███████╗   ","╚══███╔╝   ","  ███╔╝    "," ███╔╝     ","███████╗   ","╚══════╝   "]," ":["     ","     ","     ","     ","     ","     "]}}

        def bprintletter(text):
            try:
                printline = []
                for i in range(len(sym["letters"][list(sym["letters"].keys())[0]])):
                    printline.append("")
                for letter in text:
                    for line in range(len(sym["letters"][letter])):
                        printline[line] += sym["letters"][letter][line]
                print("\n".join(printline))
            except KeyError:
                bprintletter("ERROR")
                print("Unable to continue print text, unknown characters")
                avaliableKeys = []
                avaliableKeys = list(sym["letters"].keys())
                avaliableKeys = "".join(avaliableKeys)
                print(f"Avaliable: {avaliableKeys}")

        import re

        r = [text[i : i + maxlinelength] for i in range(0, len(text), maxlinelength)]
        for text in r:
            bprintletter(text)


class FileModule(object):
    def __init__(self):

        self.currentDirectory = os.getcwd() + "\\"
        self.workDirectory = self.currentDirectory + "NewLifeUtils Directory\\"
        self.space = "   "
        self.branch = "│  "
        self.tee = "├─ "
        self.last = "└─ "

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

    def get_directory_content(self, directory=""):
        return os.listdir(self.get_path(directory))

    def exists(self, path):
        return os.path.exists(get_path(path))

    def tree(
        self,
        dir_path: Path,
        level: int = -1,
        limit_to_directories: bool = False,
        length_limit: int = 1000,
    ):
        """Given a directory Path object print a visual tree structure"""
        resultpath = ""
        dir_path = Path(dir_path)  # accept string coerceable to Path
        files = 0
        directories = 0

        def inner(dir_path: Path, prefix: str = "", level=-1):
            nonlocal files, directories
            if not level:
                return  # 0, stop iterating
            if limit_to_directories:
                contents = [d for d in dir_path.iterdir() if d.is_dir()]
            else:
                contents = list(dir_path.iterdir())
            pointers = [self.tee] * (len(contents) - 1) + [self.last]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield prefix + pointer + path.name
                    directories += 1
                    extension = self.branch if pointer == self.tee else self.space
                    yield from inner(path, prefix=prefix + extension, level=level - 1)
                elif not limit_to_directories:
                    yield prefix + pointer + path.name
                    files += 1

        resultpath += "\n" + (dir_path.name)
        iterator = inner(dir_path, level=level)
        for line in islice(iterator, length_limit):
            resultpath += "\n" + (line)
        if next(iterator, None):
            resultpath += "\n" + (
                f"... length_limit, {length_limit}, reached, counted:"
            )
        resultpath += "\n" + ("")
        resultpath += "\n" + (
            f"{directories} directories" + (f", {files} files" if files else "")
        )
        return resultpath

    def old_tree(startpath):
        resultpath = ""
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, "").count(os.sep)
            indent = " " * 4 * (level)
            resultpath += "\n" + ("{}{}/".format(indent, os.path.basename(root)))
            subindent = " " * 4 * (level + 1)
            for f in files:
                resultpath += "\n" + ("{}{}".format(subindent, f))
        return resultpath


class FilelogModule(object):
    def __init__(self, File=None, String=None, Utils=None, logname="log", rr=False):
        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()
        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()
        if type(Utils) == UtilsModule:
            self.Utils = Utils
        else:
            self.Utils = UtilsModule()

        self.dateFormat = "%d-%m-%Y"
        self.timeFormat = "%H:%M:%S"

        startdate = datetime.datetime.now().strftime(self.dateFormat)
        starttime = datetime.datetime.now().strftime(self.timeFormat)

        self.errDefaultTag = "[!!!] Error"
        self.logDefaultTag = "[   ] Log"
        self.wrnDefaultTag = "[_!_] Warn"

        self.TagMaxLenght = 12

        self.errFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"
        self.logFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"
        self.wrnFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"

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
        self.logFile.close()
        if Global.lastFilelogModuleInit != self.Utils.getfromfname(self):
            Global.lastFilelogModuleInit = self.Utils.getfromfname(self)
            self.log(
                f"New Logger from {os.path.basename(__file__)}/{Global.lastFilelogModuleInit.replace(' ', '')}"
            )

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
        self.drec(self.formatter(self.logFormat, message, tag, path), end="")

    def wrn(self, message, path="main", tag=""):
        if tag == "":
            tag = self.wrnDefaultTag
        self.drec(self.formatter(self.wrnFormat, message, tag, path), end="")

    def err(self, message, path="main", tag=""):
        if tag == "":
            tag = self.errDefaultTag
        self.drec(self.formatter(self.errFormat, message, tag, path), end="")

    def cstm(self, pattern, text=""):
        self.drec(self.formatter(pattern, message, tag, path), end="")

    def drec(self, text, end="\n"):
        self.logFile = self.File.open_file(self.logFileName, path="+log", mode="a")
        self.logFile.write(text + end)
        self.logFile.close()


class DatabaseManageModule(object):
    def __init__(self, Logger=None, File=None, Except=None, Table=None):
        self.connection_state = "setup"

        if type(Logger) == LoggerModule:
            self.Logger = Logger
        else:
            self.Logger = LoggerModule()

        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()

        if type(Except) == ExceptModule:
            self.Except = Except
        else:
            self.Except = ExceptModule()

        if type(Table) == TableBuildModule:
            self.Table = Table
        else:
            self.Table = TableBuildModule()

        self.db_path = self.File.get_path("+database")

    def connect(self, db_name="default_db.db"):
        self.db_name = db_name
        try:
            self.Logger.log(f"Connecting to {self.db_name}")
            self.Logger.log(f"Path: {self.db_path}")
            self.connection = sqlite3.connect(self.db_path + self.db_name)
            self.Logger.log(f"Getting cursor for {self.db_name}...")
            self.cursor = self.connection.cursor()
        except Exception as e:
            self.Except.except_print(e)
            self.Logger.err("Failed to connect to the database")
            self.connection_state = "fault"
        else:
            self.Logger.log("Successfully connected to the database")
            self.connection_state = "connected"

    def create_table(self, table_name, fields):
        table_name = self.check_name(table_name)
        self.execute(f'CREATE TABLE {table_name} ({", ".join(fields)})')

    def add_into_table(self, table_name, values):
        pass

    def print_table_description(self, table_name):
        description = list(self.get_table_description(table_name))
        data = []
        for t in description:
            for e in t:
                data.append(e)
        self.Logger.log(
            self.Table.createMultilineTable(
                6,
                [6, 40, 10, 7, 40, 2],
                ["cid", "name", "type", "notnull", "default", "pk"] + data,
            )
        )

    def print_results_mini(self, result, sizes, header=[]):
        if header == []:
            enable_header = False
        else:
            enable_header = True
        rowCount = 1
        if result != []:
            rowCount = len(result[0])
        data = []
        for t in result:
            for e in t:
                data.append(e)
        self.Logger.log(
            self.Table.createTable(rowCount, sizes, header + data, header=enable_header)
        )

    def print_results(self, result, sizes, header=[]):
        rowCount = 1
        if result != []:
            rowCount = len(result[0])
        data = []
        for t in result:
            for e in t:
                data.append(e)
        self.Logger.log(self.Table.createMultilineTable(rowCount, sizes, header + data))

    def get_table_description(self, table_name):
        self.execute(f"PRAGMA TABLE_INFO('{table_name}')")
        res = self.get_result()
        return res

    def execute(self, request):
        if self.connection_state == "connected":
            self.Logger.log(f"Executing: {request}")
            self.cursor.execute(request)
        else:
            self.Logger.err(
                f"Unable to execute, connection state is {connection_state}"
            )

    def check_name(self, text):
        if text.split() != 1:
            return f"'{text}'"
        else:
            return text

    def get_result(self):
        self.last_result = self.cursor.fetchall()
        return self.last_result

    def get_connection_state(self):
        return self.connection_state

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor


class RandomModule(object):
    def __init__(self):
        pass

    def format_number(
        self,
        number=random.randrange(1111111111111111, 9999999999999999),
        numform="4444",
    ):
        # A total conversion
        number = int(number)
        numform = str(numform)
        # Total length
        total_length = 0
        for num in numform:
            total_length += int(num)

        # Dividing or lengthening a number
        if number == 0:
            number = 1

        if len(str(number)) < total_length:
            while len(str(number)) < total_length:
                number = number * 10
        elif len(str(number)) > total_length:
            number = int(str(number)[0:total_length])

        # Add spaces
        result = str(number)
        shift = 0
        for pos in numform:
            result = result[: int(pos) + shift] + " " + result[int(pos) + shift :]
            shift += int(pos) + 1
        return result

    def set_seed_formated(self, seed=-1):
        if seed == -1:
            seed = self.format_number()
        processed_seed = int("".join(seed.split()))
        random.seed = processed_seed
        return processed_seed


def testNlu():
    # try to init
    cm = ColorModule()
    print("ColorModule created")
    sm = StringUtilModule()
    print("StringUtilModule created")
    lm = LoggerModule(cm, enableFileLog=False)
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
    flm = DatabaseManageModule()
    print("DatabaseManageModule created")
    flm = RandomModule()
    print("RandomModule created")
    print("succeful!")
    # try to init
    # calculate elapsed
    elapsed = datetime.datetime.now()
    ColorModule()
    StringUtilModule()
    LoggerModule(cm, enableFileLog=False)
    ExceptModule(lm, sm)
    TableBuildModule(sm, cm)
    CustomShellModule(None, em, sm, cm)
    UtilsModule()
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
        f"{cm.FGC.GREEN }DatabaseManageModule",
        f"{cm.FGC.GREEN }RandomModule",
    ]
    lm.tip(cm.ACC.CLEARSCREEN + tbm.createTable(1, [40], status, "Project Status"))
    lm.wrn(f"Elapsed time for init all modules: {elapsed}")


if __name__ == "__main__":
    lm = LoggerModule()
    # testNlu()
    print(LoggerModule().color_data["table"])
    print(LoggerModule().color_data["colors"]["mediumspringgreen"])
    UtilsModule().bprint("hi")
    UtilsModule().bprint("Hello World", 6, "air")
    UtilsModule().bprint("Hello World", 6, "airs")
    input()

    #
    # test()
    # FilelogModule()
    #
    # CustomShellModule()
    # f = FileModule()
    # pyfiles = []
    # for filename in f.get_directory_content(os.getcwd()):
    #     if filename[-3:] == ".py":
    #         pyfiles.append(filename)
    # for filename in pyfiles:
    #     lm.log(f'black "{filename}"')
    # print()
