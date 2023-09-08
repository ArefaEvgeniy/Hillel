name = 'Tom'


def say_hi(name):
    def say_bye():
        global name
        name = 'Kat'
        print('Bye,', name)

    name = 'Jack'
    print('Hello,', name)
    say_bye()
    print('How are you,', name)
    return name


name = say_hi(name)
print(name)
# say_bye()
