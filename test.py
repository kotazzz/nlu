print(1)
from NewLifeUtils.ColorModule import *
from NewLifeUtils.CustomShellModule import *
from NewLifeUtils.DatabaseManageModule import *
from NewLifeUtils.ExceptModule import *
from NewLifeUtils.FileModule import *
from NewLifeUtils.LoggerModule import *
from NewLifeUtils.RequestModule import *
from NewLifeUtils.StringUtilModule import *
from NewLifeUtils.TableBuildModule import *
from NewLifeUtils.UtilsModule import *

if __name__ == '__main__':
    log(1)
    log(1,1)
    wrn(1)
    err(1)
    tip(1)
    rea(1)
    try:
        0/0
    except ZeroDivisionError as e:
        except_print(e, "wrn")
    print(create_table(2, [], ["1","222222222","3","4","3","4","3","4"]))
    print(create_multiline_table(2, [], ["1","222222222","3","4","3","4","3","4"]))
    sh = Shell()
    sh.run()
    4
