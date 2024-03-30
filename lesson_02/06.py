a = {'name': 'Bob', 'age': 34, 'city': 'Dnipro'}

print(a)
print(type(a))
print(len(a))

print('name' in a)
print('Bob' in a)

print(a['name'])
print(a['age'])

print('-' * 100)

print(a.get('age', 0))
print(a.get('nick', 0))

print('-' * 100)

print(list(a.items()))
print(list(a.keys()))
print(list(a.values()))

b = a.pop('age')
print(a)
print(b)
a['nick'] = 'Kate'
print(a)
a['city'] = 'Kiev'
print(a)
a.update({'aa': 12, 45: 'rr'})
print(a)
