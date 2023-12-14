# Серіалізувати словник у json-формат та зберегти серіалізовані
# дані в файл. А також у рядковий формат без збереження у файл.
# Десиріалізувати записані дані з диска.


import json

input_data = [
    {
        "userId": 1,
        "id": 1,
        "score": 5000.45,
        "name": "Tom",
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
]

print(input_data[0].get("name"))

with open('task_01.json', 'w') as f:
    json.dump(input_data, f)

with open('task_01.json') as f:
    new_list = f.read()

print(new_list)
print(type(new_list))
print(new_list[0:10])

with open('task_01.json') as f:
    new_list_2 = json.load(f)

print(new_list_2)
print(type(new_list_2))
print(new_list_2[0].get('score'))

my_data = json.dumps(input_data)
print(my_data)
print(my_data[:5])
print(type(my_data))

my_list = json.loads(my_data)
print(my_list)
print(type(my_list))
