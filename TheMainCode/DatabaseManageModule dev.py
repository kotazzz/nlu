from NewLifeUtils import *

if __name__ == "__main__":
    cm = ColorModule()
    sm = StringUtilModule()
    lm = LoggerModule(cm)
    em = ExceptModule(lm, sm)
    tbm = TableBuildModule(sm, cm)
    csm = CustomShellModule(None, em, sm, cm)
    um = UtilsModule()
    fm = FileModule()
    flm = FilelogModule()


    pass