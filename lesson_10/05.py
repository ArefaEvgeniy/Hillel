# Є текстовий файл. Надрукувати:
# a) його перший рядок;
# b) його п'ятий рядок;
# c) його перші 5 рядків;
# d) весь файл.

f = open('05.txt', encoding='utf-8')
data_1 = f.readline()
f.close()
print(data_1)

print('-' * 50)

with open('05.txt', encoding='utf-8') as f:
    for index, item in enumerate(f):
        if index == 4:
            print(item)

print('-' * 50)

with open('05.txt', encoding='utf-8') as f:
    for item in f:
        print(item.strip())
