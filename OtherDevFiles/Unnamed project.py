# new project
from NewLifeUtils import *
class Info(CustomShellModule.Command):
    command = "инфо"
    aliases = [command, "информация"]
    description = "Вся информация о коммандах"
    required = []
    optional = []
    skipcheck = False
    def run(console):
        console.Logger.log(f'Command "{console.run["command"]}" executed now')

if __name__ == "__main__":
    #Init CustomShellModule
    cmd = CustomShellModule()
    
    #Register commands
    cmd.registerCommand(Info)
    
    #start main cycle
    cmd.main()
