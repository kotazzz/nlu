import traceback

from NewLifeUtils.FileModule import DataStorage
from NewLifeUtils.LoggerModule import *

default_lang = {
    "type": "Type",
    "unknown": "Unknown Error",
    "about": "More information",
    "attention": "Attention",
    "info": "Info",
    "warning": "Warn",
    "error": "Error",
    "fatal": "Fatal error",
    "wrong": "Something wrong...",
}
translation = DataStorage("lang.yml", "exceptsettings", default_lang)


def except_print(type='fat', more ='', code=-1, tb = True):
    if tb:
        a = traceback.extract_tb(sys.exc_info()[2])
        exception_text = ''
        for f in a:
            pattern = '{white}"{ul}{fn}{nul}{white}" {white}({yellow}{ln}{white}): {green}{n}\n{s}{white}> {lime}{lc}\n'
            exception_text += to_format(pattern, {
                'ul': ACC.UNDERLINE,
                'nul': ACC.NO_UNDERLINE,
                'fn': f.filename,
                'ln': f.lineno,
                'n': f.name,
                'lc': f.line,
                's': ' ' * 2,
            })
        exception_text += to_format('{lightblue}{err}', {'err': traceback.format_exc().splitlines()[-1]})
    else:
        exception_text = to_format('{gray}Traceback is disabled', {})
    kshortcuts = {
            "unk": "unknown",
            "att": "attention",
            "inf": "info",
            "wrn": "warning",
            "err": "error",
            "fat": "fatal",
            "wrg": "wrong"}

    pattern = '{magenta}{d}{ul}{title}{nul}{d}\n{text}\n{red}{a}\n{magenta}{d}{td}{d}'
    cstm(pattern, {
        'ul': ACC.UNDERLINE,
        'nul': ACC.NO_UNDERLINE,
        'd': '-' * 15,
        'title': translation[kshortcuts[type]],
        'text': exception_text,
        'td': ' ' * len(translation[kshortcuts[type]]),
        'a': f'More info: {more}' if more != '' else ''
    })
    if type == 'fat':
        exit(code)
