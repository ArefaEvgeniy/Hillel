a = 100


def func_1():
    def func():
        a = 33
        print(a)
    global a
    a = 55
    print(a)
    func()


def func_2():
    print(a)


func_1()
func_2()
