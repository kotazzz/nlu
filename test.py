from os.path import join, dirname

from NewLifeUtils.ColorModule import MCC, ACC
import sys
from msvcrt import getwch

from NewLifeUtils.ColorModule import FGC
from NewLifeUtils.StringUtilModule import parse_args
from NewLifeUtils.RequestModule import req_get

counter = 0
current = ""


def complete(readed, completes):
    print(f"{ACC.CLEARSCREEN}")
    next = False
    if len(readed) > 0:
        if readed[-1] == " ":
            next = True

    def build_readed(args, ins_spase=False):
        new_readed = " ".join(args)
        if ins_spase:
            new_readed += " "
        return new_readed

    def find_aval(word, possible):
        aval = []
        for key in possible:
            if key.startswith(word):
                aval.append(key)
        return aval

    def predict(aval):
        global counter
        counter += 1
        counter %= len(aval)
        return aval[counter]

    def next_layer(complete_words, key):
        try:
            complete_words = list(completes[key].keys())
        except KeyError:
            complete_words = []
        return complete_words

    complete_words = list(completes.keys())
    parsed_readed = parse_args(readed)["split"]

    for argnum, arg in enumerate(parsed_readed, start=0):
        if len(find_aval(arg, complete_words)) == 0:
            aval = []
            predict_curr = ""
    else:
        for argnum, arg in enumerate(parsed_readed, start=0):
            aval = find_aval(arg, complete_words)
            global current
            print(f"{FGC.BBLUE}{aval} ({current})")
            if len(aval) == 1:
                parsed_readed[argnum] = aval[0]
                predict_curr = ""
            if len(aval) > 1:
                predict_curr = predict(arg, aval, next)
            if next:
                predict_curr = predict(aval)
                return build_readed(parsed_readed, True), "", complete_words
            complete_words = next_layer(complete_words, predict_curr)
            print(f"{FGC.BYELLOW}aval - {aval}")
            print(f"{FGC.BYELLOW}gen complete_words - {complete_words}")

    print(f'{FGC.RED} RES: {predict_curr} / {" ".join(aval)}')
    print(ACC.RESET)
    return build_readed(parsed_readed, False), predict_curr, aval


def smart_input(text="", completes={}, end="\n"):
    readed = ""
    print(text + MCC.save_cursor, end="")
    sys.stdout.flush()
    while True:
        key = getwch()
        if ord(key) == 224:
            key = getwch()
        elif ord(key) == 0:
            key = getwch()
        else:
            if ord(key) == 8:
                readed = readed[:-1]
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end="")

            elif ord(key) == 13:
                break
            elif ord(key) == 9:
                readed, predict, aval = complete(readed, completes)
                complete(readed, completes)
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end="")
            else:
                readed += key
                print(MCC.load_cursor + MCC.erase_nxt_window + readed, end="")
        sys.stdout.flush()
    print(end)
    return readed


if __name__ == "__main__":
    from NewLifeUtils.CustomShellModule import Shell
    c = Shell()
    c.main()

    print("Hello World")
