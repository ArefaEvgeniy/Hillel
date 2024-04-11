def summa(a, b):
    return a + b


def mines(a, b):
    return a - b


def add(a, b):
    return a * b


def func(my_list, x, y):
    for item in my_list:
        print(item(x, y))


func([summa, mines, add], 7, 5)
