from NewLifeUtils import *


class LoggerModule(object):
    def __init__(
        self, File=None, Color=None, String=None, FileLogger=None, enableFileLog=True
    ):
        if type(FileLogger) == FilelogModule():
            self.FileLogger = FileLogger
        else:
            self.FileLogger = FilelogModule()

        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()

        if type(Color) == ColorModule:
            self.Color = Color
        else:
            self.Color = ColorModule()

        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()

        self.enableFileLog = enableFileLog

        f = self.File.open_file("colors.json", mode="r+", path="+logger_data")
        try:
            self.color_map = json.loads(f.read())
        except:
            defaultcolormap = '{"Indianred":[205,92,92],"lightcoral":[240,128,128],"salmon":[250,128,114],"darksalmon":[233,150,122],"lightsalmon":[255,160,122],"crimson":[220,20,60],"red":[255,0,0],"firebrick":[178,34,34],"darkred":[139,0,0],"pink":[255,192,203],"lightpink":[255,182,193],"hotpink":[255,105,180],"deeppink":[255,20,147],"mediumvioletred":[199,21,133],"palevioletred":[219,112,147],"coral":[255,127,80],"tomato":[255,99,71],"orangered":[255,69,0],"darkorange":[255,140,0],"orange":[255,165,0],"gold":[255,215,0],"yellow":[255,255,0],"lightyellow":[255,255,224],"lemonchiffon":[255,250,205],"lightgoldenrodyellow":[250,250,210],"papayawhip":[255,239,213],"moccasin":[255,228,181],"peachpuff":[255,218,185],"palegoldenrod":[238,232,170],"khaki":[240,230,140],"darkkhaki":[189,183,107],"lavender":[230,230,250],"thistle":[216,191,216],"plum":[221,160,221],"violet":[238,130,238],"orchid":[218,112,214],"fuchsia":[255,0,255],"magenta":[255,0,255],"mediumorchid":[186,85,211],"mediumpurple":[147,112,219],"blueviolet":[138,43,226],"darkviolet":[148,0,211],"darkorchid":[153,50,204],"darkmagenta":[139,0,139],"purple":[128,0,128],"indigo":[75,0,130],"slateblue":[106,90,205],"darkslateblue":[72,61,139],"cornsilk":[255,248,220],"blanchedalmond":[255,235,205],"bisque":[255,228,196],"navajowhite":[255,222,173],"wheat":[245,222,179],"burlywood":[222,184,135],"tan":[210,180,140],"rosybrown":[188,143,143],"sandybrown":[244,164,96],"goldenrod":[218,165,32],"darkgoldenrod":[184,134,11],"peru":[205,133,63],"chocolate":[210,105,30],"saddlebrown":[139,69,19],"sienna":[160,82,45],"brown":[165,42,42],"maroon":[128,0,0],"black":[0,0,0],"gray":[128,128,128],"silver":[192,192,192],"white":[255,255,255],"olive":[128,128,0],"lime":[0,255,0],"green":[0,128,0],"aqua":[0,255,255],"teal":[0,128,128],"blue":[0,0,255],"navy":[0,0,128],"greenyellow":[173,255,47],"chartreuse":[127,255,0],"lawngreen":[124,252,0],"limegreen":[50,205,50],"palegreen":[152,251,152],"lightgreen":[144,238,144],"mediumspringgreen":[0,250,154],"springgreen":[0,255,127],"mediumseagreen":[60,179,113],"seagreen":[46,139,87],"forestgreen":[34,139,34],"darkgreen":[0,100,0],"yellowgreen":[154,205,50],"olivedrab":[107,142,35],"darkolivegreen":[85,107,47],"mediumaquamarine":[102,205,170],"darkseagreen":[143,188,143],"lightseagreen":[32,178,170],"darkcyan":[0,139,139],"cyan":[0,255,255],"lightcyan":[224,255,255],"paleturquoise":[175,238,238],"aquamarine":[127,255,212],"turquoise":[64,224,208],"mediumturquoise":[72,209,204],"darkturquoise":[0,206,209],"cadetblue":[95,158,160],"steelblue":[70,130,180],"lightsteelblue":[176,196,222],"powderblue":[176,224,230],"lightblue":[173,216,230],"skyblue":[135,206,235],"lightskyblue":[135,206,250],"deepskyblue":[0,191,255],"dodgerblue":[30,144,255],"cornflowerblue":[100,149,237],"mediumslateblue":[123,104,238],"royalblue":[65,105,225],"mediumblue":[0,0,205],"darkblue":[0,0,139],"midnightblue":[25,25,112],"snow":[255,250,250],"honeydew":[240,255,240],"mintcream":[245,255,250],"azure":[240,255,255],"aliceblue":[240,248,255],"ghostwhite":[248,248,255],"whitesmoke":[245,245,245],"seashell":[255,245,238],"beige":[245,245,220],"oldlace":[253,245,230],"floralwhite":[255,250,240],"ivory":[255,255,240],"antiquewhite":[250,235,215],"linen":[250,240,230],"lavenderblush":[255,240,245],"mistyrose":[255,228,225],"gainsboro":[220,220,220],"lightgrey":[211,211,211],"darkgrey":[169,169,169],"grey":[128,128,128],"dimgrey":[105,105,105],"lightslategrey":[119,136,153],"slategrey":[112,128,144],"darkslategrey":[47,79,79]}'
            f.write(defaultcolormap)
            self.color_map = json.loads(defaultcolormap)
        f.close()

        colors = []
        for key in self.color_map:
            self.color_map[key] = self.Color.ACC.CUSTOMRGB(*tuple(self.color_map[key]))
            colors.append(f"{self.color_map[key]}{key}{self.color_map[key]}")
        self.color_map["reset"] = self.Color.ACC.RESET

        t = TableBuildModule()
        self.color_data = {}
        self.color_data["table"] = t.createTable(5, [], colors[:-1], header=False)
        self.color_data["colors"] = colors

        self.log_pattern = "{greenyellow}[{time}] {lightgreen}{tag}{snow} : {mediumspringgreen}{message}"
        self.wrn_pattern = "{darkorange}[{time}] {orange}{tag}{snow} : {gold}{message}"
        self.err_pattern = "{crimson}[{time}] {red}{tag}{snow} : {firebrick}{message}"
        self.tip_pattern = (
            "{fuchsia}[{time}] {magenta}{tag}{snow} : {mediumorchid}{message}"
        )
        self.rea_pattern = "{cyan}[{time}] {lightcyan}{tag}{snow} : {paleturquoise}{message} > {mediumslateblue}[{readed}]"

        self.log_default_tag = "Log"
        self.wrn_default_tag = "Warn"
        self.err_default_tag = "Error"
        self.tip_default_tag = "Tip"
        self.rea_default_tag = "Read"

        #  READ

        self.date_format = "%d-%m-%Y"
        self.time_format = "%H:%M:%S"

        self.tag_length = 10

    def tag_check(self, tag, default):
        if tag == "":
            return self.String.screate(default, self.tag_length)
        else:
            return self.String.screate(tag, self.tag_length)

    def to_format(self, pattern, args):
        now = datetime.datetime.now()

        return (
            pattern.format(
                **args,
                **self.color_map,
                date=now.strftime(self.date_format),
                time=now.strftime(self.time_format),
            )
            + self.color_map["reset"]
        )

    def out(self, text):
        if self.enableFileLog:
            self.FileLogger.drec(self.String.remove_csi(text))
        print(text)

    log = lambda self, message, tag="": self.out(
        self.to_format(
            self.log_pattern,
            {"message": message, "tag": self.tag_check(tag, self.log_default_tag)},
        )
    )
    wrn = lambda self, message, tag="": self.out(
        self.to_format(
            self.wrn_pattern,
            {"message": message, "tag": self.tag_check(tag, self.wrn_default_tag)},
        )
    )
    err = lambda self, message, tag="": self.out(
        self.to_format(
            self.err_pattern,
            {"message": message, "tag": self.tag_check(tag, self.err_default_tag)},
        )
    )
    tip = lambda self, message, tag="": self.out(
        self.to_format(
            self.tip_pattern,
            {"message": message, "tag": self.tag_check(tag, self.tip_default_tag)},
        )
    )
    cstm = lambda self, pattern, text, args: self.out(self.to_format(pattern, **args))

    def read(self, message, tag=""):
        if message[-1] not in [" ", ">", ":"]:
            message += ": "
        print(
            f"{self.Color.ACC.BCUSTOMRGB(0, 43, 112)}{self.Color.ACC.CUSTOMRGB(235, 54, 30)}{message}",
            end="",
        )
        readed = input()

        self.out(
            self.Color.MCC.PREVIOUSLINE
            + self.Color.ACC.RESET
            + self.to_format(
                self.rea_pattern,
                {
                    "message": message,
                    "tag": self.tag_check(tag, self.rea_default_tag),
                    "readed": readed,
                },
            )
        )


if __name__ == "__main__":
    l = LoggerModule()
    l.log(f"This is a log")
    l.log(f"This is a log with custom tag", "MyTag1")
    l.tip(f"This is a tip")
    l.tip(f"This is a tip with custom tag", "MyTag2")
    l.wrn(f"This is a warn")
    l.wrn(f"This is a warn with custom tag", "MyTag3")
    l.err(f"This is a error")
    l.err(f"This is a error with custom tag", "MyTag4")
    l.read("hello")
    print(l.color_data["table"])
