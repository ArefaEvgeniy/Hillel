a = (1, 3, '445', 'eef', 345.7, 0, 99, True, None, (1, 2, ('aaa', 'Hello, world!')))

a_1 = ()
a_2 = tuple('Hello')

print(type(a))

print(345.7 in a)
print(len(a))

print(a[-1][-1][-1][::2])

print(a_2)
print(type(a_2))
