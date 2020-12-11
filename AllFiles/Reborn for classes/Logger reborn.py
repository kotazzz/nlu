#Logger reborn
import colorama
import datetime
import os
import random
class Logger(object):
        def __init__(self, 
            format_err = '{red}[{time}] {red}{tag}{empty}: {red}{message}\n{red}[{time}] Time : {date} - {time}', 
            format_log = '{white}[{time}] {green}{tag}{empty}: {green}{message}', 
            format_wrn = '{white}[{time}] {yellow}{tag}{empty}: {yellow}{message}', 
            format_rea = '{white}[{time}] {blue}{tag}{empty}: {blue}{message} {cyan}[{read}]', 
            format_tip = '{white}[{time}] {cyan}{tag}{empty}: {blue}{message}', 
            
            dtag_err = 'ERROR',
            dtag_log = 'LOG',
            dtag_wrn = 'WARN',
            dtag_rea = 'INPUT',
            dtag_tip = 'TIPS',
            
            date = "%d.%m.%Y", 
            time = "%H:%M:%S",
            
            tag_max = 10):
            
            colorama.init()
            
            self.normalize = f'{colorama.Fore.WHITE}{colorama.Back.BLACK}{colorama.Style.NORMAL}'
            
            self.colors_map = {
                'black':    f'{colorama.Fore.BLACK}', 
                'red':      f'{colorama.Fore.RED}',
                'green':    f'{colorama.Fore.GREEN}', 
                'yellow':   f'{colorama.Fore.YELLOW}',
                'blue':     f'{colorama.Fore.BLUE}', 
                'magenta':  f'{colorama.Fore.MAGENTA}',
                'cyan':     f'{colorama.Fore.CYAN}', 
                'white':    f'{colorama.Fore.WHITE}',
                'reset':    f'{colorama.Fore.RESET}'
            }
            
            self.format_err = self.normalize + format_err + self.normalize
            self.format_log = self.normalize + format_log + self.normalize
            self.format_wrn = self.normalize + format_wrn + self.normalize
            self.format_rea = self.normalize + format_rea + self.normalize
            self.format_tip = self.normalize + format_tip + self.normalize
            
            self.dtag_err = dtag_err
            self.dtag_log = dtag_log
            self.dtag_wrn = dtag_wrn
            self.dtag_rea = dtag_rea
            self.dtag_tip = dtag_tip
            
            self.date = date
            self.time = time
            self.tag_max = tag_max  
            self.log('Logger initilizated succeful', 'LOG INI')
        def formatter(self,pattern, message, tag, tag_max,date,time,obj={'obj':''},additional={'additional':''}):
            print(f'{type(tag_max)};{tag_max}')
            now = datetime.datetime.now()
            if len(tag) < tag_max:
                empty = f'{colorama.Fore.WHITE}{colorama.Back.BLACK}{colorama.Style.NORMAL}'+" "*(tag_max-len(tag))
            else:
                empty = f'{colorama.Fore.WHITE}{colorama.Back.BLACK}{colorama.Style.NORMAL}'
            return f'{colorama.Fore.WHITE}{colorama.Back.BLACK}{colorama.Style.NORMAL}{colorama.Cursor.UP(1)}'+\
                pattern.format(
                    **obj, **additional, 
                    date = now.strftime(date),
                    time = now.strftime(time),
                    tag = tag, empty = empty, tab = "\t", message = message,
                    
                    )
        def log(self,message,tag=''):
            if tag == '':
                tag = self.dtag_log
            print(self.formatter(self.format_log, message, tag, self.tag_max, self.date, self.time, 
            additional=self.colors_map))
        def wrn(self,message,tag=''):
            if tag == '':
                tag = self.dtag_wrn
            print(self.formatter(self.format_wrn, message, tag, self.tag_max, self.date, self.time, 
            additional=self.colors_map))
        def err(self,message,tag=''):
            if tag == '':
                tag = self.dtag_err
            print(self.formatter(self.format_err, message, tag, self.tag_max, self.date, self.time, 
            additional=self.colors_map))
        def tip(self,message,tag=''):
            if tag == '':
                tag = self.dtag_tip
            print(self.formatter(self.format_tip, message, tag, self.tag_max, self.date, self.time, 
            additional=self.colors_map))
        def rea(self,message,tag=''):
            read = input(f'{colorama.Style.DIM}{colorama.Back.BLUE}{colorama.Style.BRIGHT}{colorama.Fore.RED}{message}')
            if tag == '':
                tag = self.dtag_rea
            s =  f'{self.normalize}{colorama.Cursor.UP(1)}'
            s += self.formatter(self.format_rea, message, tag, self.tag_max,self.date, self.time, obj={'read':read}, additional=self.colors_map)
            print(s)
            

def main():
    l = Logger()
    l.wrn('hello','CUSTOM')
    l.tip('hello','CUSTOM')
    l.err('hello','CUSTOM')
    l.log('hello','CUSTOM')
    l.wrn('hello')
    l.tip('hello')
    l.err('hello')
    l.log('hello')
    l.rea('write something')
if __name__ == '__main__':
    #if False:
        main()