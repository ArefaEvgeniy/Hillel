name = 'Tom'


def say_hi():
    name = 'Sara'

    def say():
        print('I am,', name)

    print('Hello,', name)
    say()


def say_bye():
    print('Good bye,', name)


say_hi()
say_bye()
