japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'
surname_2 = 'Apeфa'

print(japan_str.encode())
print(len(japan_str.encode()))
print(japan_char.encode())
print(len(japan_char.encode()))

print(color.encode())
print(len(color.encode()))

print(surname.encode())
print(len(surname.encode()))

print(japan_char.encode('utf-16'))
print(len(japan_char.encode('utf-16')))

b = japan_str.encode('utf-8')
print(b)
print(len(b))

print(b.decode('Latin-1'))

print('-' * 50)

print(surname.encode())
print(len(surname.encode()))

print(surname_2.encode())
print(len(surname_2.encode()))
