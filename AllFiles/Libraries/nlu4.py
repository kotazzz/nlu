# -*- coding: utf-8 -*-
class NewLifeUtils(object):

    # ------------- ABOUT      -------------
    name = "NewLifeUtils"
    version = "v3.0.0 dev"
    description = "Utils for you <3"

    # ------------- STATES DEF -------------
    isInitColor = False
    isInitLogger = False
    # ------------- LIB        -------------
    class Libs:
        try:
            os = __import__("os")
            datetime = __import__("datetime")
            random = __import__("random")
            time = __import__("time")
        except ImportError as ie:
            print(ie)

    # ------------- INIT       -------------
    def __init__(self, silent=False, initColor=True, initLogger=True):
        if initColor:
            self.Color.init()
            if not silent:
                print("Color inited")
            isInitColor = True
        if initLogger:
            self.Color.init()
            if not silent:
                print("Color inited")
            isInitColor = True

    class Logger(object):
        def __init__(
            self,
            loggerPrintPattern_err="{red}[{time}] {red}{tag}{empty}: {red}{message}\n{red}[{time}] TIME "
            ": {date} - {time}",
            loggerPrintPattern_log="{reset}[{time}] {green}{tag}{empty}: {green}{message}",
            loggerPrintPattern_wrn="{reset}[{time}] {yellow}{tag}{empty}: {yellow}{message}",
            loggerPrintPattern_rea="{reset}[{time}] {blue}{tag}{empty}: {blue}{message} {cyan}[{read}]",
            loggerPrintPattern_tip="{reset}[{time}] {cyan}{tag}{empty}: {magenta}{message}",
            loggerDefaultTag_err="ERROR",
            loggerDefaultTag_log="LOG",
            loggerDefaultTag_wrn="WARN",
            loggerDefaultTag_rea="INPUT",
            loggerDefaultTag_tip="TIPS",
            loggerDateTimeFormat_date="%d.%m.%Y",
            loggerDateTimeFormat_time="%H:%M:%S",
            loggerTagMaxLenght=12,
        ):
            # def normalize string
            self.loggerNormalize = (
                f"{NewLifeUtils.Color.ACC.RESET}{NewLifeUtils.Color.ACC.NOBRIGHT}\x1B[49"
            )

            # def Colormap
            self.loggerColorMap = {
                "black": NewLifeUtils.Color.ACC.CUSTOMRGB(31, 31, 31),
                "gray": NewLifeUtils.Color.ACC.CUSTOMRGB(219, 219, 219),
                "red": NewLifeUtils.Color.ACC.CUSTOMRGB(245, 23, 23),
                "green": NewLifeUtils.Color.ACC.CUSTOMRGB(13, 209, 39),
                "yellow": NewLifeUtils.Color.ACC.CUSTOMRGB(235, 200, 23),
                "blue": NewLifeUtils.Color.ACC.CUSTOMRGB(0, 98, 235),
                "magenta": NewLifeUtils.Color.ACC.CUSTOMRGB(227, 23, 193),
                "cyan": NewLifeUtils.Color.ACC.CUSTOMRGB(24, 212, 222),
                "white": NewLifeUtils.Color.ACC.CUSTOMRGB(247, 247, 247),
                "reset": NewLifeUtils.Color.ACC.RESET+NewLifeUtils.Color.ACC.AFTERCLEAN,
            }
            # format shielding and setting up
            self.loggerPrintPattern_err = (
                self.loggerNormalize + loggerPrintPattern_err + self.loggerNormalize
            )
            self.loggerPrintPattern_log = (
                self.loggerNormalize + loggerPrintPattern_log + self.loggerNormalize
            )
            self.loggerPrintPattern_wrn = (
                self.loggerNormalize + loggerPrintPattern_wrn + self.loggerNormalize
            )
            self.loggerPrintPattern_rea = (
                self.loggerNormalize + loggerPrintPattern_rea + self.loggerNormalize
            )
            self.loggerPrintPattern_tip = (
                self.loggerNormalize + loggerPrintPattern_tip + self.loggerNormalize
            )

            # upgrading tags
            self.loggerDefaultTag_err = loggerDefaultTag_err
            self.loggerDefaultTag_log = loggerDefaultTag_log
            self.loggerDefaultTag_wrn = loggerDefaultTag_wrn
            self.loggerDefaultTag_rea = loggerDefaultTag_rea
            self.loggerDefaultTag_tip = loggerDefaultTag_tip
            # date and time format def
            self.loggerDateTimeFormat_date = loggerDateTimeFormat_date
            self.loggerDateTimeFormat_time = loggerDateTimeFormat_time
            # tag max length def
            self.loggerTagMaxLenght = loggerTagMaxLenght

        def getColorMap(self):
            return self.loggerColorMap

        @staticmethod
        def formater(
            pattern, message, tag, tag_max, date, time, obj=None, additional=None
        ):
            if additional is None:
                additional = {"additional": ""}
            if obj is None:
                obj = {"obj": ""}
            now = NewLifeUtils.Libs.datetime.datetime.now()
            if len(tag) < tag_max:
                empty = f"{NewLifeUtils.Color.ACC.RESET}" + " " * (tag_max - len(tag))
            else:
                empty = f"{NewLifeUtils.Color.ACC.RESET}"
            return (
                f"{NewLifeUtils.Color.ACC.RESET}{NewLifeUtils.Color.MCC.REWRITELINE}"
                + pattern.format(
                    **obj,
                    **additional,
                    date=now.strftime(date),
                    time=now.strftime(time),
                    tag=tag,
                    empty=empty,
                    tab="\t",
                    message=message,
                )
            )

        def log(self, message, tag=""):
            if tag == "":
                tag = self.loggerDefaultTag_log
            print(
                self.formater(
                    self.loggerPrintPattern_log,
                    message,
                    tag,
                    self.loggerTagMaxLenght,
                    self.loggerDateTimeFormat_date,
                    self.loggerDateTimeFormat_time,
                    additional=self.loggerColorMap,
                )
            )

        def wrn(self, message, tag=""):
            if tag == "":
                tag = self.loggerDefaultTag_wrn
            print(
                self.formater(
                    self.loggerPrintPattern_wrn,
                    message,
                    tag,
                    self.loggerTagMaxLenght,
                    self.loggerDateTimeFormat_date,
                    self.loggerDateTimeFormat_time,
                    additional=self.loggerColorMap,
                )
            )

        def err(self, message, tag=""):
            if tag == "":
                tag = self.loggerDefaultTag_err
            print(
                self.formater(
                    self.loggerPrintPattern_err,
                    message,
                    tag,
                    self.loggerTagMaxLenght,
                    self.loggerDateTimeFormat_date,
                    self.loggerDateTimeFormat_time,
                    additional=self.loggerColorMap,
                )
            )

        def tip(self, message, tag=""):
            if tag == "":
                tag = self.loggerDefaultTag_tip
            print(
                self.formater(
                    self.loggerPrintPattern_tip,
                    message,
                    tag,
                    self.loggerTagMaxLenght,
                    self.loggerDateTimeFormat_date,
                    self.loggerDateTimeFormat_time,
                    additional=self.loggerColorMap,
                )
            )

        def rea(self, message, tag=""):
            if message[-1] not in [' ', '>', ':']:
                message += ': '
            print(f"{NewLifeUtils.Color.ACC.BCUSTOMRGB(0, 43, 112)}{NewLifeUtils.Color.ACC.CUSTOMRGB(235, 54, 30)}{message}", end = '')
            read = input()
            
            if tag == "":
                tag = self.loggerDefaultTag_rea
            s = self.formater(
                self.loggerPrintPattern_rea,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateTimeFormat_date,
                self.loggerDateTimeFormat_time,
                obj={"read": read},
                additional=self.loggerColorMap,
            )
            print(NewLifeUtils.Color.MCC.GOTO_PREVIOUSLINE+s)
            return read

        def read(self, message, tag=""):
            return self.rea(message, tag)

    class SeedGen(object):
        def __init__(self, logger):
            self.err = lambda msg, tag: logger.err(msg, tag)
            self.log = lambda msg, tag: logger.log(msg, tag)
            self.SeedTag = {
                "log": "SEED LOG",
                "err": "SEED ERROR",
                "wrn": "SEED WARN",
                "tip": "SEED TIP",
                "rea": "SEED READ",
            }

        def setSeed(self, customseed="", display=""):
            def getRaw():

                rawseed = str(
                    int(
                        (NewLifeUtils.Libs.datetime.datetime.now().microsecond ** 3)
                        * (NewLifeUtils.Libs.datetime.datetime.now().second ** 10)
                        + (
                            NewLifeUtils.Libs.datetime.datetime.now().month
                            * NewLifeUtils.Libs.datetime.datetime.now().day
                        )
                    )
                )
                return rawseed

            def seedFormater(formated, displayTemplate=""):
                if displayTemplate != "":
                    try:
                        int(displayTemplate)
                    except ValueError:
                        self.err(
                            f"{displayTemplate} is not a numeric", self.SeedTag["err"]
                        )
                        self.wrn(
                            f'Reseting: "{displayTemplate}" -> "" ', self.SeedTag["wrn"]
                        )
                        displayTemplate = "4444"
                elif displayTemplate == "":
                    displayTemplate = "4444"
                    self.log(
                        f"Using default display - {displayTemplate}",
                        self.SeedTag["log"],
                    )
                else:
                    self.log(
                        f"Using non def display - {displayTemplate}",
                        self.SeedTag["log"],
                    )
                need, i = 0, 0
                while i < len(displayTemplate):
                    need += int(displayTemplate[i])
                    i += 1
                self.log(f"Goted {len(formated)}", self.SeedTag["log"])
                self.log(
                    f"Need seed with length > {need} (display {displayTemplate})",
                    self.SeedTag["log"],
                )
                if len(formated) < need:
                    self.log("Not enough raw", self.SeedTag["log"])
                    self.log("Adding 0-sym...", self.SeedTag["log"])
                    formated += "0" * (need - len(formated))
                    self.log(f"New raw - {formated}", self.SeedTag["log"])
                if len(formated) > need:
                    self.log("Cutting string...", self.SeedTag["log"])
                    formated = formated[0:need]
                    self.log(f"New raw - {formated}", self.SeedTag["log"])
                else:
                    self.log(f"All ok", self.SeedTag["log"])
                self.log(f"Formating...", self.SeedTag["log"])
                i = 0
                offset = 0
                formated_space = ""
                while i < len(displayTemplate):
                    offset += int(displayTemplate[i])
                    formated_space += (
                        f"{formated[offset - int(displayTemplate[i]):offset]} "
                    )
                    self.log(
                        f"#{i} (d={displayTemplate[i]};chunk {formated[offset - int(displayTemplate[i]):offset]} [{offset - int(displayTemplate[i])}:{offset}]",
                        self.SeedTag["log"],
                    )
                    self.log(f"\tresult:{formated_space} ", self.SeedTag["log"])
                    i += 1
                return {"raw": formated, "formated": formated_space}

            self.log("Starting", self.SeedTag["log"])
            # Check for set def
            if customseed != "":
                try:
                    int(customseed)
                except ValueError:
                    self.err(f"{customseed} is not a numeric", self.SeedTag["err"])
                    self.wrn(f'Reseting: "{display}" -> <random> ', self.SeedTag["wrn"])
                    self.wrn("Using auto seed", self.SeedTag["wrn"])
                    rawseed = getRaw()
                    self.log(f"New RawSeed: {rawseed}", self.SeedTag["log"])
                    self.seed = seedFormater(rawseed, display)
                else:
                    self.log(f"Using your seed ({customseed})", self.SeedTag["log"])
                    self.seed = seedFormater(customseed, display)
            else:
                self.seed = seedFormater(getRaw(), display)
                self.log("Formating ended!", self.SeedTag["log"])
                self.log(f'Raw: {self.seed["raw"]}', self.SeedTag["log"])
                self.log(f'Formated: {self.seed["formated"]}', self.SeedTag["log"])
                random = NewLifeUtils.Libs.random
                random.seed(self.seed["raw"])
                self.log(f"Randoms:", self.SeedTag["log"])
                self.log(
                    f"{random.randrange(1, 100)};{random.randrange(1, 100)};{random.randrange(1, 100)};",
                    self.SeedTag["log"],
                )
                self.log(
                    f"{random.randrange(1, 100)};{random.randrange(1, 100)};{random.randrange(1, 100)};",
                    self.SeedTag["log"],
                )

        def getSeed(self):
            return self.seed

        def randselect(self, source, use_zero=False):
            # self.logger =  Newlifeutils.Logger(dtag_log = 'RS LOG',dtag_err = 'RS ERROR',dtag_wrn = 'RS LOG',dtag_rea = 'RS READ')
            try:
                source[0]
            except IndexError:
                self.log.err(f"{source} is empty", "RS ERROR")
            except TypeError:
                self.log.err(f"{source} object is not subscriptable", "RS ERROR")
            else:
                if use_zero:
                    self.log("Can use zero", "RS LOG")
                    selector = random.randrange(1, len(source))
                else:
                    self.log("Cant use zero", "RS LOG")
                    selector = random.randrange(0, len(source))
                self.log(
                    f"Select item #{selector} from {type(source)}; result {source[selector]}",
                    "RS LOG",
                )
                return source[selector]
            return -1

    class Color(object):
        def init():
            os = NewLifeUtils.Libs.os
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

        def getColors():
            return {
                "BGC": {
                    "BLACK": "\x1B[40m",
                    "RED": "\x1B[41m",
                    "GREEN": "\x1B[42m",
                    "YELLOW": "\x1B[43m",
                    "BLUE": "\x1B[44m",
                    "PURPLE": "\x1B[45m",
                    "CYAN": "\x1B[46m",
                    "GRAY": "\x1B[47m",
                    "BGRAY": "\x1B[100m",
                    "BRED": "\x1B[101m",
                    "BGREEN": "\x1B[102m",
                    "BYELLOW": "\x1B[103m",
                    "BBLUE": "\x1B[104m",
                    "BPURPLE": "\x1B[105m",
                    "BCYAN": "\x1B[106m",
                    "WHITE": "\x1B[107m",
                },
                "FGC": {
                    "BLACK": "\x1B[30m",
                    "RED": "\x1B[31m",
                    "GREEN": "\x1B[32m",
                    "YELLOW": "\x1B[33m",
                    "BLUE": "\x1B[34m",
                    "PURPLE": "\x1B[35m",
                    "CYAN": "\x1B[36m",
                    "GRAY": "\x1B[37m",
                    "BGRAY": "\x1B[90m",
                    "BRED": "\x1B[91m",
                    "BGREEN": "\x1B[92m",
                    "BYELLOW": "\x1B[93m",
                    "BBLUE": "\x1B[94m",
                    "BPURPLE": "\x1B[95m",
                    "BCYAN": "\x1B[96m",
                    "WHITE": "\x1B[97m",
                },
                "OTH": {
                    "RESET": "\x1B[0m",
                    "UNDERLINE": "\x1B[4m",
                    "SWAP": "\x1B[7m",
                    "NOTNEGATIVE": "\x1B[27m",
                    "TOBRIGHT": "\x1B[1m",
                    "NOBRIGHT": "\x1B[2m",
                },
            }
    def BigPrint(self, text, begin = "\x1B[2m", maxlinelength=9):
        sym = {"0":[
            "--██████╗---","-██╔═████╗--","-██║██╔██║--","-████╔╝██║--","-╚██████╔╝--","--╚═════╝---"],"1":["--██╗-------","-███║-------","-╚██║-------","--██║-------","--██║-------","--╚═╝-------"],"2":["-██████╗----","-╚════██╗---","--█████╔╝---","-██╔═══╝----","-███████╗---","-╚══════╝---"],"3":["-██████╗----","-╚════██╗---","--█████╔╝---","--╚═══██╗---","-██████╔╝---","-╚═════╝----"],"4":["-██╗--██╗---","-██║--██║---","-███████║---","-╚════██║---","------██║---","------╚═╝---"],"5":["-███████╗---","-██╔════╝---","-███████╗---","-╚════██║---","-███████║---","-╚══════╝---"],"6":["--██████╗---","-██╔════╝---","-███████╗---","-██╔═══██╗--","-╚██████╔╝--","--╚═════╝---"],"7":["-███████╗---","-╚════██║---","-----██╔╝---","----██╔╝----","----██║-----","----╚═╝-----"],"8":["--█████╗----","-██╔══██╗---","-╚█████╔╝---","-██╔══██╗---","-╚█████╔╝---","--╚════╝----"],"9":["--█████╗----","-██╔══██╗---","-╚██████║---","--╚═══██║---","--█████╔╝---","--╚════╝----"],"A":["--█████╗----","-██╔══██╗---","-███████║---","-██╔══██║---","-██║--██║---","-╚═╝--╚═╝---"],"B":["-██████╗----","-██╔══██╗---","-██████╔╝---","-██╔══██╗---","-██████╔╝---","-╚═════╝----"],"C":["--██████╗---","-██╔════╝---","-██║--------","-██║--------","-╚██████╗---","--╚═════╝---"],"D":["-██████╗----","-██╔══██╗---","-██║--██║---","-██║--██║---","-██████╔╝---","-╚═════╝----"],"E":["-███████╗---","-██╔════╝---","-█████╗-----","-██╔══╝-----","-███████╗---","-╚══════╝---"],"F":["-███████╗---","-██╔════╝---","-█████╗-----","-██╔══╝-----","-██║--------","-╚═╝--------"],"G":["--██████╗---","-██╔════╝---","-██║--███╗--","-██║---██║--","-╚██████╔╝--","--╚═════╝---"],"H":["-██╗--██╗---","-██║--██║---","-███████║---","-██╔══██║---","-██║--██║---","-╚═╝--╚═╝---"],"I":["-██╗--------","-██║--------","-██║--------","-██║--------","-██║--------","-╚═╝--------"],"J":["------██╗---","------██║---","------██║---","-██---██║---","-╚█████╔╝---","--╚════╝----"],"K":["-██╗--██╗---","-██║-██╔╝---","-█████╔╝----","-██╔═██╗----","-██║--██╗---","-╚═╝--╚═╝---"],"L":["-██╗--------","-██║--------","-██║--------","-██║--------","-███████╗---","-╚══════╝---"],"M":["-███╗---███╗","-████╗-████║","-██╔████╔██║","-██║╚██╔╝██║","-██║-╚═╝-██║","-╚═╝-----╚═╝"],"N":["-███╗---██╗-","-████╗--██║-","-██╔██╗-██║-","-██║╚██╗██║-","-██║-╚████║-","-╚═╝--╚═══╝-"],"O":["--██████╗---","-██╔═══██╗--","-██║---██║--","-██║---██║--","-╚██████╔╝--","--╚═════╝---"],"P":["-██████╗----","-██╔══██╗---","-██████╔╝---","-██╔═══╝----","-██║--------","-╚═╝--------"],"Q":["--██████╗---","-██╔═══██╗--","-██║---██║--","-██║▄▄-██║--","-╚██████╔╝--","--╚══▀▀═╝---"],"R":["-██████╗----","-██╔══██╗---","-██████╔╝---","-██╔══██╗---","-██║--██║---","-╚═╝--╚═╝---"],"S":["-███████╗---","-██╔════╝---","-███████╗---","-╚════██║---","-███████║---","-╚══════╝---"],"T":["-████████╗--","-╚══██╔══╝--","----██║-----","----██║-----","----██║-----","----╚═╝-----"],"U":["-██╗---██╗--","-██║---██║--","-██║---██║--","-██║---██║--","-╚██████╔╝--","--╚═════╝---"],"V":["-██╗---██╗--","-██║---██║--","-██║---██║--","-╚██╗-██╔╝--","--╚████╔╝---","---╚═══╝----"],"W":["-██╗----██╗-","-██║----██║-","-██║-█╗-██║-","-██║███╗██║-","-╚███╔███╔╝-","--╚══╝╚══╝--"],"X":["-██╗--██╗---","-╚██╗██╔╝---","--╚███╔╝----","--██╔██╗----","-██╔╝-██╗---","-╚═╝--╚═╝---"],"Y":["-██╗---██╗--","-╚██╗-██╔╝--","--╚████╔╝---","---╚██╔╝----","----██║-----","----╚═╝-----"],"Z":["-███████╗---","-╚══███╔╝---","---███╔╝----","--███╔╝-----","-███████╗---","-╚══════╝---"],"a":["--█████╗----","-██╔══██╗---","-███████║---","-██╔══██║---","-██║--██║---","-╚═╝--╚═╝---"],"b":["-██████╗----","-██╔══██╗---","-██████╔╝---","-██╔══██╗---","-██████╔╝---","-╚═════╝----"],"c":["--██████╗---","-██╔════╝---","-██║--------","-██║--------","-╚██████╗---","--╚═════╝---"],"d":["-██████╗----","-██╔══██╗---","-██║--██║---","-██║--██║---","-██████╔╝---","-╚═════╝----"],"e":["-███████╗---","-██╔════╝---","-█████╗-----","-██╔══╝-----","-███████╗---","-╚══════╝---"],"f":["-███████╗---","-██╔════╝---","-█████╗-----","-██╔══╝-----","-██║--------","-╚═╝--------"],"g":["--██████╗---","-██╔════╝---","-██║--███╗--","-██║---██║--","-╚██████╔╝--","--╚═════╝---"],"h":["-██╗--██╗---","-██║--██║---","-███████║---","-██╔══██║---","-██║--██║---","-╚═╝--╚═╝---"],"i":["-██╗--------","-██║--------","-██║--------","-██║--------","-██║--------","-╚═╝--------"],"j":["------██╗---","------██║---","------██║---","-██---██║---","-╚█████╔╝---","--╚════╝----"],"k":["-██╗--██╗---","-██║-██╔╝---","-█████╔╝----","-██╔═██╗----","-██║--██╗---","-╚═╝--╚═╝---"],"l":["-██╗--------","-██║--------","-██║--------","-██║--------","-███████╗---","-╚══════╝---"],"m":["-███╗---███╗","-████╗-████║","-██╔████╔██║","-██║╚██╔╝██║","-██║-╚═╝-██║","-╚═╝-----╚═╝"],"n":["-███╗---██╗-","-████╗--██║-","-██╔██╗-██║-","-██║╚██╗██║-","-██║-╚████║-","-╚═╝--╚═══╝-"],"o":["--██████╗---","-██╔═══██╗--","-██║---██║--","-██║---██║--","-╚██████╔╝--","--╚═════╝---"],"p":["-██████╗----","-██╔══██╗---","-██████╔╝---","-██╔═══╝----","-██║--------","-╚═╝--------"],"q":["--██████╗---","-██╔═══██╗--","-██║---██║--","-██║▄▄-██║--","-╚██████╔╝--","--╚══▀▀═╝---"],"r":["-██████╗----","-██╔══██╗---","-██████╔╝---","-██╔══██╗---","-██║--██║---","-╚═╝--╚═╝---"],"s":["-███████╗---","-██╔════╝---","-███████╗---","-╚════██║---","-███████║---","-╚══════╝---"],"t":["-████████╗--","-╚══██╔══╝--","----██║-----","----██║-----","----██║-----","----╚═╝-----"],"u":["-██╗---██╗--","-██║---██║--","-██║---██║--","-██║---██║--","-╚██████╔╝--","--╚═════╝---"],"v":["-██╗---██╗--","-██║---██║--","-██║---██║--","-╚██╗-██╔╝--","--╚████╔╝---","---╚═══╝----"],"w":["-██╗----██╗-","-██║----██║-","-██║-█╗-██║-","-██║███╗██║-","-╚███╔███╔╝-","--╚══╝╚══╝--"],"x":["-██╗--██╗---","-╚██╗██╔╝---","--╚███╔╝----","--██╔██╗----","-██╔╝-██╗---","-╚═╝--╚═╝---"],"y":["-██╗---██╗--","-╚██╗-██╔╝--","--╚████╔╝---","---╚██╔╝----","----██║-----","----╚═╝-----"],"z":["-███████╗---","-╚══███╔╝---","---███╔╝----","--███╔╝-----","-███████╗---","-╚══════╝---"],".":["------------","------------","------------","------------","-██╗--------","-╚═╝--------"],",":["------------","------------","------------","------------","-▄█╗--------","-╚═╝--------"],"!":["-██╗--------","-██║--------","-██║--------","-╚═╝--------","-██╗--------","-╚═╝--------"],"?":["-██████╗----","-╚════██╗---","---▄███╔╝---","---▀▀══╝----","---██╗------","---╚═╝------"],":":["------------","-██╗--------","-╚═╝--------","-██╗--------","-╚═╝--------","------------"],";":["------------","-██╗--------","-╚═╝--------","-▄█╗--------","-▀═╝--------","------------"],"[":["-███╗-------","-██╔╝-------","-██║--------","-██║--------","-███╗-------","-╚══╝-------"],"]":["-███╗-------","-╚██║-------","--██║-------","--██║-------","-███║-------","-╚══╝-------"],"(":["--██╗-------","-██╔╝-------","-██║--------","-██║--------","-╚██╗-------","--╚═╝-------"],")":["-██╗--------","-╚██╗-------","--██║-------","--██║-------","-██╔╝-------","-╚═╝--------"],"<":["---██╗------","--██╔╝------","-██╔╝-------","-╚██╗-------","--╚██╗------","---╚═╝------"],">":["-██╗--------","-╚██╗-------","--╚██╗------","--██╔╝------","-██╔╝-------","-╚═╝--------"],"/":["-----██╗----","----██╔╝----","---██╔╝-----","--██╔╝------","-██╔╝-------","-╚═╝--------"],"*":["------------","-▄-██╗▄-----","--████╗-----","-▀╚██╔▀-----","---╚═╝------","------------"],"-":["------------","------------","-█████╗-----","-╚════╝-----","------------","------------"],"@":["--██████╗---","-██╔═══██╗--","-██║██╗██║--","-██║██║██║--","-╚█║████╔╝--","--╚╝╚═══╝---"],"#":["--██╗-██╗---","-████████╗--","-╚██╔═██╔╝--","-████████╗--","-╚██╔═██╔╝--","--╚═╝-╚═╝---"],"$":["-▄▄███▄▄·---","-██╔════╝---","-███████╗---","-╚════██║---","-███████║---","-╚═▀▀▀══╝---"],"%":["-██╗-██╗----","-╚═╝██╔╝----","---██╔╝-----","--██╔╝------","-██╔╝██╗----","-╚═╝-╚═╝----"],"^":["--███╗------","-██╔██╗-----","-╚═╝╚═╝-----","------------","------------","------------"],"&":["----██╗-----","----██║-----","-████████╗--","-██╔═██╔═╝--","-██████║----","-╚═════╝----"]," ":["------------","------------","------------","------------","------------","------------"]}
        def printBSource(text, color):
            try:
                printline = []
                for i in range(len(sym["a"])):
                    printline.append("")
                for letter in text:
                    for line in range(len(sym[letter])):
                        printline[line] += sym[letter][line]
                print(begin+"\n".join(printline)+self.Color.ACC.RESET)
            except KeyError:
                printBSource("ERR",'{CYAN}')
                print("Unable to print text, unknown characters")
                print("May be its unknown color?")
                avaliableKeys = []
                avaliableKeys = list(sym.keys())
                avaliableKeys = "".join(avaliableKeys)
                print(f"Avaliable: {avaliableKeys}")

        import re
        r = [text[i : i + maxlinelength] for i in range(0, len(text), maxlinelength)]
        for text in r:
            printBSource(text,begin)



def demo(nlu):
    # print basic map
    cmap, reset = nlu.Color.getColors(), nlu.Color.ACC.RESET
    bg, fg = cmap["BGC"], cmap["FGC"]
    for bgc in bg.keys():
        for fgc in fg.keys():
            if bgc == fgc:
                print(f"{reset}------", end=reset)
            else:
                print(f"{bg[bgc]}{fg[fgc]}{bgc[0:3]}{fgc[0:3]}", end=reset)
        print(reset)
    print(reset)
    # print map wit 5 Colorful blocks
    for n2 in range(1, round(255), 7):
        s = ["", "", "", "", ""]
        for n3 in range(1, round(255), 8):
            g = n2
            b = n3
            s[0] += nlu.Color.ACC.CUSTOMRGB(0, g, b) + "█"
            s[1] += nlu.Color.ACC.CUSTOMRGB(64, g, b) + "█"
            s[2] += nlu.Color.ACC.CUSTOMRGB(128, g, b) + "█"
            s[3] += nlu.Color.ACC.CUSTOMRGB(192, g, b) + "█"
            s[4] += nlu.Color.ACC.CUSTOMRGB(256, g, b) + "█"
        print("".join(s))  # f'{r}{g}{b}' reset

    # Russia flag
    print(
        nlu.Color.ACC.CUSTOMRGB(235, 235, 235)
        + "████████████████████████████████████████████"
    )
    print(
        nlu.Color.ACC.CUSTOMRGB(235, 235, 235)
        + "████████████████████████████████████████████"
    )
    print(
        nlu.Color.ACC.CUSTOMRGB(3, 69, 252)
        + "████████████████████████████████████████████"
    )
    print(
        nlu.Color.ACC.CUSTOMRGB(3, 69, 252)
        + "████████████████████████████████████████████"
    )
    print(
        nlu.Color.ACC.CUSTOMRGB(204, 43, 43)
        + "████████████████████████████████████████████"
    )
    print(
        nlu.Color.ACC.CUSTOMRGB(204, 43, 43)
        + "████████████████████████████████████████████"
    )

    # print random 20x120
    for y in range(20):
        for x in range(120):
            print(nlu.Color.ACC.RANDOMRGB() + "█", end="")
        print()
    # print gray random 20x120
    for y in range(20):
        for x in range(120):
            print(nlu.Color.ACC.RANDOMRGB("gray") + "█", end="")
        print()

    # print RGB bars bars
    print()
    s = ""
    for r in range(1, 256, 64):
        for n in range(0, 64):
            s += f"{nlu.Color.ACC.CUSTOMRGB(r+n,0,0)}█{reset}"
        print(s)
        s = ""
    s = ""
    for r in range(1, 256, 64):
        for n in range(0, 64):
            s += f"{nlu.Color.ACC.CUSTOMRGB(0,r+n,0)}█{reset}"
        print(s)
        s = ""
    s = ""
    for r in range(1, 256, 64):
        for n in range(0, 64):
            s += f"{nlu.Color.ACC.CUSTOMRGB(0,0,r+n)}█{reset}"
        print(s)
        s = ""
    s = ""
    # print CC-map (Constant Color) bars

    def screate(s, n):
        space = " " * (int(n) - len(str(s)))
        return space + str(s)

    print()
    for r in range(16, 256, 36):
        s = ""
        for n in range(0, 36):
            if (r + n) > 255:
                s += f"{reset}   "
            else:
                s += f"{nlu.Color.ACC.BCUSTOMC(r+n)}{screate(str(r + n), 3)}{reset}"
        print(s + reset)
    # print Colormap with rgb codes
    for n2 in range(1, round(255), 8):
        s = ["", "", ""]
        for n3 in range(1, round(255), 70):
            g = n2
            b = n3
            red = nlu.Color.ACC.CUSTOMRGB(255, 0, 0)
            grn = nlu.Color.ACC.CUSTOMRGB(0, 255 - round(g / 3), 0)
            blu = nlu.Color.ACC.CUSTOMRGB(0, 0, 255)
            s[
                0
            ] += f"{nlu.Color.ACC.BCUSTOMRGB(0,g,b)}{red}0  {grn}{screate(g,3)}{blu}{screate(b,3)}{reset}"
            s[
                1
            ] += f"{nlu.Color.ACC.BCUSTOMRGB(64,g,b)}{red}64 {grn}{screate(g,3)}{blu}{screate(b,3)}{reset}"
            s[
                2
            ] += f"{nlu.Color.ACC.BCUSTOMRGB(128,g,b)}{red}128{grn}{screate(g,3)}{blu}{screate(b,3)}{reset}"
        print("".join(s) + reset)  # f'{r}{g}{b}' reset

def test(nlu, logger):
    sgen = nlu.SeedGen(logger)
    demo(nlu)
    sgen.setSeed()
    print(sgen.getSeed())

    logger.log("hi!")
    nlu.Libs.os.system("echo hi")
    logger.log(f"This is a log")
    logger.log(f"This is a log with custom tag", "MyTag1")
    logger.tip(f"This is a tip")
    logger.tip(f"This is a tip with custom tag", "MyTag2")
    logger.wrn(f"This is a warn")
    logger.wrn(f"This is a warn with custom tag", "MyTag3")
    logger.err(f"This is a error")
    logger.err(f"This is a error with custom tag", "MyTag4")
    nlu.BigPrint(' . . ',nlu.Color.FGC.BLUE)
    nlu.BigPrint('  ^  ',nlu.Color.FGC.BLUE)
    nlu.BigPrint('HELLO ',nlu.Color.FGC.PURPLE)
    nlu.BigPrint('WORLD!',nlu.Color.FGC.BPURPLE)
    nlu.BigPrint('1      ',nlu.Color.ACC.CUSTOMRGB(230, 30, 16))
    nlu.BigPrint(' 2     ',nlu.Color.ACC.CUSTOMRGB(232, 156, 14))
    nlu.BigPrint('  3    ',nlu.Color.ACC.CUSTOMRGB(219, 250, 15))
    nlu.BigPrint('   4   ',nlu.Color.ACC.CUSTOMRGB(50, 250, 15))
    nlu.BigPrint('    5  ',nlu.Color.ACC.CUSTOMRGB(39, 230, 188))
    nlu.BigPrint('     6 ',nlu.Color.ACC.CUSTOMRGB(42, 48, 232))
    nlu.BigPrint('      7',nlu.Color.ACC.CUSTOMRGB(191, 12, 245))
    logger.log(f"This is a log")

if __name__ == "__main__":
    nlu = NewLifeUtils()   
    logger = nlu.Logger()
    test(nlu, logger)
    nlu = NewLifeUtils()
    logger = nlu.Logger()
    test(nlu, logger)
    logger.rea(f"This is a read")
    logger.rea(f"This is a read")
    logger.rea(f"This is a read")
    logger.rea(f"This is a read with custom tag", "MyTag5")
    input()
