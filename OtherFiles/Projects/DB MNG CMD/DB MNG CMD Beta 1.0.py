# coding=utf8
import sqlite3 as sql
import Libraries.nlu4 as nlulib4
#init main nutil object and logger
nlu = nlulib4.NewLifeUtils(silent=True)
l = nlu.Logger()
#def color spaces
FGC = nlu.Color.FGC
BGC = nlu.Color.BGC
ACC = nlu.Color.ACC
MCC = nlu.Color.MCC

#get libs from nlu
os = nlu.Libs.os
time = nlu.Libs.time

#def functions
def LoadingScreen(title, nlu):
    for n in range(1, 255, 5):
        nlu.BigPrint(title, maxlinelength=10, begin = ACC.CUSTOMRGB(n, n, n))
        print(nlu.Color.MCC.UP(7))
        time.sleep(0.0001)
    nlu.BigPrint(title, maxlinelength=10, begin = ACC.CUSTOMRGB(n, n, n))
    lineLength = 11 * len(title)
    for n in range(lineLength + 1):
        print(f'{FGC.YELLOW}{ACC.UNDERLINE}▐{"▒"*n}{"░"*(lineLength-n)}▌')
        print(MCC.UP(2))
        time.sleep(1 / 150)
    print(f"{FGC.GREEN}{ACC.UNDERLINE}▐" + lineLength * "█" + f"▌{ACC.RESET}")
    time.sleep(1 / 3)



MainStorage = {
    "HELPPAGEDATA":{
        "MAIN":{
            "NAME":"Main",
            "DESCRIPTION":"Root commands",
            "COMMANDS":{
                "help":{
                    "aliases":["help"],
                    "description":"Exit from programm",
                    "usage":{
                        "required":[],
                        "optional":['section or command'],
                    },
                },
                "exit":{
                    "aliases":["exit"],
                    "description":"Exit from programm",
                    "usage":{
                        "required":[],
                        "optional":[],
                    },
                },
                "cls":{
                    "aliases":["cls","clearscreen"],
                    "description":"Clear screen",
                    "usage":{
                        "required":[],
                        "optional":[],
                    },
                },
                "message":{
                    "aliases":["message","msg","note"],
                    "description":"Custom message. You can use this for notes. supports color",
                    "usage":{
                        "required":['message'],
                        "optional":['tag', 'color'],
                    },
                },
            },
        },
    },
}

     
    
    
#variables
title = 'DB MANAGER'
class Console(object):
    def __init__(self, nlu, dataStorage):
        #save parametrs to class`es variables
        self.nlu = nlu
        self.storage = dataStorage
        
        #def command list
        self.commands = []
        
        #setting up exit state as "run"
        self.exitState = 'run'
        
        #def libraries
        self.os = nlu.Libs.os
        self.datetime = nlu.Libs.datetime
        self.random = nlu.Libs.random
    def getAliases(self,module, command):
        for commandObj in module['COMMANDS']:
            if commandObj == command:
                return module['COMMANDS'][commandObj]['aliases']
        return command
        # commandsList = []
        # commandsList = list(module['COMMANDS'].keys())
        return 0
    def getUsage(self, module, command):
        commandsList = []
        commandsList = list(module['COMMANDS'].keys())
        commandsObject = module['COMMANDS']
        for commandObj in commandsList:
            if commandObj == command:
                syntax = f'Usage: {command}'
                if commandsObject[command]["usage"]["required"] != []:
                    syntax += f' <{"> <".join(commandsObject[command]["usage"]["required"])}>'
                if commandsObject[command]["usage"]["optional"] != []:
                    syntax += f' [{"] [".join(commandsObject[command]["usage"]["optional"])}]'
                return syntax
    def createHelpPage(self,module, nlu):
        class CLR:
            MODULE = nlu.Color.FGC.RED
            MODULEDESCRIPTION = nlu.Color.FGC.BRED
            COMMAND = nlu.Color.FGC.CYAN
            ALIASES = nlu.Color.FGC.BLUE
            DESCRIPTION = nlu.Color.FGC.PURPLE
            DESCRIPTIONTEXT = nlu.Color.FGC.BPURPLE
            SYNTAXCOMMAND = nlu.Color.ACC.UNDERLINE+nlu.Color.FGC.WHITE
            SYNTAXREQ = nlu.Color.FGC.BGRAY
            SYNTAXOPT = nlu.Color.FGC.GRAY
            R = nlu.Color.ACC.RESET
        helpPage = ''
        helpPage += f"{CLR.MODULE}{module['NAME']}{CLR.R} - {CLR.MODULEDESCRIPTION}{module['DESCRIPTION']}{CLR.R}\n"
        commandsList = []
        commandsList = list(module['COMMANDS'].keys())
        commandsObject = module['COMMANDS']
        for command in commandsList:
            helpPage += f'{CLR.COMMAND}\t{command}:\n'
            helpPage += f'{CLR.ALIASES}\t\tAliases: {", ".join(commandsObject[command]["aliases"])}{CLR.R}\n'
            helpPage += f'{CLR.DESCRIPTION}\t\tDescription: {CLR.DESCRIPTIONTEXT}{commandsObject[command]["description"]}{CLR.R}\n'
            syntax = f'{CLR.SYNTAXCOMMAND}{command}{CLR.R}'
            if commandsObject[command]["usage"]["required"] != []:
                syntax += f' {CLR.SYNTAXREQ}<{"> <".join(commandsObject[command]["usage"]["required"])}>{CLR.R}'
            if commandsObject[command]["usage"]["optional"] != []:
                syntax += f' {CLR.SYNTAXOPT}[{"] [".join(commandsObject[command]["usage"]["optional"])}]{CLR.R}'
            helpPage += f'\t\tSyntax: {syntax}{CLR.R}\n'
        return helpPage
    def parseInput(self, readed):
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
            return {
            "command":"",
            "param":[]
        }
        if len(res) == 1:
            return {
                "command":res[0],
                "param":[]
            }
        else:
            return {
                "command":res[0],
                "param":res[1:len(res)]
            }
    def registerCommand(self,commandClass):
        self.commands.append({"command":commandClass.command, "run":commandClass.run})
    
    class Executer:
        def register(self):
            self.registerCommand(self.Executer.exit)
            self.registerCommand(self.Executer.cls)
            self.registerCommand(self.Executer.message)
        class exit:
            command = 'exit'
            def run(self):
                self.exitState = '0' 
                self.logger.log(f'Exiting from console with code {self.exitState}')
        class cls:
            command = 'cls'
            def run(self):
                self.os.system('cls')
        class message:
            command = 'message'
            def run(self):
                if self.paramCount > 3:
                    return 1
                elif self.paramCount < 1:
                    return 1
                else:
                    CLR = {
                        "BLACK" : self.nlu.Color.FGC.BLACK,
                        "RED" : self.nlu.Color.FGC.RED,
                        "GREEN" : self.nlu.Color.FGC.GREEN,
                        "YELLOW" : self.nlu.Color.FGC.YELLOW,
                        "BLUE" : self.nlu.Color.FGC.BLUE,
                        "PURPLE" : self.nlu.Color.FGC.PURPLE,
                        "CYAN" : self.nlu.Color.FGC.CYAN,
                        "BGRAY" : self.nlu.Color.FGC.BGRAY,
                        "GRAY" : self.nlu.Color.FGC.GRAY,
                        "BRED" : self.nlu.Color.FGC.BRED,
                        "BGREEN" : self.nlu.Color.FGC.BGREEN,
                        "BYELLOW" : self.nlu.Color.FGC.BYELLOW,
                        "BBLUE" : self.nlu.Color.FGC.BBLUE,
                        "BPURPLE" : self.nlu.Color.FGC.BPURPLE,
                        "BCYAN" : self.nlu.Color.FGC.BCYAN,
                        "WHITE" : self.nlu.Color.FGC.WHITE,
                    }
                    message = self.parametrs[0]
                    if self.paramCount == 2:
                        tag = self.parametrs[1]
                    else:
                        tag = ''
                    if self.paramCount == 3:
                        color = self.parametrs[2]
                        
                        try:
                            color.format(**CLR)
                        except Exception:
                            self.logger.err('Invalid colors, avaliable:')
                            CLRkeys = []
                            CLRkeys = list(CLR.keys())
                            clrList = []
                            for key in CLRkeys:
                                clrList.append(CLR[key]+key)
                            self.logger.tip(', '.join(clrList))
                            color = ''
                    else:
                        color = ''
                    self.logger.log(f'{color.format(**CLR)}{message}', tag)

            

    def Main(self):
        self.logger = self.nlu.Logger()

        self.Executer.register(self)
        
        while self.exitState == 'run':
            self.path = 'MAIN'
            
            read = self.parseInput(self.logger.read(f'{self.path} >'))
            self.command = read['command']
            self.parametrs = read['param']
            self.paramCount = len(self.parametrs)
            
            isCommandExecuted = False
            for registeredCommand in self.commands:
                if self.command == '':
                    isCommandExecuted = True
                    break
                    
                if self.command in self.getAliases(self.storage['HELPPAGEDATA'][self.path],registeredCommand['command']):
                    completeCode = registeredCommand['run'](self)
                    if completeCode == 1:
                        self.logger.wrn(self.getUsage(self.storage['HELPPAGEDATA'][self.path], registeredCommand['command']), 'USAGE')
                    isCommandExecuted = True
                    
            if not isCommandExecuted:
                self.logger.wrn('Unknown command',f'{self.path} UNKNOWN')
        

#main
if __name__=="__main__":
    LoadingScreen(title, nlu)
    # helpPage = createHelpPage(MainStorage['HELPPAGEDATA']['MAIN'], nlu)
    # print(helpPage)
    # import json
    # print(json.dumps(commandsList, sort_keys=True, indent=4))
    console = Console(nlu, MainStorage)
    console.Main()
    
    
    