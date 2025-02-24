def func():
    print('func')


def func_2(t, o, p):
    """
    Calculate the area of a circle.
    Все, що завгодно можемо написати

    :param t: буль-яка функція
    :param o: dsgfdfsgdsf
    :param p: sdfgkj lknj jkhkj
    :return: return local function.
    """
    def func_3():
        """
        Function 3

        :return: None.
        """
        print('Local function')

    print('start')
    t()
    print('end')

    return func_3


a = func
del func

a()
print('-' * 50)

cc = func_2(a, 1, 2)
cc()

print(help(func_2))
print(help(cc))
