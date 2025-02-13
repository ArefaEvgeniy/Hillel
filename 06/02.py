japan = '㍿おき'
name = 'Tom'
word = 'ciào'
surname = 'Арефа'
surname_2 = 'Apeфa'

a_1 = word.encode()
print(a_1)
print(len(a_1))

a_3 = word.encode("latin-1")
print(a_3)
print(len(a_3))

b_1 = japan.encode()
print(b_1)
print(len(b_1))

japan_1 = b_1.decode("utf-8")
print(japan_1)
print(len(japan_1))

japan_2 = b_1.decode("latin-1")
print(japan_2)
print(len(japan_2))

print("-" * 100)

b_2 = word.encode()
print(b_2)
print(len(b_2))

japan_1 = b_2.decode("utf-8")
print(japan_1)
print(len(japan_1))

japan_2 = b_2.decode("latin-1")
print(japan_2)
print(len(japan_2))

a_2 = surname.encode("windows-1251")
print(a_2)
print(len(a_2))

print("-" * 50)
new = surname.encode("utf-8")
print(new)
print(len(new))

new_2 = surname_2.encode("utf-8")
print(new_2)
print(len(new_2))
