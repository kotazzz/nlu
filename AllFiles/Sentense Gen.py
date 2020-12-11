#. ^ $ * + ? { } [ ] \ | ( )
import random,time,os,datetime
from colorama import Fore,Style,Back,Cursor,init


pos = lambda y, x: Cursor.POS(x, y)
os.system('color 0f')
init()
print(f'{Style.DIM}{Fore.WHITE}{Back.BLACK}')
os.system('cls')
def selectFrom(frm):
    random_key = random.randrange(1, len(frm))
    return frm[random_key]

class Logger(object):
    def __init__(self, 
        format_err = '{date} {red}{tag}{empty} : {red}{message}{white}', 
        format_log = '{date} {green}{tag}{empty} : {green}{message}{white}', 
        format_wrn = '{date} {yellow}{tag}{empty} : {yellow}{message}{white}', 
        format_rea = '{date} {blue}{tag}{empty} : {message} {cyan}[{read}]{white}', 
        date = "[%d.%m.%Y %H:%M]", 
        tag_max = 10):
        
        self.extra = f'{Style.DIM}{Back.BLUE}{Style.BRIGHT}{Fore.RED}'
        self.normalize = f'{Fore.WHITE}{Back.BLACK}{Style.NORMAL}'
        self.format_err = format_err
        self.format_log = format_log
        self.format_wrn = format_wrn
        self.format_rea = format_rea
        self.date = date
        self.tag_max = tag_max    
    def log(self, message,tag = 'LOG'):
        now = datetime.datetime.now()
        if len(tag) < self.tag_max:
            empty = " "*(self.tag_max-len(tag))
        else:
            empty = ""
        print(self.format_log.format(
            date = now.strftime(self.date),
            tag = tag,
            empty = empty,
            tab = "\t",
            message = message,
            black=Fore.BLACK,
            red=Fore.RED,
            green=Fore.GREEN,
            yellow=Fore.YELLOW,
            blue=Fore.BLUE,
            magenta=Fore.MAGENTA,
            cyan=Fore.CYAN,
            white=Fore.WHITE,
            reset=Fore.RESET))
    def err(self, message,tag = 'ERR'):
        now = datetime.datetime.now()
        if len(tag) < self.tag_max:
            empty = " "*(self.tag_max-len(tag))
        else:
            empty = ""
        print(self.format_err.format(
            date = now.strftime(self.date),
            tag = tag,
            empty = empty,
            tab = "\t",
            message = message,
            black=Fore.BLACK,
            red=Fore.RED,
            green=Fore.GREEN,
            yellow=Fore.YELLOW,
            blue=Fore.BLUE,
            magenta=Fore.MAGENTA,
            cyan=Fore.CYAN,
            white=Fore.WHITE,
            reset=Fore.RESET))
    def wrn(self, message,tag = 'wrn'):
        now = datetime.datetime.now()
        if len(tag) < self.tag_max:
            empty = " "*(self.tag_max-len(tag))
        else:
            empty = ""
        print(self.format_wrn.format(
            date = now.strftime(self.date),
            tag = tag,
            empty = empty,
            tab = "\t",
            message = message,
            black=Fore.BLACK,
            red=Fore.RED,
            green=Fore.GREEN,
            yellow=Fore.YELLOW,
            blue=Fore.BLUE,
            magenta=Fore.MAGENTA,
            cyan=Fore.CYAN,
            white=Fore.WHITE,
            reset=Fore.RESET))
    def read(self, message,tag = 'READ'):
        now = datetime.datetime.now()
        if len(tag) < self.tag_max:
            empty = " "*(self.tag_max-len(tag))
        else:
            empty = ""
        readed = input(f'{self.extra}{message}')
        print(f'{self.normalize}{Cursor.UP(1)}'+self.format_rea.format(
            date = now.strftime(self.date),
            tag = tag,
            empty = empty,
            tab = "\t",
            message = message,
            read = readed,
            black=Fore.BLACK,
            red=Fore.RED,
            green=Fore.GREEN,
            yellow=Fore.YELLOW,
            blue=Fore.BLUE,
            magenta=Fore.MAGENTA,
            cyan=Fore.CYAN,
            white=Fore.WHITE,
            reset=Fore.RESET))
        return readed
words = {
    "VERB":[
        ["","",""],
        ["","стоял","стояла","стояло"],
        ["","лежал","лежала","лежало"]
    ],
    "OBJECT":[
        #кто, кого, кому, кого, кем, о ком
        ["","","","","",""],
        ["M","человек","человека","человеку","человека","человеком","человеке"],
        ["A","дерево","дерева","дереву","дерева","деревом","дереве"],
    ],
    "ADJECTIVE":[
        ["","","",""],
        ["","милый","милая","милое"],
        ["","красивый","красивая","красивое"],
    ]
 }

def main():
    l = Logger()
    custimseed = l.read('Введите Сид или оставьте пустую строку: ', 'SEED')
    if custimseed != '':
        random.seed(custimseed)
        l.wrn(f'Установлен сид: {custimseed}','SEED')
    else:
        seed = int(time.time())
        l.wrn(f'Установлен авто-сид: {seed}','SEED')
        random.seed(seed)
    
    l.log('Иницилизация рандом-генератора завершена','SEED')
if __name__ == '__main__':
    main()
