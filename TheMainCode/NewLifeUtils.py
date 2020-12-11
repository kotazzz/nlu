# LibsManager
# Color
# Logger
# RandomManager
# TableManager
# DatabaseManager
# ConsoleShellManager
# FileManager
# StringManager
# TracebackManager
# FilelogManager
# Utils
registered_modules = {}

def getModule(name):
    try:
        return registered_modules[name]
    except:
        print('no module found')
def registerModule(reg_class):
    registered_modules[reg_class.name] = reg_class
    
    
class Module(object):
    name = 'Module'
    dependences = []
    
    def __init__(self):
        print(f'ginit {self.name}')
        
        self.modules = {}
        for dependence in self.dependences:
            self.modules[dependence] = getModule(dependence)

class MyModule(Module):
    name = 'MyModule'
    dependences = []
    def test(self):
        print('modulefunction')
        
class MyModule2(Module):
    name = 'MyModule2'
    dependences = ['MyModule']
    def test2(self):
        self.modules['MyModule'].test()
        print('modulefunction2')
        
    
if __name__ == "__main__":
    print('hello')
    registerModule(MyModule)
    registerModule(MyModule2)
    mm1 = getModule('MyModule')
    mm2 = getModule('MyModule2')
    print()
    mm1.test()