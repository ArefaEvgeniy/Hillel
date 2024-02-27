# Серіалізувати словник у json-формат та зберегти серіалізовані
# дані в файл. А також у рядковий формат без збереження у файл.
# Десиріалізувати записані дані з диска.


import json

input_data = [
    {
        "userId": 1,
        "id": 1,
        "score": 5000.45,
        "name": "Євген",
        "completed": None,
        "children": ('Alice', 'Nick')
    },
    {
        "userId": 34,
        "id": 2,
        "score": 2.003,
        "name": "Sam",
        "completed": True
    },
    {
        "userId": 12,
        "id": 3,
        "score": 1.403,
        "name": "Peter",
        "completed": True
    },
    {
        "userId": 21,
        "id": 4,
        "score": 0.000,
        "name": "Bob",
        "completed": False
    },
]

print(input_data[0].get("children"))
#
# with open('test.txt', 'w') as file:
#     file.write(str(input_data))
#
# with open('test.txt') as file:
#     data = file.read()
#
# print(data)
# print(data[5:15])


with open('test.json', 'w') as file:
    json.dump(input_data, file)

with open('test.json') as file:
    data = json.load(file)

print(data)
print(type(data))
print(data[0].get("children"))

new_data = json.dumps(input_data)
print(new_data)
print(type(new_data))
print(new_data[5:15])

new_data_2 = json.loads(new_data)
print(new_data_2)
print(type(new_data_2))
print(new_data_2[0].get("children"))
