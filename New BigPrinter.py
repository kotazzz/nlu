#New BigPrinter

sym = {
'name':'my font',
'letters' : {
"t":[
"s",
"s",
"s",
"s",
"s",
"s",
],
"y":[
"y",
"y",
"y",
"y",
"y",
"y",
],
}}

def bprint(text, maxlinelength = 9):
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
            bprintletter("err")
            print("Unable to print text, unknown characters")
            print("May be its unknown color?")
            avaliableKeys = []
            avaliableKeys = list(sym['letters'].keys())
            avaliableKeys = "".join(avaliableKeys)
            print(f"Avaliable: {avaliableKeys}")
    
    import re
    r = [text[i : i + maxlinelength] for i in range(0, len(text), maxlinelength)]
    for text in r:
        bprintletter(text)
bprint('tyyyyyttytytt')
# ████████╗██╗   ██╗██████╗ ███████╗    ███████╗ ██████╗ ███╗   ███╗███████╗████████╗██╗  ██╗██╗███╗   ██╗ ██████╗     
# ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝     
   # ██║    ╚████╔╝ ██████╔╝█████╗      ███████╗██║   ██║██╔████╔██║█████╗     ██║   ███████║██║██╔██╗ ██║██║  ███╗    
   # ██║     ╚██╔╝  ██╔═══╝ ██╔══╝      ╚════██║██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║██║╚██╗██║██║   ██║    
   # ██║      ██║   ██║     ███████╗    ███████║╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝    
   # ╚═╝      ╚═╝   ╚═╝     ╚══════╝    ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     
                                                                                                                     