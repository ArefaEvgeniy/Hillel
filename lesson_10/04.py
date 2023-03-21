# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) весь файл.

with open('test.txt') as file:
    text = file.readline()
    print(text)
print('-' * 100)

with open('test.txt') as file:
    text = file.read()
line_5 = text.split('\n')[4]
print(line_5)
print('-' * 100)

with open('test.txt') as file:
    text = file.readlines()
for index in range(5):
    print(text[index].strip())
print('-' * 100)

with open('test.txt') as file:
    text = file.read()
    print(text)