name = 'Tom'


def say_hi(name):
    print(f'Hello, {name}')
    name = 'Sam'
    return name


def say_bye():
    def say_name():
        print(f'My name is {name}')

    say_name()
    say_hi('Cool')
    print(f'Good bye, {name}')


name = say_hi(name)
say_bye()
say_hi('RR')
...
