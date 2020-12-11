import Libraries.nlu4 as nlulib4


def LoadingScreen(title, nlu):
    ACC = nlu.Color.ACC
    FGC = nlu.Color.FGC
    MCC = nlu.Color.MCC
    time = nlu.Libs.time
    for n in range(1, 255, 5):
        nlu.BigPrint(title, maxlinelength=10, begin=ACC.CUSTOMRGB(n, n, n))
        print(nlu.Color.MCC.UP(7))
        time.sleep(0.0001)
    nlu.BigPrint(title, maxlinelength=10, begin=ACC.CUSTOMRGB(n, n, n))
    lineLength = 11 * len(title)
    for n in range(lineLength + 1):
        print(f'{FGC.YELLOW}{ACC.UNDERLINE}▐{"▒"*n}{"░"*(lineLength-n)}▌')
        print(MCC.UP(2))
        time.sleep(1 / 350)
    print(f"{FGC.GREEN}{ACC.UNDERLINE}▐" + lineLength * "█" + f"▌{ACC.RESET}")
    time.sleep(1 / 3)


class BasicModule(object):
    def __init__(self, nlu, cmdname="root", cmdabout="default console"):

        # save parametrs to class`es variables
        self.nlu = nlu
        self.logger = self.nlu.Logger()
        self.cmdname = cmdname
        self.cmdabout = cmdabout

        # def command list
        self.registeredCommands = []

        # setting up exit state as "run"
        self.exitState = "run"

    def registerCommand(self, commandClass):
        self.registeredCommands.append(
            {
                "command": commandClass.command,
                "description": commandClass.description,
                "aliases": commandClass.aliases,
                "required": commandClass.required,
                "optional": commandClass.optional,
                "run": commandClass.run,
            }
        )

    class command:
        command = "mycommand"
        description = "This is my custom command"
        aliases = [command, "mycommandalias"]
        required = ["myreq"]
        optional = ["myopt"]

        def run(console):
            console.logger.log("The command runned!")

    def __registerBasic(self):
        class _exit(self.command):
            command = "exit"
            description = "closing module"
            aliases = [command]
            required = []
            optional = []

            def run(console):
                if console.checkParamCount():
                    console.exitState = "0"
                else:
                    self.invalidUsage()

        class _cls(self.command):
            command = "cls"
            description = "clears display"
            aliases = [command, "clearscreen"]
            required = []
            optional = []

            def run(console):
                if console.checkParamCount():
                    console.nlu.Libs.os.system("cls")
                else:
                    self.invalidUsage()

        class _help(self.command):
            command = "help"
            description = "displays all commands in this module"
            aliases = [command]
            required = []
            optional = ["command"]

            def run(console):
                class CLR:
                    MDL = console.nlu.Color.FGC.RED
                    MDLDSK = console.nlu.Color.FGC.BRED
                    CMD = console.nlu.Color.FGC.BLUE
                    CMDDSK = console.nlu.Color.FGC.CYAN
                    ALS = console.nlu.Color.FGC.PURPLE
                    ALSTXT = console.nlu.Color.FGC.BPURPLE
                    STTL = console.nlu.Color.FGC.GREEN
                    SCMD = console.nlu.Color.ACC.UNDERLINE + nlu.Color.FGC.WHITE
                    SREQ = console.nlu.Color.FGC.BGRAY
                    SOPT = console.nlu.Color.FGC.GRAY
                    R = console.nlu.Color.ACC.RESET

                helpPage = ""
                if console.paramCount == 0:
                    helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
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
                    console.logger.tip(helpPage, f"{console.cmdname} HELP")
                elif console.paramCount == 1:
                    if console.parametrs[0] == "commands":
                        helpPage += f"\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n"
                        for command in console.registeredCommands:
                            helpPage += f'\t{CLR.CMD}{command["command"]}\n'
                        console.logger.tip(helpPage, f"{console.cmdname} HELP")
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
                                console.logger.tip(helpPage, f"{console.cmdname} HELP")
                                finded = True
                        if finded != True:
                            console.logger.wrn(
                                f'Cannot find command "{console.parametrs[0]}"',
                                f"{console.cmdname} HELP",
                            )
                else:
                    console.invalidUsage()

        class _hello(self.command):
            command = "hello"
            description = "builtin command"
            aliases = [command, "hi"]
            required = []
            optional = ["name"]

            def run(console):
                if console.paramCount > 1:
                    console.invalidUsage()
                elif console.paramCount == 1:
                    console.logger.log(f"Hello, {console.parametrs[0]}")
                else:
                    console.logger.log(f"Hello, world!")

        self.registerCommand(_hello)
        self.registerCommand(_exit)
        self.registerCommand(_help)
        self.registerCommand(_cls)

    def checkParamCount(self, command=""):
        if command == "":
            command = self.running
        for rcommand in console.registeredCommands:
            if rcommand["command"] == command:
                if self.paramCount > (
                    len(rcommand["required"]) + len(rcommand["optional"])
                ) and self.paramCount < len(rcommand["required"]):
                    return False
                break

        return True

    def invalidUsage(self, command=""):
        if command == "":
            command = self.running

        class CLR:
            SCMD = console.nlu.Color.ACC.UNDERLINE + nlu.Color.FGC.WHITE
            SREQ = console.nlu.Color.FGC.BGRAY
            SOPT = console.nlu.Color.FGC.GRAY
            R = console.nlu.Color.ACC.RESET

        syntax = ""
        for rcommand in console.registeredCommands:
            if rcommand["command"] == command:
                syntax = f'{CLR.SCMD}{rcommand["command"]}{CLR.R} '
                if rcommand["required"] != []:
                    syntax += f'{CLR.SREQ}<{"> <".join(rcommand["required"])}>{CLR.R} '
                if rcommand["optional"] != []:
                    syntax += f'{CLR.SOPT}[{"] [".join(rcommand["optional"])}]{CLR.R} '
        self.logger.wrn(f"Invalid usage. Syntax: {syntax}")

    def __parseInput(self, readed):
        import re

        res = re.findall(
            r"[\'][a-zA-ZА-Яа-я\d\s[\]{}()\\\.\":;,-]*[\']|\b[a-zA-Z\d]+",
            readed,
            re.MULTILINE,
        )
        res2 = []
        for item in res:
            res2.append(re.sub(r"\B'|\b'", "", item))
        res = [x for x in res2 if x != ""]
        if len(res) == 0:
            return {"command": "", "param": []}
        if len(res) == 1:
            return {"command": res[0], "param": []}
        else:
            return {"command": res[0], "param": res[1 : len(res)]}

    def Main(self):
        self.__registerBasic()
        while self.exitState == "run":
            try:
                read = self.__parseInput(self.logger.read(f"{self.cmdname} >"))
                self.command = read["command"]
                self.parametrs = read["param"]
                self.paramCount = len(self.parametrs)
                if self.command == "fuck":
                    raise Exception(
                        "fatal", "Why you so evil?...", ":_(", "TIP: you can be beter"
                    )
                self.runned = False
                self.voidcommand = False
                if self.command == "":
                    self.voidcommand = True
                else:
                    for command in self.registeredCommands:
                        if self.command in command["aliases"]:
                            self.running = command["command"]
                            command["run"](self)
                            self.runned = True
                            break
                        self.runned = False
                if not (self.runned or self.voidcommand):
                    self.logger.wrn("Unknown command", f"{self.cmdname} UNKNOWN")
            except Exception as e:
                import traceback

                if "notraceback" in e.args:
                    self.needtraceback = True
                else:
                    self.needtraceback = False
                if len(e.args) == 0:
                    err = (
                        f"\n----------------------------------\n"
                        + f"Unknown error\n"
                        + f"No message provided\n\n"
                        + f"More information:\n"
                        + f"\tType: {type(e)}\n\n"
                        + f"\tTraceback: \n\t\t{traceback.format_exc().replace(chr(10),chr(10)+chr(9)+chr(9))}\n"
                        + f"----------------------------------"
                    )
                    self.logger.err(err)
                else:
                    if "warn" in e.args:
                        e.args = tuple(
                            x
                            for x in e.args
                            if x not in ["fatal", "notraceback", "warn"]
                        )
                        err = (
                            f"\n----------------------------------\n"
                            + f"Warning!\n\n"
                            + f"More information:\n"
                            + f"\tAbout:\n\t\t{(chr(10)+chr(9)+chr(9)).join(e.args)}\n\n"
                            + f"\tType: {type(e)}\n\n"
                        )
                        if self.needtraceback:
                            e.args = tuple(x for x in e.args if x != "warn")
                            err += f"----------------------------------"
                        else:
                            err += (
                                f"\tTraceback: \n\t\t{traceback.format_exc().replace(chr(10),chr(10)+chr(9)+chr(9))}\n"
                                + f"----------------------------------"
                            )
                        self.logger.wrn(err)
                    elif "fatal" in e.args:
                        e.args = tuple(
                            x
                            for x in e.args
                            if x not in ["fatal", "notraceback", "warn"]
                        )
                        err = (
                            f"\n----------------------------------\n"
                            + f"Fatal error!\n\n"
                            + f"More information:\n"
                            + f"\tAbout:\n\t\t{(chr(10)+chr(9)+chr(9)).join(e.args)}\n\n"
                            + f"\tType: {type(e)}\n\n"
                            + f"\tProgram will stoped because this error is fatal\n"
                        )
                        if self.needtraceback:
                            e.args = tuple(x for x in e.args if x != "warn")
                            err += f"----------------------------------"
                        else:
                            err += (
                                f"\tTraceback: \n\t\t{traceback.format_exc().replace(chr(10),chr(10)+chr(9)+chr(9))}\n"
                                + f"----------------------------------"
                            )
                        self.logger.err(err)
                        self.exitState = "fatal"
                    else:
                        err = (
                            f"\n----------------------------------\n"
                            + f"Some error\n\n"
                            + f"More information:\n"
                            + f"\tAbout:\n\t\t{(chr(10)+chr(9)+chr(9)).join(e.args)}\n\n"
                            + f"\tType: {type(e)}\n\n"
                        )
                        if self.needtraceback:
                            e.args = tuple(x for x in e.args if x != "warn")
                            err += f"----------------------------------"
                        else:
                            err += (
                                f"\tTraceback: \n\t\t{traceback.format_exc().replace(chr(10),chr(10)+chr(9)+chr(9))}\n"
                                + f"----------------------------------"
                            )
                        self.logger.err(err)


if __name__ == "__main__":
    nlu = nlulib4.NewLifeUtils(silent=True)
    LoadingScreen("MYCMD", nlu)
    console = BasicModule(nlu, "MY CMD")

    class database(BasicModule.command):
        command = "database"
        description = "start database manage session"
        aliases = [command, "dbconnect"]
        required = []
        optional = []

        def run(console):
            if console.checkParamCount():
                console.logger.log("Setting up ")
                dbmanager = BasicModule(
                    console.nlu, "DB Manage", "easy way to manage database"
                )

                class startsession(BasicModule.command):
                    command = "startsession"
                    description = "setting up base with provided name"
                    aliases = [command, "start", "setup", "newsession"]
                    required = ["database name"]
                    optional = []

                    def run(console):
                        if console.checkParamCount():
                            console.log("Connected! (im kidding_")
                        else:
                            console.invalidUsage()

                dbmanager.registerCommand(startsession)
                dbmanager.Main()
            else:
                console.invalidUsage()

    console.registerCommand(database)
    console.Main()

"""
    command = 'mycommand'
    description = 'This is my custom command'
    aliases = [command, 'mycommandalias']
    required = ['myreq']
    optional = ['myopt']
    def run(console):
        if console.checkParamCount():
            #some code here
        else:
            console.invalidUsage()
"""
