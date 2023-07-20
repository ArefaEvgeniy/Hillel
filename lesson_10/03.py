f = open('test.txt')
a = f.read(10)
b = f.read(2)
c = f.read(5)
f.close()

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print('-' * 50)

f = open('test.txt')
try:
    a = f.read()
finally:
    f.close()

print(f'a: {a}')
print('-' * 50)

with open('test.txt', 'r') as file:
    a = file.readline()
    b = file.readline()

print(f'a: {a}')
print(f'b: {b}')
print('-' * 50)

with open('test.txt', 'r') as file:
    a = file.readlines()

print(f'a: {a}')

