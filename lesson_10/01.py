japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'


print(japan_str.encode())
print(japan_char.encode())
print(color.encode())
print(name.encode())
new = surname.encode()
print(new)
print(len(new))
print(new.decode('Latin'))
