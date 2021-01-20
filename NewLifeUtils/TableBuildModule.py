from NewLifeUtils.ColorModule import FGC, ACC
from NewLifeUtils.StringUtilModule import remove_csi, screate, sslice

default = "double"

custom = "╔╦╗║═╠╬╣╚╩╝"
if default == "double":
    tableManagerCurrent = "╔╦╗║═╠╬╣╚╩╝"
elif default == "single":
    tableManagerCurrent = "┌┬┐│─├┼┤└┴┘"
elif default == "vertical":
    tableManagerCurrent = "╓╥╖║─╟╫╢╙╨╜"
elif default == "horisontal":
    tableManagerCurrent = "╒╤╕│═╞╪╡╘╧╛"
elif default == "simple":
    tableManagerCurrent = "+++|-++++++"
elif default == "custom":
    tableManagerCurrent = custom
else:
    tableManagerCurrent = "╔╦╗║═╠╬╣╚╩╝"


def find_max(row_count, data):
    line_len = []
    for i in range(row_count):
        line_len.append(0)
    for linenum in range(0, len(data), row_count):
        for row in range(row_count):
            if len(remove_csi(data[linenum + row])) > line_len[row]:
                line_len[row] = len(remove_csi(data[linenum + row]))
    return line_len


def createTable(

        rowCount,
        sizes,
        data,
        title="TABLE",
        header=True,
        tableElement="",
        color="",
        align="l",
):
    if sizes == []:
        sizes = find_max(rowCount, data)
    if color == "":
        color = FGC.CYAN
    color = ACC.RESET + color
    if align == "r":
        align = "l"
    else:
        align = "r"
    # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
    # 0  1  2  3  4  5  6  7  8  9  10

    if tableElement == "":
        tableElement = tableManagerCurrent

    result = ""

    # Generate Header-line
    result += f"{color}{tableElement[0]}"

    for sizen in range(rowCount):
        result += f"{color}{tableElement[4] * sizes[sizen]}{color}{tableElement[1]}"
    result = result[:-1] + f"{color}{tableElement[2]}"

    # Generate Header
    if header:
        result += f"\n{color}{tableElement[3]}"
        for num in range(rowCount):
            result += f"{screate(data[num], sizes[num], align)}{color}{tableElement[3]}"
        result += f"\n{color}{tableElement[5]}"
        for headerPieceSize in sizes:
            result += (
                f"{color}{tableElement[4] * headerPieceSize}{color}{tableElement[6]}"
            )
        result = result[:-1] + f"{color}{tableElement[7]}"
        data = data[rowCount:]

    # Generate DataSection
    for lineNum in range(0, len(data), rowCount):
        result += f"\n{color}{tableElement[3]}"
        for rowShift in range(0, rowCount):
            try:
                result += f"{screate(data[lineNum + rowShift], sizes[rowShift], align)}{color}{tableElement[3]}"
            except:
                result += f'{screate("", sizes[rowShift], align)}{color}{tableElement[3]}'
    result += f"\n{color}{tableElement[8]}"

    # Generate Footer-line
    for sizen in range(rowCount):
        result += f"{color}{tableElement[4] * sizes[sizen]}{color}{tableElement[9]}"
    result = result[:-1] + f"{color}{tableElement[10]}{ACC.RESET}"

    return f'\n{screate(title, round(sum(sizes) / 2), "l")}\n{result}\n'


def createMultilineTable(

        rowCount,
        sizes,
        data,
        title="TABLE",
        table_element="",
        color="",
        align="l",
):
    if sizes == []:
        sizes = find_max(rowCount, data)
    if color == "":
        color = FGC.CYAN
    if align == "r":
        align = "l"
    else:
        align = "r"
    # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
    # 0  1  2  3  4  5  6  7  8  9  10
    # +  +  +  |  -  +  +  +  +  +  +
    # 0  1  2  3  4  5  6  7  8  9  10; , tableElement = '+++|-++++++'
    if table_element == "":
        table_element = tableManagerCurrent
    for i in range(len(data)):
        data[i] = sslice(data[i], sizes[i % len(sizes)])
    result = ""
    for line in range(0, len(data), rowCount):
        maxtabsize = 0
        for row in range(0, rowCount):
            if len(data[line + row]) > maxtabsize:
                maxtabsize = len(data[line + row])
        for row in range(0, rowCount):
            if len(data[line + row]) < maxtabsize:
                while len(data[line + row]) < maxtabsize:
                    data[line + row].append("")

    # Generate Header-line
    result += f"{color}{table_element[0]}"
    for headerPieceSize in sizes:
        result += (
            f"{color}{table_element[4] * headerPieceSize}{color}{table_element[1]}"
        )
    result = result[:-1] + f"{color}{table_element[2]}\n"

    # Generate DataSection
    for line in range(0, len(data), rowCount):
        block = []
        for row in range(0, rowCount):
            for blockLineNum in range(len(data[line + row])):

                try:
                    block[
                        blockLineNum
                    ] += f"{table_element[3]}{screate(data[line + row][blockLineNum], sizes[row], align)}"
                except:
                    block.append(
                        f"{table_element[3]}{screate(data[line + row][blockLineNum], sizes[row], align)}"
                    )
        for blockLineNum in range(len(data[line + row])):
            block[blockLineNum] += table_element[3]
        for line in block:
            result += f"{line}\n"

        result += f"{table_element[5]}"
        for headerPieceSize in sizes:
            result += f"{table_element[4] * headerPieceSize}{table_element[6]}"
        result = result[:-1] + f"{table_element[7]}\n"

    # Generate Footer-line
    result = result[: -1 * (2 + rowCount + sum(sizes))] + table_element[8]
    for headerPieceSize in sizes:
        result += f"{table_element[4] * headerPieceSize}{table_element[9]}"
    result = result[:-1] + f"{table_element[10]}{ACC.RESET}"

    return f'\n{screate(title + " IN DEV", round(sum(sizes) / 2), "l")}\n{result}\n'


def get_column(data, row_count, num):
    num = num % row_count
    table = []
    for line in range(0, len(data), row_count):
        linearr = []
        for row in range(0, row_count):
            linearr.append(data[line + row])
        table.append(linearr)
    results = []
    for line in table:
        results.append(line[num - 1])
    return results


def get_multi_column(data, row_count, ids):
    columns = []
    for num in ids:
        columns.append(get_column(data, row_count, num))
    sizes = len(columns[0])
    restabledata = []
    for num in range(sizes):
        for column in columns:
            restabledata.append(column[num])
    return restabledata


def join_column(columns):
    m = 0
    for elem in columns:
        if len(elem) > m:
            m = len(elem)
    for elem in columns:
        while len(elem) < m:
            elem.append("")
    table = []
    for line in range(len(columns[0])):
        for row in range(len(columns)):
            table.append(columns[row][line])
    return table


def get_record(row_count, data, record_id):
    return data[row_count * record_id: row_count * record_id + row_count]


def get_record_count(row_count, data):
    return len(data) / row_count
