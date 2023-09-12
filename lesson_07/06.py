def my_func(a: int, b: int = 10) -> float:
    """
    This is my function
    :param a: first number
    :param b: second number
    :return:
    """
    return int(a / b)


print(my_func.__doc__)
