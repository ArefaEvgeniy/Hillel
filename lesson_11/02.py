# Записати в CSV-файл наведені нижче дані.
# Після цього прочитати цей файл і вивести дані у вигляді таблиці

import csv

name_of_fields = ["Ім'я", "Клас", "Вік"]
field_01 = ["Євген", "3", "10"]
field_02 = ["Сашко", "5", "12"]
field_03 = ["Михайло", "11", "18"]

with open('task_02.csv', 'w', encoding='utf-8') as f:
  file_write = csv.writer(f, delimiter=',')
  for item in (name_of_fields, field_01, field_02, field_03):
    file_write.writerow(item)

with open('task_02+.csv', mode='r', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',')
  new_data = []
  for item in reader:
    new_data.append(item)

print(new_data)

with open('task_02+.csv', mode='r', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',')
  names = []
  for index, item in enumerate(reader):
    if index > 0:
      names.append(item[0])

print(names)
