with open('06.txt', 'wb') as f:
    f.write('Hello, ХЇЕН world\n'.encode())

with open('06.txt', encoding='utf-8') as f:
    print(f.read())

with open('06.txt', 'rb') as f:
    b = f.read()

print('-' * 50)
print(b)
print(type(b))
print(b.decode())
