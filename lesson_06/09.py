name = 'Tom'


def say_hi():
    def say_bye():
        print('Bye,', name)

    print('Hello,', name)
    say_bye()


say_hi()
print(name)
say_bye()
