import NewLifeUtils.LoggerModule       as Logger
import NewLifeUtils.StringUtilModule   as String
import NewLifeUtils.LanguageManager as Language
from NewLifeUtils import traceback
def except_print( exception, exceptionType="err", tb=True):
    errorText = "\n-------------- {ExceptionTitle} --------------------\n"
    errorText += f"Type: {type(exception).__name__}\n\n"

    if exception.args == 0:
        errorText += f'{Language.getlang("ExceptModule","unknown")}\n'
    else:
        errorText += f'{Language.getlang("ExceptModule","about")}:\n\t{(chr(10)+chr(9)).join(exception.args)}\t\n'

    if tb:

        errorText += f"\n{traceback.format_exc()}"

    errorText += "\n-------------- {ExceptionTitle} --------------------\n"

    if exceptionType == "attention":
        Logger.log(
            errorText.replace(
                "{ExceptionTitle}",
                String.screate(Language.getlang("ExceptModule", "attention"), 20),
            )
        )
    if exceptionType == "wrn":
        Logger.wrn(
            errorText.replace(
                "{ExceptionTitle}",
                String.screate(Language.getlang("ExceptModule", "warning"), 20),
            )
        )
    elif exceptionType == "err":
        Logger.err(
            errorText.replace(
                "{ExceptionTitle}",
                String.screate(Language.getlang("ExceptModule", "error"), 20),
            )
        )
    elif exceptionType == "fatal":
        Logger.err(
            errorText.replace(
                "{ExceptionTitle}",
                String.screate(Language.getlang("ExceptModule", "fatal"), 20),
            )
        )
        exit(-1)
    else:
        Logger.err(
            errorText.replace(
                "{ExceptionTitle}",
                String.screate(Language.getlang("ExceptModule", "wrong"), 20),
            )
        )
def get_etypes(self):
    return ['attention','wrn','err','fatal']
