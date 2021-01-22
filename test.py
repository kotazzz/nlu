import win32api
import win32con
import sys

from NewLifeUtils.ColorModule import ACC
from NewLifeUtils.StringUtilModule import screate

while True:
    pass

# Get states of all keys
#
# from time import sleep
#
# import win32api
# import win32con
# import sys
#
# from NewLifeUtils.ColorModule import ACC
# from NewLifeUtils.StringUtilModule import screate
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
