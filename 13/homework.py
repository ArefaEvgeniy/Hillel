def is_even(number):
    str_number = str(bin(number))
    last_element = int(str_number[-1])
    if last_element == 0:
        return True
    else:
        return False


def is_even_2(number):
    return int(bin(number)[-1]) == 0
