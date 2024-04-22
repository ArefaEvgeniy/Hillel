import csv


data = []
with open('task_02+.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    count = 0
    for item in file_reader:
        if count == 0:
            data_rows = item
            index = data_rows.index('name')
        elif item[index]:
            data.append(item)
        count += 1

with open('task_02++.csv', 'w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',')
    file_writer.writerow(data_rows)
    file_writer.writerows(data)
