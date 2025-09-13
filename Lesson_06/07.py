my_dict = {'a': 1, 'b': 2, 'c': 3, (1, 2): 4, 5: [4, 5, 6]}

my_dict.update({'d': 4, 'e': 5, 'c': 33})

print(my_dict[5])
print(my_dict[(1, 2)])
print(my_dict.keys())
for key in my_dict.keys():
    print(my_dict[key])

print('-' * 40)
for value in my_dict.values():
    print(value)

print(my_dict)

print('-' * 40)
for key, value in my_dict.items():
    print(f"{key}: {value}")

print('-' * 40)
for item in my_dict:
    print(item)

print('-' * 40)
print('b' in my_dict)
print(2 in my_dict)

print('-' * 40)
if 'c' in my_dict:
    print(my_dict['c'])

print(my_dict.get('cc', 'Oleksandr'))

# a, c  a -> 20  c -> 22
# abc

# c, a c -> 22  a -> 20
