global_variable = 10


def example_function(global_variable):
    print('func', global_variable)


def function_2():
    def func_3():
        new_variable = True
        print('func3', new_variable)
        return new_variable

    global_variable = 5
    print('func2', global_variable)
    a = func_3()
    print('a', a)
    return a


example_function(global_variable)
a = function_2()
print(global_variable)
print('a', a)
