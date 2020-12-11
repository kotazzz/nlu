class NewLifeUtils(object): 
    
    # ------------- ABOUT      -------------
    name = "NewLifeUtils"
    version = "v3.0.0 dev"
    description = "Utils for you <3"
    
    # ------------- STATES DEF -------------
    #none
    
    
    # ------------- LIB        -------------
    class Libs:
        try:
            os = __import__('os')
            datetime = __import__('datetime')
            random = __import__('random')
        except ImportError as ie:
            print(ie)
    # ------------- INIT       -------------
    def __init__(self, silent = False):
        self.color.init()

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
                
            def CUSTOMRGB(r, g, b):
                return f"\x1B[38;2;{r};{g};{b}m"
            def CUSTOML(n):
                return f"\x1B[38;5;{n}m"
                
            def BCUSTOMRGB(r, g, b):
                return f"\x1B[48;2;{r};{g};{b}m"
            def BCUSTOMD(n):
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

    class logger:
        pass
    class seedgen:
        pass
def demo(nlu):
    cmap = nlu.color.getColors()

    reset = nlu.color.ACC.RESET
    bg = cmap['BGC']
    fg = cmap['FGC']
    for bgc in bg.keys():
        for fgc in fg.keys():
            if bgc == fgc:
                print(f'{reset}------', end = reset)
            else:
                print(f'{bg[bgc]}{fg[fgc]}{bgc[0:3]}{fgc[0:3]}', end = reset)
        print(reset)
    print(reset) 
    
def main():
    nlu = NewLifeUtils()
    demo(nlu )
    reset = nlu.color.ACC.RESET
    
    for n1 in range (1,round(255),40):
        for n2 in range (1, round(255), 10):
            for n3 in range (1, round(255), 10):
                r = n1
                g = n2
                b = n3
                print(nlu.color.ACC.CUSTOMRGB(r,g,b)+'█', end = reset)#f'{r}{g}{b}' reset
            print()
        
    










main()
print('End')