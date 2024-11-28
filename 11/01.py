file = open('test_1.txt', 'w')
file.write('Hellow, world\nsecond line\n')
file.close()

file = open('test_1.txt')
try:
    text = file.read(4)
    print(text)
    text_2 = file.read(10)
    print(text_2)
finally:
    file.close()

with open('test_1.txt') as file:
    text = file.read()
    print(len(text))

print(text)

line_1 = 'третя строка'
line_2 = 'line before last'
line_3 = 'last line'
with open('test_1.txt', 'a', encoding='utf-8') as file:
    file.write(f'\n{line_1}\n{line_2}\n{line_3}')

f = open('test_1.txt', 'r', encoding='utf-8')
data = f.readlines()
f.close()
data = [i.strip() for i in data]
print(data)

print('-' * 100)
with open('test_1.txt', encoding='utf-8') as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline(), end='')
    print(file.readline().strip())

print('-' * 100)
print('Hellow, world\n')
print('second line\n')

print('-' * 100)
new_text_str = 'Новий текст'
new_text_bytes = new_text_str.encode('windows-1251')
print(new_text_str)
print(new_text_bytes)

print('-' * 100)
with open('test_1.txt', 'a', encoding='utf-8') as file:
    file.write(new_text_str)
    file.write(new_text_bytes.decode('windows-1251'))

print('-' * 100)
with open('test_1.txt', 'ab') as file:
    file.write(new_text_str.encode())
    file.write(new_text_bytes.decode('windows-1251').encode('utf-8'))

f = open('test_1.txt', encoding='utf-8')
print(f.read())
f.close()
