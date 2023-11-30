my_pets = ['alfred', 'REM', 'William', 'DogI']


def my_func(value):
    res = ''
    if isinstance(value, str) and value:
        res = value.title()
        if len(res) > 4:
            res = res[:4] + '.'

    return res


new_pets = list(map(my_func, my_pets))
print(new_pets)
