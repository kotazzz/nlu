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
        info = '\n---------------------------------------------\n'
        info += 'Это мой новый проект основанный на NLU5\n'
        info += 'Больше нет доступной информации\n'
        info += '---------------------------------------------\n'
        console.Logger.log(info)

if __name__ == "__main__":
    #Init CustomShellModule
    cmd = CustomShellModule()
    
    #Register commands
    cmd.registerCommand(Info)
    
    #start main cycle
    cmd.main()
