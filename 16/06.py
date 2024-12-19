cols_name = ["Ім'я", "Вік", "Професія"]
data = [
    ["Аліса", "28", "Інженер"],
    ["Боб", "22", "Датасаентист"],
    ["Чарлі", "35", "Дизайнер"]
]


import csv


with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cols_name)
    # writer.writerows(data)
    for item in data:
        writer.writerow(item)


with open('data_2.csv', 'r') as file:
    reader = csv.reader(file)
    sum_year = 0
    for index, row in enumerate(reader):
        print(row)
        if index == 0:
            continue
        sum_year += int(row[1]) if row[1] else 0

print("avg:", sum_year / index)
