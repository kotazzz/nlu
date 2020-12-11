# ColorModule
# LoggerModule
# ExceptModule
# CustomShellModule
# StringUtilModule
# UtilsModule
# FileModule
# FilelogModule
# TableBuildModule
# DatabaseManageModule
# RandomModule




try:
    import os
    import datetime
except ModuleNotFoundError as e:
    print(f'Unable to import dependences: {e}')
    exit(-1)
except Exception as e:
    print(e) 
    exit(-1)

class ColorModule(object):
    def __init__(self):
        os.system('')

if __name__ == "__main__":
    print('succeful')
