from NewLifeUtils import json
import NewLifeUtils.Modules.FileModule as File

lang = "en"
file = File.open_file(f"{lang}.json", "r+", path="+lang", encoding="utf-8")
filedata = file.read()

try:
    currentLangStorage = json.loads(filedata)
except:
    default = json.dumps(
            {
                "LoggerModule": {
                    "err_default_tag": "Error",
                    "log_default_tag": "Log",
                    "rea_default_tag": "Read",
                    "tip_default_tag": "Tip",
                    "wrn_default_tag": "Warn",
                },
                "ExceptModule": {
                    "about": "About Error:",
                    "attention": "Attention!",
                    "fatal": "Fatal Error!",
                    "unknown": "Unknown Error",
                    "warning": "Warning!",
                    "wrong": "Something wrong...",
                },
                "Shell": {
                    "def_cls_al1": "clearscreen",
                    "def_cls_cmd": "cls",
                    "def_cls_dsk": "clears display",
                    "def_cmdabout": "default console",
                    "def_cmdname": "root",
                    "def_exit_al1": "quit",
                    "def_exit_cmd": "exit",
                    "def_exit_dsk": "Exit from ConsoleShellManager",
                    "def_hello_al1": "hi",
                    "def_hello_cmd": "hello",
                    "def_hello_dsk": "builtin command",
                    "def_hello_op1": "name",
                    "def_help_cmd": "help",
                    "def_help_dsk": "displays all commands in this module",
                    "def_help_op1": "command|'commands'",
                    "exit1": "Exit with code:",
                    "exit2": "run command",
                    "same_name_err1": "Console commands with the same names were registered.",
                    "same_name_err2": "Commands",
                    "same_name_err3": "TIP: check register section and delete or change one of the commands",
                    "some_err1": "Why you so evil?...",
                    "some_err2": ":_(",
                    "some_err3": "TIP: you can be beter",
                    "unknown": "Unknown Command, type 'help'",
                    "welcome": "Welcome to ",
                },
            }, indent=4, sort_keys=True
        )
    file.write(default)
    currentLangStorage = json.loads(default)
    
file.close()

def getlang(modulename, key):
    if modulename not in currentLangStorage.keys():
        return " <Underfined Module> "
    else:
        try:
            return currentLangStorage[modulename][key]
        except:
            return " <Underfined Key> "
    return " <Underfined Err> "
