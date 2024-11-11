a = [1, 2, 'red', 'tt', [1, 'g', 'black'], 99]
b = (1, 2, 'red', 'tt', [1, 'g', 'black'], 99)
c = tuple([1, 2, 'red', 'tt', [1, 'g', 'black'], 99])

print(a)
print(type(a))

print(b)
print(type(b))

print(999 in a)
print(999 in b)

word = 'Red'
print(list(word))
print([word,])

print(tuple(word))
print((word,))

print(c)
print(type(c))

print(tuple((False,)))
print((False,))

print(list(b[:4]))
