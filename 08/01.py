a = 100


def func_1():
    def func():
        print(a)
    a = 10
    print(a)
    func()
    return func


def func_2():
    print(a)


my_func = func_1()
my_func()
func_2()
print("END")

aaa = print
aaa("YES", 33, 67, sep='!!!')
