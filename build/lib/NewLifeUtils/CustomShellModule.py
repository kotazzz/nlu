from NewLifeUtils.LoggerModule import *
from NewLifeUtils.ColorModule import *
from NewLifeUtils.StringUtilModule import *
from NewLifeUtils.ExceptModule import *
import os

default_translation = """
default_cmd_name: "My CMD"
default_cmd_description: "My new command line instance"
welcome: "Welcome to"
help_description: "This is the help"
cls_description: "Clears display"
hello_description: "Say 'Hello'"
exit_description: "Exit from cmd"
exit_code_label: "Exit with code"
exit_from_label: "from"

same_command:
- "Console commands with the same names were registered." 
- "Here is a list of registered console commands (their names):"
- "{list}"
"""

create_files("shell_translation", "lang.yml", "shell", default_translation)
translation = get_yaml("shell_translation", default_translation)


class Command:
    command = "commandname"
    aliases = [command, "commandalias"]
    description = "My Super Command"
    required = ["required parameter"]
    optional = ["optional parameter"]
    skipcheck = False

    def run(console):
        log(f'Command "{console.run["command"]}" executed now')


class Task:
    def execute(console):
        log(f"This is a event task")


class Function:
    name = "mygf"

    def execute(console):
        log(f"This is a global function")


class Shell(object):

    def __init__(
            self,
            name=translation["default_cmd_name"],
            about=translation["default_cmd_description"],
    ):
        self.runState = "init"
        self.cmdname = name
        self.cmdabout = about

        self.registeredInitTask = []
        self.registeredCommands = []
        self.registeredGlobalFunctions = {}
        self.registeredExitTask = []
        set_settings(
            new_tag_length=len(self.cmdname) + 5,
            new_log_default_tag=f"[L] {self.cmdname.title()}",
            new_wrn_default_tag=f"[W] {self.cmdname.title()}",
            new_err_default_tag=f"[E] {self.cmdname.title()}",
            new_tip_default_tag=f"[T] {self.cmdname.title()}",
            new_rea_default_tag=f"[R] {self.cmdname.title()}",
            new_rea_pattern="{cyan}[{time}] {lightcyan}{tag}{snow} : {paleturquoise}{message} {mediumslateblue}[{readed}]"
        )

        self.runState = "setup"
        self.fist_completer = {}

    class cls_(Command):
        command = "cls"
        description = translation["cls_description"]
        aliases = [command, "clearscreen"]
        required = []
        optional = []

        def run(console):
            os.system("cls")

    class help_(Command):
        command = "help"
        description = translation["help_description"]
        aliases = [command]
        required = []
        optional = ["command|commands"]

        def run(console):
            class CLR:
                MDL = FGC.RED
                MDLDSK = FGC.BRED
                CMD = FGC.BLUE
                CMDDSK = FGC.CYAN
                ALS = FGC.PURPLE
                ALSTXT = FGC.MAGENTA
                STTL = FGC.GREEN
                SCMD = ACC.UNDERLINE + FGC.WHITE
                SREQ = FGC.BGRAY
                SOPT = FGC.GRAY
                R = ACC.RESET

            helpPage = ""
            if console.paramCount == 0:
                helpPage += (
                    f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                )
                for command in console.registeredCommands:
                    syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                    if command["required"] != []:
                        syntax += (
                            f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                        )
                    if command["optional"] != []:
                        syntax += (
                            f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
                        )
                    helpPage += (
                            f'\t{CLR.CMD}{command["command"]}\n'
                            + f'\t\t{CLR.CMDDSK}Description {CLR.R}: {CLR.CMDDSK}{command["description"]}\n'
                            + f'\t\t{CLR.ALS}Aliases     {CLR.R}: {CLR.ALSTXT}{", ".join(command["aliases"])}\n'
                            + f"\t\t{CLR.STTL}Usage       {CLR.R}: {syntax}{CLR.R}\n"
                    )
                tip(helpPage, f"{console.cmdname} HELP")
            elif console.paramCount == 1:
                if console.parametrs[0] == "commands":
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                    for command in console.registeredCommands:
                        helpPage += f'\t{CLR.CMD}{command["command"]}\n'
                    tip(helpPage, f"{console.cmdname} HELP")
                else:
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                    finded = False
                    for command in console.registeredCommands:
                        if command["command"] == console.parametrs[0]:
                            syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                            if command["required"] != []:
                                syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                            if command["optional"] != []:
                                syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
                            helpPage += (
                                    f'\t{CLR.CMD}{command["command"]}\n'
                                    + f'\t\t{CLR.CMDDSK}Description: {command["description"]}\n'
                                    + f'\t\t{CLR.ALS}Aliases: {CLR.ALSTXT}{", ".join(command["aliases"])}\n'
                                    + f"\t\t{CLR.CMDDSK}Usage: {syntax}{CLR.R}\n"
                            )
                            tip(helpPage, f"{console.cmdname} HELP")
                            finded = True
                    if finded != True:
                        wrn(
                            f'Cannot find command "{console.parametrs[0]}"',
                            f"{console.cmdname} HELP",
                        )
            else:
                console.invalidUsage()

    class hello_(Command):
        command = "hello"
        description = translation["hello_description"]
        aliases = [command, "hi"]
        required = []
        optional = ["name"]

        def run(console):
            if console.paramCount == 1:
                log(f"Hello, {console.parametrs[0]}")
            else:
                log(f"Hello, world!")

    class exit_(Command):
        command = "exit"
        aliases = [command, "quit"]
        description = translation['exit_description']
        required = []
        optional = []
        skipcheck = False

        def run(console):
            console.runState = "quit"

    class initDefaultTask_(Task):
        def execute(console):
            log(
                f'{translation["welcome"]} {console.cmdname}'
            )
            log(console.fist_completer)

    class exitDefaultTask_(Task):
        def execute(console):
            log(
                f'{translation["exit_code_label"]}: {console.runState}, {translation["exit_from_label"]}: {console.run}'
            )

    def registerInitTask(self, regClass):
        self.registeredInitTask.append(regClass.execute)

    def registerExitTask(self, regClass):
        self.registeredExitTask.append(regClass.execute)

    def registerGlobalFunctions(self, regClass):
        self.registerGlobalFunctions.append(
            {
                "name": regClass.name,
                "execute": regClass.execute,
            }
        )

    def registerCommand(self, regClass):
        self.registeredCommands.append(
            {
                "command": regClass.command,
                "aliases": regClass.aliases,
                "description": regClass.description,
                "required": regClass.required,
                "optional": regClass.optional,
                "skipcheck": regClass.skipcheck,
                "run": regClass.run,
            }
        )

    def invalidUsage(self, command):
        class CLR:
            SCMD = ACC.UNDERLINE + FGC.WHITE
            SREQ = FGC.BGRAY
            SOPT = FGC.GRAY
            R = ACC.RESET

        syntax = ""
        syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
        if command["required"] != []:
            syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
        if command["optional"] != []:
            syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
        wrn(f"Invalid usage. Syntax: {syntax}")

    def main(self):



        self.runState = "run"

        # Basic registration

        self.registerCommand(self.cls_)
        self.registerCommand(self.help_)
        self.registerCommand(self.hello_)
        self.registerCommand(self.exit_)
        self.registerExitTask(self.exitDefaultTask_)
        self.registerInitTask(self.initDefaultTask_)
        cmdnames = []
        for command in self.registeredCommands:
            cmdnames.append(command["command"])

        if len(cmdnames) != len(set(cmdnames)):
            cmds = ', '.join(cmdnames)
            except_print(
                Exception(
                    *[cmd.format(list=cmds) for cmd in translation["same_command"]]
                ),
                exceptionType="fatal",
                tb=False,
            )
        for itask in self.registeredInitTask:
            itask(self)

        for command in self.registeredCommands:
            self.fist_completer[command['command']] = {}

        while self.runState == "run":
            try:

                readed = parse_args(
                    rea(f"{self.cmdname.title()} >", completion=self.fist_completer)
                )
                self.command = readed["command"]
                self.parametrs = readed["param"]
                self.paramCount = len(self.parametrs)

                if self.command == "fuck":
                    except_print(
                        Exception(
                            "Why you so evil?...",
                            ":_(",
                            "TIP: you can be beter",
                        ),
                        exceptionType="wrn",
                        tb=False,
                    )
                elif self.command != "":
                    for registered in self.registeredCommands:
                        if self.command in registered["aliases"]:
                            self.run = registered
                            if (
                                    not (
                                            self.paramCount
                                            > (
                                                    len(self.run["required"])
                                                    + len(self.run["optional"])
                                            )
                                            or self.paramCount < len(self.run["required"])
                                    )
                                    or self.run["skipcheck"]
                            ):
                                registered["run"](self)
                            else:
                                self.invalidUsage(registered)
                            self.run = None
                            break
                    else:
                        wrn('Unknown Command, type "help"')

            except Exception as e:
                except_print(e)

        for itask in self.registeredExitTask:
            itask(self)
