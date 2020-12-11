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
    def __init__(self, nlu, cmdname = 'root', cmdabout = 'default console'):
        # save parametrs to class`es variables
        self.nlu = nlu
        self.logger = self.nlu.Logger()
        self.cmdname = cmdname
        self.cmdabout = cmdabout
        # def command list
        self.registeredCommands= []

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
        command = 'mycommand'
        description = 'This is my custom command'
        aliases = [command, 'mycommandalias']
        required = ['myreq']
        optional = ['myopt']
        def run(self, console):
            console.logger.log('The command runned!')
            
    def __registerBasic(self):
        class _exit(self.command):
            command = 'exit'
            description = 'closing module'
            aliases = [command]
            required = []
            optional = []
            def run(console):
                console.exitState = "0"
        class _help(self.command):
            command = 'help'
            description = 'displays all commands in this module'
            aliases = [command]
            required = []
            optional = ['command']
            def run(console):
                class CLR:
                    MDL = console.nlu.Color.FGC.RED
                    MDLDSK = console.nlu.Color.FGC.BRED
                    CMD = console.nlu.Color.FGC.CYAN
                    CMDDSK = console.nlu.Color.FGC.BBLUE
                    ALS = console.nlu.Color.FGC.PURPLE
                    ALSTXT = console.nlu.Color.FGC.BPURPLE
                    SCMD = console.nlu.Color.ACC.UNDERLINE + nlu.Color.FGC.WHITE
                    SREQ = console.nlu.Color.FGC.BGRAY
                    SOPT = console.nlu.Color.FGC.GRAY
                    R = console.nlu.Color.ACC.RESET

                helpPage = ''
                if console.paramCount == 0:
                    helpPage +=f'\n{CLR.MDL}{console.cmdname} - {CLR.MDLDSK}{console.cmdabout}\n'
                    for command in console.registeredCommands:  
                        syntax = f'{CLR.SCMD}{command["command"]}{CLR.R} '
                        if command["required"] != []:
                            syntax += f'{CLR.SREQ}<{"> <".join(command["required"])}>{CLR.R} '
                        if command["optional"] != []:
                            syntax += f'{CLR.SOPT}[{"] [".join(command["optional"])}]{CLR.R} '
                        helpPage +=\
                        f'\t{CLR.CMD}{command["command"]}\n'+\
                        f'\t\t{CLR.CMDDSK}Description: {command["description"]}\n'+\
                        f'\t\t{CLR.ALS}Aliases: {CLR.ALSTXT}{command["aliases"]}\n'+\
                        f'\t\t{CLR.CMDDSK}Usage: {syntax}{CLR.R}\n'
                console.logger.tip(helpPage, f'{console.cmdname} HELP')
        self.registerCommand(_exit)
        self.registerCommand(_help)

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
            read = self.__parseInput(self.logger.read(f"{self.cmdname} >"))
            self.command = read["command"]
            self.parametrs = read["param"]
            self.paramCount = len(self.parametrs)
            for command in self.registeredCommands:
                if self.command in command['aliases']:
                    command['run'](self)
                    
    

if __name__ == "__main__":
    nlu = nlulib4.NewLifeUtils()
    LoadingScreen('MYCMD', nlu)
    console = BasicModule(nlu)
    console.Main()
    
