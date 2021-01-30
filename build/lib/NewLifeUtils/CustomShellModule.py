import os

from NewLifeUtils.ExceptModule import *
from NewLifeUtils.LoggerModule import *
from NewLifeUtils.StringUtilModule import *

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

invalid_usage: "Invalid usage. Syntax: {syntax}"


same_command:
- "Console commands with the same names were registered." 
- "Here is a list of registered console commands (their names):"
- "{list}"
"""

create_files("shell_translation", "lang.yml", "shell", default_translation)
translation = get_yaml("shell_translation", default_translation)


class Shell(object):
    def __init__(
            self,
            name=translation["default_cmd_name"],
            about=translation["default_cmd_description"],
    ):
        self.runState = "init"
        self.cmdname = name
        self.cmdabout = about

        self.registered_init_task = []
        self.registered_commands = []
        self.registeredGlobalFunctions = {}
        self.registered_exit_task = []
        self.run = None
        self.runState = "setup"
        self.fist_completer = {}

        set_settings(
            new_tag_length=len(self.cmdname) + 5,
            new_log_default_tag=f"[L] {self.cmdname.title()}",
            new_wrn_default_tag=f"[W] {self.cmdname.title()}",
            new_err_default_tag=f"[E] {self.cmdname.title()}",
            new_tip_default_tag=f"[T] {self.cmdname.title()}",
            new_rea_default_tag=f"[R] {self.cmdname.title()}",
            new_rea_pattern="{cyan}[{time}] {lightcyan}{tag}{snow} : {paleturquoise}{message} {mediumslateblue}[{readed}]",
        )

        @self.register_command(
            "exit", ["quit"], translation["exit_description"], [], []
        )
        def exit_(console):
            console.runState = "quit"

        @self.register_command(
            "cls", ["clearscreen"], translation["cls_description"], [], []
        )
        def cls_(console):
            os.system("cls")

        @self.register_command("help", [], translation["help_description"], [], [])
        def help_(console):
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
                for command in console.registered_commands:
                    syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                    if command["required"]:
                        syntax += (
                            f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                        )
                    if command["optional"]:
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
                    for command in console.registered_commands:
                        helpPage += f'\t{CLR.CMD}{command["command"]}\n'
                    tip(helpPage, f"{console.cmdname} HELP")
                else:
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                    finded = False
                    for command in console.registered_commands:
                        if command["command"] == console.parametrs[0]:
                            syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                            if command["required"]:
                                syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                            if command["optional"]:
                                syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
                            helpPage += (
                                    f'\t{CLR.CMD}{command["command"]}\n'
                                    + f'\t\t{CLR.CMDDSK}Description: {command["description"]}\n'
                                    + f'\t\t{CLR.ALS}Aliases: {CLR.ALSTXT}{", ".join(command["aliases"])}\n'
                                    + f"\t\t{CLR.CMDDSK}Usage: {syntax}{CLR.R}\n"
                            )
                            tip(helpPage, f"{console.cmdname} HELP")
                            finded = True
                    if not finded:
                        wrn(
                            f'Cannot find command "{console.parametrs[0]}"',
                            f"{console.cmdname} HELP",
                        )
            else:
                console.invalidUsage()

        @self.register_command(
            "hello", ["hi"], translation["hello_description"], [], ["name"]
        )
        def hello_(console):
            if console.paramCount == 1:
                log(f"Hello, {console.parametrs[0]}")
            else:
                log(f"Hello, world!")

        @self.register_init_task()
        def welcome(console):
            log(f'{translation["welcome"]} {console.cmdname}')

        @self.register_exit_task()
        def goodbye(console):
            log(
                f'{translation["exit_code_label"]}: {console.runState}, {translation["exit_from_label"]}: {console.run}'
            )

    def register_init_task(self):
        def register_from_decorator(command_function):
            self.registered_init_task.append(command_function)
            return command_function

        return register_from_decorator

    def register_exit_task(self):
        def register_from_decorator(command_function):
            self.registered_exit_task.append(command_function)
            return command_function

        return register_from_decorator

    def register_global_function(self, name):
        def register_from_decorator(command_function):
            self.registered_global_functions.append(
                {
                    "name": name,
                    "execute": command_function,
                }
            )
            return command_function

        return register_from_decorator

    def unregister_by_name(self, name):
        if  name not in ['exit','help']:
            for commandid, command in enumerate(self.registered_commands, start=0):
                if command['command'] == name:
                    self.registered_commands.pop(commandid)
                    break
        else:
            wrn(f"You can't get rid of the {name} command")

    def register_command(
            self,
            command,
            aliases=[],
            description="my simple command",
            required=[],
            optional=["param"],
            skipcheck=False,
    ):
        def register_from_decorator(command_function):
            self.registered_commands.append(
                {
                    "command": command,
                    "aliases": [command, *aliases],
                    "description": description,
                    "required": required,
                    "optional": optional,
                    "skipcheck": skipcheck,
                    "run": command_function,
                }
            )
            return command_function

        return register_from_decorator

    def invalidUsage(self, command):
        class CLR:
            SCMD = ACC.UNDERLINE + FGC.WHITE
            SREQ = FGC.BGRAY
            SOPT = FGC.GRAY
            R = ACC.RESET

        syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
        if command["required"]:
            syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
        if command["optional"]:
            syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
        wrn(translation["invalid_usage"].format(syntax=syntax))

    def check_commands(self):
        cmdnames = []
        for command in self.registered_commands:
            cmdnames.append(command["command"])

        if len(cmdnames) != len(set(cmdnames)):
            cmds = ", ".join(cmdnames)
            except_print(
                Exception(
                    *[cmd.format(list=cmds) for cmd in translation["same_command"]]
                ),
                exception_type="fatal",
                tb=False,
            )

    def check_params(self):
        return (
                not (
                        self.paramCount
                        > (
                                len(self.run["required"])
                                + len(self.run["optional"])
                        )
                        or self.paramCount < len(self.run["required"])
                )
                or self.run["skipcheck"]
        )

    def main(self):

        self.runState = "starting"

        for itask in self.registered_init_task:
            itask(self)

        for command in self.registered_commands:
            self.fist_completer[command["command"]] = {}

        self.runState = "run"
        while self.runState == "run":
            try:
                readed = parse_args(
                    rea(f"{self.cmdname.title()} >", completion=self.fist_completer)
                )
                self.command = readed["command"]
                self.parametrs = readed["param"]
                self.paramCount = len(self.parametrs)
                if self.command != "":
                    if self.command == "fuck":
                        except_print(
                            Exception(
                                "Why you so evil?...",
                                ":_(",
                                "TIP: you can be beter",
                            ),
                            exception_type="wrn",
                            tb=False,
                        )

                    else:
                        for registered in self.registered_commands:
                            if self.command in registered["aliases"]:
                                self.run = registered
                                if self.check_params():
                                    registered["run"](self)
                                else:
                                    self.invalidUsage(registered)
                                self.run = None
                                break
                        else:
                            wrn('Unknown Command, type "help"')

            except Exception as e:
                except_print(e)

        for itask in self.registered_exit_task:
            itask(self)
