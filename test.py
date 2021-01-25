from __future__ import print_function
from pynput.keyboard import Key, Listener
from NewLifeUtils.ColorModule import MCC, ACC
import pynput
import sys
from msvcrt import getwch

from NewLifeUtils.ColorModule import FGC
from NewLifeUtils.StringUtilModule import screate, parse_args

selector = 0


def complete(readed, completes):
    global selector
    print(f'{ACC.CLEARSCREEN}')
    parsed = parse_args(readed)
    keys = completes.keys()

    for arg in parsed["split"]:
        aval = []
        next_sel = False
        for key in keys:
            print(f'{FGC.GREEN}arg: {arg}, key: {key}, result: {key.startswith(arg)}')
            sys.stdout.flush()
            if key.startswith(arg):
                aval.append(key)
                next_sel = True
                try:
                    completes[key]
                except KeyError:
                    pass  # no completion next
                    keys = {}
                else:
                    sys.stdout.flush()
                    keys = completes[key]
                    next_sel = True
            elif key == arg:
                keys = completes[key]
                break
        if next_sel:
            selector += 1
            selector %= len(aval)
        if len(aval) > 0:
            print(f'{FGC.MAGENTA}com: {aval} ({keys}), CURRENT: {selector} - {aval[selector]}')

    return readed


def smart_input(text='', completes={}, end='\n'):
    readed = ''
    print(text + MCC.save_cursor, end='')
    sys.stdout.flush()
    while True:
        key = getwch()
        if ord(key) == 224:
            print(ord(getwch()))
        elif ord(key) == 0:
            print(ord(getwch()))
        else:
            if ord(key) == 8:
                readed = readed[:-1]
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end='')

            elif ord(key) == 13:
                break
            elif ord(key) == 9:
                readed = complete(readed, completes)
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end='')
            else:
                readed += key
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end='')
        sys.stdout.flush()
    print(end)
    return readed


if __name__ == '__main__':
    inp = smart_input('Введите текст:', {"hello": {"world": {}, "me": {}}, "hi": {"friend": {}}, "hem": {}})
    print(f'Вы ввели: {inp}')

#
# KEYS = {
#    "LBUTTON": 1,
#    "RBUTTON": 2,
#    "CANCEL": 3,
#    "MBUTTON": 4,
#    "BACK": 8,
#    "TAB": 9,
#    "CLEAR": 12,
#    "RETURN": 13,
#    "SHIFT": 16,
#    "CONTROL": 17,
#    "MENU": 18,
#    "PAUSE": 19,
#    "CAPITAL": 20,
#    "KANA": 21,
#    "HANGEUL": 21,
#    "HANGUL": 21,
#    "JUNJA": 23,
#    "FINAL": 24,
#    "HANJA": 25,
#    "KANJI": 25,
#    "ESCAPE": 27,
#    "CONVERT": 28,
#    "NONCONVERT": 29,
#    "ACCEPT": 30,
#    "MODECHANGE": 31,
#    "SPACE": 32,
#    "PRIOR": 33,
#    "NEXT": 34,
#    "END": 35,
#    "HOME": 36,
#    "LEFT": 37,
#    "UP": 38,
#    "RIGHT": 39,
#    "DOWN": 40,
#    "SELECT": 41,
#    "PRINT": 42,
#    "EXECUTE": 43,
#    "SNAPSHOT": 44,
#    "INSERT": 45,
#    "DELETE": 46,
#    "HELP": 47,
#    "LWIN": 91,
#    "RWIN": 92,
#    "APPS": 93,
#    "NUMPAD0": 96,
#    "NUMPAD1": 97,
#    "NUMPAD2": 98,
#    "NUMPAD3": 99,
#    "NUMPAD4": 100,
#    "NUMPAD5": 101,
#    "NUMPAD6": 102,
#    "NUMPAD7": 103,
#    "NUMPAD8": 104,
#    "NUMPAD9": 105,
#    "MULTIPLY": 106,
#    "ADD": 107,
#    "SEPARATOR": 108,
#    "SUBTRACT": 109,
#    "DECIMAL": 110,
#    "DIVIDE": 111,
#    "F1": 112,
#    "F2": 113,
#    "F3": 114,
#    "F4": 115,
#    "F5": 116,
#    "F6": 117,
#    "F7": 118,
#    "F8": 119,
#    "F9": 120,
#    "F10": 121,
#    "F11": 122,
#    "F12": 123,
#    "F13": 124,
#    "F14": 125,
#    "F15": 126,
#    "F16": 127,
#    "F17": 128,
#    "F18": 129,
#    "F19": 130,
#    "F20": 131,
#    "F21": 132,
#    "F22": 133,
#    "F23": 134,
#    "F24": 135,
#    "NUMLOCK": 144,
#    "SCROLL": 145,
#    "LSHIFT": 160,
#    "RSHIFT": 161,
#    "LCONTROL": 162,
#    "RCONTROL": 163,
#    "LMENU": 164,
#    "RMENU": 165,
#    "PROCESSKEY": 229,
#    "ATTN": 246,
#    "CRSEL": 247,
#    "EXSEL": 248,
#    "EREOF": 249,
#    "PLAY": 250,
#    "ZOOM": 251,
#    "NONAME": 252,
#    "PA1": 253,
#    "OEM_CLEAR": 254,
# }
# text = ''
#
# while True:
#    cp = win32api.GetCursorPos()
#    result = ''
#    sys.stdout.write(ACC.CLEARSCREEN)
#
#    for key in KEYS:
#        state = win32api.GetKeyState(KEYS[key])
#        if state != 0:
#            text = '    pressed'
#        else:
#            text = 'not pressed'
#        result += f"{screate(key, 10)}:{text}-{screate(str(state), 4)}; "
#    sys.stdout.write(result+f'\ncp: {cp}')
#    sleep(0.4)
#
#
#
