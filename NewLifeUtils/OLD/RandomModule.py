from NewLifeUtils import random

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

def set_seed_formated( seed=-1):
    if seed == -1:
        seed = format_number()
    processed_seed = int("".join(seed.split()))
    random.seed = processed_seed
    return processed_seed

