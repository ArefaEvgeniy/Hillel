# Створити список із двох елементів.
# Створити кортеж із двох елементів.
# Створити словник із однією парою. Ключ – кортеж, значення – список
# Створити словник із однією парою. Ключ – список, значення – кортеж


a = {'a': 1, 'b': 'c', 4: 1, (1, 2, 3): {4: 5}}
print(len(a))
print(a.keys())
print(a.values())
print(a.items())
b = a.pop('a')
del a[4]
print(a)
print(b)
print('c' in a.keys())
print(a.get('c', '000'))
print(a.get('b', '000'))
print(a)
a.update({'red': 'червоний', 'black': 'чорний'})
print(a)

a1 = (1, 2, 3)
a2 = [1, 2, 3]

s = {a1: a2}
print(s)
# s = {a2: a1}
# print(s)
