# Записать в CSV-файл нижеприведённые данные.
# После этого прочитать этот файл и вывести данные в виде таблицы


import csv

name_of_fields = ["Имя", "Класс", "Возраст"]
field_01 = ["Женя", "3", "10"]
field_02 = ["Саша", "5", "12"]
field_03 = ["Маша", "11", "18"]


with open('02.csv', 'w', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(name_of_fields)
    file_writer.writerow(field_01)
    file_writer.writerow(field_02)
    file_writer.writerow(field_03)

data = []
with open('02.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file)
    for index, item in enumerate(file_reader):
        if index == 0:
            keys = item
        else:
            item_key = {}
            for i, value in enumerate(item):
                item_key.update({keys[i]: value})
            data.append(item_key)

for item in data:
    print(item)
