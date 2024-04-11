def decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')

    return wrapper


@decorator
def function():
    print('I am aline function')


@decorator
def func_2():
    print('I am a new function')


# function = decorator(function)
function()
print('-' * 50)
func_2()
