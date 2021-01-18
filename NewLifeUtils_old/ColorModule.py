from os import system
system('')

class BGC:
    BLACK 	 	 = "\x1B[40m"
    RED 	 	 = "\x1B[41m"
    GREEN 	 	 = "\x1B[42m"
    YELLOW 	 	 = "\x1B[43m"
    BLUE 	 	 = "\x1B[44m"
    PURPLE 	 	 = "\x1B[45m"
    CYAN 	 	 = "\x1B[46m"
    BGRAY 	 	 = "\x1B[47m"
    GRAY 	 	 = "\x1B[100m"
    BRED 	 	 = "\x1B[101m"
    LIME 	 	 = "\x1B[102m"
    BYELLOW 	 	 = "\x1B[103m"
    BBLUE 	 	 = "\x1B[104m"
    MAGENTA 	 	 = "\x1B[105m"
    BCYAN 	 	 = "\x1B[106m"
    WHITE 	 	 = "\x1B[107m"
class FGC:
    BLACK 	  = "\x1B[30m"
    RED 	  = "\x1B[31m"
    GREEN 	  = "\x1B[32m"
    YELLOW 	  = "\x1B[33m"
    BLUE 	  = "\x1B[34m"
    PURPLE 	  = "\x1B[35m"
    CYAN 	  = "\x1B[36m"
    BGRAY 	  = "\x1B[37m"
    GRAY 	  = "\x1B[90m"
    BRED 	  = "\x1B[91m"
    LIME 	  = "\x1B[92m"
    BYELLOW 	 = "\x1B[93m"
    BBLUE 	  = "\x1B[94m"
    MAGENTA 	 = "\x1B[95m"
    BCYAN 	  = "\x1B[96m"
    WHITE 	  = "\x1B[97m"
class ACC:
    RESET = "\x1B[0m"
    RELOAD = "\x1B[!p" 
    CLEARSCREEN = "\x1Bc"
    
    BRIGHT = "\x1B[1m"
    NO_BRIGHT = "\x1B[2m"
    
    UNDERLINE = "\x1B[4m"
    NO_UNDERLINE = "\x1B[24m"
    
    REVERSE = "\x1B[7m"
    NO_REVERSE = "\x1B[27m"
    
    ALTERNATIVE_BUFF = '\x1B[?1049h'
    ORIGINAL_BUFF = '\x1B[?1049l'
    
    def TITLE(title):
        return f"\x1B]2;{title}\x07"
    

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
    CURSOR_DBLINK = '\x1B[?12h'
    CURSOR_EBLINK = '\x1B[?12l'
    CURSOR_HIDE = '\x1B[?25l'
    CURSOR_SHOW = '\x1B[?25h'
    
    ERASE_NXT_WINDOW = '\x1B[0J'
    ERASE_PRV_WINDOW = '\x1B[1J'
    ERASE_ALL_WINDOW = '\x1B[2J'
    ERASE_NXT_LINE = '\x1B[0K'
    ERASE_PRV_LINE = '\x1B[1K'
    ERASE_ALL_LINE = '\x1B[2K'
    SET_TAB = '\x1BH'
    DEL_TAB = '\x1B[0g'
    RES_TAB = '\x1B[3g'
    
    def UP(count = 1):
        return f"\x1B[{count}A"

    def DOWN(count = 1):
        return f"\x1B[{count}B"

    def RIGHT(count = 1):
        return f"\x1B[{count}C"

    def LEFT(count = 1):
        return f"\x1B[{count}D"
        
    def ROW(count = 1):
        return f"\x1B[{count}G"

    def CURSORPOSITION(x, y):
        return f"\x1B[{x};{y}H"
    def SAVE_CURSOR():
        return "\x1B[s"
    def LOAD_CURSOR():
        return "\x1B[u"
    def SCROLL_DOWN(count):
        return f"\x1B[{count}T"
    def SCROLL_UP(count):
        return f"\x1B[{count}S"
        
    def PUSH_RIGHT(count):
        return f"\x1B[{count}@"
    def ERASE_RIGHT(count):
        return f"\x1B[{count}P"
    def REPLACE_RIGHT(count):
        return f"\x1B[{count}X"
    def PUSH_DOWN(count):
        return f"\x1B[{count}L"
    def ERASE_DOWN(count):
        return f"\x1B{count}M"
        
    def NEXT_TAB(count):
        return f"\x1B{count}I"
    def PREV_TAB(count):
        return f"\x1B{count}Z"
class CUF:
    pass