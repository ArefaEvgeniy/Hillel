# Записать в CSV-файл нижеприведённые данные.
# После этого прочитать этот файл и вывести данные в виде таблицы

import csv

name_of_fields = ["Имя", "Класс", "Возраст"]
field_01 = ["Женя", "3", "10"]
field_02 = ["Саша", "5", "12"]
field_03 = ["Маша", "11", "18"]


# with open("task_02.csv", encoding="utf-8", mode="w", newline=None) as file:
#     file_csv = csv.writer(file, delimiter=',')
#     file_csv.writerow(name_of_fields)
#     for item in (field_01, field_02, field_03):
#         file_csv.writerow(item)


with open("task_02.csv", encoding="utf-8") as file:
    file_csv = csv.reader(file)
    count = 0
    for item in file_csv:
        if count == 0:
            print(item)
            print('-' * 50)
        else:
            print(item)
        count += 1
