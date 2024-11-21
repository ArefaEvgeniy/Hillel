def my_func():
    def local_func():
        print('I am a local function')

    return local_func


print(my_func)
ff = my_func()
print(ff)
ff()
