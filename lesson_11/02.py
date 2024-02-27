# Записати в CSV-файл наведені нижче дані.
# Після цього прочитати цей файл і вивести дані у вигляді таблиці


import json
import csv

with open('test.json') as file:
    data = json.load(file)

print(data)
new_list = []
for item in data:
    person = {}
    person.update({'userId': item.get('userId')})
    person.update({'id': item.get('id')})
    person.update({'score': item.get('score')})
    person.update({'name': item.get('name')})
    new_list.append(person)

print(new_list)
name_of_fields = [i for i in new_list[0].keys()]
print(name_of_fields)

with open('task.csv', 'w', newline='', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(name_of_fields)
    for item in new_list:
        fields = []
        for key in name_of_fields:
            fields.append(item.get(key))
        file_writer.writerow(fields)

print('-' * 100)

with open('task_2.csv', encoding='Windows-1251') as file:
    file_reader = csv.reader(file, delimiter=',')
    for item in file_reader:
        print(item)



a = ['userId', 'id', 'score', 'name', 'phone']
b_1 = ['1', '1', '5000.45', 'Євген', '34343']
b_2 = ['', '2', '', 'Sam', '3333']
b_3 = ['12', '3', '', '', '']
b_4 = ['21', '4', '0.0', 'Bob', '']

with open('task_0.csv', 'w', newline='', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(a)
    # file_writer.writerow(b_1)
    # file_writer.writerow(b_2)
    # file_writer.writerow(b_3)
    # file_writer.writerow(b_4)
    for item in (b_1, b_2, b_3, b_4):
        file_writer.writerow(item)

    # file_writer.writerows([b_1, b_2, b_3, b_4])

