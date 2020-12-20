# -*- coding: utf-8 -*-
###################################################################################################
# Docs 1.0 ########################################################################################
###################################################################################################
#+-------------------------------------------:---------------------------------------------------+#
#|  class NewLifeUtils                       | Main Class of utils                               |#
#|    - name                                 |    = NewLifeUtils                                 |#
#|    - version                              |    = 5.0.0                                        |#
#|    - description                          |    = 5th generation!                              |#
#|    - workingDirectory                     |    = E:\Pydev\NLUDIR                              |#
#|    - curentDirectory                      |    = E:\Pydev\                                    |#
#|    - configName                           |    = config.json                                  |#
#|    - module__                             | After init, u cam use all modules                 |#
#|                                           |                                                   |#
#|    * /initialize                          |    RQ: silent(False)                              |#
#|                                           |                                                   |#
#|    * demo                                 | Demo console that allows you to show all          |#
#|    > - -                                  | the features of this project                      |#
#|                                           |                                                   |#
#|    + LibsManager                          | Storage for streamlined access to libraries       |#
#|        * /initialize                      |    RQ: nlu       A: os=import...                  |#
#|        - os                               |    T: class                                       |#
#|        - random                           |    T: class                                       |#
#|        - time                             |    T: class                                       |#
#|        - datetime                         |    T: class                                       |#
#|        - sqlite3                          |    T: class                                       |#
#|        * getLib                           |    RQ: name  RT: class                            |#
#|                                           |                                                   |#
#|    + ColorManager                         | Provides color output capabilities                |#
#|        * /initialize                      |    RQ: nlu       A: os('')...                     |#
#|        = FGC                              |    T: class                                       |#
#|        = BGC                              |    T: class                                       |#
#|        = ACC                              |    T: class                                       |#
#|        = MCC                              |    T: class                                       |#
#|                                           |                                                   |#
#|    + LoggerManager                        | Provides the ability to display information       |#
#|    > - - - - - - -                        | in an orderly manner on the screen                |#
#|        * log                              |    R: message, tag                                |#
#|        * wrn                              |    R: message, tag                                |#
#|        * err                              |    R: message, tag                                |#
#|        * tip                              |    R: message, tag                                |#
#|        * load                             |    R: message, tag                                |#
#|        * custom                           |    R: message, tag                                |#
#|        * read                             |    R: message, tag                                |#
#|                                           |                                                   |#
#|    + RandomManager                        | A module that provides a redesigned API           |#
#|    > - - - - - - -                        | for working with pseudo-random numbers            |#
#|        - LastSeed                         |                                                   |#
#|        - Seeds                            |                                                   |#
#|        * createNewSeed                    |                                                   |#
#|        * getByID                          |                                                   |#
#|        * getLast                          |                                                   |#
#|                                           |                                                   |#
#|    + TableManager                         | Module for working with tables, displaying        |#
#|    |                                      | them on the screen and arranging them             |#
#|    > - - - - - - -                        | inside the table itself                           |#
#|        * createTable                      |                                                   |#
#|                                           |                                                   |#
#|    + DatabaseManager                      | A specialized class for working with databases    |#
#|    |                                      | and data inside them. It allows you to simplify   |#
#|    |                                      | working with them as much as possible, but due to |#
#|    |                                      | the size of the original API, it does not allow   |#
#|    |                                      | you to implement absolutely all functions,        |#
#|    > - - - - - - - -                      | so this class also provides access to direct      |#
#|                                           | database management                               |#
#|        * /initialize                      |                                                   |#
#|        - connectionState                  |                                                   |#
#|        - databaseName                     |                                                   |#
#|        - databasePath                     |                                                   |#
#|        - tableList                        |                                                   |#
#|        * startConnection                  |                                                   |#
#|        * closeConnection                  |                                                   |#
#|                                           |                                                   |#
#|    + ConsoleShellManager                  | ConsoleShell is a module that automates user      |#
#|    |                                      | input and output, creates the right               |#
#|    |                                      | development environment, and provides the         |#
#|    > - - - - - - - - - -                  | right API                                         |#
#|        * /initialize                      |                                                   |#
#|        * registerAction                   |                                                   |#
#|        * registerCommand                  |                                                   |#
#|        * registerExitTask                 |                                                   |#
#|        * registerInitTask                 |                                                   |#
#|                                           |                                                   |#
#|    + FileManager                          | Wrapper module for simplified file management     |#
#|        - currentDirectory                 |                                                   |#
#|        * openFile                         |                                                   |#
#|        * readFile                         |                                                   |#
#|        * renameFile                       |                                                   |#
#|        * copyFile                         |                                                   |#
#|        * cutFile                          |                                                   |#
#|        * closeFile                        |                                                   |#
#|        * saveFile                         |                                                   |#
#|        * goto                             |                                                   |#
#|                                           |                                                   |#
#|    + StringManager                        | Module with additional options for                |#
#|    > - - - - - - -                        | processing and converting strings                 |#
#|        * parseInput                       |                                                   |#
#|                                           |                                                   |#
#|    + TracebackManager                     | An additional module for working with             |#
#|    > - - - - - - -                        | errors during the execution of your code          |#
#|        * printTraseback                   |                                                   |#
#|        * getTraseback                     |                                                   |#
#|        * getArgs                          |                                                   |#
#|                                           |                                                   |#
#|                                           |                                                   |#
#|    + Utils                                | List of various other functions and add-ons       |#
#|    > - - -                                | that are not included in the above modules        |#
#|        - randomListSelect                 |                                                   |#
#|        - printBig                         |                                                   |#
#|                                           |                                                   |#
#|    + FileLogger                           | Add-on for working with files                     |#
#|      - direction                          |                                                   |#
#|      - fileName                           |                                                   |#
#|      * /initialize                        |                                                   |#
#|                                           |                                                   |#
#|                                           |                                                   |#
#|                                           |                                                   |#
#|      +---------------------------+        |                                                   |#
#|      |  <3  self  5.0.Xv |        |                                                   |#
#|      +---------------------------+        |                                                   |#
#|      | ***   --- KOTAZ ---   *** |        |                                                   |#
#|      +---------------------------+        |                                                   |#
#|                                           |                                                   |#
#+-------------------------------------------:---------------------------------------------------+#
###################################################################################################

####################################################################
#+----------------------------------------------------------------+#
#|   LibsManager              Color               Logger          |#
#|   RandomManager            TableManager        DatabaseManager |#
#|   ConsoleShellManager      FileManager         StringManager   |#
#|   TracebackManager         FilelogManager      Utils           |#
#+----------------------------------------------------------------+#
####################################################################


class NewLifeUtils(object):
    def __init__(self, silent = False):
        #Var set##Var set##Var set##Var set#
        
        #Init libs
        self.libsManager_os = __import__("os")
        self.libsManager_random = __import__("random")
        self.libsManager_datetime = __import__("datetime")
        self.libsManager_time = __import__("time")
        self.libsManager_sqlite3 = __import__("sqlite3")
        

        
        #Init logger
        self.loggerErrFormat="{white}[{time}] {red}{tag}{empty}: {red}{message}"
        self.loggerLogFormat="{white}[{time}] {green}{tag}{empty}{reset}: {green}{message}{reset}"
        self.loggerWrnFormat="{white}[{time}] {yellow}{tag}{empty}{reset}: {yellow}{message}{reset}"
        self.loggerReaFormat="{white}[{time}] {blue}{tag}{empty}{reset}: {blue}{message} {cyan}[{read}]{reset}"
        self.loggerTipFormat="{white}[{time}] {cyan}{tag}{empty}{reset}: {magenta}{message}{reset}"
        
        self.loggerErrDefaultTag="Error"
        self.loggerLogDefaultTag="Log"
        self.loggerWrnDefaultTag="Warn"
        self.loggerReaDefaultTag="Input"
        self.loggerTipDefaultTag="Tips"
        self.loggerDateFormat="%d-%m-%Y"
        self.loggerTimeFormat="%H:%M:%S"
        self.loggerTagMaxLenght=8
        
        self.loggerColorMap = {
                "black": self.Color_CUSTOMRGB(31, 31, 31),
                "gray": self.Color_CUSTOMRGB(219, 219, 219),
                "red": self.Color_CUSTOMRGB(245, 23, 23),
                "green": self.Color_CUSTOMRGB(13, 209, 39),
                "yellow": self.Color_CUSTOMRGB(235, 200, 23),
                "blue": self.Color_CUSTOMRGB(0, 98, 235),
                "magenta": self.Color_CUSTOMRGB(227, 23, 193),
                "cyan": self.Color_CUSTOMRGB(24, 212, 222),
                "white": self.Color_CUSTOMRGB(247, 247, 247),
                "reset": self.Color_ACC.RESET+self.Color_ACC.AFTERCLEAN,
            }
            
        #init table
        self.tableManagerOneLine = "┌┬┐│─├┼┤└┴┘"
        self.tableManagerTwoLine = "╔╦╗║═╠╬╣╚╩╝"
        self.tableManagerDoubleH = "╓╥╖║─╟╫╢╙╨╜"
        self.tableManagerDoubleV = "╒╤╕│═╞╪╡╘╧╛"
        self.tableManagerCurrent = self.tableManagerTwoLine
        
        #Var set##Var set##Var set##Var set#
        
        
        
        #init color
        self.libsManager_os.system('')
        
        
        
        #Init NewLifeUtils
        self.name = 'NewLifeUtils'
        self.version = '5.0.3'
        self.description = 'Utils For You! <3'
        self.curentDirectory = self.libsManager_os.getcwd()
        self.workingDirectory = self.curentDirectory + r'\NLUDIR'
        self.configName = 'config.json'
        self.logName = 'log-_date_.log'
        
        if not silent:
            y = self.Color_FGC.YELLOW
            w = self.Color_FGC.WHITE
            r = self.Color_FGC.RED
            gn = self.Color_FGC.GREEN
            gy = self.Color_FGC.GRAY
            self.loggerLog(f'\n{y}+------------------------- Started  ----------------------------{y}+\n'
            +f'{y}|{gy}Module name: {w}LibsManager              {gy}Status: {gn}    Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}RandomManager            {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}ConsoleShellManager      {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}TracebackManager         {gy}Status: {gn}    Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}Color                    {gy}Status: {gn}    Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}TableManager             {gy}Status: {y }    Working...   {y}|\n'
            +f'{y}|{gy}Module name: {w}FileManager              {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}FilelogManager           {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}Logger                   {gy}Status: {gn}    Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}DatabaseManager          {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}StringManager            {gy}Status: {gn}    Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}Utils                    {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}+------------------------- Complete ----------------------------{y}+\n', 'NLU5')
            data = [
            f'{gy}Module name            ',f'{gy}Status                  ',
            f'{w }LibsManager            ',f'{gn}Initializated           ',
            f'{w }RandomManager          ',f'{r }Not Initializated       ',
            f'{w }ConsoleShellManager    ',f'{r }Not Initializated       ',
            f'{w }TracebackManager       ',f'{gn}Initializated           ',
            f'{w }Color                  ',f'{gn}Initializated           ',
            f'{w }TableManager           ',f'{gn}Initializated           ',
            f'{w }FileManager            ',f'{r }Not Initializated       ',
            f'{w }FilelogManager         ',f'{r }Not Initializated       ',
            f'{w }Logger                 ',f'{gn}Initializated           ',
            f'{w }DatabaseManager        ',f'{r }Not Initializated       ',
            f'{w }StringManager          ',f'{gn}Initializated           ',
            f'{w }Utils                  ',f'{r }Not Initializated       ',
            
            ]# tableElement = '+++|-++++++',
            self.loggerLog(self.tableManagerCreateTable(2, [23,24], data, title = '', color = y, align = 'r'))
######################### COLOR ###################################     
    class Color_BGC:
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

    class Color_FGC:
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

    class Color_ACC:
        AFTERCLEAN = "\x1B[K"
        RESET = "\x1B[0m"
        UNDERLINE = "\x1B[4m"
        SWAP = "\x1B[7m"
        NOTNEGATIVE = "\x1B[27m"
        TOBRIGHT = "\x1B[1m"
        NOBRIGHT = "\x1B[2m"

    def Color_CLEARSCREEN(self, ):
        self.LibsManager_os.system("cls")
        return ""

    def Color_RANDOMRGB(self, mode="Color"):
        if mode not in ["Color", "gray"]:
            mode = "Color"
        if mode == "Color":
            r, g, b = (
                self.libsManager_random.randrange(0, 255),
                self.libsManager_random.randrange(0, 255),
                self.libsManager_random.randrange(0, 255),
            )
        else:
            r = self.libsManager_random.randrange(0, 255)
            g = r
            b = r
        return f"\x1B[38;2;{r};{g};{b}m"

    def Color_RANDOMD(self,):
        n = self.libsManager_random.randrange(0, 255)
        return f"\x1B[38;5;{n}m"

    def Color_CUSTOMRGB(self, r, g, b):
        return f"\x1B[38;2;{r};{g};{b}m"

    def Color_CUSTOMC(self, n):
        return f"\x1B[38;5;{n}m"

    def Color_BCUSTOMRGB(self, r, g, b):
        return f"\x1B[48;2;{r};{g};{b}m"

    def BCUSTOMC(n):
        return f"\x1B[48;5;{n}m"

    class Color_MCC:

        GOTO_FIRSTLINE = "\x1B[1G"
        GOTO_NEXTLINE = "\x1B[E"
        GOTO_PREVIOUSLINE = "\x1B[F"
        ERASELINE = "\x1B[2K"
        REWRITELINE = "\x1B[1G"
    def Color_UP(self, count):
        return f"\x1B[{count}A"

    def Color_DOWN(self, count):
        return f"\x1B[{count}B"

    def Color_RIGHT(self, count):
        return f"\x1B[{count}V"

    def Color_LEFT(self, count):
        return f"\x1B[{count}D"

    def Color_CURSORPOSITION(self, x, y):
        return f"\x1B[{x};{y}H"
######################### COLOR ###################################     
######################### LOGGER ##################################
    def loggerFormatter(self, pattern, message, tag, tag_max, date, time, additional=None):
        if additional is None:
            additional = {"void": ""}

        now = self.libsManager_datetime.datetime.now()
        if len(tag) < tag_max:
            empty = f"{self.Color_ACC.RESET}" + " " * (tag_max - len(tag))
        else:
            empty = f"{self.Color_ACC.RESET}"
        return (
            f"{self.Color_ACC.RESET}{self.Color_MCC.REWRITELINE}"
            + pattern.format(
                **self.loggerColorMap,
                **additional,
                date=now.strftime(date),
                time=now.strftime(time),
                tag=tag,
                empty=empty,
                tab="\t",
                message=message,
            )
        )

    def loggerLog(self, message, tag=""):
        if tag == "":
            tag = self.loggerLogDefaultTag
        print(
            self.loggerFormatter(
                self.loggerLogFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def loggerWrn(self, message, tag=""):
        if tag == "":
            tag = self.loggerWrnDefaultTag
        print(
            self.loggerFormatter(
                self.loggerWrnFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def loggerErr(self, message, tag=""):
        if tag == "":
            tag = self.loggerErrDefaultTag
        print(
            self.loggerFormatter(
                self.loggerErrFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def loggerTip(self, message, tag=""):
        if tag == "":
            tag = self.loggerTipDefaultTag
        print(
            self.loggerFormatter(
                self.loggerTipFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def loggerRea(self, message, tag=""):
        if message[-1] not in [' ', '>', ':']:
            message += ': '
        print(f"{self.Color_ACC.BCUSTOMRGB(0, 43, 112)}{self.Color_ACC.CUSTOMRGB(235, 54, 30)}{message}", end = '')
        read = input()
        
        if tag == "":
            tag = self.loggerReaDefaultTag
        s = self.loggerFormatter(
            self.loggerReaFormat,
            message,
            tag,
            self.loggerTagMaxLenght,
            self.loggerDateFormat,
            self.loggerTimeFormat,
            obj={"read": read},
            additional=self.loggerColorMap,
        )
        print(self.Color_MCC.GOTO_PREVIOUSLINE+s)
        return read

########################## LOGGER #################################  
########################## STRINGMANAGER ##########################
    def stringManagerScreate(self, string, size = 10, insert = 'r'):
        import re
        matches = re.findall(r'\\x1B\[[\d;]*[a-zA-Z]{1}', string, re.MULTILINE)
        #print(matches)
        spaces = " " * (size - len(str(string)))
        if insert == 'r':
            return  str(string) + spaces
        if insert == 'l':
            return spaces + str(string)
    def stringManagerSlice(self, text, chunkSize):
        return [text[i:i+chunkSize] for i in range(0, len(text), chunkSize)] 
########################## STRINGMANAGER ##########################
########################## TRACEBACKMANAGER #######################
    def TracebackManagerExceptionPrint(self, exception, exceptionType = 'err', tb = True):
        
        errorText =  "\n-------------- {title} --------------------\n"
        errorText += f"Type: {type(exception).__name__}\n\n"
        
        if exception.args == 0:
            errorText += f"Unknown error\n"
        else: 
            errorText += f"About Error:\n\t{(chr(10)+chr(9)).join(exception.args)}\t\n"
        
        if tb:
            import traceback
            errorText +=f"\n{traceback.format_exc()}"
            
        errorText += "\n-------------- {title} --------------------\n"
        
        if exceptionType == 'attention':
            self.loggerLog(errorText.format(title=self.stringManagerScreate('Attention!', 20)))
        if exceptionType == 'wrn':
            self.loggerWrn(errorText.format(title=self.stringManagerScreate('Warning!', 20)))
        elif exceptionType == 'err':
            self.loggerErr(errorText.format(title=self.stringManagerScreate('Error!', 20)))
        elif exceptionType == 'fatal':
            self.loggerErr(errorText.format(title=self.stringManagerScreate('Fatal Error!', 20)))
            exit(-1)
        else:
            self.loggerErr(errorText.format(title=self.stringManagerScreate('Something wrong...', 20)))
            
            
########################## TRACEBACKMANAGER #######################
########################## TABLEMANAGER   #######################
    def tableManagerCreateTable(self, rowCount, sizes, data, title = 'TABLE', header = True, tableElement = '', color = Color_FGC.CYAN, align = 'l'):
        if align == 'r':
            align = 'l'
        else:
            align = 'r'
        # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝       
        # 0  1  2  3  4  5  6  7  8  9  10  
        
        if tableElement == '':
            tableElement = self.tableManagerCurrent

        result = ''
        
        #Generate Header-line
        result += f'{color}{tableElement[0]}'
        
        for sizen in range(rowCount):
            result += f'{color}{tableElement[4]*sizes[sizen]}{color}{tableElement[1]}'
        result = result[:-1] + f'{color}{tableElement[2]}'
        
        #Generate Header
        if header:
            result += f'\n{color}{tableElement[3]}'
            for num in range(rowCount):
                result += f'{self.stringManagerScreate(data[num], sizes[num], align)}{color}{tableElement[3]}'
            result += f'\n{color}{tableElement[5]}'    
            for headerPieceSize in sizes:
                result += f'{color}{tableElement[4]*headerPieceSize}{color}{tableElement[6]}'
            result = result[:-1] + f'{color}{tableElement[7]}'
            data = data[rowCount:]
        
        #Generate DataSection
        for lineNum in range(0, len(data), rowCount):
            result += f'\n{color}{tableElement[3]}'
            for rowShift in range(0, rowCount):
                try:
                    result += f'{self.stringManagerScreate(data[lineNum+rowShift], sizes[rowShift], align)}{color}{tableElement[3]}'
                except:
                    result += f'{self.stringManagerScreate("", sizes[rowShift], align)}{color}{tableElement[3]}'
        result += f'\n{color}{tableElement[8]}'
        
        #Generate Footer-line
        for sizen in range(rowCount):
            result += f'{color}{tableElement[4]*sizes[sizen]}{color}{tableElement[9]}'
        result = result[:-1] + f'{color}{tableElement[10]}{self.Color_ACC.RESET}'
        
        return f'\n{self.stringManagerScreate(title, round(sum(sizes)/2), "l")}\n{result}\n'
    def tableManagerCreateBigTable(self, rowCount, sizes, data, title = 'TABLE', tableElement = '', color = Color_FGC.CYAN, align = 'l'):
        if align == 'r':
            align = 'l'
        else:
            align = 'r'
        # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝       
        # 0  1  2  3  4  5  6  7  8  9  10 
        # +  +  +  |  -  +  +  +  +  +  +       
        # 0  1  2  3  4  5  6  7  8  9  10; , tableElement = '+++|-++++++'
        if tableElement == '':
            tableElement = self.tableManagerCurrent
        for i in range(len(data)):
            data[i] = self.stringManagerSlice(data[i],sizes[i%len(sizes)])
        result = ''
        for line in range(0, len(data),rowCount):
            maxtabsize = 0
            for row in range(0, rowCount):
                if len(data[line+row]) > maxtabsize:
                    maxtabsize = len(data[line+row])
            for row in range(0, rowCount):
                if len(data[line+row]) < maxtabsize:
                    while len(data[line+row]) < maxtabsize:
                        data[line+row].append('')
            
        
        #Generate Header-line
        result += f'{color}{tableElement[0]}'
        for headerPieceSize in sizes:
            result += f'{color}{tableElement[4]*headerPieceSize}{color}{tableElement[1]}'
        result = result[:-1] + f'{color}{tableElement[2]}\n'
        
        
        
        #Generate DataSection
        for line in range(0, len(data),rowCount):
            block = []
            
            for row in range(0, rowCount):
                for blockLineNum in range(len(data[line+row])):
                    try:
                        block[blockLineNum] += f'{tableElement[3]}{self.stringManagerScreate(data[line+row][blockLineNum],sizes[row], align)}'
                    except:
                        block.append(f'{tableElement[3]}{self.stringManagerScreate(data[line+row][blockLineNum],sizes[row], align)}')
            for blockLineNum in range(len(data[line+row])):
                block[blockLineNum] += tableElement[3]
            for line in block:
                result += f'{line}\n'
                
            result += f'{tableElement[5]}'
            for headerPieceSize in sizes:
                result += f'{tableElement[4]*headerPieceSize}{tableElement[6]}'
            result = result[:-1] + f'{tableElement[7]}\n'
            
        
        #Generate Footer-line
        result = result[:-1*(4+sum(sizes))]+tableElement[8]
        for headerPieceSize in sizes:
            result += f'{tableElement[4]*headerPieceSize}{tableElement[9]}'
        result = result[:-1] + f'{tableElement[10]}{self.Color_ACC.RESET}'
        
        return f'\n{self.stringManagerScreate(title+" IN DEV", round(sum(sizes)/2), "l")}\n{result}\n'
########################## TABLEMANAGER   #######################




def debug(self):
        self.loggerLog(f'{self.Color_FGC.GREEN}------------------ debug info  -----------------{self.Color_ACC.RESET}')
        self.loggerLog(f'name: {self.name} version: {self.version}')
        self.loggerLog(f'description: {self.description}')
        self.loggerLog(f'curentDirectory: {self.curentDirectory}')
        self.loggerLog(f'workingDirectory: {self.workingDirectory}')
        self.loggerLog(f'configName: {self.configName} logName: {self.logName}')
        self.loggerLog(f'Color Out: {self.Color_FGC.CYAN}HI!{self.Color_ACC.RESET}')
        self.loggerLog(f'{self.Color_FGC.GREEN}------------------ debug info  -----------------{self.Color_ACC.RESET}')
        data = []
        colorList = []
        for i in range(0,50):
            data.append(f'Item #{i}')
        
        for i in range (256):
            colorList.append(f'{self.Color_RANDOMRGB()}item{self.Color_ACC.RESET}')
        #self.loggerLog(self.tableManagerCreateTable(10, [10,10,10,10,10,10,10,10,10,10], data))
        self.loggerLog(self.tableManagerCreateTable(16, [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], colorList))
        
        #self.loggerLog(self.tableManagerCreateTable(5, [20,10,30,10,40], data))
        #self.loggerLog(self.tableManagerCreateTable(4, [30,30,10,40], data, header = False))
        #self.loggerLog(self.tableManagerCreateTable(4, [30,30,10,40], data, header = False, tableElement = '+++|-++++++'))
        
        data = [
            'Следует отметить, что разбавленное изрядной долей эмпатии, рациональное мышление создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса первоочередных требований. Но независимые государства неоднозначны и будут указаны как претенденты на роль ключевых факторов. Высокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта: семантический разбор внешних противодействий позволяет выполнить важные задания по разработке дальнейших направлений развития.',
            'А также интерактивные прототипы набирают популярность среди определенных слоев населения, а значит, должны быть ограничены исключительно образом мышления. Предварительные выводы неутешительны: разбавленное изрядной долей эмпатии, рациональное мышление представляет собой интересный эксперимент проверки переосмысления внешнеэкономических политик. Стремящиеся вытеснить традиционное производство, нанотехнологии являются только методом политического участия и ассоциативно распределены по отраслям.',
            'А также активно развивающиеся страны третьего мира будут смешаны с не уникальными данными до степени совершенной неузнаваемости, из-за чего возрастает их статус бесполезности. Современные технологии достигли такого уровня, что постоянный количественный рост и сфера нашей активности не оставляет шанса для позиций, занимаемых участниками в отношении поставленных задач. Современные технологии достигли такого уровня, что экономическая повестка сегодняшнего дня предоставляет широкие возможности для первоочередных требований. Повседневная практика показывает, что курс на социально-ориентированный национальный проект в значительной степени обусловливает важность вывода текущих активов. Есть над чем задуматься: независимые государства подвергнуты целой серии независимых исследований. Также как начало повседневной работы по формированию позиции однозначно определяет каждого участника как способного принимать собственные решения касаемо экспериментов, поражающих по своей масштабности и грандиозности!',
            'Имеется спорная точка зрения, гласящая примерно следующее: акционеры крупнейших компаний неоднозначны и будут смешаны с не уникальными данными до степени совершенной неузнаваемости, из-за чего возрастает их статус бесполезности. Для современного мира социально-экономическое развитие, в своём классическом представлении, допускает внедрение модели развития. Повседневная практика показывает, что граница обучения кадров представляет собой интересный эксперимент проверки форм воздействия.',
            'Современные технологии достигли такого уровня, что реализация намеченных плановых заданий создаёт предпосылки для системы массового участия. В рамках спецификации современных стандартов, явные признаки победы институционализации смешаны с не уникальными данными до степени совершенной неузнаваемости, из-за чего возрастает их статус бесполезности! Но элементы политического процесса будут преданы социально-демократической анафеме.',
            'Принимая во внимание показатели успешности, разбавленное изрядной долей эмпатии, рациональное мышление, в своём классическом представлении, допускает внедрение соответствующих условий активизации. Но акционеры крупнейших компаний, инициированные исключительно синтетически, подвергнуты целой серии независимых исследований.',
            'Значимость этих проблем настолько очевидна, что дальнейшее развитие различных форм деятельности является качественно новой ступенью позиций, занимаемых участниками в отношении поставленных задач. В частности, граница обучения кадров требует от нас анализа системы массового участия. В рамках спецификации современных стандартов, базовые сценарии поведения пользователей превращены в посмешище, хотя само их существование приносит несомненную пользу обществу! Безусловно, сплочённость команды профессионалов в значительной степени обусловливает важность своевременного выполнения сверхзадачи. И нет сомнений, что некоторые особенности внутренней политики могут быть объединены в целые кластеры себе подобных. Господа, разбавленное изрядной долей эмпатии, рациональное мышление влечет за собой процесс внедрения и модернизации стандартных подходов.',
            'Существующая теория играет важную роль в формировании как самодостаточных, так и внешне зависимых концептуальных решений. Есть над чем задуматься: стремящиеся вытеснить традиционное производство, нанотехнологии заблокированы в рамках своих собственных рациональных ограничений. Как принято считать, некоторые особенности внутренней политики неоднозначны и будут ассоциативно распределены по отраслям. Вот вам яркий пример современных тенденций - граница обучения кадров, а также свежий взгляд на привычные вещи - безусловно открывает новые горизонты для дальнейших направлений развития. Приятно, граждане, наблюдать, как тщательные исследования конкурентов представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть представлены в исключительно положительном свете. Противоположная точка зрения подразумевает, что базовые сценарии поведения пользователей неоднозначны и будут функционально разнесены на независимые элементы.',
            'Прежде всего, повышение уровня гражданского сознания, а также свежий взгляд на привычные вещи - безусловно открывает новые горизонты для прогресса профессионального сообщества. Также как курс на социально-ориентированный национальный проект выявляет срочную потребность укрепления моральных ценностей.',
            'Как принято считать, некоторые особенности внутренней политики являются только методом политического участия и ограничены исключительно образом мышления. Реплицированные с зарубежных источников, современные исследования и по сей день остаются уделом либералов, которые жаждут быть объективно рассмотрены соответствующими инстанциями.',
            'Учитывая ключевые сценарии поведения, современная методология разработки предопределяет высокую востребованность экспериментов, поражающих по своей масштабности и грандиозности. Каждый из нас понимает очевидную вещь: сплочённость команды профессионалов говорит о возможностях распределения внутренних резервов и ресурсов. Задача организации, в особенности же социально-экономическое развитие однозначно определяет каждого участника как способного принимать собственные решения касаемо поэтапного и последовательного развития общества. Сделанные на базе интернет-аналитики выводы набирают популярность среди определенных слоев населения, а значит, должны быть объявлены нарушающими общечеловеческие нормы этики и морали. А также интерактивные прототипы призывают нас к новым свершениям, которые, в свою очередь, должны быть разоблачены. В целом, конечно, базовый вектор развития является качественно новой ступенью системы обучения кадров, соответствующей насущным потребностям.',
            'Задача организации, в особенности же социально-экономическое развитие способствует подготовке и реализации прогресса профессионального сообщества. Идейные соображения высшего порядка, а также повышение уровня гражданского сознания напрямую зависит от направлений прогрессивного развития. Также как консультация с широким активом говорит о возможностях существующих финансовых и административных условий.',
            'Равным образом, разбавленное изрядной долей эмпатии, рациональное мышление выявляет срочную потребность направлений прогрессивного развития. Высокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта: синтетическое тестирование создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса направлений прогрессивного развития.',
            'Кстати, некоторые особенности внутренней политики неоднозначны и будут описаны максимально подробно. Идейные соображения высшего порядка, а также высокотехнологичная концепция общественного уклада предопределяет высокую востребованность глубокомысленных рассуждений. Господа, высокое качество позиционных исследований предоставляет широкие возможности для своевременного выполнения сверхзадачи.',
            'Укрепление и развитие внутренней структуры влечет за собой процесс внедрения и модернизации первоочередных требований. Для современного мира укрепление и развитие внутренней структуры представляет собой интересный эксперимент проверки соответствующих условий активизации. Таким образом, дальнейшее развитие различных форм деятельности напрямую зависит от новых принципов формирования материально-технической и кадровой базы. Являясь всего лишь частью общей картины, базовые сценарии поведения пользователей лишь добавляют фракционных разногласий и заблокированы в рамках своих собственных рациональных ограничений.',
            'Укрепление и развитие внутренней структуры влечет за собой процесс внедрения и модернизации первоочередных требований. Для современного мира укрепление и развитие внутренней структуры представляет собой интересный эксперимент проверки соответствующих условий активизации. Таким образом, дальнейшее развитие различных форм деятельности напрямую зависит от новых принципов формирования материально-технической и кадровой базы. Являясь всего лишь частью общей картины, базовые сценарии поведения пользователей лишь добавляют фракционных разногласий и заблокированы в рамках своих собственных рациональных ограничений.',
        ]
        
        
        #self.loggerLog(self.tableManagerCreateBigTable(2, [58,58], data))
        
        
        
        # print(f'{self.Color_FGC.CYAN}------------------ debug logger-----------------{self.Color_ACC.RESET}')
        # self.loggerLog(f"This is a log")
        # self.loggerLog(f"This is a log with custom tag", "MyTag1")
        # self.loggerTip(f"This is a tip")
        # self.loggerTip(f"This is a tip with custom tag", "MyTag2")
        # self.loggerWrn(f"This is a warn")
        # self.loggerWrn(f"This is a warn with custom tag", "MyTag3")
        # self.loggerErr(f"This is a error")
        # self.loggerErr(f"This is a error with custom tag", "MyTag4")
        # print(f'{self.Color_FGC.CYAN}------------------ debug logger-----------------{self.Color_ACC.RESET}')
        
        # print(f'{self.Color_FGC.CYAN}------------------ debug traceback manager -----{self.Color_ACC.RESET}')
        # try:
            # a = 1/0
        # except Exception as e:
            # e.args = e.args + ('hello',)
            # self.TracebackManagerExceptionPrint(e, 'attention', False)
            # self.TracebackManagerExceptionPrint(e, 'wrn', False)
            # self.TracebackManagerExceptionPrint(e, 'err', False)
        # print(f'{self.Color_FGC.CYAN}------------------ debug traceback manager -----{self.Color_ACC.RESET}')
        
        
if __name__ == "__main__":
    print('creating self')
    nlu = NewLifeUtils()
    debug(nlu)
    print('-')
    
    
    
    
    