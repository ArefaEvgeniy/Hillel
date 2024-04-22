import json
import csv


with open('task_01.json') as file:
    input_data = json.load(file)

keys = ["userId", "id", "score", "name"]
data_rows = []
for item in input_data:
    data = []
    for key in keys:
        data.append(item.get(key, ''))
    data_rows.append(data)

print(data_rows)

with open('task_02.csv', 'w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',')
    file_writer.writerow(keys)
    for item in data_rows:
        file_writer.writerow(item)
    # file_writer.writerows(data_rows)
