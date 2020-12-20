import colorama
import datetime
import os
import random
class Newlifeutils(object):

    name = 'NewLifeUtils'
    ver = 'v1.0 beta'
    def check(self):
        try:
            os.system('color ')
            
        except NameError:
            print('ERROR: UNABLE TO INIT OS')
            exit(-1)
        try:
            random
        except NameError:
            print('ERROR: UNABLE TO INIT RANDOM')
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
        self.logger.log(f'Checked 4 modules','CHECK')
    def __init__(self):
        self.check()
        self.logger.log(f'','')
        self.logger.log(f'Thanks for using {self.name} {self.ver} ','NLU1')
        self.logger.log(f'(Check has no errors)','NLU1')
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
            return read
        def read(self,message,tag=''):
            return self.rea(message,tag)
    class Seedgen(object):
        def __init__(self, customseed='',display=''):
            self.logger =  Newlifeutils.Logger(dtag_log = 'SEED LOG',dtag_err = 'SEED ERROR',dtag_wrn = 'SEED WARN',dtag_rea = 'SEED READ')
            self.logger.log('Starting')
            #Check for set def
            if customseed != '':
                try:
                    int(customseed)
                except ValueError:
                    self.logger.err(f'{customseed} is not a numeric')
                    self.logger.wrn(f'Reseting: "{display}" -> <random> ')
                    self.logger.wrn('Using auto seed')
                    self.seed = self.formater(self.getRaw(),display)
                else:
                    self.logger.log(f'Using your seed ({customseed})')
                    self.seed = self.formater(customseed,display)
            else:
                self.seed = self.formater(self.getRaw(),display)
            self.logger.log('Formating ended!')
            self.logger.log(f'Raw: {self.seed["raw"]}')
            self.logger.log(f'Formated: {self.seed["formated"]}')
            random.seed(self.seed["raw"])
            self.logger.log(f'Randoms:')
            self.logger.log(f'{random.randrange(1,100)};{random.randrange(1,100)};{random.randrange(1,100)};')
            self.logger.log(f'{random.randrange(1,100)};{random.randrange(1,100)};{random.randrange(1,100)};')
        def getRaw(self):
            rawseed = str(int((datetime.datetime.now().microsecond**3)*(datetime.datetime.now().second**10)+(datetime.datetime.now().month*datetime.datetime.now().day)))
            self.logger.log(f'New RawSeed: {rawseed}')
            return rawseed
        def getSeed(self):
            return self.seed
            
        def formater(self, formated, display=''):
            if display != '':
                try:
                    int(display)
                except ValueError:
                    self.logger.err(f'{display} is not a numeric')
                    self.logger.wrn(f'Reseting: "{display}" -> "" ')
                    display = '4444'
            elif display == '':
                display = '4444'
                self.logger.log(f'using default display - {display}')
            else:
                self.logger.log(f'using non def display - {display}')
            need,i = 0,0
            while i < len(display):
                need +=int(display[i])
                i+=1
            self.logger.log(f'Goted {len(formated)}')
            self.logger.log(f'Need seed with length > {need} (display {display})')
            if len(formated) < need:
                self.logger.log('Not enough raw')
                self.logger.log('Adding 0-sym...')
                formated+=('0'*(need-len(formated)))
                self.logger.log(f'New raw - {formated}')
            if len(formated) > need:
                self.logger.log('Cutting string...')
                formated=formated[0:need]
                self.logger.log(f'New raw - {formated}')
            else:
                self.logger.log(f'All ok')
            self.logger.log(f'Formating...')
            i = 0
            offset = 0
            formated_space = ''
            while i < len(display):
                offset+=int(display[i])
                formated_space +=  f'{formated[offset-int(display[i]):offset]} '
                self.logger.log(f'#{i} (d={display[i]};chunk {formated[offset-int(display[i]):offset]} [{offset-int(display[i])}:{offset}]')
                self.logger.log(f'\tresult:{formated_space} ')
                i+=1
            return {
            'raw':formated,
            'formated':formated_space
            }
    def randselect(self, source, use_zero = False):
        logger =  Newlifeutils.Logger(dtag_log = 'RS LOG',dtag_err = 'RS ERROR',dtag_wrn = 'RS LOG',dtag_rea = 'RS READ')
        selector = 0
        try:
            source[0]
        except IndexError:
            logger.err(f'{source} is empty')
        except TypeError:
            logger.err(f'{source} object is not subscriptable')
        else: 
            if use_zero:
                logger.log('Can use zero')
                selector = random.randrange(1, len(source))
            else:
                logger.log('Cant use zero')
                selector = random.randrange(0, len(source))
            logger.log(f'Select item #{selector} from {type(source)}; result {source[selector]}')
            return source[selector]
        return -1
def main():
    n = Newlifeutils()
    l = Newlifeutils.Logger()
    colorama.init()
    seedgen = Newlifeutils.Seedgen()
    arr = []
    arr+=[1,2,3,4,5,6]
    arr+=[1,2,3,4,5,6]
    arr+=[1,2,3,4,5,6]
    l.log(f'Selected: {n.randselect(arr)}')
    l.log(f'Selected: {n.randselect(arr)}')
    l.log(f'Selected: {n.randselect(arr)}')
    l.log(f'Selected: {n.randselect(arr)}')
    l.wrn('hello','CUSTOM')
    
if __name__ == '__main__':
    main()