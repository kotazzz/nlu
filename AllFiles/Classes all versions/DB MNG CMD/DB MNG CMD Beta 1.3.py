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

class BasicConsole(object):
    storage = {
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
    def __init__(self, nlu):
        #save parametrs to class`es variables
        self.nlu = nlu
        
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
    def createHelpPage(self,nlu,storage, module_command = '',helpType = 'A'):
        helpPage = ''
        class C:
            MDL = nlu.Color.FGC.RED
            MDLDSC = nlu.Color.FGC.BRED
            CMD = nlu.Color.FGC.CYAN
            ALI = nlu.Color.FGC.BLUE
            DSK = nlu.Color.FGC.PURPLE
            DSKTXT = nlu.Color.FGC.BPURPLE
            SCMD = nlu.Color.ACC.UNDERLINE+nlu.Color.FGC.WHITE
            SREQ = nlu.Color.FGC.BGRAY
            SOPT = nlu.Color.FGC.GRAY
            R = nlu.Color.ACC.RESET
        if helpType == 'A':
            moduleKeys = []
            moduleKeys = list(storage.keys())
            for moduleName in moduleKeys:
                helpPage +=\
                f"\n{C.MDL}{moduleName}{C.R} - {C.MDLDSC}{storage[moduleName]['DESCRIPTION']}\n"
                
                commandList = []
                commandList = list(storage[moduleName]['COMMANDS'].keys())
                for commandName in commandList:
                    syntax = f"{C.SCMD}{commandName}{C.R}"
                    if storage[moduleName]['COMMANDS'][commandName]['usage']['required'] != []:
                        syntax += f" {C.SREQ}<{'> <'.join(storage[moduleName]['COMMANDS'][commandName]['usage']['required'])}>"
                    if storage[moduleName]['COMMANDS'][commandName]['usage']['optional'] != []:
                        syntax += f" {C.SOPT}<{'> <'.join(storage[moduleName]['COMMANDS'][commandName]['usage']['optional'])}>"
                    helpPage +=\
                    f"\t{C.CMD}{commandName}\n"+\
                    f"\t\t{C.DSK}Description: {C.DSKTXT}{storage[moduleName]['COMMANDS'][commandName]['description']}\n"+\
                    f"\t\t{C.R  }Usage      : {syntax}\n"+\
                    f"\t\t{C.ALI}Aliases    : {', '.join(storage[moduleName]['COMMANDS'][commandName]['aliases'])}\n"
                    
        elif helpType == 'M':
            moduleKeys = []
            moduleKeys = list(storage.keys())
            for moduleName in moduleKeys:
                if moduleName == module_command:
                    helpPage +=\
                    f"\n{C.MDL}{moduleName}{C.R} - {C.MDLDSC}{storage[moduleName]['DESCRIPTION']}\n"
                    commandList = []
                    commandList = list(storage[moduleName]['COMMANDS'].keys())
                    for commandName in commandList:
                        syntax = f"{C.SCMD}{commandName}{C.R}"
                        if storage[moduleName]['COMMANDS'][commandName]['usage']['required'] != []:
                            syntax += f" {C.SREQ}<{'> <'.join(storage[moduleName]['COMMANDS'][commandName]['usage']['required'])}>"
                        if storage[moduleName]['COMMANDS'][commandName]['usage']['optional'] != []:
                            syntax += f" {C.SOPT}<{'> <'.join(storage[moduleName]['COMMANDS'][commandName]['usage']['optional'])}>"
                        helpPage +=\
                        f"\t{C.CMD}{commandName}\n"+\
                        f"\t\t{C.DSK}Description: {C.DSKTXT}{storage[moduleName]['COMMANDS'][commandName]['description']}\n"+\
                        f"\t\t{C.R  }Usage      : {syntax}\n"+\
                        f"\t\t{C.ALI}Aliases    : {', '.join(storage[moduleName]['COMMANDS'][commandName]['aliases'])}\n"
        elif helpType == 'C':
            moduleObj = storage
            helpPage +=\
            f"\n{C.MDL}{moduleObj['NAME']}{C.R} : {C.MDLDSC}{moduleObj['DESCRIPTION']}\n"
            commandList = []
            commandList = list(storage['COMMANDS'].keys())
            for commandName in commandList:
                if commandName == module_command: 
                    syntax = f"{C.SCMD}{commandName}{C.R}"
                    if storage['COMMANDS'][commandName]['usage']['required'] != []:
                        syntax += f" {C.SREQ}<{'> <'.join(storage['COMMANDS'][commandName]['usage']['required'])}>"
                    if storage['COMMANDS'][commandName]['usage']['optional'] != []:
                        syntax += f" {C.SOPT}<{'> <'.join(storage['COMMANDS'][commandName]['usage']['optional'])}>"
                    helpPage +=\
                    f"\t{C.CMD}{commandName}\n"+\
                    f"\t\t{C.DSK}Description: {C.DSKTXT}{storage['COMMANDS'][commandName]['description']}\n"+\
                    f"\t\t{C.R  }Usage      : {syntax}\n"+\
                    f"\t\t{C.ALI}Aliases    : {', '.join(storage['COMMANDS'][commandName]['aliases'])}\n"
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
    class
    class BasicCommandPack:
        def register(self):
            self.registerCommand(self.BasicCommandPack.exit)
            self.registerCommand(self.BasicCommandPack.cls)
            self.registerCommand(self.BasicCommandPack.message)
            self.registerCommand(self.BasicCommandPack.help)
        class exit:
            command = 'exit'
            def run(self):
                if self.paramCount != 0:
                    return 1
                self.exitState = '0' 
                self.logger.log(f'Exiting from console with code {self.exitState}')
        class cls:
            command = 'cls'
            def run(self):
                if self.paramCount != 0:
                    return 1
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
                        tag = self.parametrs[1]
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
        class help:
            command = 'help'
            def run(self):
                if self.paramCount  == 0:
                    self.logger.tip(self.createHelpPage(self.nlu, self.storage['HELPPAGEDATA'], self.path, 'M'))
                elif self.paramCount == 1:
                    
                    moduleNames = []
                    moduleNames = list(self.storage['HELPPAGEDATA'].keys())
                    commandNames = []
                    for moduleName in moduleNames:
                        commandNames += list(self.storage['HELPPAGEDATA'][moduleName]['COMMANDS'].keys())
                    if self.parametrs[0] in moduleNames:
                        self.logger.tip(self.createHelpPage(self.nlu, self.storage['HELPPAGEDATA'], self.parametrs[0], 'M'))
                    elif self.parametrs[0] in commandNames:
                        self.logger.tip(self.createHelpPage(self.nlu, self.storage['HELPPAGEDATA'][self.path], self.parametrs[0], 'C'))
                    else:
                        self.logger.tip(self.createHelpPage(self.nlu, self.storage['HELPPAGEDATA'], self.path, 'M'))
                else:
                    return 1

    def Main(self):
        self.logger = self.nlu.Logger()

        self.BasicCommandPack.register(self)
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
    LoadingScreen('DB MANAGER', nlu)

    # console = BasicConsole(nlu)
    # console.storage['HELPPAGEDATA']['TEST'] = {}
    # console.storage['HELPPAGEDATA']['TEST']['NAME'] = 'TEST'
    # console.storage['HELPPAGEDATA']['TEST']['DESCRIPTION'] = 'My custom section'
    # console.storage['HELPPAGEDATA']['TEST']['COMMANDS'] ={
    # "test":{
            # "aliases":["test"],
            # "description":"Custom code for me",
            # "usage":{
                # "required":['text'],
                # "optional":['maxlinelength'],
            # },
        # }
    # }

    # class test:
        # command = 'test'
        # def run(self):
            # if self.paramCount > 2 | self.paramCount < 1:
                # return 1
            # else:
                # if self.paramCount == 1:
                    # self.nlu.BigPrint(self.parametrs[0])
                # if self.paramCount == 2:
                    # self.nlu.BigPrint(self.parametrs[0],self.parametrs[1])

    # console.registerCommand(test)
    # console.Main()
