# Записати в CSV-файл наведені нижче дані.
# Після цього прочитати цей файл і вивести дані у вигляді таблиці


import csv

name_of_fields = ["Ім'я", "Клас", "Вік"]
field_01 = ["Євген", "3", "10"]
field_02 = ["Сашко", "", "12"]
field_03 = ["Михайло", "11", "18"]

with open('task_02.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(name_of_fields)
    writer.writerow(field_01)
    writer.writerow(field_02)
    writer.writerow(field_03)


input_data = [
    {
        "userId": 1,
        "id": 1,
        "score": 5000.45,
        "name": "Tom",
        "completed": None
    },
    {
        "userId": 34,
        "id": 2,
        "score": 2.003,
        "name": "Sam",
        "completed": True
    },
]

name_fields = input_data[0].keys()

with open('task_01.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(name_fields)
    for item in input_data:
        value = []
        for key in name_fields:
            value.append(item[key])
        writer.writerow(value)


with open('task_01.csv', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for item in reader:
        print(item)
