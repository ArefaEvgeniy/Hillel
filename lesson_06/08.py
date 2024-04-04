name = 'Tom'


def say_hi():
    def say():
        print(surname)

    new_name = 'Bob'
    surname = 'White'
    print('Hello,', new_name, surname)
    say()
    return new_name


def say_bye():
    print(f'Good bye, {name}')


name = say_hi()
say_bye()
