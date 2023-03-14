my_pets = ['alfred', 'tabitha', 'william', 'arla']

upper_pets_1 = []
for item in my_pets:
    upper_pets_1.append(item.upper())
print('upper_pets_1:', upper_pets_1)

upper_pets_2 = [i.upper() for i in my_pets]
print('upper_pets_2:', upper_pets_2)


def func(x):
    return x.upper()


upper_pets_3 = list(map(func, my_pets))
print('upper_pets_3:', upper_pets_3)

upper_pets_4 = list(map(lambda x: x.upper(), my_pets))
print('upper_pets_4:', upper_pets_4)

upper_pets_5 = list(map(str.upper, my_pets))
print('upper_pets_5:', upper_pets_5)
