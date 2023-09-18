f = open('example.txt')
a = f.read()
f.close()
print(a)

print('-' * 50)

with open('example.txt') as f:
    a_1 = f.read(7)
    a_2 = f.read(5)
print(a_1)
print(a_2)

print('-' * 50)

with open('example.txt', 'rb') as f:
    b_1 = f.read(8)
    b_2 = f.read(4)
print(b_1)
print(b_1.decode())
print(b_2)
