def func_1(in_list):
    result = None
    max_number = max(in_list)
    min_number = min(in_list)
    result = max_number - min_number
    return result


def func_2(in_list):
    return max(in_list) - min(in_list)


def func_3(in_list):
    result = None
    if len(in_list) > 2:
        result = max(in_list) - min(in_list)
    elif len(in_list) > 1:
        result = 0
    elif len(in_list) == 1:
        result = 1
    return result


def func_4(in_list):
    if len(in_list) > 2:
        return max(in_list) - min(in_list)
    elif len(in_list) > 1:
        return 0
    elif len(in_list) == 1:
        return 1
    # else:
    #     return None
