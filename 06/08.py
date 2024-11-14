from collections import OrderedDict

dct = OrderedDict({'apple': 4, 'orange': 2, 'pear': 1, 'banana': 3})

print(dct)
print(type(dct))

for item in dct:
    print(item)

print('-' * 100)
dct_2 = {'pear': 1, 'apple': 4, 'orange': 2, 'banana': 3}

for item in dct_2:
    print(item)


