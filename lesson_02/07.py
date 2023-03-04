a = (1, 2, 3)
b = ['a', 'b', 'c']

c = {1: 2, 3: 'rrr'}
c.update({a: b})
c.update({1: 909})

print(c)
