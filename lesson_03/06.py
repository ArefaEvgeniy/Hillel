import copy

e = [12, 11, ['a', 'b', 'c'], 10]
f = copy.deepcopy(e)

print('e = ', e)
print('f = ', f)
print('id e = ', id(e))
print('id f = ', id(f))

print('id[2] e = ', id(e[2]))
print('id[2] f = ', id(f[2]))

f.append(9)
e[2].pop()
print('e = ', e)
print('f = ', f)
print('id e = ', id(e))
print('id f = ', id(f))
