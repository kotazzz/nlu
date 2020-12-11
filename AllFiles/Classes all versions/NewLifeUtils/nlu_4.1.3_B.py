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
            os = __import__('os')
            datetime = __import__('datetime')
            random = __import__('random')
            time = __import__('time')
        except ImportError as ie:
            print(ie)
    # ------------- INIT       -------------
    def __init__(self, silent = False, initColor = True, initLogger = True):
        if initColor:
            self.color.init()
            if not silent:
                print('Color inited')
            isInitColor = True
        if initLogger:
            self.color.init()
            if not silent:
                print('Color inited')
            isInitColor = True
            
    class Logger(object):
        def __init__(
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
            #def normalize string
            self.loggerNormalize = f"{NewLifeUtils.color.ACC.RESET}{NewLifeUtils.color.ACC.NOBRIGHT}"

            #def colormap
            self.loggerColorMap = {
                "black": NewLifeUtils.color.FGC.BLACK,
                "gray": NewLifeUtils.color.FGC.WHITE,
                "red": NewLifeUtils.color.FGC.BRED,
                "green": NewLifeUtils.color.FGC.BGREEN,
                "yellow": NewLifeUtils.color.FGC.YELLOW,
                "blue": NewLifeUtils.color.FGC.BBLUE,
                "magenta": NewLifeUtils.color.FGC.BPURPLE,
                "cyan": NewLifeUtils.color.FGC.BCYAN,
                "white": NewLifeUtils.color.FGC.BGRAY,
                "reset": NewLifeUtils.color.FGC.WHITE,
            }
            #format shielding and setting up
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
            
            #upgrading tags
            self.loggerDefaultTag_err = loggerDefaultTag_err
            self.loggerDefaultTag_log = loggerDefaultTag_log
            self.loggerDefaultTag_wrn = loggerDefaultTag_wrn
            self.loggerDefaultTag_rea = loggerDefaultTag_rea
            self.loggerDefaultTag_tip = loggerDefaultTag_tip
            #date and time format def
            self.loggerDateTimeFormat_date = loggerDateTimeFormat_date
            self.loggerDateTimeFormat_time = loggerDateTimeFormat_time
            #tag max length def
            self.loggerTagMaxLenght = loggerTagMaxLenght
        def getColorMap(self):
            return self.loggerColorMap

        @staticmethod
        def formater(pattern, message, tag, tag_max, date, time, obj=None, additional=None):
            if additional is None:
                additional = {"additional": ""}
            if obj is None:
                obj = {"obj": ""}
            now = NewLifeUtils.Libs.datetime.datetime.now()
            if len(tag) < tag_max:
                empty = f"{NewLifeUtils.color.ACC.RESET}" + " " * (tag_max - len(tag))
            else:
                empty = f"{NewLifeUtils.color.ACC.RESET}"
            return (
                f"{NewLifeUtils.color.ACC.RESET}{NewLifeUtils.color.MCC.REWRITELINE}"
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

    class color(object):
        def init():
            os = NewLifeUtils.Libs.os
            os.system('')
        class BGC:
            BLACK = "\x1B[40m"
            RED = "\x1B[41m"
            GREEN = "\x1B[42m"
            YELLOW = "\x1B[43m"
            BLUE = "\x1B[44m"
            PURPLE = "\x1B[45m"
            CYAN = "\x1B[46m"
            GRAY = "\x1B[47m"
            BGRAY = "\x1B[100m"
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
            GRAY = "\x1B[37m"
            BGRAY = "\x1B[90m"
            BRED = "\x1B[91m"
            BGREEN = "\x1B[92m"
            BYELLOW = "\x1B[93m"
            BBLUE = "\x1B[94m"
            BPURPLE = "\x1B[95m"
            BCYAN = "\x1B[96m"
            WHITE = "\x1B[97m"
        class ACC:
            
            CSI = "\x1B["
            RESET = "\x1B[0m"
            UNDERLINE = "\x1B[4m"
            SWAP = "\x1B[7m"
            NOTNEGATIVE = "\x1B[27m"
            TOBRIGHT = "\x1B[1m"
            NOBRIGHT = "\x1B[2m"
            
            def CLEARSCREEN():
                NewLifeUtils.Libs.os.system("cls")
                return ""
                
            def RANDOMRGB(mode = 'color'):
                if mode not in ['color', 'gray']:
                    mode = 'color'
                if mode == 'color':
                    r,g,b = NewLifeUtils.Libs.random.randrange(0,255),NewLifeUtils.Libs.random.randrange(0,255),NewLifeUtils.Libs.random.randrange(0,255)
                else:
                    r = NewLifeUtils.Libs.random.randrange(0,255)
                    g = r
                    b = r
                return f"\x1B[38;2;{r};{g};{b}m"
            def RANDOMD():
                n = NewLifeUtils.Libs.random.randrange(0,255)
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
                "BGC":{
            "BLACK" : "\x1B[40m",
            "RED" : "\x1B[41m",
            "GREEN" : "\x1B[42m",
            "YELLOW" : "\x1B[43m",
            "BLUE" : "\x1B[44m",
            "PURPLE" : "\x1B[45m",
            "CYAN" : "\x1B[46m",
            "GRAY" : "\x1B[47m",
            "BGRAY" : "\x1B[100m",
            "BRED" : "\x1B[101m",
            "BGREEN" : "\x1B[102m",
            "BYELLOW" : "\x1B[103m",
            "BBLUE" : "\x1B[104m",
            "BPURPLE" : "\x1B[105m",
            "BCYAN" : "\x1B[106m",
            "WHITE" : "\x1B[107m",
            },
            "FGC":{
            "BLACK" : "\x1B[30m",
            "RED" : "\x1B[31m",
            "GREEN" : "\x1B[32m",
            "YELLOW" : "\x1B[33m",
            "BLUE" : "\x1B[34m",
            "PURPLE" : "\x1B[35m",
            "CYAN" : "\x1B[36m",
            "GRAY" : "\x1B[37m",
            "BGRAY" : "\x1B[90m",
            "BRED" : "\x1B[91m",
            "BGREEN" : "\x1B[92m",
            "BYELLOW" : "\x1B[93m",
            "BBLUE" : "\x1B[94m",
            "BPURPLE" : "\x1B[95m",
            "BCYAN" : "\x1B[96m",
            "WHITE" : "\x1B[97m",
            },
            "OTH":{
            "RESET" : "\x1B[0m",
            "UNDERLINE" : "\x1B[4m",
            "SWAP" : "\x1B[7m",
            "NOTNEGATIVE" : "\x1B[27m",
            "TOBRIGHT" : "\x1B[1m",
            "NOBRIGHT" : "\x1B[2m",
            }
            }

    class seedgen:
        pass
def demo(nlu):
    #print basic map
    cmap,reset = nlu.color.getColors(),nlu.color.ACC.RESET
    bg,fg = cmap['BGC'],cmap['FGC']
    for bgc in bg.keys():
        for fgc in fg.keys():
            if bgc == fgc:
                print(f'{reset}------', end = reset)
            else:
                print(f'{bg[bgc]}{fg[fgc]}{bgc[0:3]}{fgc[0:3]}', end = reset)
        print(reset)
    print(reset)     
    #print map wit 5 colorful blocks
    for n2 in range (1, round(255), 7):
        s = ['','','','','']
        for n3 in range (1, round(255), 8):
            g = n2
            b = n3
            s[0] += nlu.color.ACC.CUSTOMRGB(0,g,b)+'█'
            s[1] += nlu.color.ACC.CUSTOMRGB(64,g,b)+'█'
            s[2] += nlu.color.ACC.CUSTOMRGB(128,g,b)+'█'
            s[3] += nlu.color.ACC.CUSTOMRGB(192,g,b)+'█'
            s[4] += nlu.color.ACC.CUSTOMRGB(256,g,b)+'█'
        print(''.join(s))#f'{r}{g}{b}' reset
    
    #Russia flag
    print(nlu.color.ACC.CUSTOMRGB(235, 235, 235) + "████████████████████████████████████████████")
    print(nlu.color.ACC.CUSTOMRGB(235, 235, 235) + "████████████████████████████████████████████")
    print(nlu.color.ACC.CUSTOMRGB(3, 69, 252) + "████████████████████████████████████████████")
    print(nlu.color.ACC.CUSTOMRGB(3, 69, 252) + "████████████████████████████████████████████")
    print(nlu.color.ACC.CUSTOMRGB(204, 43, 43) + "████████████████████████████████████████████")
    print(nlu.color.ACC.CUSTOMRGB(204, 43, 43) + "████████████████████████████████████████████")
    
    #print random 20x120
    for y in range(20):
        for x in range(120):
            print(nlu.color.ACC.RANDOMRGB()+'█', end = '')
        print()
    #print gray random 20x120
    for y in range(20):
        for x in range(120):
            print(nlu.color.ACC.RANDOMRGB('gray')+'█', end = '')
        print()
            
    #print RGB bars bars
    print()
    s = ""
    for r in range(1, 256, 64):
        for n in range(0, 64):
            s += f'{nlu.color.ACC.CUSTOMRGB(r+n,0,0)}█{reset}'
        print(s)
        s = ""
    s = ""
    for r in range(1, 256, 64):
        for n in range(0, 64):
            s += f'{nlu.color.ACC.CUSTOMRGB(0,r+n,0)}█{reset}'
        print(s)
        s = ""
    s = ""
    for r in range(1, 256, 64):
        for n in range(0, 64):
            s += f'{nlu.color.ACC.CUSTOMRGB(0,0,r+n)}█{reset}'
        print(s)
        s = ""
    s = ""
    #print CC-map (Constant Color) bars

    def screate(s, n):
        space = " " * (int(n) - len(str(s)))
        return space + str(s)
    print()
    for r in range(16, 256, 36):
        s = ''
        for n in range(0, 36):
            if (r + n) > 255:
                s += f'{reset}   '
            else:
                s += f'{nlu.color.ACC.BCUSTOMC(r+n)}{screate(str(r + n), 3)}{reset}'
        print(s+reset+'\n')
    #print colormap with rgb codes
    for n2 in range (1, round(255), 8):
        s = ['','','']
        for n3 in range (1, round(255), 70):
            g = n2
            b = n3
            red = nlu.color.ACC.CUSTOMRGB(255,0,0)
            grn = nlu.color.ACC.CUSTOMRGB(0,255-round(g/3),0)
            blu = nlu.color.ACC.CUSTOMRGB(0,0,255)
            s[0] += f'{nlu.color.ACC.BCUSTOMRGB(0,g,b)}{red}0  {grn}{screate(g,3)}{blu}{screate(b,3)}{reset}'
            s[1] += f'{nlu.color.ACC.BCUSTOMRGB(64,g,b)}{red}64 {grn}{screate(g,3)}{blu}{screate(b,3)}{reset}'
            s[2] += f'{nlu.color.ACC.BCUSTOMRGB(128,g,b)}{red}128{grn}{screate(g,3)}{blu}{screate(b,3)}{reset}'
        print(''.join(s)+reset)#f'{r}{g}{b}' reset
    class SeedGen(object):
        
def main():
    nlu = NewLifeUtils()
    logger = nlu.Logger()
    demo(nlu )
    logger.log('hi!')
    nlu.Libs.os.system('echo hi')
    logger.log(f"This is a log")
    logger.log(f"This is a log with custom tag", "MyTag1")
    logger.tip(f"This is a tip")
    logger.tip(f"This is a tip with custom tag", "MyTag2")
    logger.wrn(f"This is a warn")
    logger.wrn(f"This is a warn with custom tag", "MyTag3")
    logger.err(f"This is a error")
    logger.err(f"This is a error with custom tag", "MyTag4")









main()
print('End')