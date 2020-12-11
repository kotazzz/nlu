import datetime
import os
import random

# TODO: reformat and start 4th gen

# noinspection PyTypeChecker,PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,
# PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,
# PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,
# PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit,
# PyAttributeOutsideInit,PyAttributeOutsideInit
class NewLifeUtils(object):
    name = "NewLifeUtils"
    version = "v2.3 beta"

    def __init__(
        self,
        asVar=False,
        silent=False,
        Check=True,
        initColor=True,
        initLogger=True,
        initSeedgen=True,
    ):
        self.silent = silent
        if not asVar:
            if initColor:
                os.system("")
            if initLogger:
                self.InitializeLogger()
            if initSeedgen:
                self.InitSeedgen()
            if Check:
                self.Check(silent)

    @staticmethod
    def Check(silent):
        # OS
        try:
            os.system("")
        except NameError:
            if not silent:
                print("ERROR: Unable to init os")
            exit(-1)
        else:
            if not silent:
                print('Module "os" is imported')
        # RANDOM
        try:
            random
        except NameError:
            if not silent:
                print("ERROR: Unable to init random")
            exit(-1)
        else:
            if not silent:
                print('Module "random" is imported')
        # DATETIME
        try:
            datetime
        except NameError:
            if not silent:
                print("ERROR: Unable to init datetime")
            exit(-1)
        else:
            if not silent:
                print('Module "datetime" is imported')

    class BGC:
        CSI = "\x1B["
        BLACK = CSI + "40m"
        RED = CSI + "41m"
        GREEN = CSI + "42m"
        YELLOW = CSI + "43m"
        BLUE = CSI + "44m"
        PURPLE = CSI + "45m"
        CYAN = CSI + "46m"
        WHITE = CSI + "47m"
        BBLACK = CSI + "100m"
        BRED = CSI + "101m"
        BGREEN = CSI + "102m"
        BYELLOW = CSI + "103m"
        BBLUE = CSI + "104m"
        BPURPLE = CSI + "105m"
        BCYAN = CSI + "106m"
        BWHITE = CSI + "107m"

    class FGC:
        CSI = "\x1B["
        BLACK = CSI + "30m"
        RED = CSI + "31m"
        GREEN = CSI + "32m"
        YELLOW = CSI + "33m"
        BLUE = CSI + "34m"
        PURPLE = CSI + "35m"
        CYAN = CSI + "36m"
        WHITE = CSI + "37m"
        BBLACK = CSI + "90m"
        BRED = CSI + "91m"
        BGREEN = CSI + "92m"
        BYELLOW = CSI + "93m"
        BBLUE = CSI + "94m"
        BPURPLE = CSI + "95m"
        BCYAN = CSI + "96m"
        BWHITE = CSI + "97m"

    class ACC:
        CSI = "\x1B["
        RESET = CSI + "0m"
        UNDERLINE = CSI + "4m"
        NEGATIVE = CSI + "7m"
        NOTNEGATIVE = CSI + "27m"
        TOBRIGHT = CSI + "1m"
        NOBRIGHT = CSI + "2m"

        # noinspection PyMethodParameters
        def CUSTOM(r, g, b):
            CSI = "\x1B["
            return CSI + f"38;2;{r};{g};{b}m"

        # noinspection PyMethodParameters
        def CUSTOMD(i):
            CSI = "\x1B["
            return CSI + f"38;5;{i}m"

        # noinspection PyMethodParameters
        def BCUSTOM(r, g, b):
            CSI = "\x1B["
            return CSI + f"48;2;{r};{g};{b}m"

        # noinspection PyMethodParameters
        def BCUSTOMD(i):
            CSI = "\x1B["
            return CSI + f"48;5;{i}m"

    # noinspection PyTypeChecker

    class MCC:
        CSI = "\x1B["

        # noinspection PyMethodParameters
        def UP(n):
            CSI = "\x1B["
            return CSI + str(n) + "A"

        # noinspection PyMethodParameters
        def DOWN(n):
            CSI = "\x1B["
            return CSI + str(n) + "B"

        # noinspection PyMethodParameters
        def RIGHT(n):
            CSI = "\x1B["
            return CSI + str(n) + "V"

        # noinspection PyMethodParameters
        def LEFT(n):
            CSI = "\x1B["
            return CSI + str(n) + "D"

        # noinspection PyMethodParameters
        def CURSORPOSITION(x, y):
            CSI = "\x1B["
            return CSI + f"{x};{y}" + "H"

        BEGIN_LINE = CSI + "1G"
        NEXT_LINE = CSI + "E"
        PREVIOUS_LINE = CSI + "F"
        ERASELINE = CSI + "2K"
        REWRITELINE = CSI + "2K" + CSI + "1G"

        @staticmethod
        def CLEARSCREEN():
            os.system("cls")
            return ""

    def InitializeLogger(
        self,
        loggerPrintPattern_err="{red}[{time}] {red}{tag}{empty}: {red}{message}\n{red}[{time}] TIME "
        ": {date} - {time}",
        loggerPrintPattern_log="{reset}[{time}] {green}{tag}{empty}: {green}{message}",
        loggerPrintPattern_wrn="{reset}[{time}] {yellow}{tag}{empty}: {yellow}{message}",
        loggerPrintPattern_rea="{reset}[{time}] {blue}{tag}{empty}: {blue}{message} {cyan}[{read}]",
        loggerPrintPattern_tip="{reset}[{time}] {cyan}{tag}{empty}: {blue}{message}",
        loggerDefaultTag_err="ERROR",
        loggerDefaultTag_log="LOG",
        loggerDefaultTag_wrn="WARN",
        loggerDefaultTag_rea="INPUT",
        loggerDefaultTag_tip="TIPS",
        loggerDateTimeFormat_date="%d.%m.%Y",
        loggerDateTimeFormat_time="%H:%M:%S",
        loggerTagMaxLenght=12,
    ):

        self.loggerNormalize = f"{NewLifeUtils.ACC.RESET}{NewLifeUtils.ACC.NOBRIGHT}"

        self.loggerColorMap = {
            "black": NewLifeUtils.FGC.BLACK,
            "gray": NewLifeUtils.FGC.WHITE,
            "red": NewLifeUtils.FGC.BRED,
            "green": NewLifeUtils.FGC.BGREEN,
            "yellow": NewLifeUtils.FGC.YELLOW,
            "blue": NewLifeUtils.FGC.BBLUE,
            "magenta": NewLifeUtils.FGC.BPURPLE,
            "cyan": NewLifeUtils.FGC.BCYAN,
            "white": NewLifeUtils.FGC.BWHITE,
            "reset": NewLifeUtils.FGC.BWHITE,
        }

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

        self.loggerDefaultTag_err = loggerDefaultTag_err
        self.loggerDefaultTag_log = loggerDefaultTag_log
        self.loggerDefaultTag_wrn = loggerDefaultTag_wrn
        self.loggerDefaultTag_rea = loggerDefaultTag_rea
        self.loggerDefaultTag_tip = loggerDefaultTag_tip

        self.loggerDateTimeFormat_date = loggerDateTimeFormat_date
        self.loggerDateTimeFormat_time = loggerDateTimeFormat_time
        self.loggerTagMaxLenght = loggerTagMaxLenght

    def getColorMap(self):
        return self.loggerColorMap

    @staticmethod
    def formater(pattern, message, tag, tag_max, date, time, obj=None, additional=None):
        if additional is None:
            additional = {"additional": ""}
        if obj is None:
            obj = {"obj": ""}
        now = datetime.datetime.now()
        if len(tag) < tag_max:
            empty = f"{NewLifeUtils.ACC.RESET}" + " " * (tag_max - len(tag))
        else:
            empty = f"{NewLifeUtils.ACC.RESET}"
        return (
            f"{NewLifeUtils.ACC.RESET}{NewLifeUtils.MCC.REWRITELINE}"
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
        read = input(
            f"{NewLifeUtils.ACC.TOBRIGHT}{NewLifeUtils.BGC.BLUE}{NewLifeUtils.FGC.RED}{message}"
        )
        if tag == "":
            tag = self.loggerDefaultTag_rea
        s = f"{self.loggerNormalize}{NewLifeUtils.MCC.PREVIOUS_LINE}"
        s += self.formater(
            self.loggerPrintPattern_rea,
            message,
            tag,
            self.loggerTagMaxLenght,
            self.loggerDateTimeFormat_date,
            self.loggerDateTimeFormat_time,
            obj={"read": read},
            additional=self.loggerColorMap,
        )
        print(s)
        return read

    def read(self, message, tag=""):
        return self.rea(message, tag)

    def InitSeedgen(self):
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
                    (datetime.datetime.now().microsecond ** 3)
                    * (datetime.datetime.now().second ** 10)
                    + (datetime.datetime.now().month * datetime.datetime.now().day)
                )
            )
            return rawseed

        def seedFormater(formated, displayTemplate=""):
            if displayTemplate != "":
                try:
                    int(displayTemplate)
                except ValueError:
                    self.err(f"{displayTemplate} is not a numeric", self.SeedTag["err"])
                    self.wrn(
                        f'Reseting: "{displayTemplate}" -> "" ', self.SeedTag["wrn"]
                    )
                    displayTemplate = "4444"
            elif displayTemplate == "":
                displayTemplate = "4444"
                self.log(
                    f"Using default display - {displayTemplate}", self.SeedTag["log"]
                )
            else:
                self.log(
                    f"Using non def display - {displayTemplate}", self.SeedTag["log"]
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


# noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
def Demonstration(nlu):
    CSI = "\x1B["

    s = ""
    for r in range(1, 3):
        for n in range(0, 128):
            s += CSI + f"38;2;{n * r};0;0m" + "█" + CSI + "0m"
        print(s)
        s = ""
    s = ""
    for r in range(1, 3):
        for n in range(0, 128):
            s += CSI + f"38;2;0;{n * r};0m" + "█" + CSI + "0m"
        print(s)
        s = ""
    s = ""
    for r in range(1, 3):
        for n in range(0, 128):
            s += CSI + f"38;2;;0;{n * r}m" + "█" + CSI + "0m"
        print(s)
        s = ""
    s = ""

    def screate(s, n):
        space = " " * (int(n) - len(str(s)))
        return space + str(s)

    for r in range(16, 256, 36):
        for n in range(0, 36):
            if (r + n) > 255:
                s += CSI + "0m   "
            else:
                s += (
                    CSI
                    + f"38;5;{r + n}m"
                    + f"█{CSI + '7m'}{screate(str(r + n), 3)}"
                    + CSI
                    + "0m"
                )
        print(s)
        s = ""
    nlu = NewLifeUtils(silent=True)
    s = ""
    for b in range(16, 256, 36):
        for c in range(1, 36):
            if (b + c) > 255:
                s += CSI + "0m   "
            else:
                # noinspection PyTypeChecker
                s += nlu.ACC.BCUSTOMD(b + c) + screate(b + c, 4)
        print(s)
        s = ""
    print(nlu.ACC.RESET)
    for b in range(16, 256, 36):
        for c in range(1, 36):
            if (b + c) > 255:
                s += CSI + "0m   "
            else:
                # noinspection PyTypeChecker
                s += nlu.ACC.CUSTOMD(b + c) + screate(b + c, 4)
        print(s)
        s = ""
    print(nlu.BGC.WHITE)
    for b in range(16, 256, 36):
        for c in range(1, 36):
            if (b + c) > 255:
                s += CSI + "0m   "
            else:
                # noinspection PyTypeChecker
                s += nlu.ACC.CUSTOMD(b + c) + screate(b + c, 4)
        print(s)
        s = ""
    s = ""
    s2 = ""
    s3 = ""
    for b in range(1, 255, 6):
        for c in range(1, 255, 5):
            # noinspection PyTypeChecker
            s += nlu.ACC.CUSTOM(255, b, c) + "█"
            # noinspection PyTypeChecker
            s2 += nlu.ACC.CUSTOM(b, 255, c) + "█"
            # noinspection PyTypeChecker
            s3 += nlu.ACC.CUSTOM(b, c, 255) + "█"
        print(s + s2 + s3)
        s = ""
        s2 = ""
        s3 = ""
    s = ""
    s2 = ""
    s3 = ""
    for b in range(1, 255, 6):
        for c in range(1, 255, 5):
            # noinspection PyTypeChecker
            s += nlu.ACC.CUSTOM(0, 255 - b, 255 - c) + "█"
            # noinspection PyTypeChecker
            s2 += nlu.ACC.CUSTOM(255 - b, 0, 255 - c) + "█"
            # noinspection PyTypeChecker
            s3 += nlu.ACC.CUSTOM(255 - b, 255 - c, 0) + "█"
        print(s + s2 + s3)
        s = ""
        s2 = ""
        s3 = ""
    s = ""
    s2 = ""
    s3 = ""
    for b in range(1, 255, 6):
        for c in range(1, 255, 100):
            # noinspection PyTypeChecker
            s += (
                nlu.FGC.BLACK
                + nlu.ACC.BCUSTOM(255, b, c)
                + f"|255,{screate(b, 3)},{screate(c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s2 += (
                nlu.FGC.BLACK
                + nlu.ACC.BCUSTOM(b, 255, c)
                + f"|{screate(b, 3)},255,{screate(c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s3 += (
                nlu.FGC.BLACK
                + nlu.ACC.BCUSTOM(b, c, 255)
                + f"|{screate(b, 3)},{screate(c, 3)},255"
                + nlu.ACC.RESET
            )
        print(s + s2 + s3)
        s = ""
        s2 = ""
        s3 = ""
    s = ""
    s2 = ""
    s3 = ""
    # asd
    ####################################################
    for b in range(1, 255, 6):
        for c in range(1, 255, 100):
            # noinspection PyTypeChecker
            s += (
                nlu.ACC.BCUSTOM(0, 255 - b, 255 - c)
                + f"|  0,{screate(255 - b, 3)},{screate(255 - c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s2 += (
                nlu.ACC.BCUSTOM(255 - b, 0, 255 - c)
                + f"|{screate(255 - b, 3)},  0,{screate(255 - c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s3 += (
                nlu.ACC.BCUSTOM(255 - b, 255 - c, 0)
                + f"|{screate(255 - b, 3)},{screate(255 - c, 3)},  0"
                + nlu.ACC.RESET
            )
        print(s + s2 + s3)
        s = ""
        s2 = ""
        s3 = ""
    s = ""
    s2 = ""
    s3 = ""
    for b in range(1, 255, 6):
        for c in range(1, 255, 100):
            # noinspection PyTypeChecker
            s += (
                nlu.ACC.CUSTOM(255, b, c)
                + f"|255,{screate(b, 3)},{screate(c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s2 += (
                nlu.ACC.CUSTOM(b, 255, c)
                + f"|{screate(b, 3)},255,{screate(c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s3 += (
                nlu.ACC.CUSTOM(b, c, 255)
                + f"|{screate(b, 3)},{screate(c, 3)},255"
                + nlu.ACC.RESET
            )
        print(s + s2 + s3)
        s = ""
        s2 = ""
        s3 = ""
    print(nlu.ACC.NOTNEGATIVE + nlu.ACC.RESET)
    s = ""
    s2 = ""
    s3 = ""
    for b in range(1, 255, 6):
        for c in range(1, 255, 100):
            # noinspection PyTypeChecker
            s += (
                nlu.ACC.CUSTOM(0, 255 - b, 255 - c)
                + f"|  0,{screate(255 - b, 3)},{screate(255 - c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s2 += (
                nlu.ACC.CUSTOM(255 - b, 0, 255 - c)
                + f"|{screate(255 - b, 3)},  0,{screate(255 - c, 3)}"
                + nlu.ACC.RESET
            )
            # noinspection PyTypeChecker
            s3 += (
                nlu.ACC.CUSTOM(255 - b, 255 - c, 0)
                + f"|{screate(255 - b, 3)},{screate(255 - c, 3)},  0"
                + nlu.ACC.RESET
            )
        print(s + s2 + s3)
        s = ""
        s2 = ""
        s3 = ""

    def CUSTOM(r, g, b):
        CSI = "\x1B["
        return CSI + f"38;2;{r};{g};{b}m"

    print(s)
    print(CUSTOM(235, 235, 235) + "████████████████████████████████████████████")
    print(CUSTOM(235, 235, 235) + "████████████████████████████████████████████")
    print(CUSTOM(3, 69, 252) + "████████████████████████████████████████████")
    print(CUSTOM(3, 69, 252) + "████████████████████████████████████████████")
    print(CUSTOM(204, 43, 43) + "████████████████████████████████████████████")
    print(CUSTOM(204, 43, 43) + "████████████████████████████████████████████")
    nlu.log(f"This is a log")
    nlu.log(f"This is a log with custom tag", "MyTag1")
    nlu.tip(f"This is a tip")
    nlu.tip(f"This is a tip with custom tag", "MyTag2")
    nlu.wrn(f"This is a warn")
    nlu.wrn(f"This is a warn with custom tag", "MyTag3")
    nlu.err(f"This is a error")
    nlu.err(f"This is a error with custom tag", "MyTag4")
    randList = []
    for i in range(1, 100):
        randList.append(random.randrange(1, 100))
    nlu.setSeed(
        nlu.rea(f"Enter your seed or empty for auto:"),
        nlu.rea(f"Enter display appearance:"),
    )
    nlu.log("I will select one of 100 elements from list", "MySelect")
    nlu.wrn(f"RESULT IS {nlu.randselect(randList)}", "MySelect")


from PIL import Image


def de(nlu, r=""):
    r, g, b = 0, 0, 0
    s = ""
    path = "C:/Users/NewLi/Desktop"
    img = Image.open(path + "/test.png")
    print(img)
    for y in range(img.size[1]):

        for x in range(img.size[0]):
            r = img.getpixel((x, y))[0] + random.randrange(40)
            g = img.getpixel((x, y))[1] + random.randrange(40)
            b = img.getpixel((x, y))[2] + random.randrange(40)
            s += nlu.ACC.BCUSTOM(r, g, b) + " "
        print(s + nlu.ACC.RESET)
        s = ""


# TODO: get colors as dict


def main():
    nlu = NewLifeUtils(silent=True)
    nlu.setSeed("", "9")
    for i in range(5):
        r = random.randrange(111111111, 999999999)
        nlu.wrn(r)
    Demonstration(nlu)

    input()


if __name__ == "__main__":
    main()
