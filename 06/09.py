dict_one = {'a': 1, 'b': 4, 'c': 6}

print(dict_one['a'])
print(dict_one.get('a'))
print(dict_one.get('d', 33))
print(dict_one.setdefault('a', 33))
print(dict_one.setdefault('d', 33))
print(dict_one)
print(dict_one.setdefault('g'))
print(dict_one)
