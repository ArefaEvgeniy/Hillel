name = 'Bob'


def say_hello(name):
    name = 'Michle'
    print(f'Hello, {name}')


def say_bye():
    def say_otner():
        global name
        name = 'Kite'
        print(f'{name}, who are you?')

    say_otner()
    global name
    name = 'Bob'
    print(f'Bye, {name}')


say_hello(name)
name = 'Olia'
say_bye()
print(name)
