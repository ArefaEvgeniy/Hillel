name = 'Bob'


def func_1(name):
    print('1. Hello,', name)


def func_2(new_name):
    def inner_func():
        print('2. Hello,', new_name)

    new_name = 'Alice'
    inner_func()
    print('3. Hello,', new_name)

    return new_name


func_1(name)
name = func_2(name)
print('4. Hello,', name)
