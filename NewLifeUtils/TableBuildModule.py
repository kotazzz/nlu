from NewLifeUtils.ColorModule import FGC, ACC
from NewLifeUtils.StringUtilModule import remove_csi, screate, sslice


















default = "double"

custom = "╔╦╗║═╠╬╣╚╩╝"
if default == "double":
    table_manager_current = "╔╦╗║═╠╬╣╚╩╝"
elif default == "single":
    table_manager_current = "┌┬┐│─├┼┤└┴┘"
elif default == "vertical":
    table_manager_current = "╓╥╖║─╟╫╢╙╨╜"
elif default == "horisontal":
    table_manager_current = "╒╤╕│═╞╪╡╘╧╛"
elif default == "simple":
    table_manager_current = "+++|-++++++"
elif default == "custom":
    table_manager_current = custom
else:
    table_manager_current = "╔╦╗║═╠╬╣╚╩╝"


def find_max(row_count, data):
    line_len = []
    for i in range(row_count):
        line_len.append(0)
    for linenum in range(0, len(data), row_count):
        for row in range(row_count):
            if len(remove_csi(data[linenum + row])) > line_len[row]:
                line_len[row] = len(remove_csi(data[linenum + row]))
    return line_len


def create_table(
    row_count,
    sizes,
    data,
    title="TABLE",
    header=True,
    table_element="",
    color="",
    align="l",
):
    if not sizes:
        sizes = find_max(row_count, data)
    if color == "":
        color = FGC.CYAN
    color = ACC.RESET + color
    if align == "r":
        align = "l"
    else:
        align = "r"
    # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
    # 0  1  2  3  4  5  6  7  8  9  10

    if table_element == "":
        table_element = table_manager_current

    result = ""

    # Generate Header-line
    result += f"{color}{table_element[0]}"

    for sizen in range(row_count):
        result += f"{color}{table_element[4] * sizes[sizen]}{color}{table_element[1]}"
    result = result[:-1] + f"{color}{table_element[2]}"

    # Generate Header
    if header:
        result += f"\n{color}{table_element[3]}"
        for num in range(row_count):
            result += (
                f"{screate(data[num], sizes[num], align)}{color}{table_element[3]}"
            )
        result += f"\n{color}{table_element[5]}"
        for headerPieceSize in sizes:
            result += (
                f"{color}{table_element[4] * headerPieceSize}{color}{table_element[6]}"
            )
        result = result[:-1] + f"{color}{table_element[7]}"
        data = data[row_count:]

    # Generate DataSection
    for lineNum in range(0, len(data), row_count):
        result += f"\n{color}{table_element[3]}"
        for rowShift in range(0, row_count):
            try:
                result += f"{screate(data[lineNum + rowShift], sizes[rowShift], align)}{color}{table_element[3]}"
            except:
                result += (
                    f'{screate("", sizes[rowShift], align)}{color}{table_element[3]}'
                )
    result += f"\n{color}{table_element[8]}"

    # Generate Footer-line
    for sizen in range(row_count):
        result += f"{color}{table_element[4] * sizes[sizen]}{color}{table_element[9]}"
    result = result[:-1] + f"{color}{table_element[10]}{ACC.RESET}"

    return f'\n{screate(title, round(sum(sizes) / 2), "l")}\n{result}\n'


def create_multiline_table(
    row_count,
    sizes,
    data,
    title="TABLE",
    table_element="",
    color="",
    align="l",
):
    if not sizes:
        sizes = find_max(row_count, data)
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
        table_element = table_manager_current
    for i in range(len(data)):
        data[i] = sslice(data[i], sizes[i % len(sizes)])
    result = ""
    for line in range(0, len(data), row_count):
        maxtabsize = 0
        for row in range(0, row_count):
            if len(data[line + row]) > maxtabsize:
                maxtabsize = len(data[line + row])
        for row in range(0, row_count):
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
    for line in range(0, len(data), row_count):
        block = []
        for row in range(0, row_count):
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
        for blockline in block:
            result += f"{blockline}\n"

        result += f"{table_element[5]}"
        for headerPieceSize in sizes:
            result += f"{table_element[4] * headerPieceSize}{table_element[6]}"
        result = result[:-1] + f"{table_element[7]}\n"

    # Generate Footer-line
    result = result[: -1 * (2 + row_count + sum(sizes))] + table_element[8]
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
    return data[row_count * record_id : row_count * record_id + row_count]


def get_record_count(row_count, data):
    return len(data) / row_count
