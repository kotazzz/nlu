from pynput.keyboard import Key, Listener
from NewLifeUtils.ColorModule import MCC, ACC
import pynput
import sys
from msvcrt import getwch

from NewLifeUtils.ColorModule import FGC
from NewLifeUtils.StringUtilModule import screate, parse_args, remove_csi

selector = 0

current_text = ''
def complete(readed, completes):
    global selector
    global current_text
    #print(f'{ACC.CLEARSCREEN}')
    if current_text == '':
        current_text = readed
    work_parsed = parse_args(readed)["split"]
    if readed != '':
        if readed[-1] == ' ':
            work_parsed.append('')


    keys = completes.keys()


    #print(readed)
    #print(current_text)
    aval = []
    for argnum, arg in enumerate(work_parsed, start=1):
        aval = []
        next_sel = False
        for key in keys:
            #print(f'{FGC.GREEN}arg: {arg}, key: {key}, result: {key.startswith(arg)}')
            sys.stdout.flush()
            if key.startswith(arg):
                aval.append(key)
                next_sel = True
                try:
                    completes[key]
                except KeyError:
                    pass  # no completion next
                    keys = {}
                else:
                    sys.stdout.flush()
                    keys = completes[key]
                    next_sel = True

        if next_sel:
            selector += 1
            selector %= len(aval)
        if len(aval) == 1:
            work_parsed[argnum - 1] = aval[0]
        elif len(aval) > 0:
            work_parsed[argnum - 1] = aval[selector]
            #print(f'{FGC.MAGENTA}com: {aval}, next: {keys}, CURRENT: {selector} - {aval[selector]}')

    #print(ACC.RESET)

    return ' '.join(work_parsed), aval


def smart_input(text='', completes={}, end='\n'):
    readed = ''
    print(text + MCC.save_cursor, end='')
    sys.stdout.flush()
    while True:
        key = getwch()
        if ord(key) == 224:
            pass
        elif ord(key) == 0:
            pass
        else:
            if ord(key) == 8:
                readed = readed[:-1]
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end='')

            elif ord(key) == 13:
                break
            elif ord(key) == 9:
                readed, aval = complete(readed, completes)
                if len(aval) > 0:
                    avalr = ', '.join(aval)
                else:
                    avalr = 'no suggestion'
                avaltext = f'{FGC.GRAY} ({avalr}) {ACC.RESET}'
                print(MCC.load_cursor + MCC.erase_nxt_line + readed + avaltext + MCC.left(len(remove_csi(avaltext))), end='')
            else:
                readed += key
                print(MCC.load_cursor + MCC.erase_nxt_line + readed, end='')
        sys.stdout.flush()
    print(end)
    return readed


if __name__ == '__main__':
    inp = smart_input('Введите текст:', {"hello": {"world": {}, "me": {}}, "hi": {"friend": {}}, "hem": {}})
    print(f'Вы ввели: {inp}')
