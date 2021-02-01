import inspect
import random
import re

from NewLifeUtils.LoggerModule import *
from NewLifeUtils.StringUtilModule import parse_args


def select_rand_list(source, use_zero=False):
    try:
        source[0]
    except IndexError:
        err(f"{source} is empty", "RS ERROR")
    except TypeError:
        err(f"{source} object is not subscriptable", "RS ERROR")
    else:
        if use_zero:
            log("Can use zero", "RS LOG")
            selector = random.randrange(1, len(source))
        else:
            log("Cant use zero", "RS LOG")
            selector = random.randrange(0, len(source))
        log(
            f"Select item #{selector} from {type(source).__name__}; result {source[selector]}",
            "RS LOG",
        )
        return source[selector]
    return None


def getfromfname(a):
    res = ""
    for e in inspect.stack():
        try:
            res += e.code_context[0]
        except Exception:
            res += " <Unknown>"
    return res.rstrip("\n").rsplit("\n", 1)[-1]


def __partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = __partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def bprint(text, maxlinelength=9, font="default"):
    print(get_files_from_dir("fonts"))


def format_number(
    number=random.randrange(1111111111111111, 9999999999999999),
    numform="4444",
):
    # A total conversion
    number = int(number)
    numform = str(numform)
    # Total length
    total_length = 0
    for num in numform:
        total_length += int(num)

    # Dividing or lengthening a number
    if number == 0:
        number = 1

    if len(str(number)) < total_length:
        while len(str(number)) < total_length:
            number = number * 10
    elif len(str(number)) > total_length:
        number = int(str(number)[0:total_length])

    # Add spaces
    result = str(number)
    shift = 0
    for pos in numform:
        result = result[: int(pos) + shift] + " " + result[int(pos) + shift :]
        shift += int(pos) + 1
    return result

def safe_format(text, keys=None, func = None, smart=None):
    if keys is None:
        keys = {}
    if smart is None:
        smart = {}

    class SafeDict(dict):
        def __missing__(self, key):
            nonlocal func
            if smart is not {}:
                keypr = parse_args(key)
                name = keypr['command']
                if name not in smart.keys():
                    return "{" + key + "}"
                else:
                    return smart[name](*keypr['param'])
            elif func is not None:
                return "{" + str(func(key)) + "}"
            else:
                return "{" + key + "}"

    return text.format_map(SafeDict(**keys))


def set_seed_formated(seed=-1):
    if seed == -1:
        seed = format_number()
    processed_seed = int("".join(seed.split()))
    random.seed = processed_seed
    return processed_seed


def hex_to_rgb(hx, hsl=False):
    """Converts a HEX code into RGB or HSL.
    Args:
        hx (str): Takes both short as well as long HEX codes.
        hsl (bool): Converts the given HEX code into HSL value if True.
    Return:
        Tuple of length 3 consisting of either int or float values.
    Raise:
        ValueError: If given value is not a valid HEX code."""
    if re.compile(r"#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$").match(hx):
        div = 255.0 if hsl else 0
        if len(hx) <= 4:
            return tuple(
                int(hx[i] * 2, 16) / div if div else int(hx[i] * 2, 16)
                for i in (1, 2, 3)
            )
        return tuple(
            int(hx[i : i + 2], 16) / div if div else int(hx[i : i + 2], 16)
            for i in (1, 3, 5)
        )
    raise ValueError(f'"{hx}" is not a valid HEX code.')
