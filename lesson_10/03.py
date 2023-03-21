file = open('test.txt', 'w')
file.write('Line 1\nline_2\nLINE 3\nLiNe 4\nLoine 5\nLINE END')
file.close()


with open('test.txt') as file:
    text = file.read(14)
    print(text)
    text_2 = file.read(3)
    print(text_2)
    print(file.tell())
    file.seek(0)
    text_3 = file.read(3)
    print(text_3)
print('-' * 100)

file = open('test.txt')
try:
    text = file.readline()
    print(text)
    text_2 = file.readline()
    print(text_2)
    text_3 = file.readline()
    print(text_3)
finally:
    file.close()
print('-' * 100)

with open('test.txt') as file:
    text = file.readlines()
    print(text)
for item in text:
    print(item.strip())
print('FINISH')
