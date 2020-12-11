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
#|      |  <3  NewLifeUtils  5.0v   |        |                                                   |#
#|      +---------------------------+        |                                                   |#
#|      | ***   --- KOTAZ ---   *** |        |                                                   |#
#|      +---------------------------+        |                                                   |#
#|                                           |                                                   |#
#+-------------------------------------------:---------------------------------------------------+#
###################################################################################################





class NewLifeUtils(object):
    def __init__(self, silent = False):
        self.LibsManager._LibsManager__initialize(self)
        self.ColorManager._ColorManager__initialize(self)
        self.LoggerManager._LoggerManager__initialize(self)
        self.RandomManager._RandomManager__initialize(self)
        self.TableManager._TableManager__initialize(self)
        self.DatabaseManager._DatabaseManager__initialize(self)
        self.ConsoleShellManager._ConsoleShellManager__initialize(self)
        self.FileManager._FileManager__initialize(self)
        self.StringManager._StringManager__initialize(self)
        self.TracebackManager._TracebackManager__initialize(self)
        self.FileLogger._FileLogger__initialize(self)
        self.Utils._Utils__initialize(self)

        self.name = 'NewLifeUtils'
        self.version = '5.0.1'
        self.description = 'Utils For You! <3'
        self.curentDirectory = self.LibsManager.getModule(self, 'os').getcwd()
        self.workingDirectory = self.curentDirectory + r'\NLUDIR'
        self.configName = 'config.json'
        self.logName = 'log-_date_.log'
        print('-------------------debug info-------------------')
        print(f'name: {self.name} version: {self.version}')
        print(f'description: {self.description}')
        print(f'curentDirectory: {self.curentDirectory}')
        print(f'workingDirectory: {self.workingDirectory}')
        print(f'configName: {self.configName} logName: {self.logName}')
        
    class LibsManager:
            def __initialize(root):
                root.LibsManager_os = __import__('os') 
                root.LibsManager_random  = __import__('random')
                root.LibsManager_time = __import__('time')
                root.LibsManager_datetime = __import__('datetime')
                root.LibsManager_sqlite3 = __import__('sqlite3')
            def getModule(root, name):
                if name == 'os':
                    return root.LibsManager_os
                elif name == 'random':
                    return root.LibsManager_random
                elif name == 'time':
                    return root.LibsManager_time
                elif name == 'datetime':
                    return root.LibsManager_datetime
                elif name == 'sqlite3 ':
                    return root.LibsManager_sqlite3 
    class ColorManager:
            def __initialize(root):
                root.LibsManager.getModule(root, 'os').system('')
                root.ColorManager_BGC = root.ColorManager.BGC
                root.ColorManager_BGC_BLACK = "\x1B[40m"
                root.ColorManager_BGC_RED = "\x1B[41m"
                root.ColorManager_BGC_GREEN = "\x1B[42m"
                root.ColorManager_BGC_YELLOW = "\x1B[43m"
                root.ColorManager_BGC_BLUE = "\x1B[44m"
                root.ColorManager_BGC_PURPLE = "\x1B[45m"
                root.ColorManager_BGC_CYAN = "\x1B[46m"
                root.ColorManager_BGC_BGRAY = "\x1B[47m"
                root.ColorManager_BGC_GRAY = "\x1B[100m"
                root.ColorManager_BGC_BRED = "\x1B[101m"
                root.ColorManager_BGC_BGREEN = "\x1B[102m"
                root.ColorManager_BGC_BYELLOW = "\x1B[103m"
                root.ColorManager_BGC_BBLUE = "\x1B[104m"
                root.ColorManager_BGC_BPURPLE = "\x1B[105m"
                root.ColorManager_BGC_BCYAN = "\x1B[106m"
                root.ColorManager_BGC_WHITE = "\x1B[107m"
                root.ColorManager_FGC_BLACK = "\x1B[30m"
                root.ColorManager_FGC_RED = "\x1B[31m"
                root.ColorManager_FGC_GREEN = "\x1B[32m"
                root.ColorManager_FGC_YELLOW = "\x1B[33m"
                root.ColorManager_FGC_BLUE = "\x1B[34m"
                root.ColorManager_FGC_PURPLE = "\x1B[35m"
                root.ColorManager_FGC_CYAN = "\x1B[36m"
                root.ColorManager_FGC_BGRAY = "\x1B[37m"
                root.ColorManager_FGC_GRAY = "\x1B[90m"
                root.ColorManager_FGC_BRED = "\x1B[91m"
                root.ColorManager_FGC_BGREEN = "\x1B[92m"
                root.ColorManager_FGC_BYELLOW = "\x1B[93m"
                root.ColorManager_FGC_BBLUE = "\x1B[94m"
                root.ColorManager_FGC_BPURPLE = "\x1B[95m"
                root.ColorManager_FGC_BCYAN = "\x1B[96m"
                root.ColorManager_FGC_WHITE = "\x1B[97m"
                root.ColorManager_ACC_AFTERCLEAN = "\x1B[K"
                root.ColorManager_ACC_RESET = "\x1B[0m"
                root.ColorManager_ACC_UNDERLINE = "\x1B[4m"
                root.ColorManager_ACC_SWAP = "\x1B[7m"
                root.ColorManager_ACC_NOTNEGATIVE = "\x1B[27m"
                root.ColorManager_ACC_TOBRIGHT = "\x1B[1m"
                root.ColorManager_ACC_NOBRIGHT = "\x1B[2m"
                root.ColorManager_MCC_FIRSTLINE = "\x1B[1G"
                root.ColorManager_MCC_NEXTLINE = "\x1B[E"
                root.ColorManager_MCC_PREVIOUSLINE = "\x1B[F"
                root.ColorManager_MCC_ERASELINE = "\x1B[2K"
                root.ColorManager_MCC_REWRITELINE = "\x1B[1G"
                def ACC_CLEARSCREEN():
                    NewLifeUtils.Libs.os.system("cls")
                    return ""
                def ACC_RANDOMRGB(mode="Color"):
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
                def ACC_RANDOMD():
                    n = NewLifeUtils.Libs.random.randrange(0, 255)
                    return f"\x1B[38;5;{n}m"
                def ACC_CUSTOMRGB(r, g, b):
                    return f"\x1B[38;2;{r};{g};{b}m"
                def ACC_CUSTOMC(n):
                    return f"\x1B[38;5;{n}m"
                def ACC_BCUSTOMRGB(r, g, b):
                    return f"\x1B[48;2;{r};{g};{b}m"

                def ACC_BCUSTOMC(n):
                    return f"\x1B[48;5;{n}m"


                def MCC_UP(count):
                    return f"\x1B[{count}A"

                def MCC_DOWN(count):
                    return f"\x1B[{count}B"

                def MCC_RIGHT(count):
                    return f"\x1B[{count}V"

                def MCC_LEFT(count):
                    return f"\x1B[{count}D"

                def MCC_CURSORPOSITION(x, y):
                    return f"\x1B[{x};{y}H"


                
            class FCL:
                pink = 'NewLifeUtils.ColorManager.CUSTOMRGB(0,0,0)'
                purple = 'purple'
                blue = 'blue'
                cyan = 'cyan'
                green = 'green'
                bgreen = 'bgreen'
                yellow = 'yellow'
                orange = 'orange'
                red = 'red'
                brow = 'brow'
                white = 'white'
                bgray = 'bgray'
                gray = 'gray'
                black = 'black'
    class LoggerManager:
            def __initialize(root,
                    LoggerManager_logFormat = '',
                    LoggerManager_wrnFormat = '',
                    LoggerManager_errFormat = '',
                    LoggerManager_tipFormat = '',
                    LoggerManager_reaFormat = '',
                    LoggerManager_logDefaultTag = '',
                    LoggerManager_wrnDefaultTag = '',
                    LoggerManager_errDefaultTag = '',
                    LoggerManager_tipDefaultTag = '',
                    LoggerManager_reaDefaultTag = '',
                    LoggerManager_dateFormat="%d.%m.%Y",
                    LoggerManager_timeFormat="%H:%M:%S", 
                    LoggerManager_colorMap = {
                    'pink':'pink',
                    'purple':'purple',
                    'blue':'blue',
                    'cyan':'cyan',
                    'green':'green',
                    'bgreen':'bgreen',
                    'yellow':'yellow',
                    'orange':'orange',
                    'red':'red',
                    'brow':'brow',
                    'white':'white',
                    'bgray':'bgray',
                    'gray':'gray',
                    'black':'black',
                    },
                    LoggerManager_maxTagLength = 12
                ):
                root.LoggerManager_normalize = f"RESET"
                
                root.LoggerManager_logFormat =      LoggerManager_logFormat + root.LoggerManager_normalize
                root.LoggerManager_wrnFormat =      LoggerManager_wrnFormat + root.LoggerManager_normalize
                root.LoggerManager_errFormat =      LoggerManager_errFormat + root.LoggerManager_normalize
                root.LoggerManager_tipFormat =      LoggerManager_tipFormat + root.LoggerManager_normalize
                root.LoggerManager_reaFormat =      LoggerManager_reaFormat + root.LoggerManager_normalize
                
                root.LoggerManager_logDefaultTag =  LoggerManager_logDefaultTag 
                root.LoggerManager_wrnDefaultTag =  LoggerManager_wrnDefaultTag 
                root.LoggerManager_errDefaultTag =  LoggerManager_errDefaultTag 
                root.LoggerManager_tipDefaultTag =  LoggerManager_tipDefaultTag 
                root.LoggerManager_reaDefaultTag =  LoggerManager_reaDefaultTag
                
                root.LoggerManager_timeFormat =  LoggerManager_timeFormat  
                root.LoggerManager_dateFormat =  LoggerManager_dateFormat  
                
                root.LoggerManager_maxTagLength = LoggerManager_maxTagLength

                root.LoggerManager_colorMap = LoggerManager_colorMap


            
                
    class RandomManager:
            def __initialize(root):
                root.RandomManager_LastSeed = 1234_5678_9000_1111
    class TableManager:
            def __initialize(root):
                pass
    class DatabaseManager:
            def __initialize(root):
                pass
    class ConsoleShellManager:
            def __initialize(root):
                pass
    class FileManager:
            def __initialize(root):
                pass
    class StringManager:
            def __initialize(root):
                pass
    class TracebackManager:
            def __initialize(root):
                pass
    class FileLogger:
            def __initialize(root):
                pass
    class Utils:
            def __initialize(root):
                pass

        
if __name__ == "__main__":
    print('hello')
    nlu = NewLifeUtils()