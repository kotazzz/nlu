from NewLifeUtils.ColorModule import ACC, MCC
from NewLifeUtils.UtilsModule import hex_to_rgb
from NewLifeUtils.FileModule import DataStorage, LogFile
from NewLifeUtils.StringUtilModule import remove_csi
from datetime import datetime
import sys


class Formatter(dict):
    def __init__(self, *args, date_format="%d-%m-%Y", time_format="%H:%M:%S", **kwargs):
        self.date_format = "%d-%m-%Y"
        self.time_format = "%H:%M:%S"
        dict.__init__(self, *args, **kwargs)

    def __missing__(self, key):
        if key == "time":
            return datetime.now().strftime(self.time_format)
        elif key == "time":
            return datetime.now().strftime(self.date_format)
        elif key.startswith("#"):
            if key == "#reset":
                return ACC.RESET
            elif key == "#under":
                return ACC.UNDERLINE
            elif key == "#nounder":
                return ACC.NO_UNDERLINE
            elif key == "#reverse":
                return ACC.REVERSE
            elif key == "#noreverse":
                return ACC.NO_REVERSE
            else:
                return ACC.customrgb(*hex_to_rgb(key))
        else:
            return "{" + key + "}"


def create_logger(
    pattern="[{time}] {tag}: {message}",
    tag_length=7,
    default_tag="Log",
    reader=False,
    reader_bg="#24416b",
    reader_fg="#a0dbf2",
    file_log=False,
    logfile=None,
    time_format = "%d-%m-%Y",
    data_format = "%H:%M:%S",
):
    def log(message, tag=""):
        if reader:
            if not any([message.endswith(i) for i in tuple(":> ")]):
                title = message + ": "
            else:
                title = message
                message = message.rstrip(" ")
                message = message.rstrip(":")
                message = message.rstrip(">")
            sys.stdout.write(
                f"{ACC.bcustomrgb(*hex_to_rgb(reader_bg))}{ACC.customrgb(*hex_to_rgb(reader_fg))}{title}{MCC.ERASE_NXT_LINE}"
            )
            readed = input()
            sys.stdout.write(ACC.RESET + MCC.up() + MCC.ERASE_ALL_LINE)
        else:
            readed = None
        tag = ("{:<" + str(tag_length) + "}").format(tag if tag else default_tag)
        log_record = pattern.format_map(
            Formatter(tag=tag, message=message, input=readed,
            time_format = time_format,
            data_format = data_format)
        )
        sys.stdout.write(ACC.RESET + log_record + ACC.RESET + "\n")
        if file_log:
            logfile.write(remove_csi(log_record) + "\n")
        return readed

    return log


def cstm(pattern, **kwargs):
    sys.stdout.write(
        ACC.RESET + pattern.format_map(Formatter(**kwargs)) + ACC.RESET + "\n"
    )
def smart_format(pattern, **kwargs):
    return pattern.format_map(Formatter(**kwargs))

def init_from_cfg():
    default_config = {
        "log_pattern": "{#81f059}[{time}] {#6bd130}{tag}{#fff}: {#1ed476}{message}",
        "wrn_pattern": "{#cfa529}[{time}] {#d7e356}{tag}{#fff}: {#b9c726}{message}",
        "err_pattern": "{#cf4729}[{time}] {#d93b18}{tag}{#fff}: {#cf2727}{message}",
        "tip_pattern": "{#9c1fd1}[{time}] {#471dc4}{tag}{#fff}: {#219ddb}{message}",
        "rea_pattern": "{#2141a3}[{time}] {#5a51db}{tag}{#fff}: {#2459d6}{message} {#fff}: {#24d0d6}{input}",
        "log_tag": "Log",
        "wrn_tag": "Warn",
        "err_tag": "Error",
        "tip_tag": "Tip",
        "rea_tag": "Reader",
        "date_format": "%d-%m-%Y",
        "time_format": "%H:%M:%S",
        "tag_length": 7,
        "file_log": True,
        "logtime": "%d-%m-%Y-%H",
        "logname": "log-{time}",
    }
    config = DataStorage("config.yml", "logger", default_config)
    if config["file_log"]:
        now = datetime.now()
        logname = config["logname"]
        logtime = config["logtime"]
        logfile = LogFile(f"{logname.format(time=now.strftime(logtime))}.log", "logs")
    else:
        logfile = None
    log = create_logger(pattern=config["log_pattern"], default_tag=config["log_tag"], file_log=config['file_log'], logfile=logfile, tag_length=config['tag_length'])
    wrn = create_logger(pattern=config["wrn_pattern"], default_tag=config["wrn_tag"], file_log=config['file_log'], logfile=logfile, tag_length=config['tag_length'])
    err = create_logger(pattern=config["err_pattern"], default_tag=config["err_tag"], file_log=config['file_log'], logfile=logfile, tag_length=config['tag_length'])
    tip = create_logger(pattern=config["tip_pattern"], default_tag=config["tip_tag"], file_log=config['file_log'], logfile=logfile, tag_length=config['tag_length'])
    rea = create_logger(
        pattern=config["rea_pattern"], default_tag=config["rea_tag"], reader=True
    )

    return log, wrn, err, tip, rea

log, wrn, err, tip, rea = init_from_cfg()