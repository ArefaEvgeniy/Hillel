def say_hi():
    name = 'Bob'
    surname = 'White'
    print('Hello', name, surname)
    return name


def say_bye():
    print('Bye', name)


name = 'Tom'
name = say_hi()
say_bye()
print(name)
