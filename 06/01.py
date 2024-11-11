japan_str = 'おき'
name = 'Tom'
word = 'ciào'

name_b = name.encode()
print(name_b)
print(type(name_b))
print(len(name_b))

print('-' * 100)

print(word.encode())
print(len(word.encode()))

print('-' * 100)

japan_b = japan_str.encode()
print(japan_b)
print(len(japan_b))

print('-' * 100)

japan_2_b = japan_str.encode('utf-16')
print(japan_2_b)
print(len(japan_2_b))

print(japan_b.decode('utf-8'))
print(japan_b.decode('utf-16'))
print(japan_b.decode('windows-1251'))

print('-' * 100)

japan_3_b = 'Світ'.encode('windows-1251')
print(japan_3_b)
print(japan_3_b.decode('windows-1251'))
print(japan_3_b.decode('utf-16'))
