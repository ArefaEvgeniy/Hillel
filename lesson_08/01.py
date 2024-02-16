my_pets = ['alfred', 'REM', 'WiLLiam', 'AlrA']

title_pets = []
for item in my_pets:
    title_pets.append(item.title()[:5])
print(title_pets)


def my_func(x):
    return x.title()[:5]


new_pets = list(map(my_func, my_pets))
print(new_pets)

new_pets2 = list(map(lambda x: x.title()[:5], my_pets))
print(new_pets2)

new_pets3 = list(map(str.title, my_pets))
print(new_pets3)
