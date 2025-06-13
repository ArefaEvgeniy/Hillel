str_1 = "Hello, world Ї"
str_2 = "Привіт"

bytes_1 = str_1.encode()
bytes_2 = str_2.encode(encoding='utf-8')
bytes_3 = str_2.encode(encoding='utf-16')
print(bytes_1)
print(type(bytes_1))
print(bytes_2)
print(bytes_3)
print(bytes_2.decode(encoding='utf-16'))
# print(bytes_3.decode(encoding='utf-8'))
print(bytes_3.decode(encoding='windows-1251'))
print(bytes_2[8:10].decode())
