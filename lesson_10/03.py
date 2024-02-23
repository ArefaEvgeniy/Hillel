file = open('example.txt', 'r')
a = file.read()
file.close()

print(a)

print('-' * 50)
file = open('example.txt', 'r')
try:
    b = file.read(7)
    file.seek(0)
    b_1 = file.read(5)
    b_2 = file.read(18)
finally:
    file.close()

print(b)
print(type(b))
print(b_1)
print(type(b_2))
