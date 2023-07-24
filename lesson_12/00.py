import csv


scores = {'Nick': 1, 'Lack': 12, 'Kate': 11}
input_names = ('Nick', 'Tom', 'Grag', 'Lack')
numbers = [123, 444, 567, 336, 6689, 6787]

# Name  Scores  Number
# Nick    1       123
# Tom     0       444
# Grag    0       567
# Lack    12      336

names_of_col = ['Name', 'Scores', 'Number']

with open("task_00.csv", mode="w") as file:
    file_csv = csv.writer(file)
    file_csv.writerow(names_of_col)
    for index, name in enumerate(input_names):
        data = []
        data.append(name)
        data.append(scores.get(name, 0))
        data.append(numbers[index])
        file_csv.writerow(data)
