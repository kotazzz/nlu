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
        self.registeredExitActions = []
        self.registeredInitActions = []
        self.registeredFunctions = {}

        # setting up exit state as "run"
        self.exitState = "run"

    def registerFunction(self, functuion, name):
        self.registeredFunctions[name] = functuion

    def registerExit(self, functuion):
        self.registeredExitActions.append(functuion)

    def registerInit(self, functuion):
        self.registeredInitActions.append(functuion)

    def registerCommand(self, commandClass):
        self.registeredCommands.append(
            {
                "command": commandClass.command,
                "description": commandClass.description,
                "aliases": commandClass.aliases,
                "required": commandClass.required,
                "optional": commandClass.optional,
                "dontcheckopt": commandClass.dontcheckopt,
                "run": commandClass.run,
            }
        )

    class command:
        command = "mycommand"
        description = "This is my custom command"
        aliases = [command, "mycommandalias"]
        required = ["myreq"]
        optional = ["myopt"]
        dontcheckopt = False

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
                console.exitState = "0"

        class _cls(self.command):
            command = "cls"
            description = "clears display"
            aliases = [command, "clearscreen"]
            required = []
            optional = []

            def run(console):
                console.nlu.Libs.os.system("cls")

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
                if console.paramCount == 1:
                    console.logger.log(f"Hello, {console.parametrs[0]}")
                else:
                    console.logger.log(f"Hello, world!")

        self.registerCommand(_hello)
        self.registerCommand(_exit)
        self.registerCommand(_help)
        self.registerCommand(_cls)

    def invalidUsage(self):
        command = self.running

        class CLR:
            SCMD = console.nlu.Color.ACC.UNDERLINE + nlu.Color.FGC.WHITE
            SREQ = console.nlu.Color.FGC.BGRAY
            SOPT = console.nlu.Color.FGC.GRAY
            R = console.nlu.Color.ACC.RESET

        syntax = ""
        syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
        if command["required"] != []:
            syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
        if command["optional"] != []:
            syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
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

    def ExceptionPrint(self, e):
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
                    x for x in e.args if x not in ["fatal", "notraceback", "warn"]
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
                    x for x in e.args if x not in ["fatal", "notraceback", "warn"]
                )
                err = (
                    f"\n----------------------------------\n"
                    + f"Fatal error!\n\n"
                    + f"More information:\n"
                    + f"\tAbout:\n\t\t{(chr(10)+chr(9)+chr(9)).join(e.args)}\n\n"
                    + f"\tType: {type(e)}\n\n"
                    + f"\tModule will stoped now because this error is fatal\n"
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

    def Main(self):
        self.__registerBasic()
        for registeredAction in self.registeredInitActions:
            registeredAction(self)
        commandlist = []
        commandObj = []

        for registered in self.registeredCommands:
            commandlist.append(registered["command"])
            commandObj.append(
                {
                    "command": registered["command"],
                    "description": registered["description"],
                    "aliases": (", ".join(registered["aliases"])),
                    "parametrs": (
                        "REQ:"
                        + ", ".join(registered["required"])
                        + "  OPT:"
                        + ", ".join(registered["optional"])
                    ),
                }
            )

        setCommandlist = set(commandlist)
        if not (len(commandlist) == len(setCommandlist)):
            import json

            self.ExceptionPrint(
                Exception(
                    "fatal",
                    "notraceback",
                    "commands with the same names are registered in the session",
                    "TIP: check all registered commands",
                    f"Registered commands: {', '.join(commandlist)}",
                    f"Command object: \n{json.dumps(commandObj, sort_keys=True, indent=4)}",
                )
            )

        while self.exitState == "run":
            try:
                read = self.__parseInput(self.logger.read(f"{self.cmdname} >"))
                self.command = read["command"]
                self.parametrs = read["param"]
                self.paramCount = len(self.parametrs)
                if self.command == "fuck":
                    raise Exception(
                        "warn",
                        "notraceback",
                        "Why you so evil?...",
                        ":_(",
                        "TIP: you can be beter",
                    )

                self.runned = False
                self.voidcommand = False
                if self.command == "":
                    self.voidcommand = True
                else:
                    for command in self.registeredCommands:
                        if self.command in command["aliases"]:
                            self.running = command
                            if (
                                not (
                                    self.paramCount
                                    > (
                                        len(self.running["required"])
                                        + len(self.running["optional"])
                                    )
                                    or self.paramCount < len(self.running["required"])
                                )
                                or self.running["dontcheckopt"]
                            ):
                                command["run"](self)
                            else:
                                self.invalidUsage()
                            self.runned = True
                            break
                        self.runned = False
                if not (self.runned or self.voidcommand):
                    self.logger.wrn(
                        "Unknown command, type 'help' for get advanced help",
                        f"{self.cmdname} UNKNOWN",
                    )
            except Exception as e:
                self.ExceptionPrint(e)
        for registeredAction in self.registeredExitActions:
            registeredAction(self)


if __name__ == "__main__":
    nlu = nlulib4.NewLifeUtils(silent=True)
    LoadingScreen("MYCMD", nlu)
    console = BasicModule(nlu, "MY CMD")

    class database(BasicModule.command):
        command = "database"
        description = "start database manage session"
        aliases = [command, "dbconnect", "db"]
        required = []
        optional = []

        def run(console):
            console.logger.log(f"Start up from '{console.cmdname}' to 'DB Manage'")
            dbmanager = BasicModule(
                console.nlu, "DB Manage", "easy way to manage database"
            )
            def createTable(console, rowCount, sizes, data, title="TABLE"):
                def screate(s, n):
                    space = " " * (int(n) - len(str(s)))
                    return space + str(s)

                # ╔══════╦═══════════╗
                table = "╔"
                for i in range(rowCount):  # 1111111
                    table += sizes[i] * "═" + "╦"
                table = table[:-1] + "╗\n║"

                # ╔══════╦═══════════╗
                # ║title ║title2     ║ [0] [1]
                for text in range(rowCount):  # 222222
                    table += screate(data[text], sizes[text]) + "║"
                table += "\n╠"

                # ╔══════╦═══════════╗
                # ║title ║title2     ║ [0] [1]
                # ╠══════╬═══════════╣
                for i in range(rowCount):  # 33333333
                    table += sizes[i] * "═" + "╬"
                table = table[:-1] + "╣\n║"

                # ╔══════╦═══════════╗
                # ║title ║title2     ║ [0] [1]
                # ╠══════╬═══════════╣
                # ║d1    ║123        ║ [2] [3]
                # ║d2    ║1232       ║ [4] [5]
                # ║d3    ║123 1234   ║ [6] [7]

                data = data[rowCount:]  # data[0:n]-[0:1] = [2:n]
                for datatext in range(
                    0, len(data), rowCount
                ):  # 4444444
                    for i in range(rowCount):
                        table += (
                            f"{screate(data[datatext+i], sizes[i])}║"
                        )
                    table += "\n║"
                table = table[:-1] + "╚"

                # ╔══════╦═══════════╗
                # ║title ║title2     ║ [0] [1]
                # ╠══════╬═══════════╣
                # ║d1    ║123        ║ [2] [3]
                # ║d2    ║1232       ║ [4] [5]
                # ║d3    ║123 1234   ║ [6] [7]
                # ╚══════╩═══════════╝
                for i in range(rowCount):  # 1111111
                    table += sizes[i] * "═" + "╩"
                table = table[:-1] + "╝\n"
                console.logger.tip(f'{title}:\n{table}')




            def getMaxSizeRecord(console, response, rowsCount, tableInfo):
                
                lineLengths = []  # Вычисляем начальную длину названия поля
                for i in range(rowsCount):
                    lineLengths.append(len(rowsNamesData[i][1]))
                
                for line in response:  # В каждой записи
                    for row in range(rowsCount):  # Для каждого столбца
                        if (
                            len(str(line[row])) > lineLengths[row]
                        ):  # Если длина строки в записи[столбце] больше
                            lineLengths[row] = len(
                                str(line[row])
                            )  # Устанавливаем ее как максимальную для столбца
                return lineLengths
            def checkConnection(console):
                try:
                    if console.connectState == "succeful":
                        console.logger.log(f"Connection state: {console.connectState}")
                        return True
                    elif console.connectState == "firstentry":
                        console.logger.wrn(f"You not connected to base any time")
                        console.logger.wrn(f"Type 'startsession' to start session")
                        return False
                    else:
                        console.logger.wrn(f"Connection state: {console.connectState}")
                        return False
                except AttributeError:

                    return False

            def initConnectionState(console):
                console.logger.log(f"Setup connection...")
                console.connectState = "firstentry"

            def saveAll(console):
                if console.registeredFunctions["checkConnection"](console):
                    console.connection.commit()
                    console.logger.log("Saving all before exit complete succeful!")
                else:
                    console.logger.wrn("Unable to save, no connection")

            def closeConnection(console):
                if console.registeredFunctions["checkConnection"](console):
                    console.connection.close()
                    console.connectState = "disconnected"
                    console.logger.log("Connection closing complete")

            def exitTask(console):
                if console.connectState == "succeful":
                    console.registeredFunctions["saveAll"](console)
                    console.registeredFunctions["closeConnection"](console)

            class startsession(BasicModule.command):
                command = "startsession"
                description = "setting up base with provided name"
                aliases = [command, "start", "setup", "newsession"]
                required = ["database name"]
                optional = []

                def run(console):
                    console.logger.log("Importing sqlite3...")
                    console.sqlite3 = __import__("sqlite3")
                    console.logger.log("Importing os...")
                    console.os = __import__("os")
                    console.basename = console.parametrs[0]
                    console.cwd = console.os.getcwd() + "\\_DB\\"
                    if console.os.path.exists(console.cwd):
                        console.logger.log(f"{console.cwd} directory exists")
                    else:
                        console.logger.wrn(
                            f"{console.cwd} not exists... creating for you"
                        )
                        console.os.mkdir(console.cwd)
                    console.basefpath = console.cwd + console.basename
                    console.logger.log(f"Setting db name to {console.basename}...")
                    console.logger.log(f"Current path: {console.cwd}")
                    console.logger.log(f"Connecting to {console.basename}.. .")
                    console.connection = console.sqlite3.connect(console.basefpath)
                    console.logger.log(f"Creating cursor {console.basename}...")
                    console.cursor = console.connection.cursor()
                    console.logger.log(f"Succeful connected!")
                    console.connectState = "succeful"

            class check(BasicModule.command):
                command = "check"
                description = "displays data base state"
                aliases = [command, "state"]
                required = []
                optional = []

                def run(console):
                    console.registeredFunctions["checkConnection"](console)

            class createtable(BasicModule.command):
                command = "createtable"
                description = "creating table"
                aliases = [command, "ctable", "newtable"]
                required = ["name", "field", "type"]
                optional = ["field2", "type2"]
                dontcheckopt = True

                def run(console):
                    if console.registeredFunctions["checkConnection"](console):
                        name = console.parametrs[0]
                        fieldtypes = []
                        fieldnames = []
                        if len(console.parametrs[1:]) > 1:
                            if len(console.parametrs) % 2 == 1:
                                fieldtypes = console.parametrs[1:][1::2]
                                fieldnames = console.parametrs[1:][::2]
                                for fieldtype in fieldtypes:
                                    if fieldtype not in ["text", "int"]:
                                        console.logger.wrn(
                                            f"Wrong field type: {fieldtype}"
                                        )
                                        break
                                else:
                                    console.logger.tip(f"Create table '{name}'")
                                    fields = []
                                    for fieldnum in range(len(fieldnames)):
                                        fields.append(
                                            f"{fieldnames[fieldnum]} {fieldtypes[fieldnum]}"
                                        )
                                    execute = (
                                        f'CREATE TABLE {name} ({", ".join(fields)})'
                                    )
                                    console.logger.tip(f"Executing: {execute}")
                                    try:
                                        console.cursor.execute(execute)
                                    except console.sqlite3.OperationalError:
                                        console.logger.wrn(
                                            f"'{name}' is already exists!"
                                        )
                                    else:
                                        console.logger.log(
                                            f"Succeful created table {name}!"
                                        )
                            else:
                                console.logger.wrn(
                                    f"Something wrong: not given the name of a table or field is incorrectly documented"
                                )
                        else:
                            console.logger.wrn(
                                f"not given the name of a table or field is incorrectly documented"
                            )
                    else:
                        console.logger.wrn(f"Connectrion state: {console.connectState}")
                        console.logger.wrn(f"Unable create table: no connection")

            class adddata(BasicModule.command):

                command = "adddata"
                description = "adding data into atble"
                aliases = [command, "insert"]
                required = ["table", "field"]
                optional = ["field2"]
                dontcheckopt = True

                def run(console):
                    if console.registeredFunctions["checkConnection"](console):
                        table = console.parametrs[0]
                        fields = console.parametrs[1:]
                        execute = f"PRAGMA TABLE_INFO('{table}')"
                        console.logger.log(f"Getting count of fields: {execute}...")
                        console.cursor.execute(execute)
                        response = list(console.cursor.fetchall())
                        console.logger.log(f"Fields: {len(response)}")
                        if len(fields) > len(response):
                            console.logger.wrn(
                                f"Too many fields to add; Need: {len(response)}, Provided: {len(fields)}"
                            )
                        if len(fields) < len(response):
                            console.logger.wrn(
                                f"too few fields to add; Need: {len(response)}, Provided: {len(fields)}"
                            )
                        else:
                            execute = f"INSERT INTO {table} VALUES ('{(chr(39)+', '+chr(39)).join(fields)}')"
                            console.logger.log(f"Executing: {execute}")
                            console.cursor.execute(execute)

            class describe(BasicModule.command):

                command = "describe"
                description = "displays fields in table"
                aliases = [command]
                required = ["table"]
                optional = []
                dontcheckopt = True

                def run(console):
                    if console.registeredFunctions["checkConnection"](console):
                        if console.paramCount == 1:

                            def screate(s, n):
                                space = " " * (int(n) - len(str(s)))
                                return space + str(s)

                            table = console.parametrs[0]
                            execute = f"PRAGMA TABLE_INFO('{table}')"
                            console.logger.log(f"Executing: {execute}")
                            console.cursor.execute(execute)
                            response = console.cursor.fetchall()
                            result = ""
                            sizes = [3, 20, 15, 7, 20, 2]
                            
                            # ╔═╦═══╗
                            # ║t║tit║
                            # ╠═╬═══╣

                            result += f'╔{"═"*sizes[0]}╦{"═"*sizes[1]}╦{"═"*sizes[2]}╦{"═"*sizes[3]}╦{"═"*sizes[4]}╦{"═"*sizes[5]}╗\n'
                            result += f'║{screate("cid",sizes[0])}║{screate("name",sizes[1])}║{screate("type",sizes[2])}║{screate("notnull",sizes[3])}║{screate("default",sizes[4])}║{screate("pk",sizes[5])}║\n'
                            result += f'╠{"═"*sizes[0]}╬{"═"*sizes[1]}╬{"═"*sizes[2]}╬{"═"*sizes[3]}╬{"═"*sizes[4]}╬{"═"*sizes[5]}╣\n'

                            # for ...:║d║123║
                            #         ║d║456║
                            for fieldraw in response:
                                field = list(fieldraw)
                                for rowid in range(len(field)):
                                    result += f"║{screate(field[rowid],sizes[rowid])}"
                                result += f"║\n"
                            result += f'╚{"═"*sizes[0]}╩{"═"*sizes[1]}╩{"═"*sizes[2]}╩{"═"*sizes[3]}╩{"═"*sizes[4]}╩{"═"*sizes[5]}╝\n'
                            console.logger.log(f"\n{result}")

            class show(BasicModule.command):
                command = "show"
                description = "Displays all data in table"
                aliases = [command, "displaytable", "tabledata", "datatable"]
                required = ["table"]
                optional = []

                def run(console):
                    if console.registeredFunctions["checkConnection"](console):
                        try:

                            table = console.parametrs[0]
                            # Получаю данные из таблицы
                            execute = f"SELECT * FROM {table}"
                            console.logger.log(f"Executing: {execute}")
                            console.cursor.execute(execute)
                            response = console.cursor.fetchall()
                            # Получаю Описание таблицы
                            execute = f"PRAGMA TABLE_INFO('{table}')"
                            console.cursor.execute(execute)
                            
                            tableInfo = list(
                                console.cursor.fetchall()
                            ) 
                            rowsCount = len(tableInfo)  # Количество столбцов


                            # Вычисляем максимальную длину столбца
                            lineLengths = console.registeredFunctions["getMaxSizeRecord"](console, response, rowsCount, tableInfo)
                            
                            
                            data = []
                            for i in range(rowsCount): # Получаем названия полей
                                data.append(tableInfo[i][1])        # Начинаем собирать шапку
                                
                            for record in response:  # Для записи в таблице
                                for element in record:  # Для каждого элемента
                                    data.append(
                                        element
                                    )  # Добавляем его в общую массу, генератор сам разберется
                            console.logger.wrn(f"data {data} lineLengths {lineLengths} RESPPPPPP {response} tableInfotableInfo {tableInfo}'")
                            console.registeredFunctions["createTable"](console, rowsCount, lineLengths, data)


                        except Exception as e:
                            if e.args[0][0:13] == "no such table":
                                console.logger.wrn(f"No such table named '{table}'")
                            else:
                                console.ExceptionPrint(e)

            class saveall(BasicModule.command):
                command = "saveall"
                description = "saving any changes with database"
                aliases = [command]
                required = []
                optional = []

                def run(console):
                    console.registeredFunctions["saveAll"](console)

            class closeconnection(BasicModule.command):
                command = "closeconnection"
                description = "closing connection"
                aliases = [command]
                required = []
                optional = []

                def run(console):
                    console.registeredFunctions["closeConnection"](console)

            dbmanager.registerFunction(getMaxSizeRecord, "getMaxSizeRecord")
            dbmanager.registerFunction(createTable, "createTable")
            dbmanager.registerFunction(checkConnection, "checkConnection")
            dbmanager.registerFunction(saveAll, "saveAll")
            dbmanager.registerFunction(closeConnection, "closeConnection")
            dbmanager.registerInit(initConnectionState)
            dbmanager.registerExit(exitTask)
            dbmanager.registerCommand(saveall)
            dbmanager.registerCommand(closeconnection)
            dbmanager.registerCommand(startsession)
            dbmanager.registerCommand(check)
            dbmanager.registerCommand(createtable)
            dbmanager.registerCommand(adddata)
            dbmanager.registerCommand(describe)
            dbmanager.registerCommand(show)
            dbmanager.Main()

    console.registerCommand(database)
    console.Main()

"""
class mycmd(BasicModule.command):
    command = 'mycommand'
    description = 'This is my custom command'
    aliases = [command, 'mycommandalias']
    required = ['myreq']
    optional = ['myopt']
    dontcheckopt = False
    def run(console):
        #some code here
"""
