global_variable = 10


def example_function():
    print('func', global_variable)


def function_2(new_variable):
    def func_3(global_variable):
        print('func3', global_variable)

    global_variable = 5
    print('func2', global_variable)
    func_3(new_variable)


example_function()
function_2(global_variable)
print(global_variable)
