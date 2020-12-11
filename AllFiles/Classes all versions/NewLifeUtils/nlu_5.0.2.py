###################################################################################################
# Docs 1.0 ########################################################################################
###################################################################################################
#+-------------------------------------------:---------------------------------------------------+#
#|  class self                       | Main Class of utils                               |#
#|    - name                                 |    = self                                 |#
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


class self(object):
    def __init__(self, silent = False):
        #Var set##Var set##Var set##Var set#
        
        #Init libs
        self.libsManager_os = __import__("os")
        self.libsManager_random = __import__("random")
        self.libsManager_datetime = __import__("datetime")
        self.libsManager_time = __import__("time")
        self.libsManager_sqlite3 = __import__("sqlite3")
        

        
        #Init libs
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
                "black": self.Color_ACC.CUSTOMRGB(31, 31, 31),
                "gray": self.Color_ACC.CUSTOMRGB(219, 219, 219),
                "red": self.Color_ACC.CUSTOMRGB(245, 23, 23),
                "green": self.Color_ACC.CUSTOMRGB(13, 209, 39),
                "yellow": self.Color_ACC.CUSTOMRGB(235, 200, 23),
                "blue": self.Color_ACC.CUSTOMRGB(0, 98, 235),
                "magenta": self.Color_ACC.CUSTOMRGB(227, 23, 193),
                "cyan": self.Color_ACC.CUSTOMRGB(24, 212, 222),
                "white": self.Color_ACC.CUSTOMRGB(247, 247, 247),
                "reset": self.Color_ACC.RESET+self.Color_ACC.AFTERCLEAN,
            }
        #Var set##Var set##Var set##Var set#
        
        
        
        #init color
        self.libsManager_os.system('')
        
        
        
        #Init self
        self.name = 'self'
        self.version = '5.0.2'
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
            +f'{y}|{gy}Module name: {w}TracebackManager         {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}Color                    {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}TableManager             {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}FileManager              {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}FilelogManager           {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}Logger                   {gy}Status: {gn}    Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}DatabaseManager          {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}StringManager            {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}|{gy}Module name: {w}Utils                    {gy}Status: {r }Not Initializated{y}|\n'
            +f'{y}+------------------------- Complete ----------------------------{y}+\n', 'NLU5')
##########################COLOR####################################     
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

        def CLEARSCREEN():
            self.LibsManager_os.system("cls")
            return ""

        def RANDOMRGB(mode="Color"):
            if mode not in ["Color", "gray"]:
                mode = "Color"
            if mode == "Color":
                r, g, b = (
                    self.LibsManager_random.randrange(0, 255),
                    self.LibsManager_random.randrange(0, 255),
                    self.LibsManager_random.randrange(0, 255),
                )
            else:
                r = self.LibsManager_random.randrange(0, 255)
                g = r
                b = r
            return f"\x1B[38;2;{r};{g};{b}m"

        def RANDOMD():
            n = self.LibsManager_random.randrange(0, 255)
            return f"\x1B[38;5;{n}m"

        def CUSTOMRGB(r, g, b):
            return f"\x1B[38;2;{r};{g};{b}m"

        def CUSTOMC(n):
            return f"\x1B[38;5;{n}m"

        def BCUSTOMRGB(r, g, b):
            return f"\x1B[48;2;{r};{g};{b}m"

        def BCUSTOMC(n):
            return f"\x1B[48;5;{n}m"

    class Color_MCC:
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
##########################COLOR####################################     
##########################LOGGER###################################
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

##########################LOGGER###################################  



def debug(self):
        print(f'{self.Color_FGC.GREEN}------------------ debug info  -----------------{self.Color_ACC.RESET}')
        print(f'name: {self.name} version: {self.version}')
        print(f'description: {self.description}')
        print(f'curentDirectory: {self.curentDirectory}')
        print(f'workingDirectory: {self.workingDirectory}')
        print(f'configName: {self.configName} logName: {self.logName}')
        print(f'Color Out: {self.Color_FGC.CYAN}HI!{self.Color_ACC.RESET}')
        print(f'{self.Color_FGC.GREEN}------------------ debug info  -----------------{self.Color_ACC.RESET}')
        print(f'{self.Color_FGC.CYAN}------------------ debug logger-----------------{self.Color_ACC.RESET}')
        self.loggerLog(f"This is a log")
        self.loggerLog(f"This is a log with custom tag", "MyTag1")
        self.loggerTip(f"This is a tip")
        self.loggerTip(f"This is a tip with custom tag", "MyTag2")
        self.loggerWrn(f"This is a warn")
        self.loggerWrn(f"This is a warn with custom tag", "MyTag3")
        self.loggerErr(f"This is a error")
        self.loggerErr(f"This is a error with custom tag", "MyTag4")
        print(f'{self.Color_FGC.CYAN}------------------ debug logger-----------------{self.Color_ACC.RESET}')
        
        
if __name__ == "__main__":
    print('creating self')
    nlu = self()
    debug(nlu)
    print('-')
    
    
    
    