import keyboard
import os
import time

from colorama import Fore,Style,Back,Cursor,init
pos = lambda y, x: Cursor.POS(x, y)
def initialisation():
    os.system('color 0f')
    cls()
    init()
    print(f'{Style.DIM}{Fore.WHITE}{Back.BLACK}')
def cls():
    os.system('cls')
def hello():
    print(f"""
{Style.DIM}{Fore.BLUE}{Back.BLACK}===================================================================================={Style.DIM}{Fore.RED}{Back.BLACK}
______                                   _ 
| ___ \                                 | |
| |_/ /_ _ ___ _____      _____  _ __ __| |
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
| | | (_| \__ \__ \\ V  V / (_) | | | (_| |
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|                                          
 _____                           _             
|  __ \                         | |            
| |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
 \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
{Style.DIM}{Fore.BLUE}{Back.BLACK}====================================================================================
""")
simple_line = "┌┬┐│─├┼┤└┴┘"
double_line = "╔╦╗║═╠╬╣╚╩╝"
double_vert = "╓╥╖║─╟╫╢╙╨╜"
double_hori = "╒╤╕│═╞╪╡╘╧╛"





def main():
    initialisation()
    hello()
    time.sleep(1)
    cls()
    
    print(f'╔══════╤═══════════════════════════════════════════════════════════════════════════╗')
    print(f'║Input:│                                                                           ║')
    print(f'╟──────┴───────────────────────────────────────────────────────────────────────────╢')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'║                                                                                  ║')
    print(f'╟──────────────────────────────────────────────────────────────────────────────────╢')
    print(f'║if you dont know, what you need to type - write "/help" for get any help about    ║')
    print(f'╚══════════════════════════════════════════════════════════════════════════════════╝{pos(1,9)}{input(pos(2,9))}')
    
    
    

            
if __name__ == '__main__':
    main()