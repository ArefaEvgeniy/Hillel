def func():
    def func_2():
        print('This is a second function')

    return func_2


a = func()
a()

func()()
