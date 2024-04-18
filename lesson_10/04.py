f = open('test.txt')
text = f.read(7)
f.seek(0)
text_2 = f.read(3)
text_3 = f.read(7)
f.close()

print(text)
print(text_2)
print(text_3)

print('-' * 50)

with open('test.txt') as f:
    text = f.read(7)
    f.seek(0)
    text_2 = f.read(3)
    text_3 = f.read(7)

print(text)
print(text_2)
print(text_3)

print('-' * 50)

with open('test.txt') as f:
    text = f.read()
print(text)

print('-' * 50)

with open('test.txt') as f:
    print(f.readline().strip())
    print(f.readline().strip())

print('-' * 50)

with open('test.txt') as f:
    print(f.readlines())
