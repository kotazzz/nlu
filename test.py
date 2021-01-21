import msvcrt
def smart_input():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"\xe0":
                key2 = msvcrt.getch()
            if key == b"\x00":
                key2 = msvcrt.getch()
            else:
                key2 = ''
            print(f'{key.decode("cp866").upper().encode("cp866")} {key2.decode("utf-8") }')
            print(f'{type(key)}')
if __name__ == '__main__':
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"\xe0":
                key2 = msvcrt.getch()
            if key == b"\x00":
                key2 = msvcrt.getch()
            else:
                key2 = ''
            print(f'{chr(ord(key)).encode().decode("utf-16")}')