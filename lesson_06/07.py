name = 'Tom'


def say_hi():
    global name
    name = 'Sara'
    print('Hello,', name)


def say_bye():
    print('Good bye,', name)


say_hi()
say_bye()
