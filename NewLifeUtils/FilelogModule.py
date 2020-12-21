import NewLifeUtils.FileModule       as File
import NewLifeUtils.UtilsModule      as Utils
import NewLifeUtils.StringUtilModule as String
from NewLifeUtils import datetime, json

rr=False
logname="log"
dateFormat = "%d-%m-%Y"
timeFormat = "%H:%M:%S"

startdate = datetime.datetime.now().strftime(dateFormat)
starttime = datetime.datetime.now().strftime(timeFormat)

errDefaultTag = "[!!!] Error"
logDefaultTag = "[   ] Log"
wrnDefaultTag = "[_!_] Warn"

TagMaxLenght = 12

errFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"
logFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"
wrnFormat = "[{date}|{time}] <{path}>:{tag}: {message}\n"

if rr:
    file_snumber = 1
    while os.path.exists(
        f'{File.get_path("+log")}{logname}-{startdate}-{file_snumber}.log'
    ):
        file_snumber += 1
    logFileName = f"{logname}-{startdate}-{file_snumber}.log"
    logFile = File.open_file(logFileName, path="+log", mode="w")
else:
    logFileName = f"{logname}-{startdate}.log"
logFile = File.open_file(logFileName, path="+log", mode="a")
logFile.close()
tmpfile = File.open_file('logdata.tmp', 'w+', '+temp', 'utf-8')
tmprea = tmpfile.read()
if tmprea != '':
    tmpdata = json.loads()
else:
    tmpdata = {'lastFilelogModuleInit':Utils.getfromfname(None)}
    

if tmpdata['lastFilelogModuleInit']!= Utils.getfromfname(None):
    tmpdata['lastFilelogModuleInit'] = Utils.getfromfname(None)
    log(
        f"New Logger from {os.path.basename(__file__)}/{tmpdata['lastFilelogModuleInit'].replace(' ', '')}"
    )
tmpfile.write(json.dumps(tmpdata))
tmpfile.close()

def formatter( pattern, message, tag, path, additional=None):
    if additional is None:
        additional = {"void": ""}

    now = datetime.datetime.now()
    tag = String.screate(tag, TagMaxLenght)

    return pattern.format(
        **additional,
        date=now.strftime(dateFormat),
        time=now.strftime(timeFormat),
        tag=tag,
        path=path,
        tab="\t",
        message=message,
    )

def log( message, path="main", tag=""):
    if tag == "":
        tag = logDefaultTag
    drec(formatter(logFormat, message, tag, path), end="")

def wrn( message, path="main", tag=""):
    if tag == "":
        tag = wrnDefaultTag
    drec(formatter(wrnFormat, message, tag, path), end="")

def err( message, path="main", tag=""):
    if tag == "":
        tag = errDefaultTag
    drec(formatter(errFormat, message, tag, path), end="")

def cstm( pattern, text=""):
    drec(formatter(pattern, message, tag, path), end="")

def drec( text, end="\n"):
    logFile = File.open_file(logFileName, path="+log", mode="a")
    logFile.write(text + end)
    logFile.close()
