#Hkr
import msvcrt
import os
import sys
import random

from ctypes import windll, byref, wintypes
from ctypes.wintypes import SMALL_RECT

STDOUT = -11
WIN_X = 100
WIN_Y = 60
hdl = windll.kernel32.GetStdHandle(STDOUT)
rect = wintypes.SMALL_RECT(0, 0, WIN_X, WIN_Y) # (left, top, right, bottom)
windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))

os.system('')
#    72 
# 75 80 77

def Hello():
    posx = 3
    posy = 3
    sys.stdout.write('WELCOME! press any key to continue\n')
    while True:
        key = ord(msvcrt.getch())
        if key == 13:
            sys.stdout.write('\x1Bc')
        elif key == 224:
            key = ord(msvcrt.getch())
            if key == 72:
                posy -=1
            elif key == 75:
                posx -=1
            elif key == 80:
                posy +=1
            elif key == 77:
                posx +=1
        if posx < 0:
            posx = 0
        if posy < 0:
            posy = 0
        if posx > WIN_Y-2:
            posx = WIN_Y-2
        if posy > WIN_X-2:
            posy = WIN_X-2
        sys.stdout.write(f"\x1B[48;2;{random.randrange(0,255)};{random.randrange(0,255)};{random.randrange(0,255)}m\x1B[{posy};{posx}H \n")
def Exit():
    exit(0)
    
selected = 0 
menu = {
"run":Hello,
"exit":Exit
}



sys.stdout.write('WELCOME! press any key to continue\n\033[?25h')
while True:
    key = ord(msvcrt.getch())
    if key == 119:
        selected =  (selected-1) % len(menu)
    elif key == 115:
        selected =  (selected+1) % len(menu)
    elif key == 13:
        sys.stdout.write('\x1Bc')
        menu[list(menu.keys())[selected]]()
    sys.stdout.write('\x1Bc')
    for elem_num in range(len(menu)):
        if elem_num == selected:
            sys.stdout.write(f'> {list(menu.keys())[elem_num]}\n')
        else:
            sys.stdout.write(f'  {list(menu.keys())[elem_num]}\n')
sys.stdout.write('\x1Bc')