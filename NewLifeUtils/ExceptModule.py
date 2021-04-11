import traceback
import sys

from NewLifeUtils.FileModule import DataStorage
from NewLifeUtils.LoggerModule import cstm, smart_format

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


def except_print(type="fat", more="", code=-1, tb=True, run = True):
    if tb:
        a = traceback.extract_tb(sys.exc_info()[2])
        exception_text = ""
        for f in a:
            pattern = '{#fff}"{#under}{#7193c9}{file}{#fff}{#nounder}" {#fff}({#42eb77}{lineno}{#fff}): {#de6a50}{content}\n  {#fff}> {#22bf2a}{line}\n'
            #'{white}"{ul}{fn}{nul}{white}" {white}({yellow}{ln}{white}): {green}{n}\n{s}{white}> {lime}{lc}\n'
            exception_text += smart_format(
                pattern,
                file= f.filename,
                lineno= f.lineno,
                content= f.name,
                line= f.line,
            )
        exception_text += smart_format(
            "{#169181}{err}", err = traceback.format_exc().splitlines()[-1]
        )
    else:
        exception_text = smart_format("{#757575}Traceback is disabled")
    kshortcuts = {
        "unk": "unknown",
        "att": "attention",
        "inf": "info",
        "wrn": "warning",
        "err": "error",
        "fat": "fatal",
        "wrg": "wrong",
    }

    pattern = "{#db8e2a}{d}{#under}{title}{#nounder}{d}\n{text}\n{#e352d5}{a}\n{#db8e2a}{d}{td}{d}"
    if run:
        cstm(
            pattern,
            
                d= "-" * 15,
                title= translation[kshortcuts[type]],
                text= exception_text,
                td= " " * len(translation[kshortcuts[type]]),
                a=f"More info: {more}" if more else "",
        )
    else:
        return smart_format(pattern,
            
                d= "-" * 15,
                title= translation[kshortcuts[type]],
                text= exception_text,
                td= " " * len(translation[kshortcuts[type]]),
                a= f"More info: {more}" if more != "" else "",
            )
    if type == "fat":
        exit(code)
