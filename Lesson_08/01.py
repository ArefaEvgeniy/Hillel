name = 'Bob'


def func_1():
    print('1. Hello,', name)


def func_2():
    def inner_func():
        print('2. Hello,', name)

    global name
    name = 'Alice'
    inner_func()
    print('3. Hello,', name)


func_1()
func_2()
print('4. Hello,', name)
