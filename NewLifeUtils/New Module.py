#new module
###################################################################
import re
def remove_csi(text):
    return (
        re.sub(
            r"\\x1[bB]\[[\d;]*[a-zA-Z]{1}",
            "",
            text.encode("unicode_escape").decode(),
        )
        .encode()
        .decode("unicode_escape")
    )
def screate(text, size = 10, align = 'l', fill_letter = ' '):
    text = str(text)
    spaces = str(fill_letter) * (size - len(remove_csi(text)))
    if align == "r":
        return spaces + text
    if align == "l":
        return text + spaces
def sslice(text, chunk_size):
    text = str(text)
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
def parseArgs(readed):
    # [\'][a-zA-ZА-Яа-я\d\s[\]{}()\\\.\":;,-]*[\']|\b[a-zA-Z\d]+
    # [\"\'][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,-]*[\"\']|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,-]+
    # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,\'-]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-]+
    # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+
    # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@#_=%?\*\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+ (NOW)
    result = re.findall(
        r"[\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@#_=%?\*\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+",
        readed,
        re.MULTILINE,
    )
    temp = []
    for item in result:
        temp.append(re.sub(r"\B'|\b'", "", item))
    result = [x for x in temp if x != ""]
    if len(result) == 0:
        return {"command": "", "param": []}
    if len(result) == 1:
        return {"command": result[0], "param": []}
    else:
        return {"command": result[0], "param": result[1 : len(result)]}
    return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]
    
    
    
###################################################################
def build_table(data, sizes):
    for line in data:
        for row in line:
            print(screate(row), end = '')
        print()

table = [
    [1,2,3],
    [4,5,6]

]

#build_table(table, None)
import os
os.system('')
print(f'\x1B[sOIUYGTYHUIJOKPL:')
print(f'asdfsgdf')
print(f'\x1B[u11111111111')
















