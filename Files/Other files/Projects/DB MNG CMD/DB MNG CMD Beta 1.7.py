raise RuntimeError('This programm is not availiable')
# import sqlite3 as sql
# import Libraries.nlu2 as cr3fb
# import time
# import os
# class WelcomeScreen:
    # def set():
        # pass
# class CustomCmd:
    # pass    
# # TODO: (PRCS)Create clases and refacor code
# # TODO: Optimize startup
# # TODO: Issue: on Linux start page displays wrong# nlu = cr3fb.NewLifeUtils(silent=True)# welcome_str = """
# ███████╗ ██████╗ ██╗         ███╗   ███╗███╗   ██╗ ██████╗ ██████╗ 
# ██╔════╝██╔═══██╗██║         ████╗ ████║████╗  ██║██╔════╝ ██╔══██╗
# ███████╗██║   ██║██║         ██╔████╔██║██╔██╗ ██║██║  ███╗██████╔╝
# ╚════██║██║▄▄ ██║██║         ██║╚██╔╝██║██║╚██╗██║██║   ██║██╔══██╗
# ███████║╚██████╔╝███████╗    ██║ ╚═╝ ██║██║ ╚████║╚██████╔╝██║  ██║
# ╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
# """# for n in range(1, 255, 5):
    # print(nlu.ACC.CUSTOM(n, n, n) + welcome_str + nlu.MCC.UP(9), end="")
    # time.sleep(0.0001)
# print(welcome_str)
# lineLength = 60
# for n in range(lineLength + 1):
    # print(f'{nlu.FGC.YELLOW}{nlu.ACC.UNDERLINE}▐{"▒"*n}{"░"*(lineLength-n)}▌')
    # print(nlu.MCC.UP(2))
    # time.sleep(1 / 150)
# print(f"{nlu.FGC.GREEN}{nlu.ACC.UNDERLINE}▐" + lineLength * "█" + f"▌{nlu.ACC.RESET}")
# time.sleep(1 / 3)
# os.system("cls")# # START CMD
# import re
# def parseInput(readed):
    # if readed != "":
        # res = re.findall(
            # r"[\"\'][a-zA-ZА-Яа-я\d\s[\]{}()\\\?\/\.:;,-]*[\"\']|\b[a-zA-Z\d\\\.:;,\?\/-]+",
            # readed,
            # re.MULTILINE,
        # )
        # print(res)
        # print(type(res))
        # res2 = []
        # for item in res:
            # res2.append(re.sub(r"['\"]", "", item))
        # res = [x for x in res2 if x != ""]
        # for word in res:
            # print(word)
            # sourceline  = re.compile(word, re.IGNORECASE)
            # newl = re.sub('[:]{3}','-')
            # print(newl)
        # return res
    # else:
        # return []
# def createHelpPage(data):
    # colorMap = nlu.getColorMap()
    # black = colorMap["black"]
    # gray = colorMap["gray"]
    # red = colorMap["red"]
    # green = colorMap["green"]
    # yellow = colorMap["yellow"]
    # blue = colorMap["blue"]
    # magenta = colorMap["magenta"]
    # cyan = colorMap["cyan"]
    # white = colorMap["white"]
    # reset = colorMap["reset"]    # helpPage = ""
    # for page in data["description"]:
        # for section in data["description"][page]:
            # # print(f'{page}:{section}')
            # if section == page:
                # helpPage += f"{red}SECTION: {section}\n"
                # helpPage += f'{cyan}ABOUT: {data["description"][section][section]}\n'
                # helpPage += f"{blue}COMMANDS\n"
            # else:
                # helpPage += f"\t{green}{section}:\n"
                # helpPage += (
                    # f'\t\t{gray}About: {white}{data["description"][page][section]}\n'
                # )
                # helpPage += f'\t\t{yellow}Syntax: {data["syntax"][page][section]}\n'
                # helpPage += f'\t\t{magenta}Aliases: {" ".join(data["aliases"][page][section])}\n'
    # helpPage += f"{reset}"
    # return helpPage
# data = {
    # "aliases": {
        # "MAIN": {
            # "exit": ["exit", "quit", "q"],
            # "help": ["help"],
            # "clear": ["cls"],
            # "nludemo": ["nludemo"],
            # "dbconnect": ["dbconnect", "dbc", "db", "database"],
        # },
        # "DBASE": {
            # "exit": ["exit"],
            # "create": ["create"],
            # "remove": ["remove"],
            # "read": ["read"],
            # "describe": ["describe"],
            # "write": ["write"],
            # "readdb": ["readdb"],
            # "cursormode": ["cursormode", "cmode"],
        # },
    # },
    # "description": {
        # "MAIN": {
            # "MAIN": "The main section of programm",
            # "exit": "Exit from program",
            # "help": "Get help like this",
            # "clear": "Clear window",
            # "nludemo": "Demonstrate nlu lib",
            # "dbconnect": "Connect to database",
        # },
        # "DBASE": {
            # "DBASE": "DataBase Manage commands",
            # "exit": "Exit from db manage mode",
            # "create": "Create table",
            # "remove": "Remove table",
            # "read": "Display data, stored in table",
            # "describe": "Describe selected table",
            # "write": "Write new record in table",
            # "readdb": "Read all, that writed in data base",
            # "cursormode": "Change cursor mode or get state",
        # },
    # },
    # "syntax": {
        # "MAIN": {
            # "exit": "",
            # "help": "",
            # "clear": "",
            # "nludemo": "",
            # "dbconnect": "",
        # },
        # "DBASE": {
            # "exit": "",
            # "create": "",
            # "remove": "",
            # "read": "",
            # "describe": "",
            # "write": "",
            # "readdb": "",
            # "cursormode": "Change cursor mode or get state",
        # },
    # },
# }
# nlu.log(f"Working in this dirrectory: {os.getcwd()}")
# helpPage = createHelpPage(data)
# aliases = data["aliases"]
# #----------#----------#----------#----------#----------#----------#----------#----------#----------
# path = 'TEST'
# readed = nlu.read(path + " >", path)
# res = parseInput(readed)
# if len(res) > 0:
    # command = res[0]
# else:
    # command = ""
# if len(res) > 1:
    # parametrs = res[1:]
# else:
    # parametrs = []# parlen = len(parametrs)# while True:
    # path = "MAIN"
    # readed = nlu.read(path + " >", path)
    # res = parseInput(readed)
    # if len(res) > 0:
        # command = res[0]
    # else:
        # command = ""
    # if len(res) > 1:
        # parametrs = res[1:]
    # else:
        # parametrs = []    # parlen = len(parametrs)    # if command in aliases[path]["exit"]:
        # break
    # elif command in aliases[path]["nludemo"]:
        # cr3fb.Demonstration(nlu)
    # elif command in aliases[path]["help"]:
        # nlu.tip(helpPage, path + "/HELP")
    # elif command in aliases[path]["clear"]:
        # os.system("cls")
    # elif command in aliases[path]["dbconnect"]:
        # path = "DBASE"
        # if parlen == 1:
            # db_name = parametrs[0]        # elif parlen == 0:
            # nlu.tip(f"Do you want use polygon.db?", path)
            # nlu.tip(f"Enter 'y' for yes or 'n' for no", path)
            # nlu.tip(f"Also you can enter name of database", path)
            # ans = nlu.read(path + " >", path)
            # if ans == "y":
                # db_name = "polygon.db"
            # else:
                # db_name = ""
        # if db_name != "":
            # cursorMode = False
            # nlu.log(f"Loading DB. Name: {db_name}", path)
            # base = sql.connect(db_name)
            # nlu.log(f"Succeful connect to {db_name}", path)
            # cursor = base.cursor()
            # nlu.log(f"Succeful created cursor for {db_name}", path)
            # while True:
                # readed = nlu.read(path + " >", path)
                # res = parseInput(readed)
                # if len(res) > 0:
                    # command = res[0]
                # else:
                    # command = ""
                # if len(res) > 1:
                    # parametrs = res[1:]
                # else:
                    # parametrs = []
                # parlen = len(parametrs)
                
                # if command in aliases[path]["exit"]:
                    # break
                # elif command in aliases[path]["cursormode"]:
                        # if parlen == 0:
                            # nlu.log(f'Cursor mode state: {cursorMode}')
                        # if parlen == 1:
                            # if parametrs[0] == 'true':
                                # oldCursorMode = cursorMode
                                # cursorMode = True
                                # nlu.log(f'Cursor mode state changed from: {oldCursorMode} to {cursorMode}')
                            # elif parametrs[0] == 'false':
                                # oldCursorMode = cursorMode
                                # cursorMode = False
                                # nlu.log(f'Cursor mode state changed from: {oldCursorMode} to {cursorMode}')
                            # elif parametrs[0] == 'turn':
                                # oldCursorMode = cursorMode
                                # cursorMode = not cursorMode
                                # nlu.log(f'Cursor mode state changed from: {oldCursorMode} to {cursorMode}')
                            # else:
                                # nlu.wrn(f'Invalid syntax. Now Cursor mode state: {cursorMode}')
                        # if parlen > 1:
                            # nlu.wrn(f'Invalid syntax. Now Cursor mode state: {cursorMode}')
                # else:
                    # if cursorMode:
                        # try:
                            # cursor.execute(command, parametrs)
                        # except:
                            # nlu.err('Invalid cursor sql syntax')
                    # else:
                        # if command in aliases[path]["readdb"]:
                            # nlu.log(cursor.fetchall())
                        
                        # elif command == "":
                            # pass
                        # else:
                            # nlu.wrn("Unknown command, type help for help", "UNKNOWN")
    # elif command == "":
        # pass
    # else:
        # nlu.wrn("Unknown command, type help for help", "UNKNOWN")
# path = "ROOT"
# nlu.log("Shutting down...", path)# # "create": "",
# # "remove": "",
# # "read": "",
# # "describe": "",
# # "write": "",
# # "cursormode": "Change cursor mode or get state",
# # db_name = "polygon.db"
# # nlu.log(f"Loading DB. Name: {db_name}")
# # base = sql.connect(db_name)
# # nlu.log(f"Succeful connect to {db_name}")
# # cursor = base.cursor()
# # nlu.log(f"Succeful created cursor for {db_name}")
# # sql = "SELECT * FROM albums WHERE artist=?"
# # cursor.execute(sql, [("Red")])
# # print(cursor.fetchall()) # or use fetchone()# # print("Here's a listing of all the records in the table:")
# # for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
# # print(row)# # print("Results from a LIKE query:")
# # sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
# # cursor.execute(sql)# # print(cursor.fetchall())
