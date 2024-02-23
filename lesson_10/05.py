# Є текстовий файл. Надрукувати:
# a) його перший рядок;
# b) його п'ятий рядок;
# c) його перші 5 рядків;
# d) весь файл.

with open('example.txt') as f:
    a_1 = f.readline()
print(a_1)

print('-' * 50)

with open('example.txt') as f:
    for index, item in enumerate(f):
        if index == 4:
            print(item)

print('-' * 50)

with open('example.txt') as f:
    a = f.readlines()
print(a[4].strip('\n'))

print('-' * 50)
with open('example.txt') as f:
    for index, item in enumerate(f):
        if index <= 4:
            print(item.strip('\n'))

print('-' * 50)
with open('example.txt') as f:
    a = f.read()
print(a)
