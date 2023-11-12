a_1 = set('23')
a_2 = {1, None, 2, 'red', 3, 3, 0, 3.0, True, (1, 2, 3)}

b = 4
a_2.add(b)

print(a_1)
print(a_2)

a_2.add('rr')
print(a_2)

a_2.add('rr')
a_2.add('rr')
print(a_2)

print('red' in a_2)

d = [0, 1, 1, 4, 66, 77, 34, 0, 22, 11, 1, 4, 66, 4, 4, 0, 11, 1, 66, 0]

d_new = list(set(d))
print(d_new)

d_new_2 = set(d)
print(list(d_new_2))

frozenset()
