# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) весь файл.
# е) распечатать все строки в которых есть слово 'second'


f = open('test.txt')
data = f.readline()
f.close()
print(data)
print('-' * 50)


f = open('test.txt')
for index, item in enumerate(f):
    if index == 4:
        print(item)
f.close()
print('-' * 50)


f = open('test.txt')
for index, item in enumerate(f):
    if index < 5:
        print(item.strip())
f.close()
print('-' * 50)


f = open('test.txt')
print(f.read())
f.close()
print('-' * 50)


f = open('test.txt')
for index, item in enumerate(f):
    if 'second' in item.lower():
        print(item)
f.close()
