##############################################################
# _   _ _____ _____ _____________   __   _____  _____ _   _  #
#| | | |_   _/  ___|_   _| ___ \ \ / /  |  __ \|  ___| \ | | #
#| |_| | | | \ `--.  | | | |_/ /\ V /   | |  \/| |__ |  \| | #
#|  _  | | |  `--. \ | | |    /  \ /    | | __ |  __|| . ` | #
#| | | |_| |_/\__/ / | | | |\ \  | |    | |_\ \| |___| |\  | #
#\_| |_/\___/\____/  \_/ \_| \_| \_/     \____/\____/\_| \_/ #
##############################################################

#################### IMPORTS   ###############################
from enum import Enum
import random
import datetime

#################### SEED SETTINGS ###########################
version = '2.0 beta'
nowtime = datetime.datetime.now()

#################### SEED SETTINGS ###########################
class Seedgen(object):
    def __init__(self, display = ""):
        self.nowtime = datetime.datetime.now()
        self.rawseed = str(int((nowtime.microsecond**3)*(nowtime.second**10)+(nowtime.month*nowtime.day)))
        print('formula: microsecond^3 * second^10 + month*day')
        print(f'result: {self.rawseed}')
        print(f'length result: {len(self.rawseed)}')
        print(f'display: {display}')
        self.errcode = 0
        if len(display) != 0:
            # init L/B
            if display[0] == 'L':
                self.seedDisplayMode = 'L'
            elif display[0] == 'B':
                self.seedDisplayMode = 'B'
            else:
                print('[-1] INVALID TYPE')
                print('Unable to set mask. restart program and try again')
                print('----------UNABLE TO START----------')
                self.errcode = -1
            #init length
            if len(display) > 7:
                print('[-2] INVALID LENGTH')
                print('Unable to set mask. restart program and try again')
                print('----------UNABLE TO START----------')
                self.errcode = -2
            i = 1
            #valid mask
            while i < len(display):
                if display[i] in '01234':
                    print(f'Read mask#{i} : {display[i]} is valid')
                elif display[i] in '56789':
                    print(f'Read mask#{i} : {display[i]} is invalid')
                    print(f'[-3] {display[i]} bigger then 4')
                    print('Unable to set mask. restart program and try again')
                    print('----------UNABLE TO START----------')
                    self.errcode = -3
                else:
                    print(f'Read mask#{i} : {display[i]} is invalid')
                    print(f'[-4] {display[i]} is not a numeric')
                    print('Unable to set mask. restart program and try again')
                    print('----------UNABLE TO START----------')
                    self.errcode = -4
                i+=1
        else:
            print('using mask: B4444')
            display = 'B4444'
            self.seedDisplayMode = 'B'
        if not(self.errcode < 0):
            #parse dm = L
            self.seed = ''
            if  self.seedDisplayMode == 'L':
                print('No errors while parsing')
                print('Start to parsing mask as L type')
                i = 1
                self.seed = ''
                offset = 0
                while i < len(display):
                    offset += int(display[i])
                    print(f'''setting block#{i}, length: {display[i]}
                    getting chunk {len(self.rawseed)-offset}-{len(self.rawseed)-(offset-int(display[i]))}. 
                    this is {self.rawseed[(len(self.rawseed)-offset):(len(self.rawseed)-(offset-int(display[i])))]}''')
                    self.seed += f'{self.rawseed[len(self.rawseed)-offset:len(self.rawseed)-(offset-int(display[i]))]} '
                    i+=1
            #parse dm = L
            if  self.seedDisplayMode == 'B': 
                print('No errors while parsing')
                print('Start to parsing mask as L type')
                i = 1
                self.seed = ''
                offset = 0
                while i < len(display):
                    offset += int(display[i])
                    print(f'''setting block#{i}, length: {display[i]}
                    getting chunk {offset-int(display[i])}-{offset}. 
                    this is {self.rawseed[offset-int(display[i]):offset]}''')
                    self.seed += f'{self.rawseed[offset-int(display[i]):offset]} '
                    i+=1
        print(f'using the seed: {"".join(self.seed.split())}')
        random.seed("".join(self.seed.split()))
    def customSeed(self, seed):
        self.seed = seed
    def getSeed(self):
        return self.seed
        
#################### HERO CLASS ###############################
#кто, кого, кому, кого, кем, о ком
class People(object):
    lib = {
        "NAMES": [
            ["","","","","",""],
            ["W","Лиза","Лизы","Лизе","Лизы","Лизой","Лизе"],
            ["M","Семен","Семена","Семену","Семена","Семеном","Семену"]
        ],
        "SURNAMES": [
            ["",""],
            ["Желдак","Желдак"],
            ["Луганский","Луганская"]
        ],
        "SEX": [
            "",
            "Мужской",
            "Женский",
            "Трансгендерный"
        ],
        "HEALTH_PROBLEMS": [
            ["",""],
            ["Нет проблем","Здоровье"],
            ["Плохой слух","Слух"],
            ["Плохое зрение","Зрение"]
        ]
    }
    def selectFrom(self, frm):
        random_key = random.randrange(1, len(frm))
        return frm[random_key]
    def __init__(self):
        self.name = self.selectFrom(self.lib["NAMES"])
        
        if self.name[0] == "W":
            if random.getrandbits(1):
                self.sex = self.lib["SEX"][2]
            else:
                self.sex = self.lib["SEX"][3]
        elif self.name[0] == "M":
            self.sex = self.lib["SEX"][1]

        if self.sex == self.lib["SEX"][1]:
            self.surname = self.selectFrom(self.lib["SURNAMES"])[0]
        else:
            self.surname = self.selectFrom(self.lib["SURNAMES"])[1]
#################### VARIABLES ###############################

#################### PREPARE   ###############################


#################### MAIN      ###############################
def main():
    want_exit = False
    while not want_exit: 
        seedgen = Seedgen()#input('your mask:')
        inp = input("Введите сид или оставьте пустую строку для рандома")
        if inp != "":
            seedgen.customSeed(inp)
        print()
        
        if seedgen.errcode < 0:
            print(f'exiting. err code: {seedgen.errcode}')
            exit(seedgen.errcode)
        else:
            print(seedgen.getSeed())
            print()
            print()
            print()
            hero = People()
            print(f'''
            {hero.name[1]} {hero.surname} ({hero.sex})
            ''')
        if input('Введите "1" для выхода: ') == '1':
            want_exit = True
        else:
            print('Вы отказались о твыхода. Перезапуск генератора...')
            
if __name__ == '__main__':
    main()
