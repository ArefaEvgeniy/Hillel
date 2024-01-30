import copy

e = [12, 11, 10]
f = copy.copy(e)
d = e[:]
print('e = ', e)
print('f = ', f)
print('d = ', d)
print('id e = ', id(e))
print('id f = ', id(f))
print('id d = ', id(d))

f.append(9)
print('e = ', e)
print('f = ', f)
print('d = ', d)
print('id e = ', id(e))
print('id f = ', id(f))
print('id d = ', id(d))
