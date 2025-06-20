name = 'Bob'


def say_bye(name, a, b):
    print(f'Bye, {name}')
    return name


name = say_bye(name, 22, 'Red')

print(name)
