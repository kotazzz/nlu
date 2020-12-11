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
#|    + vkApiManager                         | Module for working with VKApi                     |#
#|        - token                            |                                                   |#
#|        - groupid                          |                                                   |#
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