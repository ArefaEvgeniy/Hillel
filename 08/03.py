a = 100


def func_1():
    def func():
        a = 33
        print(a)
    a = 55
    print(a)
    func()
    return a


def func_2(a):
    print(a)


a = func_1()
func_2(a)
