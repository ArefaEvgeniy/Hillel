japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'

print(color)
print(color.encode())
print(len(color.encode()))
print('-' * 50)
print(surname)
print(surname.encode())
print(len(surname.encode()))
print('-' * 50)
print(surname.encode('utf-16'))
print(len(surname.encode('utf-16')))
# print('-' * 50)
# surname_encode = surname.encode('utf-16')
# print(surname_encode.decode('utf-8'))
print('-' * 50)
japan_char_encode = japan_char.encode('utf-8')
print(japan_char_encode)
print('-' * 50)
print(japan_str.encode())
print(len(japan_str.encode()))
print(japan_str.encode('utf-16'))
print(len(japan_str.encode('utf-16')))
print(japan_str.encode('utf-32'))
print(len(japan_str.encode('utf-32')))

print('-' * 50)


a = b'\xff\xfeA0C0H0J0M0 \x00R0Z0\x7f3\xdc0\x9b0'
print(a)
print(a.decode('utf-16'))

a_1 = 'ぁぃえおき げず㍿ボ゛'
a_2 = a_1.encode('utf-8')  # b'\xff\xfeA0C0H0J0M0 \x00R0Z0\x7f3\xdc0\x9b0'

print('-' * 50)

b_1 = surname.encode()
print(surname)
print(b_1)
print(b_1.decode('Latin-1'))

print('-' * 50)

b_2 = 'Тom'.encode()
print('Тom')
print(b_2)
print(b_2.decode('Latin-1'))
