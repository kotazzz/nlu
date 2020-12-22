#One Screen Prj
import keyboard
import os
import sys
import random
from ColorModule import MCC, ACC

winsize_x = 70
winsize_y = 30
os.system(f"mode con cols={winsize_x} lines={winsize_y}")
print(MCC.CURSOR_HIDE)
window_storage = []
for y in range(winsize_y):
    xa = []
    for x in range(winsize_x):
        xa.append(' ')
    window_storage.append(xa)

cursor = {'x':0, 'y':0}

def load_screen(screen = window_storage):
    s = ''
    for line in screen:
        s += ''.join(line)+'\n'
    sys.stdout.write(s[:-1])
def get_pos_x():
    return cursor['x']
def get_pos_y():
    return cursor['y']
def goto_cur(x,y):
    cursor['x'] = x
    cursor['y'] = y
def right(count = 1):
    cursor['y'] = get_pos_y()+count
def nl(count = 1):
    cursor['y'] = 0
    cursor['x'] = get_pos_x()+count
    return ''
def cmdp(text):
    for letter in text:
        if cursor['y'] > (winsize_x - 1):
           cursor['y'] = 0
           cursor['x'] = get_pos_x() + 1
        if cursor['x'] > (winsize_y - 1):
           cursor['x'] = 0
        window_storage[get_pos_x()][get_pos_y()] = letter
        right(1)

def cmdi():
    i = ''
    while 'enter' not in pressed:
        t = ''.join(list(pressed.keys()))
        if t != ''.join(list(pressed.keys())):
            i = t
        
    cmdp(i+' '+str(list(pressed.keys())))
pressed = {}
def main_keyer(keyer):
    if keyer.event_type == 'down':
        pressed[keyer.name] = 'down'
    else:
        del pressed[keyer.name]
    
keyboard.hook(main_keyer)

cmdp(f'hello')
nl(2)
cmdp(f'meow')

while True:
    load_screen()
    cmdi()
    #cmdp(str(pressed))

