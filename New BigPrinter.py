#New BigPrinter
from NewLifeUtils import *
files = ['Font.json','Font2.json']
import json
def bprint(text, maxlinelength = 9, font = 'default'):
    for file in files:
        current = open(file, encoding = 'utf-8')
        fontsrc = json.loads(current.read())
        if fontsrc['name'] == font:
            sym = fontsrc
            break
    else:
        print('cant found')
        
    def bprintletter(text):
        try:
            printline = []
            for i in range(len(sym['letters'][list(sym['letters'].keys())[0]])):
                printline.append("")
            for letter in text:
                for line in range(len(sym['letters'][letter])):
                    printline[line] += sym['letters'][letter][line]
            print("\n".join(printline))
        except KeyError :
            bprintletter("ERROR")
            print("Unable to continue print text, unknown characters")
            avaliableKeys = []
            avaliableKeys = list(sym['letters'].keys())
            avaliableKeys = "".join(avaliableKeys)
            print(f"Avaliable: {avaliableKeys}")
    
    import re
    r = [text[i : i + maxlinelength] for i in range(0, len(text), maxlinelength)]
    for text in r:
        bprintletter(text)
bprint('hello')
bprint('hello', font = 'air')
                                                                                                              