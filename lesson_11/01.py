# Сериализовать словарь в json-формат и сохранить сериализованные
# данные в файл. А также в строковый формат без сохранения в файл.
# Десириализовать записанные данные с диска.


import json

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
        "completed": True,
        "children": ('Anna', 'Bill')
    },
]

with open('task_01.json', 'w') as f:
    json.dump(input_data, f)

with open('task_01.json') as f:
    new_data = json.load(f)

print(input_data)
print(type(input_data))
print(new_data)
print(type(new_data))


json_data = json.dumps(input_data)
print(json_data)
print(type(json_data))
print(json_data[0:15])
print(json_data[0])
print(len(json_data))

new_data_2 = json.loads(json_data)
print(new_data_2)
print(type(new_data_2))
print(new_data_2[0])
print(len(new_data_2))
