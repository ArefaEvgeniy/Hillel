japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'

print(japan_str)
print(japan_str.encode())
print(len(japan_str.encode()))
print('-' * 50)
print(japan_char)
print(japan_char.encode())
print(len(japan_char.encode()))
print('-' * 50)
print(name)
print(name.encode())
print(len(name.encode()))
print('-' * 50)
print(surname)
print(surname.encode())
print(len(surname.encode()))
print('-' * 50)
print('Aрeфa')
print('Aрeфa'.encode())
print(len('Aрeфa'.encode()))

print('-' * 50)
new = japan_str.encode('utf-16')
print(japan_str)
print(new)
print(new.decode('latin-1'))

print('-' * 50)
print(len(japan_str.encode()))
print(len(japan_str.encode('utf-16')))

# UNICODE
# 00000000 00000000 00000000 00000000
#
# utf-8
# utf-16
# utf-32
#
# 'qwerкy'
#
# ASCII
#
# 00000000
# 00000001
# 00000010
# 00000011
# 00000100
# ...
# 11111111
#
# 2 ** 8 = 256
#
# A a
# 0-9
#
# 128
#
# 0
# 1
#
# 00
# 01
# 10
# 11

