my_pets = ['alfred', 'rem', 'ALRA', 'BacK']

new_pets = []
for item in my_pets:
    new_pets.append(item.title() + f'_{len(item)}')

print(new_pets)


def my_func(x):
    return x.title() + f'_{len(x)}'


new_pets_2 = list(map(my_func, my_pets))
print(new_pets_2)


new_pets_3 = list(map(lambda x: x.title() + f'_{len(x)}', my_pets))
print(new_pets_3)
