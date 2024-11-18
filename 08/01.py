global_variable = 10


def example_function():
    print('func', global_variable)


def function_2():
    def func_3():
        print('func3', global_variable)

    global_variable = 5
    print('func2', global_variable)
    func_3()


example_function()
function_2()
print(global_variable)
