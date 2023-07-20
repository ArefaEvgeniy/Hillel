japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'

print(len(japan_str))
print(japan_str.encode())
print(len(japan_str.encode()))
print('-' * 50)
print(len(japan_str))
print(japan_str.encode("utf-16"))
print(len(japan_str.encode("utf-16")))
print('-' * 50)
print(len(japan_char))
print(japan_char.encode())
print(len(japan_char.encode()))
print('-' * 50)
print(len(japan_char))
print(japan_char.encode("utf-16"))
print(len(japan_char.encode("utf-16")))
print('-' * 50)
print(len(color))
print(color.encode())
print(len(color.encode()))
print('-' * 50)
print(len(name))
print(name.encode())
print(len(name.encode()))
print('-' * 50)
print(len(surname))
print(surname.encode())
print(len(surname.encode()))

