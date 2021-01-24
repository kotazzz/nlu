import NewLifeUtils.LoggerModule       as Logger
import NewLifeUtils.ColorModule      as Color
import NewLifeUtils.StringUtilModule as String
import NewLifeUtils.ExceptModule    as Except
import NewLifeUtils.LanguageManager as Language


class Command:
    command = "commandname"
    aliases = [command, "commandalias"]
    description = "My Super Duper Command"
    required = ["required parametr"]
    optional = ["optional parametr"]
    skipcheck = False

    def run(console):
        Logger.log(f'Command "{console.run["command"]}" executed now')

class Task:
    def execute(console):
        Logger.log(f"This is a event task")

class Function:
    name = "mygf"
    def execute(console):
        Logger.log(f"This is a global function")
        
class Shell(object):
    



    def __init__(
        self,
        name=Language.getlang("Shell", "def_cmdname"),
        about=Language.getlang("Shell", "def_cmdabout"),
    ):
        self.runState = "init"

        self.cmdname = name
        self.cmdabout = about

        self.registeredInitTask = []
        self.registeredCommands = []
        self.registeredGlobalFunctions = {}
        self.registeredExitTask = []
        Logger.TagMaxLenght = len(self.cmdname) + 5
        Logger.logDefaultTag = f"[L] {self.cmdname.title()}"
        Logger.wrnDefaultTag = f"[W] {self.cmdname.title()}"
        Logger.errDefaultTag = f"[E] {self.cmdname.title()}"
        Logger.tipDefaultTag = f"[T] {self.cmdname.title()}"
        Logger.reaDefaultTag = f"[R] {self.cmdname.title()}"
        Logger.reaFormat = (
            "{white}[{time}] {blue}{tag}{empty}{reset}: {cyan}{read}{reset}"
        )

        self.runState = "setup"

    class cls_(Command):
        command = Language.getlang("Shell", "def_cls_cmd")
        description = Language.getlang("Shell", "def_cls_dsk")
        aliases = [command, Language.getlang("Shell", "def_cls_al1")]
        required = []
        optional = []

        def run(console):
            os.system("cls")

    class help_(Command):
        command = Language.getlang("Shell", "def_help_cmd")
        description = Language.getlang("Shell", "def_help_dsk")
        aliases = [command]
        required = []
        optional = [Language.getlang("Shell", "def_help_op1")]

        def run(console):
            class CLR:
                MDL = Color.FGC.RED
                MDLDSK = Color.FGC.BRED
                CMD = Color.FGC.BLUE
                CMDDSK = Color.FGC.CYAN
                ALS = Color.FGC.PURPLE
                ALSTXT = Color.FGC.BPURPLE
                STTL = Color.FGC.GREEN
                SCMD = Color.ACC.UNDERLINE + Color.FGC.WHITE
                SREQ = Color.FGC.BGRAY
                SOPT = Color.FGC.GRAY
                R = Color.ACC.RESET

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
                Logger.tip(helpPage, f"{console.cmdname} HELP")
            elif console.paramCount == 1:
                if console.parametrs[0] == "commands":
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                    for command in console.registeredCommands:
                        helpPage += f'\t{CLR.CMD}{command["command"]}\n'
                    Logger.tip(helpPage, f"{console.cmdname} HELP")
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
                            Logger.tip(helpPage, f"{console.cmdname} HELP")
                            finded = True
                    if finded != True:
                        Logger.wrn(
                            f'Cannot find command "{console.parametrs[0]}"',
                            f"{console.cmdname} HELP",
                        )
            else:
                console.invalidUsage()

    class hello_(Command):
        command = Language.getlang("Shell", "def_hello_cmd")
        description = Language.getlang("Shell", "def_hello_dsk")
        aliases = [command, Language.getlang("Shell", "def_hello_al1")]
        required = []
        optional = [Language.getlang("Shell", "def_hello_op1")]

        def run(console):
            if console.paramCount == 1:
                Logger.log(f"Hello, {console.parametrs[0]}")
            else:
                Logger.log(f"Hello, world!")

    class exit_(Command):
        command = Language.getlang("Shell", "def_exit_cmd")
        aliases = [command, Language.getlang("Shell", "def_exit_al1")]
        description = Language.getlang("Shell", "def_exit_dsk")
        required = []
        optional = []
        skipcheck = False

        def run(console):
            console.runState = "quit"

    class initDefaultTask_(Task):
        def execute(console):
            Logger.log(
                f'{Language.getlang("Shell", "welcome")} {console.cmdname}'
            )

    class exitDefaultTask_(Task):
        def execute(console):
            Logger.log(
                f'{Language.getlang("Shell", "exit1")}: {console.runState}, {Language.getlang("Shell", "exit2")}: {console.run}'
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
            SCMD = Color.ACC.UNDERLINE + Color.FGC.WHITE
            SREQ = Color.FGC.BGRAY
            SOPT = Color.FGC.GRAY
            R = Color.ACC.RESET

        syntax = ""
        syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
        if command["required"] != []:
            syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
        if command["optional"] != []:
            syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
        Logger.wrn(f"Invalid usage. Syntax: {syntax}")

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
            Except.except_print(
                Exception(
                    "Console commands with the same names were registered. here is a list of registered console commands (their names)",
                    f"Commands: {', '.join(cmdnames)}",
                    "TIP: check register section and delete or change one of the commands",
                ),
                exceptionType="fatal",
                tb=False,
            )
        for itask in self.registeredInitTask:
            itask(self)

        while self.runState == "run":
            try:
                readed = String.parse_args(
                    Logger.rea(f"{self.cmdname.title()} >")
                )
                self.command = readed["command"]
                self.parametrs = readed["param"]
                self.paramCount = len(self.parametrs)

                if self.command == "fuck":
                    Except.except_print(
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
                        Logger.wrn('Unknown Command, type "help"')

            except Exception as e:
                Except.except_print(e)

        for itask in self.registeredExitTask:
            itask(self)
