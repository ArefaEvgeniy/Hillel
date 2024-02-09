def say_hi():
    global name
    name = 'Bob'
    surname = 'White'
    print('Hello', name, surname)


def say_bye():
    print('Bye', name)


name = 'Tom'
say_hi()
say_bye()
print(name)
