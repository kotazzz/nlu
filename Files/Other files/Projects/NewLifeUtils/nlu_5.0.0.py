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

        name = 'NewLifeUtils'
        version = '5.0.0'
        description = 'Utils For You! <3'
        workingDirectory = ''
        curentDirectory = ''
        configName = 'config.json'

    class LibsManager:
            def __initialize(root):
                root.libs_os = __import__('os') 
                root.libs_random  = __import__('random')
                root.libs_time = __import__('time')
                root.libs_datetime = __import__('datetime')
                root.libs_sqlite3 = __import__('sqlite3')
                
    class ColorManager:
            def __initialize(root):
                pass
    class LoggerManager:
            def __initialize(root):
                pass
    class RandomManager:
            def __initialize(root):
                pass
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