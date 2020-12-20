# My Exception
print('hello')
class NewLifeUtilsWorkError(Exception):
    def __init__(self, text):
        self.txt = text

class  Other(NewLifeUtilsWorkError):
    def __init__(self, text):
        self.txt = text
        
raise Other('a')