import NewLifeUtils.Modules.FileModule       as File
import NewLifeUtils.Modules.ColorModule      as Color
import NewLifeUtils.Modules.StringUtilModule as String
import NewLifeUtils.Modules.FilelogModule    as FileLogger
from NewLifeUtils import json
import NewLifeUtils.InternalStorage.LanguageManager
# File
# Color
# String
# FileLogger

enableFileLog = True

f = File.open_file("colors.json", mode="r+", path="+logger_data")

try:
    color_map = json.loads(f.read())
except Exception as e:
    print(e)
    defaultcolormap = '{"Indianred":[205,92,92],"lightcoral":[240,128,128],"salmon":[250,128,114],"darksalmon":[233,150,122],"lightsalmon":[255,160,122],"crimson":[220,20,60],"red":[255,0,0],"firebrick":[178,34,34],"darkred":[139,0,0],"pink":[255,192,203],"lightpink":[255,182,193],"hotpink":[255,105,180],"deeppink":[255,20,147],"mediumvioletred":[199,21,133],"palevioletred":[219,112,147],"coral":[255,127,80],"tomato":[255,99,71],"orangered":[255,69,0],"darkorange":[255,140,0],"orange":[255,165,0],"gold":[255,215,0],"yellow":[255,255,0],"lightyellow":[255,255,224],"lemonchiffon":[255,250,205],"lightgoldenrodyellow":[250,250,210],"papayawhip":[255,239,213],"moccasin":[255,228,181],"peachpuff":[255,218,185],"palegoldenrod":[238,232,170],"khaki":[240,230,140],"darkkhaki":[189,183,107],"lavender":[230,230,250],"thistle":[216,191,216],"plum":[221,160,221],"violet":[238,130,238],"orchid":[218,112,214],"fuchsia":[255,0,255],"magenta":[255,0,255],"mediumorchid":[186,85,211],"mediumpurple":[147,112,219],"blueviolet":[138,43,226],"darkviolet":[148,0,211],"darkorchid":[153,50,204],"darkmagenta":[139,0,139],"purple":[128,0,128],"indigo":[75,0,130],"slateblue":[106,90,205],"darkslateblue":[72,61,139],"cornsilk":[255,248,220],"blanchedalmond":[255,235,205],"bisque":[255,228,196],"navajowhite":[255,222,173],"wheat":[245,222,179],"burlywood":[222,184,135],"tan":[210,180,140],"rosybrown":[188,143,143],"sandybrown":[244,164,96],"goldenrod":[218,165,32],"darkgoldenrod":[184,134,11],"peru":[205,133,63],"chocolate":[210,105,30],"saddlebrown":[139,69,19],"sienna":[160,82,45],"brown":[165,42,42],"maroon":[128,0,0],"black":[0,0,0],"gray":[128,128,128],"silver":[192,192,192],"white":[255,255,255],"olive":[128,128,0],"lime":[0,255,0],"green":[0,128,0],"aqua":[0,255,255],"teal":[0,128,128],"blue":[0,0,255],"navy":[0,0,128],"greenyellow":[173,255,47],"chartreuse":[127,255,0],"lawngreen":[124,252,0],"limegreen":[50,205,50],"palegreen":[152,251,152],"lightgreen":[144,238,144],"mediumspringgreen":[0,250,154],"springgreen":[0,255,127],"mediumseagreen":[60,179,113],"seagreen":[46,139,87],"forestgreen":[34,139,34],"darkgreen":[0,100,0],"yellowgreen":[154,205,50],"olivedrab":[107,142,35],"darkolivegreen":[85,107,47],"mediumaquamarine":[102,205,170],"darkseagreen":[143,188,143],"lightseagreen":[32,178,170],"darkcyan":[0,139,139],"cyan":[0,255,255],"lightcyan":[224,255,255],"paleturquoise":[175,238,238],"aquamarine":[127,255,212],"turquoise":[64,224,208],"mediumturquoise":[72,209,204],"darkturquoise":[0,206,209],"cadetblue":[95,158,160],"steelblue":[70,130,180],"lightsteelblue":[176,196,222],"powderblue":[176,224,230],"lightblue":[173,216,230],"skyblue":[135,206,235],"lightskyblue":[135,206,250],"deepskyblue":[0,191,255],"dodgerblue":[30,144,255],"cornflowerblue":[100,149,237],"mediumslateblue":[123,104,238],"royalblue":[65,105,225],"mediumblue":[0,0,205],"darkblue":[0,0,139],"midnightblue":[25,25,112],"snow":[255,250,250],"honeydew":[240,255,240],"mintcream":[245,255,250],"azure":[240,255,255],"aliceblue":[240,248,255],"ghostwhite":[248,248,255],"whitesmoke":[245,245,245],"seashell":[255,245,238],"beige":[245,245,220],"oldlace":[253,245,230],"floralwhite":[255,250,240],"ivory":[255,255,240],"antiquewhite":[250,235,215],"linen":[250,240,230],"lavenderblush":[255,240,245],"mistyrose":[255,228,225],"gainsboro":[220,220,220],"lightgrey":[211,211,211],"darkgrey":[169,169,169],"grey":[128,128,128],"dimgrey":[105,105,105],"lightslategrey":[119,136,153],"slategrey":[112,128,144],"darkslategrey":[47,79,79]}'
    f.write(defaultcolormap)
    color_map = json.loads(defaultcolormap)
f.close()
origcolors = color_map
colors = []
for key in color_map:
    color_map[key] = Color.ACC.CUSTOMRGB(*tuple(color_map[key]))
    colors.append(f"{color_map[key]}{key}{color_map[key]}")
color_map["reset"] = Color.ACC.RESET

color_data = {}
color_data["tabledate"] = colors[:-1]
color_data["colors"] = origcolors

log_pattern = (
    "{greenyellow}[{time}] {lightgreen}{tag}{snow} : {mediumspringgreen}{message}"
)
wrn_pattern = "{darkorange}[{time}] {orange}{tag}{snow} : {gold}{message}"
err_pattern = "{crimson}[{time}] {red}{tag}{snow} : {firebrick}{message}"
tip_pattern = "{fuchsia}[{time}] {magenta}{tag}{snow} : {mediumorchid}{message}"
rea_pattern = "{cyan}[{time}] {lightcyan}{tag}{snow} : {paleturquoise}{message} > {mediumslateblue}[{readed}]"

log_default_tag = getlang("LoggerModule", "log_default_tag")
wrn_default_tag = getlang("LoggerModule", "wrn_default_tag")
err_default_tag = getlang("LoggerModule", "err_default_tag")
tip_default_tag = getlang("LoggerModule", "tip_default_tag")
rea_default_tag = getlang("LoggerModule", "rea_default_tag")

#  READ

date_format = "%d-%m-%Y"
time_format = "%H:%M:%S"

tag_length = 10


def tag_check( tag, default):
    if tag == "":
        return String.screate(default, tag_length)
    else:
        return String.screate(tag, tag_length)


def to_format( pattern, args):
    now = datetime.datetime.now()

    return (
        pattern.format(
            **args,
            **color_map,
            date=now.strftime(date_format),
            time=now.strftime(time_format),
        )
        + color_map["reset"]
    )


def out( text):
    if enableFileLog:
        FileLogger.drec(String.remove_csi(text))
    print(text)


log = lambda  message, tag="": out(
    to_format(
        log_pattern,
        {"message": message, "tag": tag_check(tag, log_default_tag)},
    )
)
wrn = lambda  message, tag="": out(
    to_format(
        wrn_pattern,
        {"message": message, "tag": tag_check(tag, wrn_default_tag)},
    )
)
err = lambda  message, tag="": out(
    to_format(
        err_pattern,
        {"message": message, "tag": tag_check(tag, err_default_tag)},
    )
)
tip = lambda  message, tag="": out(
    to_format(
        tip_pattern,
        {"message": message, "tag": tag_check(tag, tip_default_tag)},
    )
)
cstm = lambda  pattern, text, args: out(to_format(pattern, **args))

rea = lambda  message, tag="": read(message, tag)


def read( message, tag=""):
    if message[-1] not in [" ", ">", ":"]:
        message += ": "
    print(
        f"{Color.ACC.BCUSTOMRGB(0, 43, 112)}{Color.ACC.CUSTOMRGB(235, 54, 30)}{message}",
        end="",
    )
    readed = input()

    out(
        Color.MCC.PREVIOUSLINE
        + Color.ACC.RESET
        + to_format(
            rea_pattern,
            {
                "message": message,
                "tag": tag_check(tag, rea_default_tag),
                "readed": readed,
            },
        )
    )
    return readed
