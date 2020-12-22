#GrafB
from ColorModule import *
from StringUtilModule import remove_csi,screate
import random

    
def graf(a):
    sr = max(a)/2
    def fsr(a):
        return (sum(a)/len(a))
    print('\n'*max(a))
    def RRGB(r,g,b):
       return ACC.BCUSTOMRGB(r,g,b)+ACC.CUSTOMRGB(255-r,255-g,255-b)
       
    i = int(255/max(a))
    mds = 0
    for i in a:
        if mds < len(str(i)):
            mds = len(str(i))
    for column in a:
        if column == max(a):
            clr = RRGB(0,0,255)
            sym = clr+'-'*mds+ACC.RESET
        elif column > fsr(a):
            clr = RRGB(0,column*i,0)
            sym = clr+'▒'*mds+ACC.RESET
        else:
            clr = RRGB(column*i,0,0)
            sym = clr+'░'*mds+ACC.RESET
            
        print(f'{MCC.SAVE_CURSOR()}{(sym+MCC.UP()+MCC.LEFT(len(remove_csi(sym))))*column}{MCC.LOAD_CURSOR()}{MCC.RIGHT(0)}', end = '')
        rd = random.randrange (0,2)
        if rd == 0:
            r,g,b = random.randrange (100,200),0,0
        elif rd == 1:
            r,g,b = 0,random.randrange (100,200),0
        elif rd == 2:
            r,g,b = 0,0,random.randrange (100,200)
        print(f'{MCC.DOWN()}{MCC.LEFT()}{clr}{screate(str(column), mds)}{MCC.UP()}', end = '')
    print(ACC.RESET+MCC.CURSORPOSITION(1,-1))
    print(ACC.RESET+MCC.CURSORPOSITION(1,-1))

import os
while True:
    a = []
    for i in range(0,20):
        a.append(random.randrange(0,20))
    a.append(20)
    print(a)
    graf(a)
    __import__('time').sleep(1)
    os.system('cls')