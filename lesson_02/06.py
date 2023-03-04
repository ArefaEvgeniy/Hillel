d = {1: 'a', 'b': [1, 2, 3, {'ss': 'we', 'g': 'tty'}], 'c': 1111}

print(d['b'][3]['g'])

print(list(d.values()))
print(list(d.keys()))
print(list(d.items()))

print(d.get(0, 'default value'))
