a = {1: 'aa', 2: 'tt', 'r': 33, 3: 33}

print(len(a))

print(a[2])
print(a['r'])
print(a.get('rrr', 'Не має'))

print(tuple(a.keys()))
print(tuple(a.values()))
print(list(a.items()))
