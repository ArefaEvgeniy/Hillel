# Є текстовий файл. Надрукувати:
# a) його перший рядок;
# b) його п'ятий рядок;
# c) його перші 5 рядків;
# d) весь файл.

with open('05.txt', 'rt') as vasil:
    print(vasil.readline())


with open('05.txt', 'rt') as vasil:
    data = vasil.readlines()
    print(data[4])

print('-' * 50)

with open('05.txt', 'rt') as f:
    for index, item in enumerate(f):
        if index == 4:
            print(item.strip('\n'))

print('-' * 50)

with open('05.txt', 'rt') as f:
    for index, item in enumerate(f):
        if index <= 4:
            print(item.strip('\n'))

print('-' * 50)

with open('05.txt', 'rt') as f:
    for index, item in enumerate(f):
        print(item.strip('\n'))

print('-' * 50)

try:
    f = open('05.txt')
    new_data = f.readlines()
finally:
    f.close()


for item in new_data:
    print(item.strip('\n'))
