# Є текстовий файл. Надрукувати:
# a) його перший рядок;
# b) його п'ятий рядок;
# c) його перші 5 рядків;
# d) весь файл.


f = open('example.txt')
print(f.readline().strip())
f.close()

print('-' * 50)

f = open('example.txt')
for index, item in enumerate(f):
    if index == 4:
        print(item.strip())
f.close()

print('-' * 50)

with open('example.txt') as f:
    for index, item in enumerate(f):
        if index <= 4:
            print(item.strip())

print('-' * 50)

f = open('example.txt')
print(f.read())
f.close()
