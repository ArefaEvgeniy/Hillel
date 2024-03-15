def func_1():
    def func_2():
        print('FUNC_2')

    func_2()
    return func_2


def func_3():
    ...
    yield 10


a = func_1()

func_3()
a()
