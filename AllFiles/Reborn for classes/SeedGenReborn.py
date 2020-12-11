import colorama
import datetime
import os
class newlifeutils(object):

    name = 'NewLifeUtils'
    ver = 'v1.0 beta'
    def __init__(self):
        try:
            os.system('color 0f')
            os.system('cls')
        except NameError:
            print('ERROR: UNABLE TO INIT OS')
            exit(-1)
        try:
            colorama.init()
        except NameError:
            print('ERROR: UNABLE TO INIT COLORAMA')
            exit(-1)
        finally:
            colorama.init()
        try:
            now = datetime.datetime.now()
        except NameError:
            print('ERROR: UNABLE TO INIT DATETIME')
            exit(-1)
        self.logger = self.Logger()
        self.logger.log(f'Thanks for using {self.name} {self.ver}','NLU1')
        # try {
            # Logger.log(f'')
            # }
        
#-----------------------#-----------------------#-----------------------
    class Logger(object):
        
        def __init__(self, 
            format_err = '{date} {red}{tag}{empty} : {red}{message}{white}', 
            format_log = '{date} {green}{tag}{empty} : {green}{message}{white}', 
            format_wrn = '{date} {yellow}{tag}{empty} : {yellow}{message}{white}', 
            format_rea = '{date} {blue}{tag}{empty} : {message} {cyan}[{read}]{white}', 
            date = "[%d.%m.%Y %H:%M]", 
            tag_max = 10):
            
            colorama.init()
            
            self.extra = f'{colorama.Style.DIM}{colorama.Back.BLUE}{colorama.Style.BRIGHT}{colorama.Fore.RED}'
            self.normalize = f'{colorama.Fore.WHITE}{colorama.Back.BLACK}{colorama.Style.NORMAL}'
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
                black=colorama.Fore.BLACK,
                red=colorama.Fore.RED,
                green=colorama.Fore.GREEN,
                yellow=colorama.Fore.YELLOW,
                blue=colorama.Fore.BLUE,
                magenta=colorama.Fore.MAGENTA,
                cyan=colorama.Fore.CYAN,
                white=colorama.Fore.WHITE,
                reset=colorama.Fore.RESET))
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
                black=colorama.Fore.BLACK,
                red=colorama.Fore.RED,
                green=colorama.Fore.GREEN,
                yellow=colorama.Fore.YELLOW,
                blue=colorama.Fore.BLUE,
                magenta=colorama.Fore.MAGENTA,
                cyan=colorama.Fore.CYAN,
                white=colorama.Fore.WHITE,
                reset=colorama.Fore.RESET))
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
                black=colorama.Fore.BLACK,
                red=colorama.Fore.RED,
                green=colorama.Fore.GREEN,
                yellow=colorama.Fore.YELLOW,
                blue=colorama.Fore.BLUE,
                magenta=colorama.Fore.MAGENTA,
                cyan=colorama.Fore.CYAN,
                white=colorama.Fore.WHITE,
                reset=colorama.Fore.RESET))
        def read(self, message,tag = 'READ'):
            now = datetime.datetime.now()
            if len(tag) < self.tag_max:
                empty = " "*(self.tag_max-len(tag))
            else:
                empty = ""
            readed = input(f'{self.extra}{message}')
            print(f'{self.normalize}{colorama.Cursor.UP(1)}'+self.format_rea.format(
                date = now.strftime(self.date),
                tag = tag,
                empty = empty,
                tab = "\t",
                message = message,
                read = readed,
                black=colorama.Fore.BLACK,
                red=colorama.Fore.RED,
                green=colorama.Fore.GREEN,
                yellow=colorama.Fore.YELLOW,
                blue=colorama.Fore.BLUE,
                magenta=colorama.Fore.MAGENTA,
                cyan=colorama.Fore.CYAN,
                white=colorama.Fore.WHITE,
                reset=colorama.Fore.RESET))
            return readed
newlifeutils()
l = newlifeutils.Logger()
#----------------------
import datetime,time,random

def main():
    seedgen = Seedgen(l.read('seed:'), l.read('display:'))

if __name__ == '__main__':
    time.sleep(2)
    main()
    
    
    # i = 0
    # best = 0
    # while i < 1000:
        # now = datetime.datetime.now()
        # rawseed = str(int((now.microsecond**3)*(now.second**10)+(now.month*now.day)))
        # if int(len(rawseed)) > best:
            # print(f'new best #{i} ({rawseed})')
            # best = int(rawseed)
        # print(f'#{i}:{len(rawseed)}')
        # time.sleep(1/100)
        # i+=1
    # print('========'+str(best))

    # print(rawseed)